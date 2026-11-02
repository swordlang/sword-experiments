# Results

## gh-linux-arm64

```
platform: gh-linux-arm64
date: 2026-11-02T17:19:11Z
uname: Linux 7.0.0-1017-azure aarch64
cpu: 0xd49
cores: 4
cc: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
openmp: -fopenmp
shield: shield 0.4.1 (Temper)
sword commit: edc5ba8
python: Python 3.12.3
threads: 1 2 3 4 6 8 10 16
sum_n: 10000000 mc_n: 10000000 math_n: 1000000 reps: 7
only: all
note: GitHub-hosted runner ubuntu-24.04-arm, shared with other jobs; times are indicative
```

### E1 — summation of 10^7 doubles

**uniform** (correctly rounded sum 5000576.9172228221)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 237 | 6.19 | 6.19 | 1 |
| c-omp | 7 of 8 | 21–237 | 6.48 | 1.61 | 4 |
| c-ompkahan | 1 of 8 | 0 | 23.88 | 5.96 | 4 |
| sword-plain | 1 of 8 | 0 | 2.56 | 0.65 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.34 | 6.37 | 4 |
| sword-exact | 1 of 8 | 0 | 26.77 | 7.68 | 4 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 6.56 | 6.56 | 1 |
| c-omp | 8 of 8 | 37–243 | 6.97 | 1.71 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 23.76 | 5.97 | 4 |
| sword-plain | 1 of 8 | 35 | 2.38 | 0.66 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.21 | 6.37 | 4 |
| sword-exact | 1 of 8 | 0 | 45.77 | 12.64 | 6 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 3 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 4 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732607 | 49.5 | 12.6 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 48.0 | 12.0 | 4 |
| c-philox | 8 of 8 | 0.74688899599929437 … 0.74688899599935521 | 180.0 | 45.2 | 4 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 205.3 | 51.6 | 6 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 85.3 | 21.5 | 4 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 265.8 | 69.5 | 6 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 15.41 | 16.95 |
| sinnear | 6.98 | 3.16 |
| cos | 15.70 | 17.01 |
| exp | 6.14 | 8.78 |
| expunit | 3.23 | 7.17 |
| log | 4.05 | 8.30 |

## gh-linux-x86_64

```
platform: gh-linux-x86_64
date: 2026-11-02T17:19:11Z
uname: Linux 7.0.0-1017-azure x86_64
cpu: AMD EPYC 7763 64-Core Processor
cores: 4
cc: gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
openmp: -fopenmp
shield: shield 0.4.1 (Temper)
sword commit: edc5ba8
python: Python 3.14.4
threads: 1 2 3 4 6 8 10 16
sum_n: 10000000 mc_n: 10000000 math_n: 1000000 reps: 7
only: all
note: GitHub-hosted runner ubuntu-latest, shared with other jobs; times are indicative
```

### E1 — summation of 10^7 doubles

**uniform** (correctly rounded sum 5000576.9172228221)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 237 | 9.57 | 9.57 | 1 |
| c-omp | 7 of 8 | 21–237 | 9.57 | 2.46 | 4 |
| c-ompkahan | 1 of 8 | 0 | 37.52 | 9.51 | 4 |
| sword-plain | 1 of 8 | 0 | 3.70 | 1.81 | 8 |
| sword-kahan | 1 of 8 | 0 | 12.82 | 6.36 | 4 |
| sword-exact | 1 of 8 | 0 | 31.65 | 15.85 | 2 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 9.55 | 9.55 | 1 |
| c-omp | 8 of 8 | 36–243 | 9.58 | 2.43 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 37.53 | 9.50 | 4 |
| sword-plain | 1 of 8 | 35 | 3.68 | 1.76 | 6 |
| sword-kahan | 1 of 8 | 0 | 13.19 | 6.39 | 4 |
| sword-exact | 1 of 8 | 0 | 56.35 | 22.40 | 6 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 3 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 5 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440227 … 0.74692123466732596 | 51.5 | 22.3 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 47.6 | 21.5 | 4 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.74688899599935521 | 221.3 | 79.1 | 4 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 250.5 | 89.7 | 4 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 129.6 | 39.7 | 8 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 302.7 | 114.6 | 6 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 20.01 | 23.33 |
| sinnear | 9.45 | 2.83 |
| cos | 19.79 | 23.15 |
| exp | 7.68 | 7.91 |
| expunit | 3.45 | 7.92 |
| log | 3.78 | 7.40 |

## gh-macos-arm64

```
platform: gh-macos-arm64
date: 2026-11-02T17:28:59Z
uname: Darwin 25.6.0 arm64
cpu: Apple M1 (Virtual)
cores: 3
cc: Apple clang version 21.0.0 (clang-2100.1.1.101)
openmp: -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp
shield: shield 0.4.1 (Temper)
sword commit: edc5ba8
python: Python 3.15.1
threads: 1 2 3 4 6 8 10 16
sum_n: 10000000 mc_n: 10000000 math_n: 1000000 reps: 7
only: all
note: GitHub-hosted runner macos-latest, shared with other jobs; times are indicative
```

