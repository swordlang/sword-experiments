"""Medians of a run.sh CSV, per kernel and thread count.

    python3 -I analyze.py <file.csv>

rewr/orig is what the rewrite costs in C; sword/rewr is what is left, the
language against the same loops in C.
"""
import csv
import statistics
import sys


def main():
    times = {}
    kernels = []
    for row in csv.DictReader(open(sys.argv[1])):
        k = row["kernel"]
        if k not in kernels:
            kernels.append(k)
        times.setdefault((k, int(row["threads"]), row["version"]), []).append(float(row["seconds"]))
    print("| kernel | threads | C, s | C rewritten, s | Sword, s | rewritten / C | Sword / rewritten |")
    print("|---|---|---|---|---|---|---|")
    for k in kernels:
        for t in (1, 4):
            m = {v: statistics.median(times[(k, t, v)]) for v in ("orig", "rewr", "sword")}
            print("| %s | %d | %.3f | %.3f | %.3f | %.2f | %.2f |" % (
                k, t, m["orig"], m["rewr"], m["sword"], m["rewr"] / m["orig"], m["sword"] / m["rewr"]))


main()
