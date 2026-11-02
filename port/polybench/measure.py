"""How much each kernel changed in the port, measured from the sources.

    python3 -I measure.py <PolyBench/C 4.2.1 directory>     CSV on stdout

The directory is the one run.sh downloads into POLYBENCH.

C side: the body of kernel_<name>. Sword side: every function but main and
start. Counted on each: statement lines (no blank lines, comments, pragmas or
lines of braces alone), loops, and the arrays the kernel is handed. The class
is the one the port states at its top. A rewritten kernel is "form" when it
has no loop and no array the C does not, and "work" when it has: a copy, a
transpose, a second loop.
"""
import glob
import os
import re
import sys


def braced(text, at):
    start = text.index("{", at)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return text[start:]


def strip(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    lines = []
    for line in text.split("\n"):
        s = line.strip()
        if s and not s.startswith("#") and not re.fullmatch(r"[{}]+;?", s):
            lines.append(s)
    return lines


def c_kernel(path, name):
    text = open(path).read()
    m = re.search(r"\bkernel_%s\s*\(" % re.escape(name.replace("-", "_")), text)
    head = ""
    if m:
        depth = 1
        for i in range(m.end(), len(text)):
            depth += {"(": 1, ")": -1}.get(text[i], 0)
            if depth == 0:
                head = text[m.end():i]
                break
    arrays = len(re.findall(r"POLYBENCH_[123]D", head))
    body = strip(braced(text, m.end())) if m else []
    return body, arrays


def sword_kernel(path):
    """Lines written once; loops counted once per call, as the C writes them."""
    text = open(path).read()
    funcs, arrays = {}, None
    for m in re.finditer(r"^func (\w+)\(([^)]*)\)", text, flags=re.M):
        funcs[m.group(1)] = strip(braced(text, m.end()))
        if m.group(1) == "kernel":
            arrays = len(re.findall(r"\[\]", m.group(2)))
    helpers = [f for f in funcs if f not in ("main", "start", "kernel")]

    def loops(name, seen=()):
        own = sum(len(re.findall(r"\bfor\b", l)) for l in funcs[name])
        for h in helpers:
            if h != name and h not in seen:
                calls = sum(len(re.findall(r"\b%s\(" % h, l)) for l in funcs[name])
                own += calls * loops(h, seen + (name,))
        return own

    if "kernel" in funcs:
        body = funcs["kernel"] + [l for h in helpers for l in funcs[h]]
        nloops = loops("kernel")
    else:
        # The kernel is a sequence of calls in main (3mm): its helpers, and
        # the arrays main allocates.
        body = [l for h in helpers for l in funcs[h]]
        nloops = sum(sum(len(re.findall(r"\b%s\(" % h, l)) for l in funcs["main"]) * loops(h)
                     for h in helpers)
        arrays = sum(l.count("mem.Alloc") for l in funcs["main"])
    return body, arrays, nloops, text


def loops_c(lines):
    return sum(len(re.findall(r"\bfor\s*\(", l)) for l in lines)


def main():
    src, port = sys.argv[1], os.path.dirname(os.path.abspath(__file__))
    print("kernel,class,c_lines,sword_lines,c_loops,sword_loops,parallel_loops,"
          "c_arrays,sword_arrays,kind")
    for path in sorted(glob.glob(os.path.join(port, "*.sword"))):
        name = os.path.basename(path)[:-6]
        found = glob.glob(os.path.join(src, "**", name, name + ".c"), recursive=True)
        if not found:
            continue
        cl, ca = c_kernel(found[0], name)
        sl, sa, sloops, text = sword_kernel(path)
        cls = re.search(r"// Class: ([a-z ]+)", text)
        cls = cls.group(1).strip() if cls else "?"
        par = sum(l.count("parallel for") for l in sl)
        if cls == "rewritten":
            kind = "form" if sloops <= loops_c(cl) and sa <= ca else "work"
        else:
            kind = ""
        print(",".join(str(x) for x in (name, cls, len(cl), len(sl), loops_c(cl),
                                         sloops, par, ca, sa, kind)))


main()
