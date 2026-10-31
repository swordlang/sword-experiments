#!/bin/sh
# compare/run.sh <platform> — the five kernels in every language, into
# results/<platform>/compare.csv, with the versions and flags in compare-env.txt.
#
# Needs a built Sword compiler (SHIELD), a C and a C++ compiler with OpenMP
# (CC, CXX), and go, cargo and zig on the PATH. LANGS picks a subset.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
platform=${1:?usage: compare/run.sh <platform>}
CC=${CC:-cc}
CXX=${CXX:-c++}
SHIELD=${SHIELD:-$here/../../sword/shield}
LANGS=${LANGS:-"sword c cpp rust zig go"}
KERNELS=${KERNELS:-"sum saxpy stencil mandelbrot nbody"}
THREADS=${THREADS:-"1 2 4 8 16"}
REPS=${REPS:-5}
ROUNDS=${ROUNDS:-3}
NOTE=${NOTE:-}
if [ -z "${OMPFLAGS:-}" ] && [ "$(uname)" = Darwin ]; then
    omp=$(brew --prefix libomp 2>/dev/null || echo /opt/homebrew/opt/libomp)
    OMPFLAGS="-Xpreprocessor -fopenmp -I$omp/include -L$omp/lib -lomp"
fi
OMPFLAGS=${OMPFLAGS:--fopenmp}
CFLAGS="-O2"
CXXFLAGS="-std=c++17 -O2 -pthread"
out=$here/../results/$platform
mkdir -p "$out"
build=$(mktemp -d)
trap 'rm -rf "$build"' EXIT

has() { case " $LANGS " in *" $1 "*) return 0 ;; esac; return 1; }

{
    echo "platform: $platform"
    echo "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "uname: $(uname -srm)"
    if [ -r /proc/cpuinfo ]; then
        echo "cpu: $(grep -m1 -E 'model name|^Model|CPU part' /proc/cpuinfo | cut -d: -f2- | sed 's/^ //')"
    else
        echo "cpu: $(sysctl -n machdep.cpu.brand_string 2>/dev/null)"
    fi
    echo "cores: $(getconf _NPROCESSORS_ONLN)"
    echo "threads: $THREADS reps: $REPS rounds: $ROUNDS"
    has sword && echo "sword: $($SHIELD --version), commit ${SWORD_REV:-$(git -C "$(dirname "$SHIELD")" rev-parse --short HEAD 2>/dev/null || echo unknown)}, default flags"
    has c && echo "c: $($CC --version | head -1); $CFLAGS $OMPFLAGS"
    has cpp && echo "cpp: $($CXX --version | head -1); $CXXFLAGS"
    has rust && echo "rust: $(rustc --version), $(cargo --version); cargo build --release; rayon $(sed -n 's/^rayon = "=\(.*\)"/\1/p' "$here/rust/Cargo.toml")"
    has zig && echo "zig: $(zig version); -O safe and -O fast"
    has go && echo "go: $(go version); go build"
    [ -n "$NOTE" ] && echo "note: $NOTE"
} > "$out/compare-env.txt"

# Each entry is "name|binary|method": the C program takes its method between
# the kernel and the thread count, the others take <kernel> <threads> <reps>.
progs=$build/progs
: > "$progs"
if has sword; then
    $SHIELD "$here/sword/bench.sword" -o "$build/sword"
    echo "sword|$build/sword|" >> "$progs"
fi
if has c; then
    $CC $CFLAGS $OMPFLAGS -o "$build/c" "$here/c/bench.c" -lm
    printf '%s\n' "c-serial|$build/c|serial" "c-restrict|$build/c|restrict" "c-omp|$build/c|omp" >> "$progs"
fi
if has cpp; then
    $CXX $CXXFLAGS -o "$build/cpp" "$here/cpp/bench.cpp"
    echo "cpp-thread|$build/cpp|" >> "$progs"
fi
if has rust; then
    cargo build --quiet --release --manifest-path "$here/rust/Cargo.toml" --target-dir "$build/rust"
    cp "$here/rust/Cargo.lock" "$out/compare-Cargo.lock"
    echo "rust-rayon|$build/rust/release/bench|" >> "$progs"
fi
if has zig; then
    for mode in safe fast; do
        zig build-exe -O $mode "$here/zig/bench.zig" -femit-bin="$build/zig-$mode" \
            --cache-dir "$build/zig-cache" --global-cache-dir "$build/zig-cache"
    done
    printf '%s\n' "zig-safe|$build/zig-safe|" "zig-fast|$build/zig-fast|" >> "$progs"
fi
if has go; then
    (cd "$here/go" && go build -o "$build/go" .)
    echo "go|$build/go|" >> "$progs"
fi

# Rounds go through every program in turn, so that no language always runs on
# a cold or a hot machine; analyze.py takes the median across rounds.
echo "round,kernel,method,threads,check,median_ns" > "$out/compare.csv"
for round in $(seq 1 "$ROUNDS"); do
    for k in $KERNELS; do
        while IFS='|' read -r name bin method; do
            case $name in
                c-serial|c-restrict) ts=1 ;;
                *) ts=$THREADS ;;
            esac
            for t in $ts; do
                if [ -n "$method" ]; then
                    line=$("$bin" "$k" "$method" "$t" "$REPS" < /dev/null)
                else
                    line=$(SWORD_THREADS=$t "$bin" "$k" "$t" "$REPS" < /dev/null)
                fi
                echo "$round,$line" >> "$out/compare.csv"
            done
        done < "$progs"
    done
    echo "round $round done"
done
echo "done: $out/compare.csv"
