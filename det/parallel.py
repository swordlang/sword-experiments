"""How many of the functions that run something in parallel are det.

    python3 -I det/parallel.py <shield> <label> <target>...

Prints one line of JSON for the set: its functions, how many are det, how
many are parallel, how many of those are det, and why the others are not.

A target is a .sword file or a package directory, passed to `shield det` as is.
A function is parallel when its own body has `scope`, `spawn` or `parallel for`.
Its body is found from the position shield det prints, by matching braces in
the source, skipping strings and comments.
"""
import json
import re
import subprocess
import sys

HEAD = re.compile(r"^(\S+):(\d+):(\d+): (\S+): (det|not det|det when .*)$")
PARALLEL = re.compile(r"\bscope\s*\{|\bspawn\b|\bparallel\s+for\b")

CAUSES = [
    ("atomic", "atomic"),
    ("shared", "shared value"),
    ("select", "several channels at once"),
    ("channel", "channel"),
    ("outside", "calls out of the language"),
    ("address", "address into a number"),
    ("indirect", "calls through"),
]


def body(path, line, cache={}):
    if path not in cache:
        try:
            cache[path] = open(path).read().split("\n")
        except OSError:
            cache[path] = None
    lines = cache[path]
    if lines is None:
        return ""
    text = "\n".join(lines[line - 1:])
    depth, i, start, n = 0, 0, None, len(text)
    while i < n:
        c = text[i]
        if text.startswith("//", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == '"':
            i += 1
            while i < n and text[i] != '"':
                i += 2 if text[i] == "\\" else 1
        elif c == "{":
            if start is None:
                start = i
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0 and start is not None:
                return re.sub(r"//[^\n]*", "", text[start:i + 1])
        i += 1
    return ""


def cause(reasons):
    last = reasons[-1] if reasons else ""
    for name, words in CAUSES:
        if words in last:
            return name
    return "other: " + last.split(": ", 1)[-1][:60]


def run(shield, target):
    out = subprocess.run([shield, "det", target, "-all"], capture_output=True, text=True)
    funcs, cur = [], None
    for line in (out.stdout + out.stderr).split("\n"):
        m = HEAD.match(line)
        if m:
            path, ln, _, name, verdict = m.groups()
            cur = {"name": name, "verdict": verdict, "reasons": [],
                   "parallel": bool(PARALLEL.search(body(path, int(ln))))}
            funcs.append(cur)
        elif cur is not None and line.startswith("    "):
            cur["reasons"].append(line.strip())
    return funcs


def main():
    shield, label, targets = sys.argv[1], sys.argv[2], sys.argv[3:]
    total = det = par = par_det = par_cond = 0
    causes = {}
    for t in targets:
        for f in run(shield, t):
            total += 1
            ok = f["verdict"] == "det"
            det += ok
            if not f["parallel"]:
                continue
            par += 1
            par_det += ok
            par_cond += f["verdict"].startswith("det when")
            if f["verdict"] == "not det":
                c = cause(f["reasons"])
                causes[c] = causes.get(c, 0) + 1
    print(json.dumps({"set": label, "functions": total, "det": det,
                      "parallel": par, "parallel_det": par_det,
                      "parallel_det_conditional": par_cond,
                      "parallel_not_det_by_cause": causes}))


main()
