## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.2 | 1.5 | 0.7 | 1.4 | 1.0 | 1 |
| sword-without-walked | 4.4 | 2.4 | 1.1 | 1.5 | 1.5 | 1 |
| sword-without-walked-mut | 2.9 | 1.5 | 0.7 | 0.9 | 0.9 | 1 |
| sword-without-captures | 3.3 | 1.5 | 0.7 | 1.0 | 0.9 | 1 |
| sword-without-versioned | 3.0 | 1.5 | 0.7 | 1.1 | 0.9 | 1 |
| sword-without-split | 3.0 | 1.5 | 0.7 | 1.1 | 1.1 | 1 |
| sword-without-deferred | 3.1 | 1.7 | 0.7 | 1.0 | 1.0 | 1 |
| sword-without-lanes | 6.5 | 3.3 | 1.6 | 2.2 | 1.8 | 1 |
| c-serial | 6.6 |  |  |  |  | 1 |
| c-restrict | 6.6 |  |  |  |  | 1 |
| c-omp | 6.9 | 3.5 | 1.7 | 1.8 | 2.2 | 8 |
| c-lanes | 3.4 |  |  |  |  | 1 |
| c-lanes-omp | 3.5 | 1.7 | 0.8 | 1.2 | 1.2 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.5 | 3.3 | 1.6 | 2.0 | 2.2 | 7 |
| cpp-thread | 6.7 | 3.5 | 1.8 | 2.0 | 2.3 | 5 |
| rust-rayon | 6.5 | 3.3 | 1.6 | 1.6 | 1.7 | 9 |
| zig-safe | 6.8 | 3.6 | 2.1 | 2.8 | 3.0 | 5 |
| zig-fast | 6.9 | 3.6 | 2.1 | 2.7 | 2.8 | 5 |
| go | 6.5 | 3.3 | 1.7 | 1.8 | 1.9 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1.9 | 1.6 | 1.7 | 1.6 | 1.6 | 1 |
| sword-without-walked | 2.8 | 1.7 | 1.7 | 1.8 | 1.8 | 1 |
| sword-without-walked-mut | 2.0 | 1.6 | 1.6 | 1.6 | 1.7 | 1 |
| sword-without-captures | 2.0 | 2.1 | 1.6 | 1.7 | 1.6 | 1 |
| sword-without-versioned | 2.0 | 1.8 | 1.5 | 1.6 | 1.8 | 1 |
| sword-without-split | 2.0 | 1.7 | 1.8 | 1.6 | 1.9 | 1 |
| sword-without-deferred | 2.1 | 1.6 | 1.5 | 1.7 | 1.9 | 1 |
| sword-without-lanes | 8.2 | 4.1 | 2.1 | 2.1 | 2.2 | 1 |
| c-serial | 8.2 |  |  |  |  | 1 |
| c-restrict | 8.2 |  |  |  |  | 1 |
| c-omp | 8.2 | 4.1 | 2.1 | 2.1 | 2.7 | 7 |
| c-lanes | 2.4 |  |  |  |  | 1 |
| c-lanes-omp | 2.3 | 1.6 | 1.7 | 1.6 | 1.9 | 1 |
| c-fastmath-serial | 2.2 |  |  |  |  | 1 |
| c-fastmath-omp | 8.2 | 4.1 | 2.1 | 2.8 | 2.7 | 7 |
| cpp-thread | 8.3 | 4.2 | 2.2 | 3.3 | 3.4 | 5 |
| rust-rayon | 8.3 | 4.1 | 2.2 | 2.1 | 2.2 | 10 |
| zig-safe | 8.5 | 4.5 | 2.7 | 3.5 | 3.7 | 5 |
| zig-fast | 8.5 | 4.5 | 2.7 | 3.5 | 3.8 | 5 |
| go | 8.2 | 4.2 | 2.2 | 2.2 | 2.2 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1.7 | 1.2 | 0.8 | 0.7 | 0.7 | 1 |
| sword-without-walked | 3.0 | 1.5 | 1.0 | 0.9 | 0.9 | 1 |
| sword-without-walked-mut | 1.9 | 0.8 | 0.7 | 0.7 | 0.7 | 1 |
| sword-without-captures | 1.6 | 0.8 | 0.7 | 0.7 | 0.7 | 1 |
| sword-without-versioned | 1.5 | 0.8 | 0.7 | 0.7 | 0.7 | 1 |
| sword-without-split | 1.5 | 0.9 | 0.7 | 0.7 | 0.7 | 1 |
| sword-without-deferred | 1.5 | 0.8 | 0.7 | 0.7 | 0.7 | 1 |
| sword-without-lanes | 8.8 | 4.4 | 2.3 | 2.0 | 2.0 | 1 |
| c-serial | 8.8 |  |  |  |  | 1 |
| c-restrict | 8.7 |  |  |  |  | 1 |
| c-omp | 8.9 | 4.4 | 2.3 | 2.4 | 2.4 | 5 |
| c-lanes | 1.5 |  |  |  |  | 1 |
| c-lanes-omp | 1.5 | 0.8 | 0.7 | 0.7 | 0.8 | 1 |
| c-fastmath-serial | 1.5 |  |  |  |  | 1 |
| c-fastmath-omp | 1.4 | 0.8 | 0.7 | 0.8 | 0.9 | 5 |
| cpp-thread | 8.8 | 4.7 | 2.4 | 2.4 | 2.5 | 5 |
| rust-rayon | 9.0 | 4.4 | 2.4 | 2.0 | 2.1 | 12 |
| zig-safe | 8.8 | 4.5 | 2.4 | 2.4 | 2.5 | 5 |
| zig-fast | 8.8 | 4.4 | 2.3 | 2.5 | 2.5 | 5 |
| go | 9.3 | 4.8 | 2.5 | 2.5 | 2.4 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.8 | 3.6 | 2.1 | 2.0 | 2.0 | 1 |
| sword-without-walked | 6.9 | 3.5 | 1.9 | 2.0 | 2.1 | 1 |
| sword-without-walked-mut | 6.9 | 3.5 | 1.9 | 2.0 | 2.0 | 1 |
| sword-without-captures | 8.7 | 5.0 | 2.6 | 2.7 | 2.8 | 1 |
| sword-without-versioned | 7.2 | 3.8 | 1.9 | 1.9 | 2.0 | 1 |
| sword-without-split | 7.0 | 3.5 | 1.9 | 1.9 | 2.0 | 1 |
| sword-without-deferred | 6.9 | 3.6 | 1.9 | 1.9 | 2.1 | 1 |
| sword-without-lanes | 7.0 | 3.5 | 1.9 | 2.0 | 2.3 | 1 |
| c-serial | 7.2 |  |  |  |  | 1 |
| c-restrict | 6.9 |  |  |  |  | 1 |
| c-omp | 7.1 | 3.8 | 2.1 | 3.0 | 2.5 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 7.0 | 3.9 | 2.0 | 2.9 | 2.6 | 1 |
| cpp-thread | 7.8 | 4.1 | 2.3 | 3.0 | 3.1 | 1 |
| rust-rayon | 7.2 | 3.7 | 2.0 | 2.0 | 2.2 | 1 |
| zig-safe | 11.0 | 5.9 | 3.3 | 4.2 | 4.2 | 1 |
| zig-fast | 8.9 | 4.8 | 2.9 | 3.7 | 3.7 | 1 |
| go | 7.0 | 4.1 | 2.2 | 2.1 | 2.3 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 4.6 | 3.8 | 3.7 | 3.7 | 3.8 | 1 |
| sword-without-walked | 4.4 | 3.7 | 3.8 | 3.8 | 3.9 | 1 |
| sword-without-walked-mut | 4.4 | 3.7 | 3.8 | 3.7 | 3.8 | 1 |
| sword-without-captures | 8.4 | 4.5 | 4.2 | 4.2 | 4.2 | 1 |
| sword-without-versioned | 4.7 | 3.8 | 3.9 | 3.9 | 4.0 | 1 |
| sword-without-split | 4.6 | 3.9 | 3.8 | 3.7 | 3.8 | 1 |
| sword-without-deferred | 4.6 | 3.9 | 3.8 | 3.7 | 4.1 | 1 |
| sword-without-lanes | 4.2 | 3.6 | 3.6 | 3.5 | 3.5 | 1 |
| c-serial | 4.3 |  |  |  |  | 1 |
| c-restrict | 4.2 |  |  |  |  | 1 |
| c-omp | 4.4 | 3.6 | 3.5 | 3.8 | 3.6 | 1 |
| c-fastmath-serial | 4.2 |  |  |  |  | 1 |
| c-fastmath-omp | 4.5 | 3.6 | 3.5 | 3.8 | 3.9 | 1 |
| cpp-thread | 4.8 | 3.6 | 3.6 | 3.8 | 3.8 | 1 |
| rust-rayon | 4.4 | 3.9 | 4.2 | 4.4 | 4.4 | 1 |
| zig-safe | 8.7 | 4.6 | 4.7 | 5.0 | 5.3 | 1 |
| zig-fast | 6.6 | 3.9 | 4.0 | 4.5 | 4.7 | 1 |
| go | 5.7 | 4.3 | 3.9 | 3.7 | 3.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.9 | 1.9 | 1.6 | 1.5 | 1.5 | 1 |
| sword-without-walked | 2.9 | 1.6 | 1.4 | 1.5 | 1.5 | 1 |
| sword-without-walked-mut | 2.8 | 1.6 | 1.5 | 1.5 | 1.5 | 1 |
| sword-without-captures | 6.9 | 3.8 | 1.9 | 1.7 | 1.7 | 1 |
| sword-without-versioned | 3.0 | 1.6 | 1.4 | 1.5 | 1.5 | 1 |
| sword-without-split | 3.0 | 1.7 | 1.5 | 1.5 | 1.5 | 1 |
| sword-without-deferred | 2.8 | 1.7 | 1.4 | 1.4 | 1.5 | 1 |
| sword-without-lanes | 2.7 | 1.7 | 1.5 | 1.5 | 1.5 | 1 |
| c-serial | 3.3 |  |  |  |  | 1 |
| c-restrict | 3.2 |  |  |  |  | 1 |
| c-omp | 3.4 | 2.9 | 1.9 | 1.5 | 1.6 | 1 |
| c-fastmath-serial | 3.3 |  |  |  |  | 1 |
| c-fastmath-omp | 3.1 | 2.3 | 2.3 | 1.8 | 1.6 | 1 |
| cpp-thread | 3.1 | 2.9 | 2.1 | 1.8 | 1.8 | 1 |
| rust-rayon | 2.8 | 2.6 | 1.9 | 1.8 | 2.0 | 1 |
| zig-safe | 9.2 | 4.9 | 2.7 | 2.7 | 2.5 | 1 |
| zig-fast | 7.2 | 3.6 | 2.2 | 2.4 | 2.3 | 1 |
| go | 5.6 | 3.7 | 2.1 | 1.9 | 1.9 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 78.3 | 39.1 | 19.6 | 23.3 | 25.4 | 1 |
| sword-without-walked | 77.3 | 39.5 | 19.5 | 22.6 | 24.1 | 1 |
| sword-without-walked-mut | 79.0 | 39.7 | 20.0 | 22.8 | 25.0 | 1 |
| sword-without-captures | 84.4 | 42.3 | 21.4 | 24.2 | 26.8 | 1 |
| sword-without-versioned | 77.5 | 38.6 | 19.5 | 24.0 | 24.1 | 1 |
| sword-without-split | 91.1 | 45.9 | 22.7 | 25.6 | 29.5 | 1 |
| sword-without-deferred | 77.5 | 39.0 | 19.5 | 23.2 | 25.3 | 1 |
| sword-without-lanes | 77.9 | 38.9 | 19.6 | 22.4 | 23.9 | 1 |
| c-serial | 54.0 |  |  |  |  | 1 |
| c-restrict | 54.1 |  |  |  |  | 1 |
| c-omp | 51.1 | 25.1 | 12.5 | 16.7 | 14.3 | 1 |
| c-fastmath-serial | 54.3 |  |  |  |  | 1 |
| c-fastmath-omp | 50.5 | 24.9 | 12.5 | 15.2 | 14.9 | 1 |
| cpp-thread | 57.8 | 28.4 | 15.4 | 18.7 | 20.2 | 1 |
| rust-rayon | 92.5 | 46.3 | 23.9 | 23.2 | 23.7 | 1 |
| zig-safe | 94.6 | 48.6 | 27.8 | 35.8 | 35.8 | 1 |
| zig-fast | 42.9 | 22.4 | 14.3 | 18.7 | 21.4 | 1 |
| go | 78.3 | 39.6 | 19.9 | 22.3 | 21.6 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 84.4 | 41.8 | 35.2 | 36.0 | 36.9 | 1 |
| sword-without-walked | 85.5 | 40.0 | 35.3 | 36.4 | 36.8 | 1 |
| sword-without-walked-mut | 87.0 | 43.1 | 37.4 | 38.3 | 38.9 | 1 |
| sword-without-captures | 88.2 | 45.6 | 38.4 | 39.5 | 40.5 | 1 |
| sword-without-versioned | 80.9 | 41.0 | 35.1 | 36.6 | 37.2 | 1 |
| sword-without-split | 99.6 | 49.5 | 41.1 | 42.6 | 43.8 | 1 |
| sword-without-deferred | 79.7 | 41.7 | 35.1 | 36.7 | 38.1 | 1 |
| sword-without-lanes | 86.0 | 43.1 | 35.1 | 36.4 | 36.9 | 1 |
| c-serial | 48.1 |  |  |  |  | 1 |
| c-restrict | 54.5 |  |  |  |  | 1 |
| c-omp | 48.7 | 25.9 | 17.9 | 18.3 | 19.9 | 1 |
| c-fastmath-serial | 59.1 |  |  |  |  | 1 |
| c-fastmath-omp | 56.2 | 27.8 | 18.7 | 20.3 | 21.2 | 1 |
| cpp-thread | 52.8 | 28.9 | 19.8 | 27.3 | 24.7 | 1 |
| rust-rayon | 93.8 | 47.4 | 44.1 | 45.4 | 44.9 | 1 |
| zig-safe | 74.1 | 39.7 | 37.4 | 46.0 | 46.6 | 1 |
| zig-fast | 53.7 | 30.6 | 23.3 | 30.2 | 31.3 | 1 |
| go | 80.6 | 41.1 | 32.5 | 29.9 | 31.3 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 37.1 | 18.9 | 10.1 | 8.4 | 8.5 | 1 |
| sword-without-walked | 34.6 | 17.6 | 9.9 | 8.3 | 8.7 | 1 |
| sword-without-walked-mut | 39.3 | 20.7 | 10.9 | 10.1 | 9.4 | 1 |
| sword-without-captures | 56.4 | 32.2 | 14.5 | 11.9 | 12.0 | 1 |
| sword-without-versioned | 34.5 | 18.1 | 9.9 | 8.3 | 8.5 | 1 |
| sword-without-split | 60.4 | 32.8 | 16.3 | 13.3 | 13.5 | 1 |
| sword-without-deferred | 37.6 | 20.1 | 10.6 | 8.9 | 9.0 | 1 |
| sword-without-lanes | 37.3 | 20.2 | 10.0 | 8.4 | 8.5 | 1 |
| c-serial | 31.0 |  |  |  |  | 1 |
| c-restrict | 30.8 |  |  |  |  | 1 |
| c-omp | 30.6 | 15.7 | 8.5 | 8.6 | 9.0 | 1 |
| c-fastmath-serial | 30.9 |  |  |  |  | 1 |
| c-fastmath-omp | 31.1 | 15.7 | 8.6 | 8.7 | 9.0 | 1 |
| cpp-thread | 31.3 | 18.1 | 10.3 | 11.8 | 10.8 | 1 |
| rust-rayon | 66.6 | 35.6 | 18.2 | 14.3 | 15.2 | 1 |
| zig-safe | 67.8 | 36.1 | 19.0 | 19.4 | 19.8 | 1 |
| zig-fast | 28.8 | 16.1 | 9.3 | 9.6 | 10.3 | 1 |
| go | 62.6 | 33.1 | 17.9 | 17.4 | 17.0 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.7 | 346.5 | 173.6 | 175.8 | 176.7 | 1 |
| sword-without-walked | 692.7 | 346.5 | 173.7 | 176.8 | 176.8 | 1 |
| sword-without-walked-mut | 692.7 | 346.5 | 173.7 | 175.7 | 176.2 | 1 |
| sword-without-captures | 692.6 | 346.5 | 173.6 | 177.3 | 176.4 | 1 |
| sword-without-versioned | 692.6 | 346.5 | 173.7 | 174.7 | 176.6 | 1 |
| sword-without-split | 692.6 | 346.5 | 173.6 | 176.7 | 176.5 | 1 |
| sword-without-deferred | 692.7 | 346.5 | 173.7 | 175.6 | 177.5 | 1 |
| sword-without-lanes | 692.7 | 346.5 | 173.8 | 175.1 | 175.8 | 1 |
| c-serial | 646.8 |  |  |  |  | 1 |
| c-restrict | 647.6 |  |  |  |  | 1 |
| c-omp | 635.8 | 318.2 | 159.7 | 160.2 | 160.0 | 1 |
| c-fastmath-serial | 626.8 |  |  |  |  | 1 |
| c-fastmath-omp | 627.6 | 313.9 | 157.2 | 157.2 | 157.4 | 1 |
| cpp-thread | 853.9 | 427.3 | 214.2 | 228.2 | 217.3 | 1 |
| rust-rayon | 692.8 | 347.1 | 174.0 | 173.9 | 174.1 | 1 |
| zig-safe | 681.9 | 341.7 | 171.8 | 188.9 | 174.6 | 1 |
| zig-fast | 897.0 | 448.8 | 225.1 | 247.3 | 230.2 | 1 |
| go | 678.3 | 339.6 | 170.5 | 181.1 | 174.7 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 763.4 | 381.9 | 203.6 | 205.3 | 206.7 | 1 |
| sword-without-walked | 763.3 | 382.0 | 203.4 | 204.1 | 206.9 | 1 |
| sword-without-walked-mut | 763.2 | 381.9 | 203.3 | 205.1 | 206.6 | 1 |
| sword-without-captures | 763.3 | 382.0 | 203.2 | 204.7 | 205.9 | 1 |
| sword-without-versioned | 763.2 | 382.0 | 203.2 | 204.0 | 205.9 | 1 |
| sword-without-split | 763.2 | 381.9 | 203.3 | 205.4 | 206.7 | 1 |
| sword-without-deferred | 763.0 | 381.9 | 203.5 | 205.0 | 206.4 | 1 |
| sword-without-lanes | 763.1 | 382.0 | 203.4 | 204.5 | 207.1 | 1 |
| c-serial | 711.0 |  |  |  |  | 1 |
| c-restrict | 711.0 |  |  |  |  | 1 |
| c-omp | 710.7 | 355.7 | 176.9 | 177.0 | 177.0 | 1 |
| c-fastmath-serial | 705.2 |  |  |  |  | 1 |
| c-fastmath-omp | 707.4 | 354.1 | 177.2 | 176.9 | 177.0 | 1 |
| cpp-thread | 710.7 | 355.8 | 176.8 | 191.8 | 182.1 | 1 |
| rust-rayon | 715.4 | 348.0 | 213.2 | 211.6 | 211.8 | 1 |
| zig-safe | 719.5 | 360.5 | 197.4 | 214.8 | 201.1 | 1 |
| zig-fast | 718.5 | 360.0 | 190.1 | 203.6 | 194.6 | 1 |
| go | 688.4 | 349.3 | 206.6 | 211.3 | 208.1 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 781.5 | 403.5 | 208.1 | 166.1 | 166.5 | 1 |
| sword-without-walked | 773.5 | 403.3 | 208.3 | 166.2 | 169.6 | 1 |
| sword-without-walked-mut | 789.3 | 403.3 | 208.1 | 166.8 | 170.9 | 1 |
| sword-without-captures | 791.9 | 404.1 | 208.4 | 165.5 | 166.2 | 1 |
| sword-without-versioned | 774.9 | 403.8 | 207.4 | 165.3 | 169.2 | 1 |
| sword-without-split | 774.2 | 403.8 | 207.9 | 165.6 | 166.1 | 1 |
| sword-without-deferred | 774.5 | 403.5 | 208.3 | 167.0 | 167.3 | 1 |
| sword-without-lanes | 774.3 | 403.5 | 208.2 | 201.0 | 192.9 | 1 |
| c-serial | 653.6 |  |  |  |  | 1 |
| c-restrict | 657.9 |  |  |  |  | 1 |
| c-omp | 655.2 | 350.3 | 175.1 | 139.3 | 139.3 | 1 |
| c-fastmath-serial | 549.5 |  |  |  |  | 1 |
| c-fastmath-omp | 554.2 | 299.3 | 147.8 | 117.5 | 117.7 | 1 |
| cpp-thread | 655.0 | 341.6 | 175.6 | 139.5 | 140.7 | 1 |
| rust-rayon | 766.3 | 398.9 | 205.3 | 165.2 | 164.3 | 1 |
| zig-safe | 775.6 | 403.9 | 207.9 | 165.1 | 165.7 | 1 |
| zig-fast | 802.4 | 407.0 | 205.8 | 163.1 | 163.7 | 1 |
| go | 791.0 | 412.2 | 212.9 | 193.7 | 172.9 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.6 | 125.9 | 64.0 | 66.2 | 68.1 | 1 |
| sword-without-walked | 250.8 | 125.8 | 64.0 | 66.9 | 69.0 | 1 |
| sword-without-walked-mut | 251.8 | 126.0 | 63.1 | 65.3 | 68.5 | 1 |
| sword-without-captures | 251.6 | 126.0 | 63.9 | 67.0 | 68.8 | 1 |
| sword-without-versioned | 270.6 | 135.5 | 68.1 | 70.7 | 70.1 | 1 |
| sword-without-split | 251.8 | 126.0 | 64.0 | 65.9 | 69.2 | 1 |
| sword-without-deferred | 251.7 | 126.1 | 64.0 | 66.8 | 69.2 | 1 |
| sword-without-lanes | 250.9 | 125.8 | 63.2 | 65.1 | 66.8 | 1 |
| c-serial | 237.6 |  |  |  |  | 1 |
| c-restrict | 237.6 |  |  |  |  | 1 |
| c-omp | 238.6 | 119.5 | 59.9 | 63.4 | 64.6 | 1 |
| c-fastmath-serial | 237.8 |  |  |  |  | 1 |
| c-fastmath-omp | 243.7 | 122.2 | 61.3 | 64.0 | 65.0 | 1 |
| cpp-thread | 240.3 | 120.4 | 61.2 | 70.1 | 70.3 | 1 |
| rust-rayon | 246.0 | 122.6 | 62.0 | 62.0 | 63.1 | 1 |
| zig-safe | 271.8 | 137.0 | 71.4 | 80.9 | 84.2 | 1 |
| zig-fast | 271.7 | 136.9 | 71.4 | 79.9 | 84.9 | 1 |
| go | 252.2 | 126.4 | 63.8 | 68.9 | 68.3 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 254.0 | 127.5 | 127.0 | 127.6 | 129.2 | 1 |
| sword-without-walked | 254.0 | 127.4 | 127.0 | 127.4 | 128.5 | 1 |
| sword-without-walked-mut | 254.1 | 127.4 | 127.0 | 127.2 | 129.5 | 1 |
| sword-without-captures | 254.1 | 127.7 | 127.0 | 127.2 | 128.5 | 1 |
| sword-without-versioned | 255.7 | 128.8 | 127.6 | 128.0 | 129.6 | 1 |
| sword-without-split | 254.3 | 127.4 | 127.1 | 127.3 | 128.8 | 1 |
| sword-without-deferred | 254.1 | 127.4 | 127.0 | 127.4 | 129.0 | 1 |
| sword-without-lanes | 254.1 | 127.3 | 127.0 | 127.2 | 128.4 | 1 |
| c-serial | 64.1 |  |  |  |  | 1 |
| c-restrict | 63.6 |  |  |  |  | 1 |
| c-omp | 115.9 | 58.1 | 53.3 | 54.4 | 55.9 | 1 |
| c-fastmath-serial | 63.6 |  |  |  |  | 1 |
| c-fastmath-omp | 63.7 | 32.0 | 31.8 | 33.5 | 32.4 | 1 |
| cpp-thread | 117.0 | 59.0 | 54.2 | 61.1 | 58.9 | 1 |
| rust-rayon | 256.8 | 128.8 | 128.3 | 128.6 | 130.7 | 1 |
| zig-safe | 254.9 | 129.1 | 129.7 | 137.8 | 139.8 | 1 |
| zig-fast | 255.2 | 129.3 | 129.8 | 138.4 | 139.5 | 1 |
| go | 454.9 | 230.0 | 143.6 | 150.4 | 149.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 74.0 | 38.9 | 20.2 | 16.6 | 16.7 | 1 |
| sword-without-walked | 74.2 | 40.1 | 20.2 | 16.5 | 16.7 | 1 |
| sword-without-walked-mut | 74.2 | 39.7 | 21.2 | 16.8 | 16.7 | 1 |
| sword-without-captures | 74.5 | 43.9 | 22.6 | 16.6 | 16.7 | 1 |
| sword-without-versioned | 116.6 | 67.9 | 36.2 | 31.7 | 25.7 | 1 |
| sword-without-split | 74.2 | 38.8 | 20.2 | 16.5 | 16.6 | 1 |
| sword-without-deferred | 74.1 | 42.9 | 22.5 | 17.9 | 18.0 | 1 |
| sword-without-lanes | 74.0 | 38.8 | 22.0 | 16.5 | 16.7 | 1 |
| c-serial | 76.8 |  |  |  |  | 1 |
| c-restrict | 71.6 |  |  |  |  | 1 |
| c-omp | 71.0 | 37.1 | 19.4 | 19.2 | 18.4 | 1 |
| c-fastmath-serial | 39.3 |  |  |  |  | 1 |
| c-fastmath-omp | 39.2 | 20.6 | 10.7 | 10.7 | 10.4 | 1 |
| cpp-thread | 71.4 | 37.3 | 19.6 | 19.6 | 20.0 | 1 |
| rust-rayon | 74.2 | 39.0 | 20.2 | 16.3 | 16.9 | 1 |
| zig-safe | 114.4 | 60.2 | 31.2 | 31.5 | 30.7 | 1 |
| zig-fast | 112.2 | 58.8 | 30.6 | 30.5 | 30.2 | 1 |
| go | 97.0 | 50.8 | 26.4 | 26.0 | 22.7 | 1 |

