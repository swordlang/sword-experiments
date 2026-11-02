# Results

## gh-linux-arm64

```
platform: gh-linux-arm64
date: 2026-11-01T22:45:26Z
uname: Linux 7.0.0-1017-azure aarch64
cpu: 0xd49
cores: 4
cc: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
openmp: -fopenmp
shield: shield 0.4.0 (Temper)
sword commit: dbf77e0
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
| c-serial | 1 of 1 | 237 | 6.48 | 6.48 | 1 |
| c-omp | 7 of 8 | 20–237 | 6.64 | 1.64 | 4 |
| c-ompkahan | 1 of 8 | 0 | 23.71 | 5.97 | 4 |
| sword-plain | 1 of 8 | 0 | 3.73 | 0.64 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.23 | 6.40 | 6 |
| sword-exact | 1 of 8 | 0 | 26.82 | 7.69 | 4 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 6.40 | 6.40 | 1 |
| c-omp | 8 of 8 | 37–243 | 6.82 | 1.64 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 23.71 | 5.95 | 4 |
| sword-plain | 1 of 8 | 35 | 3.71 | 0.60 | 4 |
| sword-kahan | 1 of 8 | 0 | 25.27 | 6.35 | 4 |
| sword-exact | 1 of 8 | 0 | 45.86 | 13.04 | 6 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 2 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 4 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440205 … 0.74692123466732596 | 49.5 | 12.4 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 48.0 | 12.0 | 4 |
| c-philox | 8 of 8 | 0.74688899599929437 … 0.74688899599935532 | 179.9 | 45.2 | 16 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 204.8 | 51.5 | 6 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 85.5 | 21.5 | 4 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 266.4 | 70.4 | 16 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 15.43 | 17.03 |
| sinnear | 6.99 | 3.15 |
| cos | 15.67 | 17.04 |
| exp | 6.14 | 8.70 |
| expunit | 3.23 | 7.21 |
| log | 4.05 | 8.32 |

## gh-linux-x86_64

```
platform: gh-linux-x86_64
date: 2026-11-01T22:45:32Z
uname: Linux 7.0.0-1017-azure x86_64
cpu: AMD EPYC 7763 64-Core Processor
cores: 4
cc: gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
openmp: -fopenmp
shield: shield 0.4.0 (Temper)
sword commit: dbf77e0
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
| c-serial | 1 of 1 | 237 | 9.50 | 9.50 | 1 |
| c-omp | 7 of 8 | 20–237 | 9.53 | 2.43 | 4 |
| c-ompkahan | 1 of 8 | 0 | 37.48 | 9.51 | 4 |
| sword-plain | 1 of 8 | 0 | 3.60 | 1.73 | 16 |
| sword-kahan | 1 of 8 | 0 | 12.72 | 6.37 | 4 |
| sword-exact | 1 of 8 | 0 | 31.50 | 15.83 | 2 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 9.53 | 9.53 | 1 |
| c-omp | 8 of 8 | 37–243 | 9.52 | 2.47 | 4 |
| c-ompkahan | 3 of 8 | 0–1 | 37.52 | 9.45 | 4 |
| sword-plain | 1 of 8 | 35 | 3.51 | 1.79 | 16 |
| sword-kahan | 1 of 8 | 0 | 12.84 | 6.35 | 4 |
| sword-exact | 1 of 8 | 0 | 61.21 | 24.03 | 10 |

### E1b — the same run repeated, thread count fixed (mixed data)

| method | threads | runs | distinct results |
|---|---|---|---|
| c-omp | 2 | 100 | 1 |
| sword-plain | 2 | 100 | 1 |
| c-omp | 4 | 100 | 1 |
| sword-plain | 4 | 100 | 1 |
| c-omp | 8 | 100 | 2 |
| sword-plain | 8 | 100 | 1 |
| c-omp | 16 | 100 | 5 |
| sword-plain | 16 | 100 | 1 |

### E2 — Monte Carlo, integral of exp(-x²) on [0, 1]

