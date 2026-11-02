#!/bin/sh
# port/cilk/fftsizes.sh BUILD — after BUILD=... ./run.sh fft, compares fft
# with its serial elision at sizes that reach every codelet and the general
# radix, on the input re = i, im = i / 2 instead of the program's ones,
# whose transform is nearly all zeros. Prints one line per size.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
build=$1
CRUN=${CRUN:-}
SHIELD=${SHIELD:-$here/../../../sword/shield}
t=$build/fftsizes
mkdir -p "$t"
cp "$build"/fft/*.c "$build"/fft/*.h "$t/"
perl -pi -e 's/c_re\(in\[i\]\) = 1\.0;/c_re(in[i]) = i;/; s/c_im\(in\[i\]\) = 1\.0;/c_im(in[i]) = 0.5 * i;/' "$t/fft.c"
$CRUN sh -c "cd '$t' && gcc -O2 -ffp-contract=off -std=gnu99 -fcommon -w -I. -o c fft.c rand.c getoptions.c -lm"
for n in 1048576 1966080 1000 36 64 32 4096 6 12 97 2187 393216; do
    perl -pe "s/n := i64\(1024 \* 1024\)/n := i64($n)/; s/x: Cx\{re: 1\.0, im: 1\.0\}/x: Cx{re: f32(i64(i)), im: f32(0.5 * f64(i))}/" "$here/fft.sword" > "$t/f.sword"
    $SHIELD "$t/f.sword" -o "$t/s"
    c=$($CRUN sh -c "cd '$t' && ./c -n $n" | grep 'out bits')
    s1=$(SWORD_THREADS=1 "$t/s" | grep 'out bits')
    s4=$(SWORD_THREADS=4 "$t/s" | grep 'out bits')
    same=$([ "$c" = "$s1" ] && echo yes || echo no)
    agree=$([ "$s1" = "$s4" ] && echo yes || echo no)
    echo "fft -n $n,$same,$agree"
done