### E1 — summation of 10^7 doubles

**uniform** (correctly rounded sum 5000576.9172228221)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 237 | 11.20 | 11.20 | 1 |
| c-omp | 7 of 8 | 20–237 | 12.25 | 4.58 | 8 |
| c-ompkahan | 1 of 8 | 0 | 47.42 | 17.16 | 16 |
| sword-plain | 1 of 8 | 0 | 1.96 | 1.56 | 8 |
| sword-kahan | 1 of 8 | 0 | 13.40 | 5.18 | 8 |
| sword-exact | 1 of 8 | 0 | 29.05 | 11.57 | 10 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 13.64 | 13.64 | 1 |
| c-omp | 8 of 8 | 37–243 | 11.17 | 4.23 | 10 |
| c-ompkahan | 3 of 8 | 0–1 | 53.47 | 16.91 | 6 |
| sword-plain | 1 of 8 | 35 | 1.69 | 1.57 | 16 |
| sword-kahan | 1 of 8 | 0 | 11.96 | 5.10 | 8 |
| sword-exact | 1 of 8 | 0 | 60.47 | 20.31 | 10 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 1 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 1 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732596 | 74.7 | 24.4 | 16 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 39.9 | 17.4 | 10 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.74688899599935521 | 130.3 | 58.4 | 6 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 330.8 | 108.6 | 10 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 174.5 | 48.1 | 10 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 422.9 | 125.7 | 10 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 8.43 | 20.80 |
| sinnear | 1.97 | 2.68 |
| cos | 8.69 | 20.15 |
| exp | 7.21 | 5.71 |
| expunit | 2.48 | 6.56 |
| log | 2.78 | 5.81 |

## E1, E2 — Sword's answers on different platforms

| experiment | method | platforms | runs | distinct results |
|---|---|---|---|---|
| E1 mixed | c-serial | 3 | 3 | 1 |
| E1 mixed | c-omp | 3 | 24 | 12 |
| E1 mixed | c-ompkahan | 3 | 24 | 3 |
| E1 mixed | sword-plain | 3 | 24 | 1 |
| E1 mixed | sword-kahan | 3 | 24 | 1 |
| E1 mixed | sword-exact | 3 | 24 | 1 |
| E1 uniform | c-serial | 3 | 3 | 1 |
| E1 uniform | c-omp | 3 | 24 | 10 |
| E1 uniform | c-ompkahan | 3 | 24 | 1 |
| E1 uniform | sword-plain | 3 | 24 | 1 |
| E1 uniform | sword-kahan | 3 | 24 | 1 |
| E1 uniform | sword-exact | 3 | 24 | 1 |
| E2 | c-thread | 3 | 24 | 11 |
| E2 | c-index | 3 | 24 | 10 |
| E2 | c-philox | 3 | 24 | 10 |
| E2 | sword-plain | 3 | 24 | 1 |
| E2 | sword-mix | 3 | 24 | 1 |
| E2 | sword-exact | 3 | 24 | 1 |

## E3 — the same arguments on different platforms

| function | platforms | C library: results that differ | std/num: results that differ |
|---|---|---|---|
| sin | gh-linux-arm64 vs gh-linux-x86_64 | 0 of 1000000 | 0 of 1000000 |
| sin | gh-linux-arm64 vs gh-macos-arm64 | 40563 of 1000000 | 0 of 1000000 |
| sin | gh-linux-x86_64 vs gh-macos-arm64 | 40563 of 1000000 | 0 of 1000000 |
| cos | gh-linux-arm64 vs gh-linux-x86_64 | 0 of 1000000 | 0 of 1000000 |
| cos | gh-linux-arm64 vs gh-macos-arm64 | 40715 of 1000000 | 0 of 1000000 |
| cos | gh-linux-x86_64 vs gh-macos-arm64 | 40715 of 1000000 | 0 of 1000000 |
| exp | gh-linux-arm64 vs gh-linux-x86_64 | 0 of 1000000 | 0 of 1000000 |
| exp | gh-linux-arm64 vs gh-macos-arm64 | 1765 of 1000000 | 0 of 1000000 |
| exp | gh-linux-x86_64 vs gh-macos-arm64 | 1765 of 1000000 | 0 of 1000000 |
| log | gh-linux-arm64 vs gh-linux-x86_64 | 0 of 1000000 | 0 of 1000000 |
| log | gh-linux-arm64 vs gh-macos-arm64 | 7 of 1000000 | 0 of 1000000 |
| log | gh-linux-x86_64 vs gh-macos-arm64 | 7 of 1000000 | 0 of 1000000 |