| method | distinct results | values seen | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-thread | 8 of 8 | 0.74684708827440194 … 0.74692123466732596 | 51.5 | 22.3 | 4 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 47.3 | 21.5 | 4 |
| c-philox | 8 of 8 | 0.74688899599929437 … 0.74688899599935521 | 217.9 | 79.2 | 4 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 250.4 | 89.8 | 4 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 129.4 | 39.6 | 4 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 302.0 | 114.3 | 6 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 19.92 | 23.29 |
| sinnear | 9.43 | 2.82 |
| cos | 19.75 | 23.19 |
| exp | 7.67 | 7.91 |
| expunit | 3.43 | 7.75 |
| log | 3.75 | 7.40 |

## gh-macos-arm64

```
platform: gh-macos-arm64
date: 2026-11-01T22:45:16Z
uname: Darwin 25.6.0 arm64
cpu: Apple M1 (Virtual)
cores: 3
cc: Apple clang version 21.0.0 (clang-2100.1.1.101)
openmp: -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp
shield: shield 0.4.0 (Temper)
sword commit: dbf77e0
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
| c-serial | 1 of 1 | 237 | 10.36 | 10.36 | 1 |
| c-omp | 7 of 8 | 20–237 | 11.08 | 5.04 | 16 |
| c-ompkahan | 1 of 8 | 0 | 46.85 | 17.08 | 8 |
| sword-plain | 1 of 8 | 0 | 2.17 | 1.50 | 16 |
| sword-kahan | 1 of 8 | 0 | 14.36 | 5.41 | 4 |
| sword-exact | 1 of 8 | 0 | 28.43 | 12.14 | 4 |

**mixed** (correctly rounded sum 159165645829.89481)

| method | distinct results | error (ULPs) | 1 thread (ms) | fastest (ms) | at threads |
|---|---|---|---|---|---|
| c-serial | 1 of 1 | 243 | 13.18 | 13.18 | 1 |
| c-omp | 8 of 8 | 37–243 | 10.40 | 4.27 | 16 |
| c-ompkahan | 3 of 8 | 0–1 | 47.69 | 16.45 | 16 |
| sword-plain | 1 of 8 | 35 | 2.47 | 1.67 | 10 |
| sword-kahan | 1 of 8 | 0 | 11.73 | 3.99 | 10 |
| sword-exact | 1 of 8 | 0 | 49.30 | 19.97 | 10 |

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
| c-thread | 8 of 8 | 0.74684708827440216 … 0.74692123466732596 | 70.7 | 17.8 | 6 |
| c-index | 8 of 8 | 0.74675913289815332 … 0.74675913289820595 | 50.2 | 11.7 | 8 |
| c-philox | 7 of 8 | 0.74688899599929437 … 0.74688899599935521 | 120.2 | 34.7 | 4 |
| sword-plain | 1 of 8 | 0.74688899599934688 | 279.7 | 80.2 | 6 |
| sword-mix | 1 of 8 | 0.74675913289817752 | 185.5 | 39.6 | 16 |
| sword-exact | 1 of 8 | 0.74688899599934688 | 360.3 | 93.6 | 4 |

### E3 — elementary functions, cost

| function | C library (ns/call) | std/num (ns/call) |
|---|---|---|
| sin | 7.76 | 18.71 |
| sinnear | 2.00 | 2.73 |
| cos | 8.62 | 20.22 |
| exp | 5.92 | 5.38 |
| expunit | 2.62 | 6.26 |
| log | 2.79 | 6.29 |

## E1, E2 — Sword's answers on different platforms

| experiment | method | platforms | runs | distinct results |
|---|---|---|---|---|
| E1 mixed | c-serial | 3 | 3 | 1 |
| E1 mixed | c-omp | 3 | 24 | 13 |
| E1 mixed | c-ompkahan | 3 | 24 | 3 |
| E1 mixed | sword-plain | 3 | 24 | 1 |
| E1 mixed | sword-kahan | 3 | 24 | 1 |
| E1 mixed | sword-exact | 3 | 24 | 1 |
| E1 uniform | c-serial | 3 | 3 | 1 |
| E1 uniform | c-omp | 3 | 24 | 8 |
| E1 uniform | c-ompkahan | 3 | 24 | 1 |
| E1 uniform | sword-plain | 3 | 24 | 1 |
| E1 uniform | sword-kahan | 3 | 24 | 1 |
| E1 uniform | sword-exact | 3 | 24 | 1 |
| E2 | c-thread | 3 | 24 | 13 |
| E2 | c-index | 3 | 24 | 12 |
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

