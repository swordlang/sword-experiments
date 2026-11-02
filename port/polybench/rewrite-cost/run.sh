#!/bin/sh
# port/polybench/rewrite-cost/run.sh <rounds> <out.csv> — what the nine "work"
# rewrites cost in time, apart from the language.
#
# Each kernel three ways: C as PolyBench has it with OpenMP on the parallel
# loop the port names (orig), C rewritten the way the Sword port is, the same
# loops marked (rewr), and the Sword port. First, at SMALL_DATASET with the
# dump in "%a", both C versions must give the bits of unmodified PolyBench at
# 1 and 4 threads; then at LARGE_DATASET, alternating within each round, at 1
# and 4 threads. Kernel time only: PolyBench's timer, a clock in the Sword copy.
# analyze.py prints the medians.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
CC=${CC:-clang}
SHIELD=${SHIELD:-$here/../../../../sword/shield}
if [ -z "${OMPFLAGS:-}" ]; then
    if [ -d /opt/homebrew/opt/libomp ]; then
        o=/opt/homebrew/opt/libomp
        OMPFLAGS="-Xpreprocessor -fopenmp -I$o/include -L$o/lib -lomp"
    else
        OMPFLAGS=-fopenmp
    fi
fi
rounds=$1; out=$2
sha=426519ee8443a5f2175de6a3e9328cda8917a5e33053d0e8f59855ab56d689a4
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT
pb=$build/pb
mkdir -p "$pb"
curl -sSfL -o "$build/pb.tar.gz" \
    "https://sourceforge.net/projects/polybench/files/polybench-c-4.2.1-beta.tar.gz/download"
echo "$sha  $build/pb.tar.gz" | shasum -a 256 -c > /dev/null
tar -xzf "$build/pb.tar.gz" -C "$pb" --strip-components 1
find "$pb" -name '*.h' -exec sed -i.orig -e 's/"%0.2lf "/"%a "/' -e 's/"%0.2f "/"%a "/' {} +
U=$pb/utilities

python3 -I "$here/kernels.py" "$pb" "$build/gen" > "$build/dirs.txt"
python3 -I "$here/sword.py" "$here/.." "$build/sw" > /dev/null

while read -r k dir; do
    g=$build/gen/$k
    $CC -O2 -ffp-contract=off -DSMALL_DATASET -DPOLYBENCH_DUMP_ARRAYS -I"$U" -I"$dir" \
        -o "$g/pb" "$dir/$k.c" "$U/polybench.c" -lm
    "$g/pb" 2> "$g/pb.out" > /dev/null
    for v in orig rewr; do
        # shellcheck disable=SC2086
        $CC -O2 -ffp-contract=off $OMPFLAGS -DSMALL_DATASET -DPOLYBENCH_DUMP_ARRAYS \
            -I"$U" -I"$dir" -o "$g/$v.small" "$g/$v.c" "$U/polybench.c" -lm
        for t in 1 4; do
            OMP_NUM_THREADS=$t "$g/$v.small" 2> "$g/$v$t.out" > /dev/null
            cmp -s "$g/pb.out" "$g/$v$t.out" || { echo "$k: $v at $t threads is not PolyBench's" >&2; exit 1; }
        done
        # shellcheck disable=SC2086
        $CC -O2 -ffp-contract=off $OMPFLAGS -DLARGE_DATASET -DPOLYBENCH_TIME \
            -I"$U" -I"$dir" -o "$g/$v.large" "$g/$v.c" "$U/polybench.c" -lm
    done
    (cd "$build/sw" && $SHIELD "$k.sword" -o "$k.bin")
done < "$build/dirs.txt"

echo "round,kernel,threads,version,seconds" > "$out"
for r in $(seq 1 "$rounds"); do
    while read -r k dir; do
        for t in 1 4; do
            for v in orig rewr sword; do
                if [ $v = sword ]; then
                    ns=$(SWORD_THREADS=$t "$build/sw/$k.bin" | cut -d' ' -f1)
                    s=$(echo "scale=6; $ns / 1000000000" | bc)
                else
                    s=$(OMP_NUM_THREADS=$t "$build/gen/$k/$v.large" | tail -1)
                fi
                echo "$r,$k,$t,$v,$s" >> "$out"
            done
        done
    done < "$build/dirs.txt"
done
