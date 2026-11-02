#!/bin/sh
# diagnose/run.sh <platform> — the six programs of the diagnostics table, into
# results/<platform>/diagnose.csv and diagnose-messages.txt.
#
# Each Sword program is built as written, with det on the function that
# matters, and what the compiler says is kept; then built again with det taken
# off, and run. The C and Rust programs are built with every warning on, and
# run. RUNS runs each, at THREADS threads for Sword.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
platform=${1:?usage: diagnose/run.sh <platform>}
CC=${CC:-cc}
SHIELD=${SHIELD:-$here/../../sword/shield}
RUNS=${RUNS:-20}
THREADS=${THREADS:-4}
out=$here/../results/$platform
mkdir -p "$out"
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT

$CC -O2 -Wall -Wextra -pedantic -std=c11 -pthread -o "$build/c" "$here/c/diagnose.c" 2> "$build/c-warnings"
RUSTFLAGS="-D warnings" cargo build --quiet --release --locked \
    --manifest-path "$here/rust/Cargo.toml" --target-dir "$build/rust" 2> "$build/rust-warnings"

count() {
    i=0
    while [ $i -lt "$RUNS" ]; do
        "$@"
        i=$((i + 1))
    done | sort -u | wc -l | tr -d ' '
}

: > "$out/diagnose-messages.txt"
echo "program,language,compiles,warnings,runs,answers" > "$out/diagnose.csv"
for p in pool senders poll ticket clock ccall; do
    # The message, with the path of the standard library cut to std/.
    if $SHIELD "$here/sword/$p.sword" -o "$build/refused" > "$build/msg" 2>&1; then
        sword_det=yes
    else
        sword_det=no
    fi
    {
        echo "== $p.sword"
        grep -E ': (error|note): ' "$build/msg" | sed -e "s|^$here/sword/||" -e 's|^.*/std/|std/|'
    } >> "$out/diagnose-messages.txt"
    echo "$p,sword-det,$sword_det,,," >> "$out/diagnose.csv"
    sed 's/^det func/func/' "$here/sword/$p.sword" > "$build/$p.sword"
    $SHIELD "$build/$p.sword" -o "$build/$p"
    echo "$p,sword,yes,0,$RUNS,$(SWORD_THREADS=$THREADS count "$build/$p")" >> "$out/diagnose.csv"
    echo "$p,c,yes,$(grep -c warning "$build/c-warnings" || true),$RUNS,$(count "$build/c" "$p")" >> "$out/diagnose.csv"
    echo "$p,rust,yes,0,$RUNS,$(count "$build/rust/release/diagnose" "$p")" >> "$out/diagnose.csv"
done
cp "$here/rust/Cargo.lock" "$out/diagnose-Cargo.lock"
echo "done: $out/diagnose.csv"