## Answers across every platform and thread count

| method | sum | saxpy | stencil | mandelbrot | nbody |
|---|---:|---:|---:|---:|---:|
| sword | 1 | 1 | 1 | 1 | 1 |
| sword-without-walked | 1 | 1 | 1 | 1 | 1 |
| sword-without-walked-mut | 1 | 1 | 1 | 1 | 1 |
| sword-without-captures | 1 | 1 | 1 | 1 | 1 |
| sword-without-versioned | 1 | 1 | 1 | 1 | 1 |
| sword-without-split | 1 | 1 | 1 | 1 | 1 |
| sword-without-deferred | 1 | 1 | 1 | 1 | 1 |
| sword-without-lanes | 1 | 1 | 1 | 1 | 1 |
| c-serial | 1 | 1 | 1 | 1 | 1 |
| c-restrict | 1 | 1 | 1 | 1 | 1 |
| c-omp | 9 | 1 | 1 | 1 | 1 |
| c-lanes | 1 |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 |
| c-fastmath-omp | 14 | 1 | 2 | 2 | 1 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 |
| rust-rayon | 24 | 1 | 1 | 1 | 1 |
| zig-safe | 5 | 1 | 1 | 1 | 1 |
| zig-fast | 5 | 1 | 1 | 1 | 1 |
| go | 5 | 1 | 1 | 2 | 1 |
