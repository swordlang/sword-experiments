"""Copies of the nine Sword ports at PolyBench's LARGE_DATASET, timed.

    python3 -I sword.py <port/polybench> <out dir>

Each copy prints the kernel's time in nanoseconds and a sum of its output
array, in place of the dump. The clock starts where the work the C kernel
does starts: at the kernel call, or at trmm's copy of B, which the port
takes in main.
"""
import os
import re
import shutil
import sys

LARGE = {
    "lu": {"N": 2000}, "ludcmp": {"N": 2000}, "floyd-warshall": {"N": 2800},
    "trmm": {"M": 1000, "N": 1200}, "symm": {"M": 1000, "N": 1200},
    "gramschmidt": {"M": 1000, "N": 1200}, "covariance": {"M": 1200, "N": 1400},
    "correlation": {"M": 1200, "N": 1400}, "deriche": {"W": 4096, "H": 2160},
}
OUT = {"lu": "a", "ludcmp": "x", "floyd-warshall": "path", "trmm": "b",
       "symm": "c", "gramschmidt": "r", "covariance": "cov",
       "correlation": "corr", "deriche": "out"}


def main():
    port, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    shutil.copytree(os.path.join(port, "pb"), os.path.join(out, "pb"), dirs_exist_ok=True)
    for name, sizes in LARGE.items():
        text = open(os.path.join(port, name + ".sword")).read()
        for c, v in sizes.items():
            text, n = re.subn(r"^const %s = \d+$" % c, "const %s = %d" % (c, v), text, flags=re.M)
            assert n == 1, (name, c)
        text = text.replace('import "pb"', 'import "pb"\nimport "std/io"\nimport "std/time"')
        lines = text.split("\n")
        call = next(i for i, l in enumerate(lines) if re.match(r"\s+kernel\(", l))
        begin = call
        if name == "trmm":
            begin = next(i for i, l in enumerate(lines) if "for i in 0..b0.len" in l or "b0[i] = b[i]" in l)
            if "b0[i] = b[i]" in lines[begin]:
                begin -= 1
        o = OUT[name]
        cast = "f64(%s[i])" % o
        after = ["    ns := time.Since(t0).AsNanos()",
                 "    mut sum := 0.0",
                 "    for i in 0..%s.len {" % o,
                 "        sum += %s" % cast,
                 "    }",
                 '    try io.Printf("{} {}\\n", ns, sum)']
        lines = lines[:begin] + ["    t0 := time.Now()"] + lines[begin:call + 1] + after + lines[call + 1:]
        lines = [l for l in lines if "pb.Dump" not in l]
        open(os.path.join(out, name + ".sword"), "w").write("\n".join(lines))
        print(name)


main()
