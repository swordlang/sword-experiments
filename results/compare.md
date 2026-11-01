## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.2 | 1.5 | 0.7 | 0.9 | 1.0 | 1 |
| sword-native | 3.2 | 1.6 | 0.8 | 0.9 | 1.0 | 1 |
| sword-without-walked | 4.4 | 2.4 | 1.1 | 1.6 | 1.2 | 1 |
| sword-without-walked-mut | 3.0 | 1.5 | 0.7 | 1.1 | 0.9 | 1 |
| sword-without-captures | 3.2 | 1.5 | 0.7 | 1.1 | 0.8 | 1 |
| sword-without-versioned | 3.2 | 1.6 | 0.8 | 1.1 | 1.0 | 1 |
| sword-without-split | 3.0 | 1.6 | 0.8 | 1.1 | 1.2 | 1 |
| sword-without-deferred | 3.5 | 1.5 | 0.7 | 1.0 | 1.2 | 1 |
| sword-without-lanes | 6.4 | 3.3 | 1.7 | 2.0 | 2.2 | 1 |
| sword-without-steady | 3.1 | 1.5 | 0.8 | 1.2 | 1.0 | 1 |
| c-serial | 6.6 |  |  |  |  | 1 |
| c-restrict | 6.7 |  |  |  |  | 1 |
| c-omp | 6.7 | 3.4 | 1.7 | 2.0 | 2.0 | 8 |
| c-lanes | 3.6 |  |  |  |  | 1 |
| c-lanes-omp | 3.5 | 1.8 | 0.9 | 1.3 | 1.2 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.4 | 3.3 | 1.8 | 2.0 | 2.1 | 7 |
| c-native-serial | 6.4 |  |  |  |  | 1 |
| c-native-omp | 6.4 | 3.2 | 1.6 | 1.8 | 1.8 | 8 |
| c-native-lanes | 3.4 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.6 | 1.9 | 0.9 | 1.2 | 1.1 | 1 |
| c-clang-serial | 6.4 |  |  |  |  | 1 |
| c-clang-omp | 6.4 | 3.3 | 1.6 | 2.4 | 2.1 | 5 |
| cpp-thread | 7.0 | 3.5 | 1.8 | 2.0 | 2.4 | 5 |
| rust-rayon | 6.5 | 3.3 | 1.6 | 1.6 | 1.6 | 11 |
| zig-safe | 6.5 | 3.5 | 2.1 | 2.7 | 2.8 | 5 |
| zig-fast | 6.6 | 3.5 | 2.1 | 2.7 | 2.9 | 5 |
| go | 6.5 | 3.4 | 1.7 | 1.8 | 1.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.5 | 1.9 | 1.5 | 1.6 | 1.7 | 1 |
| sword-native | 3.1 | 1.7 | 1.5 | 1.6 | 1.7 | 1 |
| sword-without-walked | 4.6 | 2.5 | 1.7 | 1.8 | 1.8 | 1 |
| sword-without-walked-mut | 3.4 | 1.9 | 1.5 | 1.5 | 1.6 | 1 |
| sword-without-captures | 3.4 | 1.9 | 1.5 | 1.5 | 1.6 | 1 |
| sword-without-versioned | 3.4 | 1.9 | 1.5 | 1.6 | 1.6 | 1 |
| sword-without-split | 3.5 | 1.9 | 1.5 | 1.5 | 1.6 | 1 |
| sword-without-deferred | 3.4 | 1.9 | 1.5 | 1.6 | 1.6 | 1 |
| sword-without-lanes | 9.5 | 4.8 | 2.4 | 2.5 | 2.6 | 1 |
| sword-without-steady | 3.5 | 1.9 | 1.5 | 1.6 | 1.6 | 1 |
| c-serial | 9.5 |  |  |  |  | 1 |
| c-restrict | 9.5 |  |  |  |  | 1 |
| c-omp | 9.5 | 4.8 | 2.4 | 2.5 | 2.6 | 7 |
| c-lanes | 3.8 |  |  |  |  | 1 |
| c-lanes-omp | 3.8 | 2.0 | 1.5 | 1.6 | 1.9 | 1 |
| c-fastmath-serial | 3.4 |  |  |  |  | 1 |
| c-fastmath-omp | 9.5 | 4.8 | 2.4 | 2.5 | 2.6 | 8 |
| c-native-serial | 9.5 |  |  |  |  | 1 |
| c-native-omp | 9.5 | 4.8 | 2.4 | 2.7 | 3.2 | 6 |
| c-native-lanes | 3.7 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.7 | 2.0 | 1.5 | 1.7 | 1.9 | 1 |
| c-clang-serial | 9.5 |  |  |  |  | 1 |
| c-clang-omp | 9.6 | 4.8 | 2.4 | 3.7 | 3.7 | 5 |
| cpp-thread | 9.6 | 4.9 | 2.6 | 3.9 | 3.6 | 5 |
| rust-rayon | 9.5 | 4.8 | 2.5 | 2.5 | 2.5 | 8 |
| zig-safe | 9.8 | 5.2 | 3.2 | 4.0 | 4.5 | 5 |
| zig-fast | 9.8 | 5.2 | 3.1 | 4.0 | 4.2 | 5 |
| go | 9.6 | 4.9 | 2.5 | 2.6 | 2.5 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.4 | 2.1 | 2.0 | 2.2 | 1.9 | 1 |
| sword-native | 2.5 | 2.1 | 1.9 | 2.1 | 2.0 | 1 |
| sword-without-walked | 3.6 | 2.5 | 2.2 | 2.1 | 2.0 | 1 |
| sword-without-walked-mut | 2.4 | 2.1 | 2.2 | 2.2 | 2.0 | 1 |
| sword-without-captures | 2.3 | 1.9 | 1.9 | 2.1 | 2.2 | 1 |
| sword-without-versioned | 2.0 | 2.1 | 1.9 | 1.9 | 1.7 | 1 |
| sword-without-split | 2.2 | 2.2 | 1.8 | 1.8 | 1.9 | 1 |
| sword-without-deferred | 2.1 | 2.1 | 1.8 | 1.6 | 1.8 | 1 |
| sword-without-lanes | 11.5 | 6.0 | 4.4 | 4.4 | 4.1 | 1 |
| sword-without-steady | 2.1 | 2.0 | 1.8 | 1.7 | 1.9 | 1 |
| c-serial | 13.0 |  |  |  |  | 1 |
| c-restrict | 12.5 |  |  |  |  | 1 |
| c-omp | 13.6 | 6.2 | 5.5 | 4.9 | 4.4 | 5 |
| c-lanes | 2.5 |  |  |  |  | 1 |
| c-lanes-omp | 2.7 | 2.1 | 2.0 | 2.2 | 2.1 | 1 |
| c-fastmath-serial | 2.4 |  |  |  |  | 1 |
| c-fastmath-omp | 2.4 | 2.2 | 1.8 | 1.7 | 2.0 | 5 |
| c-native-serial | 11.4 |  |  |  |  | 1 |
| c-native-omp | 11.7 | 5.9 | 5.4 | 4.2 | 4.7 | 5 |
| c-native-lanes | 2.2 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.2 | 2.5 | 1.9 | 1.9 | 1.9 | 1 |
| c-clang-serial | 10.5 |  |  |  |  | 1 |
| c-clang-omp | 11.1 | 6.5 | 5.5 | 4.5 | 4.6 | 5 |
| cpp-thread | 11.3 | 6.8 | 6.1 | 5.3 | 5.7 | 5 |
| rust-rayon | 11.6 | 6.6 | 4.4 | 4.1 | 4.3 | 12 |
| zig-safe | 11.4 | 6.9 | 5.3 | 4.5 | 5.0 | 5 |
| zig-fast | 10.4 | 5.3 | 5.4 | 4.7 | 4.7 | 5 |
| go | 12.7 | 6.8 | 5.0 | 4.9 | 5.0 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.0 | 3.6 | 1.9 | 1.9 | 2.3 | 1 |
| sword-native | 6.9 | 3.5 | 1.9 | 1.9 | 2.0 | 1 |
| sword-without-walked | 6.3 | 3.5 | 2.0 | 1.9 | 2.1 | 1 |
| sword-without-walked-mut | 6.9 | 3.5 | 1.9 | 1.9 | 2.1 | 1 |
| sword-without-captures | 9.0 | 5.1 | 2.7 | 2.7 | 2.8 | 1 |
| sword-without-versioned | 6.4 | 3.5 | 1.9 | 1.9 | 2.0 | 1 |
| sword-without-split | 6.5 | 3.4 | 2.0 | 2.0 | 2.0 | 1 |
| sword-without-deferred | 6.3 | 3.5 | 2.0 | 1.9 | 2.0 | 1 |
| sword-without-lanes | 7.0 | 3.6 | 1.9 | 2.0 | 2.1 | 1 |
| sword-without-steady | 6.3 | 3.7 | 1.9 | 2.0 | 2.2 | 1 |
| c-serial | 7.0 |  |  |  |  | 1 |
| c-restrict | 6.5 |  |  |  |  | 1 |
| c-omp | 6.2 | 3.8 | 2.0 | 2.7 | 2.3 | 1 |
| c-fastmath-serial | 6.3 |  |  |  |  | 1 |
| c-fastmath-omp | 6.9 | 3.8 | 2.0 | 2.7 | 2.3 | 1 |
| c-native-serial | 6.8 |  |  |  |  | 1 |
| c-native-omp | 6.5 | 3.7 | 2.0 | 2.8 | 2.4 | 1 |
| c-clang-serial | 6.4 |  |  |  |  | 1 |
| c-clang-omp | 7.0 | 3.7 | 1.8 | 2.7 | 2.3 | 1 |
| cpp-thread | 7.5 | 4.0 | 2.3 | 2.4 | 2.8 | 1 |
| rust-rayon | 7.2 | 3.7 | 2.0 | 2.0 | 2.3 | 1 |
| zig-safe | 11.4 | 6.0 | 3.3 | 4.3 | 4.3 | 1 |
| zig-fast | 9.0 | 4.8 | 2.8 | 3.6 | 3.4 | 1 |
| go | 7.6 | 4.0 | 2.2 | 2.2 | 2.3 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 5.8 | 4.1 | 4.0 | 4.0 | 4.0 | 1 |
| sword-native | 5.2 | 4.0 | 4.0 | 3.9 | 4.0 | 1 |
| sword-without-walked | 5.7 | 4.1 | 3.9 | 3.9 | 4.1 | 1 |
| sword-without-walked-mut | 5.7 | 4.2 | 4.0 | 4.1 | 4.1 | 1 |
| sword-without-captures | 8.9 | 4.9 | 4.3 | 4.3 | 4.3 | 1 |
| sword-without-versioned | 5.6 | 4.0 | 4.0 | 4.0 | 4.1 | 1 |
| sword-without-split | 5.8 | 4.1 | 3.9 | 4.0 | 4.3 | 1 |
| sword-without-deferred | 5.8 | 4.0 | 4.0 | 4.1 | 4.0 | 1 |
| sword-without-lanes | 5.8 | 4.0 | 4.1 | 4.1 | 4.0 | 1 |
| sword-without-steady | 5.6 | 4.1 | 4.0 | 4.1 | 4.1 | 1 |
| c-serial | 5.4 |  |  |  |  | 1 |
| c-restrict | 5.6 |  |  |  |  | 1 |
| c-omp | 6.7 | 4.5 | 4.0 | 4.2 | 4.2 | 1 |
| c-fastmath-serial | 5.4 |  |  |  |  | 1 |
| c-fastmath-omp | 6.5 | 4.4 | 4.1 | 4.3 | 4.1 | 1 |
| c-native-serial | 5.3 |  |  |  |  | 1 |
| c-native-omp | 6.6 | 4.2 | 4.0 | 4.0 | 4.1 | 1 |
| c-clang-serial | 5.7 |  |  |  |  | 1 |
| c-clang-omp | 5.7 | 4.0 | 4.0 | 4.2 | 4.3 | 1 |
| cpp-thread | 7.0 | 4.3 | 4.1 | 4.4 | 4.6 | 1 |
| rust-rayon | 5.9 | 4.2 | 4.2 | 4.2 | 4.7 | 1 |
| zig-safe | 11.0 | 5.7 | 5.6 | 6.1 | 6.9 | 1 |
| zig-fast | 8.8 | 4.8 | 4.7 | 5.0 | 5.6 | 1 |
| go | 7.2 | 6.9 | 4.5 | 4.4 | 4.6 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 5.9 | 6.0 | 5.6 | 5.7 | 5.4 | 1 |
| sword-native | 5.7 | 6.0 | 5.4 | 5.4 | 5.4 | 1 |
| sword-without-walked | 6.6 | 6.4 | 5.8 | 5.6 | 5.6 | 1 |
| sword-without-walked-mut | 6.3 | 6.4 | 5.6 | 5.3 | 5.3 | 1 |
| sword-without-captures | 10.1 | 8.0 | 6.0 | 6.3 | 6.2 | 1 |
| sword-without-versioned | 6.5 | 6.0 | 5.9 | 6.4 | 5.8 | 1 |
| sword-without-split | 7.1 | 5.8 | 5.8 | 5.6 | 5.9 | 1 |
| sword-without-deferred | 7.1 | 6.2 | 5.5 | 5.6 | 5.6 | 1 |
| sword-without-lanes | 5.9 | 5.7 | 5.4 | 5.9 | 5.8 | 1 |
| sword-without-steady | 6.6 | 6.3 | 5.5 | 5.8 | 5.9 | 1 |
| c-serial | 5.8 |  |  |  |  | 1 |
| c-restrict | 6.0 |  |  |  |  | 1 |
| c-omp | 5.9 | 5.9 | 5.5 | 5.7 | 5.3 | 1 |
| c-fastmath-serial | 5.8 |  |  |  |  | 1 |
| c-fastmath-omp | 6.1 | 6.0 | 5.8 | 5.3 | 5.5 | 1 |
| c-native-serial | 7.4 |  |  |  |  | 1 |
| c-native-omp | 5.9 | 5.6 | 5.9 | 5.5 | 5.5 | 1 |
| c-clang-serial | 8.0 |  |  |  |  | 1 |
| c-clang-omp | 7.5 | 5.8 | 5.6 | 5.6 | 6.3 | 1 |
| cpp-thread | 6.1 | 5.7 | 5.6 | 5.7 | 5.5 | 1 |
| rust-rayon | 5.9 | 5.6 | 5.6 | 5.6 | 5.8 | 1 |
| zig-safe | 13.4 | 7.3 | 7.1 | 6.9 | 6.7 | 1 |
| zig-fast | 8.7 | 7.7 | 6.6 | 6.2 | 6.3 | 1 |
| go | 7.8 | 6.2 | 5.4 | 6.2 | 6.3 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 78.0 | 39.8 | 19.9 | 23.1 | 25.1 | 1 |
| sword-native | 63.9 | 32.2 | 16.0 | 19.1 | 20.5 | 1 |
| sword-without-walked | 77.5 | 39.2 | 19.7 | 23.8 | 25.0 | 1 |
| sword-without-walked-mut | 79.1 | 39.9 | 20.0 | 22.6 | 25.2 | 1 |
| sword-without-captures | 84.9 | 42.9 | 21.4 | 24.5 | 28.0 | 1 |
| sword-without-versioned | 77.9 | 39.5 | 19.7 | 23.2 | 23.8 | 1 |
| sword-without-split | 91.0 | 45.9 | 22.7 | 25.3 | 28.5 | 1 |
| sword-without-deferred | 77.8 | 38.9 | 19.4 | 23.5 | 23.7 | 1 |
| sword-without-lanes | 77.4 | 39.2 | 19.7 | 22.8 | 24.8 | 1 |
| sword-without-steady | 77.6 | 38.8 | 19.6 | 22.8 | 23.5 | 1 |
| sword-rows | 21.3 | 11.5 | 5.7 | 7.7 | 8.0 | 1 |
| c-serial | 54.0 |  |  |  |  | 1 |
| c-restrict | 54.2 |  |  |  |  | 1 |
| c-omp | 51.2 | 24.9 | 12.4 | 16.1 | 14.3 | 1 |
| c-fastmath-serial | 53.9 |  |  |  |  | 1 |
| c-fastmath-omp | 51.4 | 25.0 | 12.5 | 15.6 | 15.1 | 1 |
| c-native-serial | 42.5 |  |  |  |  | 1 |
| c-native-omp | 42.4 | 20.4 | 10.2 | 13.4 | 12.9 | 1 |
| c-clang-serial | 50.2 |  |  |  |  | 1 |
| c-clang-omp | 47.7 | 23.5 | 11.8 | 17.4 | 15.1 | 1 |
| cpp-thread | 57.6 | 28.5 | 15.0 | 19.0 | 19.9 | 1 |
| rust-rayon | 92.2 | 46.2 | 23.2 | 23.3 | 23.9 | 1 |
| rust-slices | 21.2 | 10.9 | 5.7 | 5.7 | 6.2 | 1 |
| zig-safe | 94.9 | 48.8 | 27.9 | 34.4 | 36.0 | 1 |
| zig-fast | 43.3 | 22.0 | 14.4 | 18.9 | 21.2 | 1 |
| go | 79.1 | 40.3 | 20.3 | 22.5 | 21.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 91.8 | 42.5 | 40.5 | 41.4 | 42.3 | 1 |
| sword-native | 85.5 | 43.6 | 40.1 | 42.7 | 42.3 | 1 |
| sword-without-walked | 83.1 | 44.0 | 40.4 | 41.9 | 42.7 | 1 |
| sword-without-walked-mut | 82.4 | 42.3 | 40.3 | 42.2 | 43.0 | 1 |
| sword-without-captures | 90.8 | 44.2 | 43.0 | 43.6 | 46.7 | 1 |
| sword-without-versioned | 83.6 | 43.0 | 40.1 | 41.2 | 42.5 | 1 |
| sword-without-split | 103.8 | 52.1 | 50.8 | 52.1 | 53.3 | 1 |
| sword-without-deferred | 84.9 | 42.7 | 40.1 | 40.8 | 41.5 | 1 |
| sword-without-lanes | 85.1 | 44.7 | 41.1 | 41.6 | 41.7 | 1 |
| sword-without-steady | 86.7 | 43.1 | 40.0 | 40.9 | 41.8 | 1 |
| sword-rows | 31.9 | 17.5 | 13.2 | 14.0 | 14.7 | 1 |
| c-serial | 37.9 |  |  |  |  | 1 |
| c-restrict | 36.1 |  |  |  |  | 1 |
| c-omp | 43.0 | 18.7 | 17.3 | 18.1 | 19.0 | 1 |
| c-fastmath-serial | 48.6 |  |  |  |  | 1 |
| c-fastmath-omp | 48.8 | 26.2 | 21.0 | 22.1 | 23.8 | 1 |
| c-native-serial | 36.2 |  |  |  |  | 1 |
| c-native-omp | 43.0 | 22.1 | 18.7 | 21.5 | 18.4 | 1 |
| c-clang-serial | 45.2 |  |  |  |  | 1 |
| c-clang-omp | 44.3 | 23.0 | 22.6 | 29.8 | 29.4 | 1 |
| cpp-thread | 55.0 | 25.2 | 22.9 | 29.5 | 27.3 | 1 |
| rust-rayon | 108.2 | 54.9 | 48.5 | 50.2 | 49.7 | 1 |
| rust-slices | 27.5 | 18.0 | 12.7 | 13.6 | 14.4 | 1 |
| zig-safe | 83.1 | 44.5 | 45.4 | 56.8 | 56.1 | 1 |
| zig-fast | 41.0 | 23.7 | 23.4 | 27.1 | 34.9 | 1 |
| go | 91.4 | 48.6 | 47.6 | 47.9 | 47.7 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 42.3 | 37.6 | 22.9 | 20.9 | 20.9 | 1 |
| sword-native | 49.1 | 41.6 | 25.1 | 25.8 | 29.4 | 1 |
| sword-without-walked | 61.4 | 37.5 | 22.2 | 22.6 | 22.6 | 1 |
| sword-without-walked-mut | 74.1 | 41.5 | 32.2 | 29.0 | 27.9 | 1 |
| sword-without-captures | 77.4 | 50.1 | 30.6 | 33.6 | 34.8 | 1 |
| sword-without-versioned | 51.3 | 44.1 | 26.3 | 25.8 | 26.0 | 1 |
| sword-without-split | 88.9 | 61.7 | 35.0 | 34.6 | 34.3 | 1 |
| sword-without-deferred | 57.0 | 34.9 | 27.0 | 25.1 | 24.0 | 1 |
| sword-without-lanes | 47.9 | 37.4 | 25.0 | 23.5 | 22.3 | 1 |
| sword-without-steady | 65.6 | 35.3 | 24.2 | 22.5 | 23.0 | 1 |
| sword-rows | 35.8 | 27.8 | 21.2 | 20.6 | 20.4 | 1 |
| c-serial | 52.6 |  |  |  |  | 1 |
| c-restrict | 57.1 |  |  |  |  | 1 |
| c-omp | 55.1 | 35.5 | 30.6 | 23.0 | 23.8 | 1 |
| c-fastmath-serial | 53.8 |  |  |  |  | 1 |
| c-fastmath-omp | 55.4 | 35.7 | 30.0 | 20.1 | 22.1 | 1 |
| c-native-serial | 46.0 |  |  |  |  | 1 |
| c-native-omp | 47.7 | 35.7 | 25.3 | 23.9 | 19.5 | 1 |
| c-clang-serial | 50.9 |  |  |  |  | 1 |
| c-clang-omp | 53.7 | 31.1 | 25.2 | 23.5 | 22.0 | 1 |
| cpp-thread | 51.2 | 23.4 | 25.4 | 23.4 | 23.7 | 1 |
| rust-rayon | 144.3 | 48.4 | 44.6 | 37.6 | 43.5 | 1 |
| rust-slices | 34.5 | 21.8 | 27.8 | 17.3 | 18.6 | 1 |
| zig-safe | 102.1 | 54.3 | 47.9 | 36.4 | 46.0 | 1 |
| zig-fast | 40.9 | 28.6 | 27.7 | 27.6 | 29.5 | 1 |
| go | 96.5 | 47.1 | 43.5 | 41.2 | 37.6 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.8 | 346.5 | 173.7 | 176.2 | 176.5 | 1 |
| sword-native | 684.0 | 342.1 | 171.6 | 173.4 | 174.9 | 1 |
| sword-without-walked | 692.6 | 346.5 | 173.6 | 176.9 | 176.4 | 1 |
| sword-without-walked-mut | 692.7 | 346.5 | 173.6 | 175.6 | 175.9 | 1 |
| sword-without-captures | 692.6 | 346.5 | 173.7 | 175.1 | 176.2 | 1 |
| sword-without-versioned | 692.6 | 346.5 | 173.7 | 175.7 | 176.3 | 1 |
| sword-without-split | 692.6 | 346.5 | 173.7 | 175.2 | 177.3 | 1 |
| sword-without-deferred | 692.7 | 346.5 | 174.0 | 176.2 | 176.6 | 1 |
| sword-without-lanes | 692.6 | 346.5 | 173.6 | 176.2 | 177.2 | 1 |
| sword-without-steady | 692.7 | 346.5 | 173.6 | 176.0 | 176.4 | 1 |
| c-serial | 648.3 |  |  |  |  | 1 |
| c-restrict | 646.2 |  |  |  |  | 1 |
| c-omp | 636.9 | 318.8 | 159.7 | 159.6 | 159.7 | 1 |
| c-fastmath-serial | 627.7 |  |  |  |  | 1 |
| c-fastmath-omp | 627.6 | 313.9 | 157.2 | 157.4 | 157.3 | 1 |
| c-native-serial | 652.3 |  |  |  |  | 1 |
| c-native-omp | 647.9 | 323.8 | 162.9 | 162.8 | 162.4 | 1 |
| c-clang-serial | 770.4 |  |  |  |  | 1 |
| c-clang-omp | 768.2 | 384.7 | 193.2 | 193.7 | 193.2 | 1 |
| cpp-thread | 853.9 | 427.3 | 214.5 | 236.1 | 217.7 | 1 |
| rust-rayon | 693.0 | 347.1 | 173.9 | 174.1 | 174.1 | 1 |
| zig-safe | 683.2 | 342.2 | 171.9 | 185.8 | 174.6 | 1 |
| zig-fast | 897.0 | 448.9 | 225.3 | 236.7 | 230.0 | 1 |
| go | 678.5 | 339.3 | 170.5 | 179.2 | 174.0 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 838.0 | 419.7 | 230.8 | 232.9 | 233.4 | 1 |
| sword-native | 830.0 | 415.7 | 224.7 | 226.6 | 228.0 | 1 |
| sword-without-walked | 837.8 | 419.8 | 230.8 | 231.9 | 233.2 | 1 |
| sword-without-walked-mut | 837.8 | 419.6 | 230.7 | 232.0 | 233.3 | 1 |
| sword-without-captures | 838.1 | 419.9 | 230.7 | 231.8 | 233.4 | 1 |
| sword-without-versioned | 838.1 | 420.0 | 230.7 | 232.6 | 233.6 | 1 |
| sword-without-split | 838.5 | 419.8 | 230.6 | 232.2 | 233.6 | 1 |
| sword-without-deferred | 837.9 | 419.8 | 230.6 | 232.8 | 234.0 | 1 |
| sword-without-lanes | 838.1 | 419.7 | 230.8 | 232.0 | 234.9 | 1 |
| sword-without-steady | 838.3 | 419.8 | 230.6 | 232.8 | 234.2 | 1 |
| c-serial | 798.1 |  |  |  |  | 1 |
| c-restrict | 798.1 |  |  |  |  | 1 |
| c-omp | 798.5 | 399.8 | 212.0 | 212.1 | 212.3 | 1 |
| c-fastmath-serial | 793.6 |  |  |  |  | 1 |
| c-fastmath-omp | 794.0 | 397.7 | 212.9 | 213.0 | 213.3 | 1 |
| c-native-serial | 798.0 |  |  |  |  | 1 |
| c-native-omp | 798.6 | 399.8 | 211.9 | 212.1 | 212.2 | 1 |
| c-clang-serial | 826.2 |  |  |  |  | 1 |
| c-clang-omp | 823.7 | 413.2 | 225.3 | 225.7 | 225.9 | 1 |
| cpp-thread | 798.8 | 400.3 | 212.2 | 231.4 | 217.5 | 1 |
| rust-rayon | 830.0 | 415.6 | 226.9 | 227.1 | 227.5 | 1 |
| zig-safe | 835.6 | 419.1 | 227.1 | 248.9 | 232.0 | 1 |
| zig-fast | 833.0 | 417.8 | 225.8 | 236.9 | 230.3 | 1 |
| go | 827.0 | 414.8 | 224.6 | 234.2 | 227.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1076.6 | 532.6 | 375.9 | 348.8 | 375.4 | 1 |
| sword-native | 1065.6 | 489.9 | 340.6 | 360.3 | 337.2 | 1 |
| sword-without-walked | 1107.4 | 520.9 | 326.2 | 340.4 | 378.9 | 1 |
| sword-without-walked-mut | 1115.5 | 543.8 | 386.7 | 380.1 | 370.9 | 1 |
| sword-without-captures | 1102.9 | 547.3 | 382.3 | 386.8 | 380.7 | 1 |
| sword-without-versioned | 1021.5 | 509.9 | 360.2 | 402.9 | 377.8 | 1 |
| sword-without-split | 1096.9 | 559.9 | 364.8 | 362.8 | 395.4 | 1 |
| sword-without-deferred | 1026.5 | 552.5 | 356.2 | 335.0 | 395.0 | 1 |
| sword-without-lanes | 1077.4 | 490.1 | 308.1 | 333.6 | 368.7 | 1 |
| sword-without-steady | 1015.5 | 582.7 | 343.7 | 388.2 | 352.8 | 1 |
| c-serial | 829.8 |  |  |  |  | 1 |
| c-restrict | 833.6 |  |  |  |  | 1 |
| c-omp | 804.6 | 398.1 | 324.4 | 307.7 | 289.3 | 1 |
| c-fastmath-serial | 676.3 |  |  |  |  | 1 |
| c-fastmath-omp | 684.6 | 377.9 | 278.4 | 222.9 | 245.1 | 1 |
| c-native-serial | 964.7 |  |  |  |  | 1 |
| c-native-omp | 1013.2 | 456.5 | 338.8 | 320.7 | 362.0 | 1 |
| c-clang-serial | 853.0 |  |  |  |  | 1 |
| c-clang-omp | 783.3 | 411.5 | 270.7 | 272.6 | 282.5 | 1 |
| cpp-thread | 848.2 | 453.1 | 261.9 | 289.6 | 281.3 | 1 |
| rust-rayon | 984.5 | 539.0 | 319.7 | 322.4 | 351.9 | 1 |
| zig-safe | 932.6 | 471.9 | 306.8 | 322.8 | 371.7 | 1 |
| zig-fast | 988.5 | 525.1 | 385.6 | 446.5 | 366.9 | 1 |
| go | 1121.9 | 582.7 | 460.4 | 399.1 | 408.0 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.8 | 126.0 | 64.1 | 66.0 | 69.9 | 1 |
| sword-native | 246.8 | 123.6 | 62.3 | 65.4 | 68.1 | 1 |
| sword-without-walked | 251.2 | 125.8 | 63.9 | 66.9 | 69.0 | 1 |
| sword-without-walked-mut | 251.7 | 126.1 | 63.0 | 66.0 | 67.5 | 1 |
| sword-without-captures | 251.6 | 126.1 | 64.1 | 66.9 | 69.0 | 1 |
| sword-without-versioned | 270.8 | 135.5 | 68.3 | 71.0 | 71.2 | 1 |
| sword-without-split | 251.8 | 126.0 | 63.9 | 66.7 | 69.1 | 1 |
| sword-without-deferred | 251.5 | 126.0 | 65.4 | 66.9 | 69.1 | 1 |
| sword-without-lanes | 251.6 | 125.9 | 63.1 | 66.4 | 67.7 | 1 |
| sword-without-steady | 246.8 | 126.0 | 64.1 | 67.3 | 69.2 | 1 |
| c-serial | 237.6 |  |  |  |  | 1 |
| c-restrict | 237.6 |  |  |  |  | 1 |
| c-omp | 238.8 | 119.5 | 60.0 | 64.1 | 63.7 | 1 |
| c-fastmath-serial | 237.8 |  |  |  |  | 1 |
| c-fastmath-omp | 243.7 | 122.2 | 61.2 | 64.8 | 65.4 | 1 |
| c-native-serial | 250.4 |  |  |  |  | 1 |
| c-native-omp | 248.8 | 124.5 | 62.6 | 67.9 | 66.1 | 1 |
| c-clang-serial | 242.9 |  |  |  |  | 1 |
| c-clang-omp | 246.6 | 123.3 | 61.9 | 66.6 | 77.1 | 1 |
| cpp-thread | 240.2 | 120.3 | 61.2 | 69.9 | 71.4 | 1 |
| rust-rayon | 252.3 | 125.8 | 63.5 | 63.6 | 64.0 | 1 |
| zig-safe | 271.8 | 137.0 | 71.3 | 81.0 | 84.8 | 1 |
| zig-fast | 271.8 | 137.0 | 71.2 | 79.8 | 84.2 | 1 |
| go | 252.4 | 126.4 | 63.6 | 70.7 | 68.8 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 304.2 | 152.7 | 149.7 | 150.3 | 151.3 | 1 |
| sword-native | 302.9 | 151.8 | 150.0 | 150.4 | 151.5 | 1 |
| sword-without-walked | 304.8 | 152.9 | 149.8 | 150.1 | 151.4 | 1 |
| sword-without-walked-mut | 303.9 | 152.6 | 149.9 | 150.7 | 151.4 | 1 |
| sword-without-captures | 304.9 | 153.1 | 149.9 | 150.7 | 151.4 | 1 |
| sword-without-versioned | 311.9 | 156.7 | 152.9 | 153.5 | 154.1 | 1 |
| sword-without-split | 304.1 | 152.5 | 149.9 | 150.7 | 152.1 | 1 |
| sword-without-deferred | 304.3 | 152.8 | 149.7 | 150.3 | 151.4 | 1 |
| sword-without-lanes | 304.8 | 153.0 | 149.8 | 150.2 | 151.3 | 1 |
| sword-without-steady | 304.5 | 152.8 | 149.8 | 150.6 | 151.4 | 1 |
| c-serial | 73.7 |  |  |  |  | 1 |
| c-restrict | 73.6 |  |  |  |  | 1 |
| c-omp | 129.9 | 65.2 | 58.3 | 59.6 | 60.8 | 1 |
| c-fastmath-serial | 72.4 |  |  |  |  | 1 |
| c-fastmath-omp | 73.0 | 36.6 | 36.5 | 37.2 | 37.3 | 1 |
| c-native-serial | 73.6 |  |  |  |  | 1 |
| c-native-omp | 130.0 | 65.2 | 58.4 | 59.9 | 61.0 | 1 |
| c-clang-serial | 310.0 |  |  |  |  | 1 |
| c-clang-omp | 316.2 | 155.0 | 152.2 | 155.0 | 153.3 | 1 |
| cpp-thread | 130.5 | 65.9 | 59.5 | 66.9 | 66.0 | 1 |
| rust-rayon | 309.6 | 155.4 | 151.3 | 151.6 | 151.9 | 1 |
| zig-safe | 305.7 | 155.0 | 153.7 | 162.8 | 164.8 | 1 |
| zig-fast | 304.3 | 154.3 | 153.4 | 160.5 | 164.2 | 1 |
| go | 529.2 | 265.7 | 170.1 | 181.6 | 180.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 134.3 | 73.7 | 53.5 | 50.0 | 47.6 | 1 |
| sword-native | 138.0 | 72.7 | 48.6 | 41.8 | 58.5 | 1 |
| sword-without-walked | 133.9 | 72.4 | 52.1 | 52.7 | 48.8 | 1 |
| sword-without-walked-mut | 106.2 | 61.4 | 47.9 | 39.7 | 38.1 | 1 |
| sword-without-captures | 117.1 | 68.5 | 50.8 | 48.2 | 48.1 | 1 |
| sword-without-versioned | 177.3 | 94.2 | 60.5 | 69.5 | 69.5 | 1 |
| sword-without-split | 97.0 | 52.5 | 40.5 | 35.3 | 40.8 | 1 |
| sword-without-deferred | 131.0 | 69.8 | 52.3 | 50.4 | 46.2 | 1 |
| sword-without-lanes | 93.5 | 52.1 | 41.9 | 34.7 | 39.8 | 1 |
| sword-without-steady | 98.1 | 50.1 | 33.6 | 41.7 | 40.3 | 1 |
| c-serial | 96.5 |  |  |  |  | 1 |
| c-restrict | 93.5 |  |  |  |  | 1 |
| c-omp | 93.6 | 44.5 | 37.7 | 36.3 | 34.9 | 1 |
| c-fastmath-serial | 50.2 |  |  |  |  | 1 |
| c-fastmath-omp | 49.6 | 26.0 | 25.4 | 19.7 | 19.4 | 1 |
| c-native-serial | 98.1 |  |  |  |  | 1 |
| c-native-omp | 94.3 | 54.2 | 40.7 | 36.1 | 32.7 | 1 |
| c-clang-serial | 97.8 |  |  |  |  | 1 |
| c-clang-omp | 96.1 | 50.3 | 40.5 | 39.8 | 38.3 | 1 |
| cpp-thread | 89.2 | 44.6 | 39.5 | 37.2 | 41.6 | 1 |
| rust-rayon | 96.7 | 47.2 | 31.8 | 33.7 | 34.0 | 1 |
| zig-safe | 146.4 | 71.3 | 54.8 | 57.6 | 65.8 | 1 |
| zig-fast | 145.3 | 76.8 | 52.8 | 57.0 | 54.6 | 1 |
| go | 146.2 | 82.9 | 75.2 | 62.8 | 60.8 | 1 |

