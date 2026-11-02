"""The diagnostics' table, from <dir>/*/diagnose.csv, as Markdown on stdout.

For each program and language: whether it compiled, with how many warnings,
and how many different answers it gave in its runs, on every platform; then
what Sword said when the function was marked det.

    python3 diagnose/analyze.py results/e5 > results/e5/diagnose.md
"""
import csv
import sys
from pathlib import Path

root = Path(sys.argv[1])
platforms = sorted(p for p in root.iterdir() if (p / "diagnose.csv").exists())
if not platforms:
    sys.exit(f"no diagnose.csv under {root}")

rows = {}
order = []
for p in platforms:
    with open(p / "diagnose.csv") as f:
        for r in csv.DictReader(f):
            key = (r["program"], r["language"])
            if key not in rows:
                rows[key] = {}
                order.append(key)
            rows[key][p.name] = r


def cell(r):
    if r is None:
        return ""
    if r["compiles"] != "yes":
        return "refused"
    return f'{r["answers"]} of {r["runs"]}'


print("## Answers in repeated runs\n")
print("Distinct answers out of the runs; *refused* means it did not compile.\n")
print("| program | language | " + " | ".join(p.name for p in platforms) + " |")
print("|---|---|" + "---:|" * len(platforms))
for key in order:
    print(f"| {key[0]} | {key[1]} | " + " | ".join(cell(rows[key].get(p.name)) for p in platforms) + " |")

warned = [(k, p) for k in order for p, r in rows[k].items() if r["warnings"] not in ("", "0")]
print("\nWarnings from the compilers that accepted them: "
      + ("none." if not warned else ", ".join(f"{k[0]}/{k[1]} on {p}" for k, p in warned)))

messages = platforms[0] / "diagnose-messages.txt"
if messages.exists():
    print(f"\n## What Sword says with det\n\nFrom {platforms[0].name}; the messages are the same on every platform.\n")
    print("```")
    print(messages.read_text().rstrip())
    print("```")
