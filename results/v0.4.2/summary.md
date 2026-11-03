# Results

## gh-linux-arm64

```
platform: gh-linux-arm64
date: 2026-11-02T22:27:32Z
uname: Linux 7.0.0-1017-azure aarch64
cpu: 0xd49
cores: 4
cc: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
openmp: -fopenmp
shield: shield 0.4.2 (Temper)
sword commit: 7f186d7
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
| c-serial | 1 of 1 | 237 | 6.55 | 6.55 | 1 |
| c-omp | 7 of 8 | 21–237 | 7.14 | 1.61 | 4 |
| c-ompkahan | 1 of 8 | 0 | 23.83 | 5.95 | 4 |
| sword-plain | 1 of 8 | 0 | 3.34 | 0.71 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.38 | 6.37 | 4 |
| sword-exact | 1 of 8 | 0 | 26.73 | 7.66 | 4 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 6.52 | 6.52 | 1 |
| c-omp | 8 of 8 | 37–243 | 6.95 | 1.58 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 23.75 | 5.96 | 4 |
| sword-plain | 1 of 8 | 35 | 2.51 | 0.64 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.31 | 6.41 | 4 |
| sword-exact | 1 of 8 | 0 | 45.79 | 13.10 | 4 |

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
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732596 | 49.5 | 12.4 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 48.1 | 12.0 | 4 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.7468889959993551 | 179.9 | 45.1 | 8 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 205.4 | 51.9 | 10 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 85.1 | 21.5 | 6 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 265.2 | 70.0 | 8 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 15.40 | 16.96 |
| sinnear | 6.96 | 3.18 |
| cos | 15.67 | 16.95 |
| exp | 6.16 | 8.77 |
| expunit | 3.26 | 7.16 |
| log | 4.05 | 8.30 |

## gh-linux-x86_64

```
platform: gh-linux-x86_64
date: 2026-11-02T22:25:54Z
uname: Linux 7.0.0-1017-azure x86_64
cpu: AMD EPYC 9V74 80-Core Processor
cores: 4
cc: gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
openmp: -fopenmp
shield: shield 0.4.2 (Temper)
sword commit: 7f186d7
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
| c-serial | 1 of 1 | 237 | 10.59 | 10.59 | 1 |
| c-omp | 7 of 8 | 21–237 | 10.60 | 2.68 | 4 |
| c-ompkahan | 1 of 8 | 0 | 42.27 | 10.65 | 4 |
| sword-plain | 1 of 8 | 0 | 2.25 | 1.63 | 3 |
| sword-kahan | 1 of 8 | 0 | 14.49 | 7.16 | 3 |
| sword-exact | 1 of 8 | 0 | 33.75 | 16.28 | 8 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 10.59 | 10.59 | 1 |
| c-omp | 8 of 8 | 37–243 | 10.59 | 2.68 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 42.30 | 10.62 | 4 |
| sword-plain | 1 of 8 | 35 | 2.16 | 1.57 | 8 |
| sword-kahan | 1 of 8 | 0 | 14.51 | 7.15 | 4 |
| sword-exact | 1 of 8 | 0 | 67.51 | 25.01 | 6 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 3 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 6 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732596 | 54.9 | 21.2 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 43.8 | 20.3 | 4 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.74688899599935521 | 191.6 | 78.5 | 4 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 269.2 | 94.7 | 4 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 145.1 | 41.9 | 4 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 311.0 | 121.6 | 8 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 22.28 | 25.07 |
| sinnear | 10.42 | 2.81 |
| cos | 22.10 | 24.95 |
| exp | 8.43 | 7.85 |
| expunit | 3.88 | 8.54 |
| log | 4.23 | 8.11 |

## gh-macos-arm64

```
platform: gh-macos-arm64
date: 2026-11-02T22:28:44Z
uname: Darwin 25.6.0 arm64
cpu: Apple M1 (Virtual)
cores: 3
cc: Apple clang version 21.0.0 (clang-2100.1.1.101)
openmp: -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp
shield: shield 0.4.2 (Temper)
sword commit: 7f186d7
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
| c-serial | 1 of 1 | 237 | 11.43 | 11.43 | 1 |
| c-omp | 7 of 8 | 20–237 | 11.94 | 4.05 | 3 |
| c-ompkahan | 1 of 8 | 0 | 49.22 | 15.27 | 4 |
| sword-plain | 1 of 8 | 0 | 1.60 | 1.60 | 1 |
| sword-kahan | 1 of 8 | 0 | 13.16 | 4.49 | 4 |
| sword-exact | 1 of 8 | 0 | 26.14 | 9.50 | 10 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 13.78 | 13.78 | 1 |
| c-omp | 8 of 8 | 37–243 | 12.58 | 4.56 | 6 |
| c-ompkahan | 3 of 8 | 0–1 | 51.30 | 15.66 | 8 |
| sword-plain | 1 of 8 | 35 | 3.88 | 1.46 | 4 |
| sword-kahan | 1 of 8 | 0 | 15.19 | 3.98 | 4 |
| sword-exact | 1 of 8 | 0 | 58.08 | 16.29 | 6 |

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
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732596 | 75.9 | 19.7 | 10 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 43.1 | 12.6 | 16 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.74688899599935521 | 124.5 | 40.9 | 3 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 271.5 | 80.0 | 8 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 160.9 | 40.9 | 4 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 417.5 | 106.9 | 8 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 8.65 | 20.33 |
| sinnear | 1.87 | 2.73 |
| cos | 8.58 | 21.63 |
| exp | 6.00 | 5.47 |
| expunit | 2.74 | 6.56 |
| log | 3.06 | 6.20 |

## E1, E2 — Sword's answers on different platforms

| experiment | method | platforms | runs | distinct results |
|---|---|---|---|---|
| E1 mixed | c-serial | 3 | 3 | 1 |
| E1 mixed | c-omp | 3 | 24 | 9 |
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
| E2 | c-thread | 3 | 24 | 10 |
| E2 | c-index | 3 | 24 | 12 |
| E2 | c-philox | 3 | 24 | 9 |
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

