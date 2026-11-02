#!/bin/sh
# port/cilk/run.sh [program...] — each Sword port against the serial elision
# of the Cilk-5.4.6 example it comes from.
#
# Downloads Cilk-5.4.6 (once, into CILK or a temporary directory) at a pinned
# commit and checks its hash. Each example becomes its serial elision: the
# keywords cilk, spawn, sync, inlet and abort taken out, elision.h in place
# of the Cilk library, built with GCC, since an inlet becomes a nested
# function. CRUN, when set, is a prefix that runs GCC and the elision
# somewhere else (a container on a machine without GCC). The C runs in a
# directory with the example's input files, with the arguments on the
# port's "// Args:" line, and the lines of its output that match
# "// Answer:" are the answer. Each "// Patch:" line is a perl substitution
# applied to the elision first, for a program whose own output rounds a
# floating point result: the patch prints its bits instead. The Sword port runs at 1 and at 4
# threads and must print exactly those lines. Prints one line per program:
# program,class,same_answer,threads_agree.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
GCC=${GCC:-gcc}
CRUN=${CRUN:-}
SHIELD=${SHIELD:-$here/../../../sword/shield}
commit=ad2223b731e8d7d5f6969b44a82a9125cd961c19
sha=620ce25f66bd5c622ddf5434c64846ee334954dd0a234963b25d7123c8a775d5
build=${BUILD:-$(mktemp -d)}
[ -n "${BUILD:-}" ] || trap 'rm -rf "$build"' EXIT
cilk=${CILK:-$build/cilk}
if [ ! -d "$cilk/examples" ]; then
    mkdir -p "$cilk"
    curl -sSfL -o "$build/cilk.tar.gz" \
        "https://github.com/jaeger401/cilk/archive/$commit.tar.gz"
    echo "$sha  $build/cilk.tar.gz" | shasum -a 256 -c > /dev/null
    tar -xzf "$build/cilk.tar.gz" -C "$cilk" --strip-components 1
fi

elide() {
    perl -pe 's|#include <cilk-lib.cilkh>|#include "elision.h"|;
              s|#include "config.h"||;
              s/\bcilk[ \t]+//g;
              s/\bspawn[ \t]+//g;
              s/\bsync[ \t]*;/;/g;
              s/\binlet[ \t]+//g;
              s/\babort[ \t]*;/;/g' "$1" > "$2"
}

programs=${*:-$(cd "$here" && ls *.sword | sed 's/\.sword$//')}
for p in $programs; do
    out="$build/$p"
    mkdir -p "$out"
    cp "$here/elision.h" "$cilk/examples/getoptions.c" "$cilk/examples/getoptions.h" \
        "$cilk"/examples/*.input "$out/"
    elide "$cilk/examples/$p.cilk" "$out/$p.c"
    elide "$cilk/examples/rand.cilk" "$out/rand.c"
    sed -n 's|^// Patch: *||p' "$here/$p.sword" | while IFS= read -r patch; do
        perl -pi -e "$patch" "$out/$p.c"
    done
    args=$(sed -n "s|^// Args: *||p" "$here/$p.sword" | head -1)
    answer=$(sed -n 's|^// Answer: *||p' "$here/$p.sword" | head -1)
    $CRUN $GCC -O2 -ffp-contract=off -std=gnu99 -fcommon -w -I "$out" \
        -o "$out/c" "$out/$p.c" "$out/rand.c" "$out/getoptions.c" -lm
    $CRUN sh -c "cd '$out' && ./c $args" > "$out/c.out"
    grep -E "$answer" "$out/c.out" > "$out/c.ans" || true
    $SHIELD "$here/$p.sword" -o "$out/sword"
    SWORD_THREADS=1 "$out/sword" > "$out/sword1.out"
    SWORD_THREADS=4 "$out/sword" > "$out/sword4.out"
    class=$(sed -n 's|^// Class: \([a-z ]*\).*|\1|p' "$here/$p.sword" | head -1)
    same=$(cmp -s "$out/c.ans" "$out/sword1.out" && echo yes || echo no)
    agree=$(cmp -s "$out/sword1.out" "$out/sword4.out" && echo yes || echo no)
    echo "$p,$class,$same,$agree"
done