## Answers across every platform and thread count

| method | sum | saxpy | stencil | mandelbrot | nbody |
|---|---:|---:|---:|---:|---:|
| sword | 1 | 1 | 1 | 1 | 1 |
| sword-native | 1 | 1 | 1 | 1 | 1 |
| sword-without-walked | 1 | 1 | 1 | 1 | 1 |
| sword-without-walked-mut | 1 | 1 | 1 | 1 | 1 |
| sword-without-captures | 1 | 1 | 1 | 1 | 1 |
| sword-without-versioned | 1 | 1 | 1 | 1 | 1 |
| sword-without-split | 1 | 1 | 1 | 1 | 1 |
| sword-without-deferred | 1 | 1 | 1 | 1 | 1 |
| sword-without-lanes | 1 | 1 | 1 | 1 | 1 |
| sword-without-steady | 1 | 1 | 1 | 1 | 1 |
| sword-rows |  |  | 1 |  |  |
| c-serial | 1 | 1 | 1 | 1 | 1 |
| c-restrict | 1 | 1 | 1 | 1 | 1 |
| c-omp | 8 | 1 | 1 | 1 | 1 |
| c-lanes | 1 |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 |
| c-fastmath-omp | 13 | 1 | 2 | 2 | 1 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 |
| c-native-omp | 9 | 1 | 1 | 1 | 1 |
| c-native-lanes | 1 |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 |
| rust-rayon | 22 | 1 | 1 | 1 | 1 |
| rust-slices |  |  | 1 |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 |
| zig-fast | 5 | 1 | 1 | 1 | 1 |
| go | 5 | 1 | 1 | 2 | 1 |
