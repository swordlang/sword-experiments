#!/bin/sh
# port/polybench/run.sh [kernel...] — each Sword port against PolyBench's own C.
#
# Downloads PolyBench/C 4.2.1 (once, into POLYBENCH or a temporary directory),
# checks its hash, and builds every kernel with SMALL_DATASET, the arrays
# dumped, and "%a" in place of "%0.2lf " and "%0.2f " so the dump is exact.
# Each Sword port runs at 1 and at 4 threads; compare.py says whether its
# arrays are the C's, bit for bit. Prints one line per kernel:
# kernel,class,same_bits,threads_agree.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
CC=${CC:-cc}
SHIELD=${SHIELD:-$here/../../../sword/shield}
sha=426519ee8443a5f2175de6a3e9328cda8917a5e33053d0e8f59855ab56d689a4
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT
pb=${POLYBENCH:-$build/pb}
if [ ! -d "$pb/utilities" ]; then
    mkdir -p "$pb"
    curl -sSfL -o "$build/pb.tar.gz" \
        "https://sourceforge.net/projects/polybench/files/polybench-c-4.2.1-beta.tar.gz/download"
    echo "$sha  $build/pb.tar.gz" | shasum -a 256 -c > /dev/null
    tar -xzf "$build/pb.tar.gz" -C "$pb" --strip-components 1
fi

kernels=${*:-$(cd "$here" && ls *.sword | sed 's/\.sword$//')}
for k in $kernels; do
    src=$(cd "$pb" && sed 's|^\./||' utilities/benchmark_list | grep "/$k/$k.c$")
    dir=$(dirname "$pb/$src")
    mkdir -p "$build/$k"
    cp "$dir"/*.c "$dir"/*.h "$build/$k/"
    sed -i.orig -e 's/"%0.2lf "/"%a "/' -e 's/"%0.2f "/"%a "/' "$build/$k/$k.h"
    $CC -O2 -ffp-contract=off -DSMALL_DATASET -DPOLYBENCH_DUMP_ARRAYS -I "$pb/utilities" \
        -o "$build/$k/c" "$build/$k/$k.c" "$pb/utilities/polybench.c" -lm
    "$build/$k/c" 2> "$build/$k/c.out" > /dev/null
    $SHIELD "$here/$k.sword" -o "$build/$k/sword"
    SWORD_THREADS=1 "$build/$k/sword" > "$build/$k/sword1.out"
    SWORD_THREADS=4 "$build/$k/sword" > "$build/$k/sword4.out"
    class=$(sed -n 's|^// Class: \([a-z ]*\).*|\1|p' "$here/$k.sword" | head -1)
    same=$(python3 -I "$here/compare.py" "$build/$k/c.out" "$build/$k/sword1.out")
    agree=$(cmp -s "$build/$k/sword1.out" "$build/$k/sword4.out" && echo yes || echo no)
    echo "$k,$class,$same,$agree"
done
