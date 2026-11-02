#!/bin/sh
# det/run.sh — how much of the code that runs in parallel the compiler infers
# det, in five sets: the PolyBench and Cilk ports, the Sword programs of these
# experiments, the language's own tests that compile, and its standard
# library, each package listed as a library. One line of JSON per set into
# results/det.jsonl, and the table on stdout.
#
# Needs the language's repository (SWORD) with its compiler built.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
SWORD=${SWORD:-$here/../../sword}
SHIELD=${SHIELD:-$SWORD/shield}
out=$here/../results/det.jsonl
p() { python3 -I "$here/parallel.py" "$SHIELD" "$@"; }
# The diagnose programs are left out: each is written to be refused.
experiments="$here/../compare/sword/bench.sword $here/../compare/sword/rows.sword
    $here/../math/num.sword $here/../mc/mc.sword $here/../sum/sum.sword"
tests=$(grep -L '^// expect-error' "$SWORD"/tests/*.sword)
{
    p polybench "$here"/../port/polybench/*.sword
    p cilk "$here"/../port/cilk/*.sword
    # shellcheck disable=SC2086
    p experiments $experiments
    # shellcheck disable=SC2086
    p tests $tests
    p std "$SWORD"/std/*/
} > "$out"
echo "shield: $($SHIELD --version), commit $(git -C "$SWORD" rev-parse --short HEAD)"
python3 -I - "$out" <<'PY'
import json, sys
print("| set | functions | det | parallel | parallel and det | not det, by cause |")
print("|---|---:|---:|---:|---:|---|")
for line in open(sys.argv[1]):
    d = json.loads(line)
    causes = ", ".join(f"{k} {v}" for k, v in sorted(d["parallel_not_det_by_cause"].items(), key=lambda kv: -kv[1]))
    print(f"| {d['set']} | {d['functions']} | {d['det']} | {d['parallel']} | {d['parallel_det']} | {causes} |")
PY
