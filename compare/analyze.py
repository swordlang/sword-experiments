"""The comparison's tables, from results/*/compare.csv, as Markdown on stdout.

For each kernel and platform: the time of every method at every thread count
(the median across rounds of each run's median, in milliseconds), and how many
different answers the method gave across thread counts and rounds.

    python3 compare/analyze.py [results-dir] > results/compare.md
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "results")
kernels = ["sum", "saxpy", "stencil", "mandelbrot", "nbody"]
methods = ["sword", "c-serial", "c-restrict", "c-omp", "c-lanes", "c-lanes-omp",
           "c-fastmath-serial", "c-fastmath-omp", "cpp-thread", "rust-rayon",
           "zig-safe", "zig-fast", "go"]

pieces = ["walked", "walked-mut", "captures", "versioned", "split", "deferred", "lanes"]
methods[1:1] = [f"sword-without-{p}" for p in pieces]

platforms = sorted(p for p in root.iterdir() if (p / "compare.csv").exists())
if not platforms:
    sys.exit(f"no compare.csv under {root}")

for kernel in kernels:
    print(f"## {kernel}\n")
    for platform in platforms:
        times = defaultdict(list)
        checks = defaultdict(set)
        threads = set()
        with open(platform / "compare.csv") as f:
            for row in csv.DictReader(f):
                if row["kernel"] != kernel:
                    continue
                t = int(row["threads"])
                threads.add(t)
                times[row["method"], t].append(int(row["median_ns"]))
                checks[row["method"]].add(row["check"])
        if not checks:
            continue
        ts = sorted(threads)
        print(f"**{platform.name}**, ms\n")
        print("| method | " + " | ".join(str(t) for t in ts) + " | answers |")
        print("|---|" + "---:|" * len(ts) + "---:|")
        for m in [m for m in methods if m in checks]:
            cells = []
            for t in ts:
                v = times.get((m, t))
                cells.append(f"{statistics.median(v) / 1e6:.1f}" if v else "")
            print(f"| {m} | " + " | ".join(cells) + f" | {len(checks[m])} |")
        print()

# The answers each method gave, counted over every platform and thread count
# together: a method with one answer per kernel gives the same bits everywhere.
answers = defaultdict(set)
for platform in platforms:
    with open(platform / "compare.csv") as f:
        for row in csv.DictReader(f):
            answers[row["method"], row["kernel"]].add(row["check"])
print("## Answers across every platform and thread count\n")
print("| method | " + " | ".join(kernels) + " |")
print("|---|" + "---:|" * len(kernels))
for m in methods:
    if any((m, k) in answers for k in kernels):
        print(f"| {m} | " + " | ".join(str(len(answers[m, k])) if (m, k) in answers else ""
                                      for k in kernels) + " |")
