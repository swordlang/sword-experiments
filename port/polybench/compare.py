"""compare.py <c dump> <sword dump>: whether the arrays are the same, bit for bit.

The C dump is PolyBench's, with "%a" for every element, between "begin dump:"
and "end   dump:" lines; a kernel that prints its newline after an element
leaves the first one glued to the array's name. The Sword one has a "== NAME"
line per array and the bits of each element in hex, one a line, or "== NAME
ints" and decimals for a kernel whose type is int. Prints "yes", or "no" with
the first place they differ and how far apart they are: in ULPs for floats.
"""
import re
import struct
import sys


def c_arrays(path):
    arrays, name = {}, None
    for line in open(path):
        m = re.match(r"begin dump: ([A-Za-z_]\w*?)(-?0x.*)?$", line)
        if m:
            name = m.group(1)
            arrays[name] = []
            line = m.group(2) or ""
        if line.startswith("end   dump:"):
            name = None
            continue
        if name:
            for tok in line.split():
                if "0x" not in tok:
                    arrays[name].append(("int", int(tok)))
                    continue
                bits = struct.unpack("<Q", struct.pack("<d", float.fromhex(tok)))[0]
                arrays[name].append(bits)
    return arrays


def sword_arrays(path):
    arrays, name, ints = {}, None, False
    for line in open(path):
        line = line.strip()
        if line.startswith("== "):
            name, _, kind = line[3:].partition(" ")
            ints = kind == "ints"
            arrays[name] = []
        elif line and name:
            arrays[name].append(("int", int(line)) if ints else int(line, 16))
    return arrays


def ordered(b):
    return b if b < 1 << 63 else (1 << 63) - b


def distance(x, y):
    if isinstance(x, tuple) != isinstance(y, tuple):
        return float("inf")
    if isinstance(x, tuple):
        return abs(x[1] - y[1])
    return abs(ordered(x) - ordered(y))


c, s = c_arrays(sys.argv[1]), sword_arrays(sys.argv[2])
if sorted(c) != sorted(s):
    print(f"no: arrays {sorted(c)} against {sorted(s)}")
    sys.exit(0)
worst = 0
first = None
for name in c:
    if len(c[name]) != len(s[name]):
        print(f"no: {name} has {len(c[name])} elements against {len(s[name])}")
        sys.exit(0)
    for i, (x, y) in enumerate(zip(c[name], s[name])):
        if x != y:
            worst = max(worst, distance(x, y))
            if first is None:
                first = (name, i)
print("yes" if first is None else f"no: first at {first[0]}[{first[1]}], at most {worst} apart")
