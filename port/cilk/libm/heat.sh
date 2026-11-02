#!/bin/sh
# port/cilk/libm/heat.sh BUILD — heat's elision once more, with glibc's sin
# and exp replaced by the values std/num gives for the same arguments, read
# from a table. BUILD is the directory run.sh was given (BUILD=...), after
# `run.sh heat`. Prints the C's grid bits and the port's; they are the same
# when the only difference between the two is the maths library.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
out=$1/heat
SHIELD=${SHIELD:-$here/../../../../sword/shield}
GCC=${GCC:-gcc}
CRUN=${CRUN:-}
$SHIELD "$here/values.sword" -o "$out/values"
"$out/values" > "$out/values.txt"
{
    echo '#include <math.h>'
    echo 'static unsigned long long SIN[512] = {'
    sed -n 's/^sin \(.*\)/0x\1ULL,/p' "$out/values.txt"
    echo '};'
    echo 'static unsigned long long EXP[101] = {'
    sed -n 's/^exp \(.*\)/0x\1ULL,/p' "$out/values.txt"
    echo '};'
    cat <<'C'
static double tsin(double x) {
    int i;
    for (i = 0; i < 512; i++)
        if (0.0 + i * (1.570796326794896558 / 511) == x) {
            double v; memcpy(&v, &SIN[i], 8); return v;
        }
    abort();
}
static double texp(double x) {
    int i;
    for (i = 0; i <= 100; i++)
        if (-2 * (0.0 + i * (0.0000001 / 100)) == x) {
            double v; memcpy(&v, &EXP[i], 8); return v;
        }
    abort();
}
#define sin tsin
#define exp texp
C
} > "$out/table.h"
perl -pe 's|#include <getoptions.h>|#include <getoptions.h>\n#include "table.h"|' "$out/heat.c" > "$out/heat-table.c"
$CRUN $GCC -O2 -ffp-contract=off -std=gnu99 -fcommon -w -I "$out" \
    -o "$out/c-table" "$out/heat-table.c" "$out/rand.c" "$out/getoptions.c" -lm
echo "C with Sword's sin and exp: $($CRUN sh -c "cd '$out' && ./c-table" | grep 'grid bits')"
echo "Sword:                      $(grep 'grid bits' "$out/sword1.out")"
