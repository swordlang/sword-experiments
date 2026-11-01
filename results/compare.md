## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.5 | 1.2 | 0.6 | 0.8 | 0.7 | 1 |
| sword-native | 2.9 | 1.4 | 0.7 | 1.1 | 1.1 | 1 |
| sword-without-walked | 4.6 | 2.5 | 1.2 | 1.5 | 1.4 | 1 |
| sword-without-walked-mut | 3.0 | 1.6 | 0.7 | 0.8 | 0.7 | 1 |
| sword-without-captures | 2.6 | 1.4 | 0.7 | 0.8 | 0.8 | 1 |
| sword-without-versioned | 2.7 | 1.5 | 0.7 | 1.2 | 0.9 | 1 |
| sword-without-split | 2.6 | 1.5 | 0.7 | 1.3 | 1.4 | 1 |
| sword-without-deferred | 2.9 | 1.5 | 0.7 | 0.9 | 0.7 | 1 |
| sword-without-lanes | 6.2 | 3.2 | 1.7 | 1.7 | 1.7 | 1 |
| sword-without-steady | 2.4 | 1.3 | 0.6 | 0.6 | 0.8 | 1 |
| c-serial | 6.3 |  |  |  |  | 1 |
| c-restrict | 6.1 |  |  |  |  | 1 |
| c-omp | 6.5 | 3.2 | 1.5 | 2.3 | 2.0 | 5 |
| c-lanes | 2.9 |  |  |  |  | 1 |
| c-lanes-omp | 3.0 | 1.5 | 0.7 | 1.1 | 0.9 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.5 | 3.3 | 1.8 | 2.0 | 2.0 | 6 |
| c-native-serial | 6.2 |  |  |  |  | 1 |
| c-native-omp | 6.1 | 3.1 | 1.6 | 1.8 | 2.0 | 7 |
| c-native-lanes | 2.9 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.8 | 1.4 | 0.7 | 1.0 | 0.9 | 1 |
| c-clang-serial | 6.3 |  |  |  |  | 1 |
| c-clang-omp | 6.2 | 3.1 | 1.5 | 2.3 | 1.9 | 5 |
| cpp-thread | 6.5 | 3.3 | 1.8 | 2.5 | 2.6 | 5 |
| rust-rayon | 6.4 | 3.5 | 1.6 | 1.6 | 1.6 | 9 |
| zig-safe | 6.9 | 3.5 | 2.1 | 2.6 | 2.6 | 5 |
| zig-fast | 6.7 | 3.5 | 2.1 | 2.7 | 3.0 | 5 |
| go | 6.7 | 3.3 | 1.8 | 1.8 | 1.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.4 | 1.8 | 1.4 | 1.5 | 1.5 | 1 |
| sword-native | 2.9 | 1.7 | 1.4 | 1.4 | 1.5 | 1 |
| sword-without-walked | 4.5 | 2.4 | 1.8 | 2.0 | 1.9 | 1 |
| sword-without-walked-mut | 3.6 | 1.9 | 1.4 | 1.6 | 1.6 | 1 |
| sword-without-captures | 3.4 | 2.0 | 1.5 | 1.6 | 1.6 | 1 |
| sword-without-versioned | 3.3 | 1.9 | 1.5 | 1.5 | 1.6 | 1 |
| sword-without-split | 3.4 | 1.9 | 1.5 | 1.5 | 1.6 | 1 |
| sword-without-deferred | 3.4 | 1.9 | 1.5 | 1.7 | 1.7 | 1 |
| sword-without-lanes | 9.5 | 4.8 | 2.5 | 2.5 | 2.7 | 1 |
| sword-without-steady | 3.3 | 1.8 | 1.5 | 1.5 | 1.5 | 1 |
| c-serial | 9.5 |  |  |  |  | 1 |
| c-restrict | 9.5 |  |  |  |  | 1 |
| c-omp | 9.5 | 4.8 | 2.4 | 2.5 | 3.1 | 6 |
| c-lanes | 3.9 |  |  |  |  | 1 |
| c-lanes-omp | 3.9 | 2.1 | 1.5 | 1.9 | 1.8 | 1 |
| c-fastmath-serial | 3.4 |  |  |  |  | 1 |
| c-fastmath-omp | 9.5 | 4.8 | 2.4 | 2.5 | 3.2 | 5 |
| c-native-serial | 9.5 |  |  |  |  | 1 |
| c-native-omp | 9.5 | 4.8 | 2.4 | 3.2 | 3.1 | 7 |
| c-native-lanes | 3.7 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.7 | 2.0 | 1.4 | 1.7 | 1.7 | 1 |
| c-clang-serial | 9.5 |  |  |  |  | 1 |
| c-clang-omp | 9.5 | 4.8 | 2.4 | 3.7 | 3.7 | 5 |
| cpp-thread | 9.6 | 4.9 | 2.6 | 3.8 | 3.5 | 5 |
| rust-rayon | 9.5 | 4.8 | 2.5 | 2.5 | 2.6 | 10 |
| zig-safe | 9.8 | 5.2 | 3.2 | 4.1 | 4.3 | 5 |
| zig-fast | 9.8 | 5.2 | 3.1 | 4.0 | 4.2 | 5 |
| go | 9.6 | 4.8 | 2.5 | 2.5 | 2.6 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.0 | 2.1 | 2.0 | 1.9 | 2.0 | 1 |
| sword-native | 2.1 | 2.0 | 1.9 | 2.0 | 1.8 | 1 |
| sword-without-walked | 3.7 | 2.0 | 2.0 | 2.1 | 2.2 | 1 |
| sword-without-walked-mut | 1.9 | 1.8 | 1.9 | 1.7 | 1.9 | 1 |
| sword-without-captures | 1.9 | 1.9 | 2.0 | 2.2 | 2.3 | 1 |
| sword-without-versioned | 2.0 | 2.7 | 2.1 | 2.0 | 2.0 | 1 |
| sword-without-split | 2.2 | 1.8 | 2.0 | 2.0 | 2.1 | 1 |
| sword-without-deferred | 2.0 | 2.2 | 2.1 | 2.1 | 2.1 | 1 |
| sword-without-lanes | 10.4 | 6.5 | 4.0 | 4.1 | 4.0 | 1 |
| sword-without-steady | 2.1 | 2.1 | 2.1 | 1.7 | 2.1 | 1 |
| c-serial | 11.4 |  |  |  |  | 1 |
| c-restrict | 11.3 |  |  |  |  | 1 |
| c-omp | 11.4 | 5.8 | 5.6 | 4.6 | 4.9 | 5 |
| c-lanes | 2.1 |  |  |  |  | 1 |
| c-lanes-omp | 2.0 | 2.1 | 2.0 | 1.9 | 2.0 | 1 |
| c-fastmath-serial | 2.1 |  |  |  |  | 1 |
| c-fastmath-omp | 2.2 | 2.0 | 2.0 | 1.9 | 2.1 | 5 |
| c-native-serial | 11.8 |  |  |  |  | 1 |
| c-native-omp | 11.8 | 6.5 | 5.9 | 5.0 | 4.9 | 5 |
| c-native-lanes | 2.2 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.2 | 2.4 | 2.0 | 1.9 | 2.1 | 1 |
| c-clang-serial | 11.7 |  |  |  |  | 1 |
| c-clang-omp | 11.4 | 6.4 | 5.8 | 5.1 | 4.8 | 5 |
| cpp-thread | 11.7 | 6.8 | 6.2 | 4.5 | 5.0 | 5 |
| rust-rayon | 11.0 | 6.2 | 4.4 | 4.5 | 4.5 | 11 |
| zig-safe | 11.9 | 6.7 | 6.4 | 4.8 | 5.1 | 5 |
| zig-fast | 11.8 | 6.4 | 5.9 | 5.3 | 6.4 | 5 |
| go | 12.4 | 6.2 | 5.3 | 4.9 | 4.8 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.7 | 3.5 | 1.9 | 1.8 | 2.2 | 1 |
| sword-native | 6.8 | 3.3 | 1.7 | 1.8 | 1.7 | 1 |
| sword-without-walked | 5.9 | 3.5 | 1.9 | 1.7 | 2.2 | 1 |
| sword-without-walked-mut | 5.6 | 2.9 | 1.8 | 1.8 | 2.5 | 1 |
| sword-without-captures | 8.8 | 5.1 | 2.6 | 2.7 | 2.9 | 1 |
| sword-without-versioned | 6.6 | 3.4 | 1.8 | 1.9 | 2.0 | 1 |
| sword-without-split | 6.7 | 3.4 | 1.8 | 2.0 | 2.1 | 1 |
| sword-without-deferred | 6.4 | 3.5 | 1.8 | 1.8 | 1.9 | 1 |
| sword-without-lanes | 5.7 | 3.3 | 1.6 | 1.7 | 1.9 | 1 |
| sword-without-steady | 6.4 | 3.2 | 1.6 | 1.8 | 2.2 | 1 |
| c-serial | 6.3 |  |  |  |  | 1 |
| c-restrict | 6.7 |  |  |  |  | 1 |
| c-omp | 6.7 | 3.6 | 2.0 | 2.8 | 2.3 | 1 |
| c-fastmath-serial | 6.9 |  |  |  |  | 1 |
| c-fastmath-omp | 6.3 | 3.7 | 2.0 | 2.7 | 2.4 | 1 |
| c-native-serial | 6.8 |  |  |  |  | 1 |
| c-native-omp | 6.8 | 3.6 | 2.0 | 2.9 | 2.2 | 1 |
| c-clang-serial | 6.5 |  |  |  |  | 1 |
| c-clang-omp | 6.6 | 3.3 | 1.8 | 2.5 | 2.3 | 1 |
| cpp-thread | 7.1 | 4.0 | 2.2 | 2.3 | 2.7 | 1 |
| rust-rayon | 6.6 | 3.5 | 1.9 | 2.0 | 2.2 | 1 |
| zig-safe | 11.2 | 5.9 | 3.2 | 3.9 | 4.0 | 1 |
| zig-fast | 9.2 | 5.0 | 2.8 | 3.3 | 3.6 | 1 |
| go | 7.1 | 4.0 | 2.2 | 2.2 | 2.3 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 5.8 | 4.3 | 4.2 | 4.1 | 4.3 | 1 |
| sword-native | 5.0 | 3.9 | 3.9 | 4.0 | 4.0 | 1 |
| sword-without-walked | 5.7 | 4.6 | 4.2 | 4.1 | 4.3 | 1 |
| sword-without-walked-mut | 5.9 | 4.0 | 4.0 | 4.4 | 4.4 | 1 |
| sword-without-captures | 8.7 | 4.8 | 4.3 | 4.3 | 4.2 | 1 |
| sword-without-versioned | 5.9 | 3.9 | 4.4 | 3.8 | 4.2 | 1 |
| sword-without-split | 5.7 | 4.4 | 4.2 | 3.9 | 4.1 | 1 |
| sword-without-deferred | 5.9 | 4.3 | 4.1 | 4.4 | 4.3 | 1 |
| sword-without-lanes | 6.1 | 4.4 | 4.2 | 4.1 | 4.1 | 1 |
| sword-without-steady | 5.9 | 4.2 | 4.0 | 4.1 | 4.0 | 1 |
| c-serial | 5.6 |  |  |  |  | 1 |
| c-restrict | 5.5 |  |  |  |  | 1 |
| c-omp | 7.1 | 4.2 | 4.1 | 4.6 | 5.1 | 1 |
| c-fastmath-serial | 5.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.9 | 4.3 | 4.1 | 4.1 | 4.2 | 1 |
| c-native-serial | 5.5 |  |  |  |  | 1 |
| c-native-omp | 6.7 | 4.4 | 4.1 | 4.0 | 4.1 | 1 |
| c-clang-serial | 6.0 |  |  |  |  | 1 |
| c-clang-omp | 5.9 | 4.0 | 4.0 | 4.2 | 4.3 | 1 |
| cpp-thread | 7.0 | 4.3 | 4.2 | 4.3 | 4.6 | 1 |
| rust-rayon | 6.1 | 4.3 | 4.1 | 4.2 | 4.6 | 1 |
| zig-safe | 11.0 | 5.7 | 5.6 | 6.1 | 6.9 | 1 |
| zig-fast | 8.9 | 5.1 | 4.9 | 5.6 | 5.6 | 1 |
| go | 7.5 | 5.0 | 4.8 | 4.8 | 4.8 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.3 | 5.3 | 5.4 | 5.6 | 5.5 | 1 |
| sword-native | 6.2 | 6.4 | 5.7 | 6.0 | 6.4 | 1 |
| sword-without-walked | 6.1 | 6.1 | 5.8 | 5.8 | 5.3 | 1 |
| sword-without-walked-mut | 6.5 | 5.6 | 5.3 | 5.4 | 5.5 | 1 |
| sword-without-captures | 9.7 | 6.6 | 5.5 | 6.2 | 5.9 | 1 |
| sword-without-versioned | 6.2 | 5.6 | 5.2 | 5.5 | 5.7 | 1 |
| sword-without-split | 5.8 | 5.8 | 5.4 | 5.3 | 5.8 | 1 |
| sword-without-deferred | 6.4 | 5.9 | 5.4 | 5.3 | 5.4 | 1 |
| sword-without-lanes | 5.8 | 5.3 | 5.2 | 5.4 | 5.4 | 1 |
| sword-without-steady | 5.4 | 5.3 | 5.8 | 5.5 | 5.6 | 1 |
| c-serial | 5.7 |  |  |  |  | 1 |
| c-restrict | 5.8 |  |  |  |  | 1 |
| c-omp | 5.9 | 5.8 | 6.2 | 6.0 | 5.6 | 1 |
| c-fastmath-serial | 6.8 |  |  |  |  | 1 |
| c-fastmath-omp | 6.3 | 6.1 | 5.7 | 5.4 | 5.6 | 1 |
| c-native-serial | 6.3 |  |  |  |  | 1 |
| c-native-omp | 6.8 | 5.6 | 6.0 | 5.6 | 5.9 | 1 |
| c-clang-serial | 5.8 |  |  |  |  | 1 |
| c-clang-omp | 5.6 | 5.9 | 5.9 | 5.5 | 6.0 | 1 |
| cpp-thread | 6.3 | 5.7 | 5.9 | 5.6 | 5.8 | 1 |
| rust-rayon | 6.0 | 6.0 | 5.9 | 6.9 | 6.4 | 1 |
| zig-safe | 12.1 | 8.0 | 8.2 | 7.0 | 6.9 | 1 |
| zig-fast | 11.0 | 7.0 | 6.6 | 6.3 | 6.5 | 1 |
| go | 10.4 | 6.8 | 6.4 | 6.1 | 6.1 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 76.2 | 38.2 | 19.5 | 23.1 | 26.1 | 1 |
| sword-native | 61.0 | 31.1 | 15.9 | 19.3 | 21.5 | 1 |
| sword-without-walked | 76.1 | 38.2 | 19.5 | 21.9 | 23.7 | 1 |
| sword-without-walked-mut | 78.8 | 39.2 | 19.7 | 22.8 | 24.9 | 1 |
| sword-without-captures | 83.3 | 42.8 | 21.4 | 26.0 | 26.2 | 1 |
| sword-without-versioned | 76.7 | 39.4 | 19.7 | 23.6 | 24.5 | 1 |
| sword-without-split | 89.8 | 45.7 | 22.7 | 26.1 | 26.5 | 1 |
| sword-without-deferred | 76.5 | 38.7 | 19.3 | 22.3 | 26.0 | 1 |
| sword-without-lanes | 76.0 | 38.8 | 19.3 | 23.3 | 23.2 | 1 |
| sword-without-steady | 77.3 | 38.8 | 19.5 | 22.9 | 25.4 | 1 |
| sword-rows | 20.7 | 10.7 | 5.5 | 7.9 | 7.0 | 1 |
| c-serial | 53.9 |  |  |  |  | 1 |
| c-restrict | 54.0 |  |  |  |  | 1 |
| c-omp | 48.4 | 24.8 | 12.3 | 15.3 | 14.3 | 1 |
| c-fastmath-serial | 54.6 |  |  |  |  | 1 |
| c-fastmath-omp | 51.5 | 26.2 | 12.4 | 16.2 | 14.8 | 1 |
| c-native-serial | 42.9 |  |  |  |  | 1 |
| c-native-omp | 42.4 | 20.4 | 10.2 | 12.9 | 12.1 | 1 |
| c-clang-serial | 47.2 |  |  |  |  | 1 |
| c-clang-omp | 46.6 | 23.0 | 11.8 | 17.8 | 17.2 | 1 |
| cpp-thread | 57.2 | 27.7 | 15.1 | 19.7 | 19.7 | 1 |
| rust-rayon | 91.8 | 46.4 | 23.3 | 23.5 | 23.7 | 1 |
| rust-slices | 20.7 | 10.3 | 5.5 | 5.6 | 6.2 | 1 |
| zig-safe | 95.6 | 48.3 | 27.3 | 34.8 | 35.2 | 1 |
| zig-fast | 42.7 | 21.4 | 13.9 | 17.8 | 20.9 | 1 |
| go | 76.4 | 38.5 | 19.5 | 22.8 | 21.9 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 90.3 | 44.3 | 40.1 | 41.0 | 42.0 | 1 |
| sword-native | 87.8 | 43.6 | 40.2 | 41.8 | 42.7 | 1 |
| sword-without-walked | 84.2 | 43.7 | 40.6 | 40.8 | 42.2 | 1 |
| sword-without-walked-mut | 84.8 | 41.8 | 40.4 | 41.1 | 43.0 | 1 |
| sword-without-captures | 89.3 | 44.6 | 44.5 | 44.8 | 45.2 | 1 |
| sword-without-versioned | 84.3 | 42.9 | 40.0 | 40.8 | 42.5 | 1 |
| sword-without-split | 104.1 | 52.9 | 51.2 | 51.5 | 53.0 | 1 |
| sword-without-deferred | 85.4 | 42.5 | 40.5 | 40.9 | 41.8 | 1 |
| sword-without-lanes | 87.4 | 43.6 | 40.1 | 41.4 | 42.2 | 1 |
| sword-without-steady | 85.7 | 43.8 | 40.5 | 41.4 | 42.7 | 1 |
| sword-rows | 32.6 | 18.2 | 13.8 | 14.5 | 15.3 | 1 |
| c-serial | 37.0 |  |  |  |  | 1 |
| c-restrict | 36.9 |  |  |  |  | 1 |
| c-omp | 41.3 | 22.4 | 17.3 | 18.5 | 19.1 | 1 |
| c-fastmath-serial | 49.2 |  |  |  |  | 1 |
| c-fastmath-omp | 54.7 | 25.1 | 21.6 | 22.7 | 24.4 | 1 |
| c-native-serial | 37.7 |  |  |  |  | 1 |
| c-native-omp | 38.0 | 19.5 | 20.1 | 18.4 | 19.2 | 1 |
| c-clang-serial | 44.8 |  |  |  |  | 1 |
| c-clang-omp | 44.3 | 23.5 | 22.5 | 30.2 | 25.5 | 1 |
| cpp-thread | 50.0 | 25.4 | 22.7 | 29.2 | 29.8 | 1 |
| rust-rayon | 109.8 | 55.0 | 48.7 | 50.0 | 49.7 | 1 |
| rust-slices | 32.2 | 16.7 | 13.2 | 15.5 | 15.9 | 1 |
| zig-safe | 83.0 | 44.5 | 45.5 | 55.5 | 56.5 | 1 |
| zig-fast | 42.1 | 24.2 | 23.6 | 27.5 | 35.3 | 1 |
| go | 87.6 | 48.0 | 47.5 | 47.6 | 47.4 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 55.8 | 38.1 | 35.2 | 25.5 | 29.4 | 1 |
| sword-native | 54.6 | 38.7 | 29.7 | 27.0 | 29.9 | 1 |
| sword-without-walked | 56.7 | 37.4 | 24.7 | 30.4 | 27.2 | 1 |
| sword-without-walked-mut | 68.7 | 33.2 | 27.9 | 26.7 | 25.3 | 1 |
| sword-without-captures | 77.6 | 46.9 | 35.3 | 32.2 | 32.9 | 1 |
| sword-without-versioned | 51.5 | 37.7 | 26.3 | 24.4 | 22.7 | 1 |
| sword-without-split | 86.5 | 63.6 | 39.0 | 43.3 | 32.5 | 1 |
| sword-without-deferred | 59.9 | 49.5 | 23.3 | 24.8 | 25.1 | 1 |
| sword-without-lanes | 62.1 | 41.9 | 23.2 | 24.3 | 24.7 | 1 |
| sword-without-steady | 59.3 | 43.1 | 21.3 | 21.6 | 25.4 | 1 |
| sword-rows | 33.9 | 27.3 | 23.7 | 24.7 | 21.3 | 1 |
| c-serial | 44.4 |  |  |  |  | 1 |
| c-restrict | 50.7 |  |  |  |  | 1 |
| c-omp | 49.5 | 35.7 | 27.4 | 26.8 | 24.7 | 1 |
| c-fastmath-serial | 56.8 |  |  |  |  | 1 |
| c-fastmath-omp | 58.4 | 38.0 | 31.1 | 33.5 | 25.1 | 1 |
| c-native-serial | 53.8 |  |  |  |  | 1 |
| c-native-omp | 56.5 | 37.5 | 29.2 | 23.8 | 24.1 | 1 |
| c-clang-serial | 44.4 |  |  |  |  | 1 |
| c-clang-omp | 46.3 | 33.4 | 29.9 | 26.7 | 21.1 | 1 |
| cpp-thread | 47.8 | 40.3 | 27.1 | 26.9 | 25.1 | 1 |
| rust-rayon | 122.3 | 57.8 | 38.2 | 42.8 | 43.0 | 1 |
| rust-slices | 30.8 | 22.5 | 23.7 | 22.7 | 21.5 | 1 |
| zig-safe | 116.8 | 71.1 | 62.7 | 52.0 | 52.7 | 1 |
| zig-fast | 52.6 | 32.6 | 28.9 | 26.8 | 24.8 | 1 |
| go | 92.8 | 68.5 | 54.0 | 49.0 | 44.7 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.9 | 346.6 | 173.6 | 176.9 | 175.6 | 1 |
| sword-native | 684.0 | 342.2 | 171.5 | 173.7 | 174.6 | 1 |
| sword-without-walked | 693.0 | 346.6 | 173.7 | 177.3 | 175.8 | 1 |
| sword-without-walked-mut | 692.9 | 346.6 | 173.8 | 175.3 | 176.4 | 1 |
| sword-without-captures | 692.8 | 346.6 | 174.0 | 175.8 | 177.0 | 1 |
| sword-without-versioned | 692.8 | 346.6 | 174.7 | 175.1 | 176.9 | 1 |
| sword-without-split | 692.6 | 346.6 | 173.9 | 175.1 | 177.3 | 1 |
| sword-without-deferred | 692.8 | 346.5 | 173.8 | 175.2 | 176.6 | 1 |
| sword-without-lanes | 692.9 | 346.6 | 174.0 | 176.3 | 176.2 | 1 |
| sword-without-steady | 692.7 | 346.6 | 173.9 | 176.2 | 176.5 | 1 |
| c-serial | 646.9 |  |  |  |  | 1 |
| c-restrict | 647.4 |  |  |  |  | 1 |
| c-omp | 636.8 | 318.5 | 159.9 | 159.7 | 159.4 | 1 |
| c-fastmath-serial | 627.3 |  |  |  |  | 1 |
| c-fastmath-omp | 627.9 | 314.0 | 157.3 | 157.3 | 157.3 | 1 |
| c-native-serial | 652.6 |  |  |  |  | 1 |
| c-native-omp | 647.6 | 325.2 | 163.6 | 163.2 | 163.2 | 1 |
| c-clang-serial | 770.6 |  |  |  |  | 1 |
| c-clang-omp | 768.3 | 384.9 | 193.1 | 193.4 | 193.5 | 1 |
| cpp-thread | 853.9 | 427.3 | 214.6 | 237.0 | 217.9 | 1 |
| rust-rayon | 693.2 | 347.3 | 174.1 | 173.9 | 174.1 | 1 |
| zig-safe | 683.8 | 342.7 | 172.1 | 190.5 | 175.7 | 1 |
| zig-fast | 897.2 | 449.0 | 225.5 | 247.8 | 229.9 | 1 |
| go | 678.2 | 339.7 | 170.5 | 176.2 | 173.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 838.6 | 419.9 | 230.8 | 234.4 | 234.1 | 1 |
| sword-native | 830.2 | 415.9 | 224.9 | 226.9 | 227.0 | 1 |
| sword-without-walked | 838.5 | 420.2 | 231.0 | 233.0 | 234.3 | 1 |
| sword-without-walked-mut | 838.4 | 419.8 | 230.9 | 232.5 | 234.2 | 1 |
| sword-without-captures | 838.2 | 419.8 | 231.0 | 234.4 | 234.5 | 1 |
| sword-without-versioned | 838.7 | 420.0 | 231.7 | 233.1 | 233.8 | 1 |
| sword-without-split | 838.3 | 419.9 | 231.0 | 233.6 | 233.3 | 1 |
| sword-without-deferred | 838.4 | 420.0 | 230.9 | 233.5 | 234.1 | 1 |
| sword-without-lanes | 838.5 | 420.0 | 231.0 | 232.7 | 234.9 | 1 |
| sword-without-steady | 838.5 | 419.8 | 231.2 | 232.4 | 235.3 | 1 |
| c-serial | 798.4 |  |  |  |  | 1 |
| c-restrict | 798.2 |  |  |  |  | 1 |
| c-omp | 798.7 | 400.0 | 212.2 | 212.2 | 212.4 | 1 |
| c-fastmath-serial | 793.9 |  |  |  |  | 1 |
| c-fastmath-omp | 794.3 | 397.8 | 212.9 | 213.1 | 213.4 | 1 |
| c-native-serial | 798.4 |  |  |  |  | 1 |
| c-native-omp | 798.7 | 399.9 | 212.1 | 212.2 | 212.3 | 1 |
| c-clang-serial | 826.3 |  |  |  |  | 1 |
| c-clang-omp | 824.1 | 413.2 | 225.5 | 225.7 | 225.5 | 1 |
| cpp-thread | 798.8 | 400.5 | 212.4 | 223.7 | 216.4 | 1 |
| rust-rayon | 829.7 | 415.9 | 228.8 | 227.5 | 227.6 | 1 |
| zig-safe | 835.9 | 418.8 | 227.3 | 247.4 | 231.3 | 1 |
| zig-fast | 833.5 | 417.8 | 226.2 | 245.4 | 231.0 | 1 |
| go | 828.0 | 414.8 | 224.4 | 229.7 | 228.7 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1096.6 | 563.5 | 383.4 | 388.9 | 374.5 | 1 |
| sword-native | 1111.5 | 566.2 | 383.7 | 366.8 | 382.7 | 1 |
| sword-without-walked | 1189.0 | 590.9 | 398.2 | 377.0 | 390.7 | 1 |
| sword-without-walked-mut | 1177.4 | 559.4 | 382.4 | 381.7 | 386.6 | 1 |
| sword-without-captures | 1173.3 | 557.5 | 361.9 | 388.7 | 379.2 | 1 |
| sword-without-versioned | 1170.4 | 572.0 | 395.3 | 395.9 | 384.4 | 1 |
| sword-without-split | 1134.1 | 615.1 | 412.3 | 400.4 | 375.6 | 1 |
| sword-without-deferred | 1085.4 | 577.0 | 396.7 | 395.4 | 391.0 | 1 |
| sword-without-lanes | 1109.9 | 561.5 | 389.2 | 416.5 | 410.5 | 1 |
| sword-without-steady | 1162.4 | 572.1 | 379.5 | 372.8 | 404.0 | 1 |
| c-serial | 931.4 |  |  |  |  | 1 |
| c-restrict | 951.7 |  |  |  |  | 1 |
| c-omp | 922.0 | 454.3 | 312.0 | 320.1 | 323.0 | 1 |
| c-fastmath-serial | 782.6 |  |  |  |  | 1 |
| c-fastmath-omp | 780.0 | 398.7 | 273.6 | 293.2 | 266.9 | 1 |
| c-native-serial | 1059.2 |  |  |  |  | 1 |
| c-native-omp | 1137.5 | 560.5 | 409.2 | 361.0 | 375.3 | 1 |
| c-clang-serial | 923.8 |  |  |  |  | 1 |
| c-clang-omp | 930.7 | 507.0 | 316.7 | 320.1 | 334.8 | 1 |
| cpp-thread | 969.1 | 513.1 | 329.2 | 326.8 | 332.2 | 1 |
| rust-rayon | 1093.6 | 588.7 | 400.4 | 403.4 | 482.8 | 1 |
| zig-safe | 1165.1 | 610.7 | 396.5 | 386.0 | 394.5 | 1 |
| zig-fast | 1143.8 | 567.1 | 410.9 | 382.4 | 389.4 | 1 |
| go | 1174.1 | 624.1 | 398.4 | 391.4 | 430.7 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.6 | 126.0 | 64.9 | 67.0 | 69.4 | 1 |
| sword-native | 246.9 | 123.6 | 62.2 | 64.8 | 68.2 | 1 |
| sword-without-walked | 251.3 | 125.8 | 64.4 | 67.0 | 68.9 | 1 |
| sword-without-walked-mut | 251.8 | 126.1 | 64.0 | 66.2 | 66.4 | 1 |
| sword-without-captures | 251.6 | 126.1 | 64.8 | 66.9 | 69.0 | 1 |
| sword-without-versioned | 270.6 | 135.5 | 68.1 | 71.0 | 71.5 | 1 |
| sword-without-split | 252.1 | 125.7 | 64.1 | 68.3 | 69.2 | 1 |
| sword-without-deferred | 251.7 | 126.0 | 64.0 | 66.0 | 66.8 | 1 |
| sword-without-lanes | 251.6 | 125.9 | 63.1 | 66.1 | 67.2 | 1 |
| sword-without-steady | 251.8 | 126.1 | 64.0 | 67.0 | 69.2 | 1 |
| c-serial | 237.7 |  |  |  |  | 1 |
| c-restrict | 237.6 |  |  |  |  | 1 |
| c-omp | 238.7 | 119.6 | 60.1 | 60.5 | 63.0 | 1 |
| c-fastmath-serial | 237.9 |  |  |  |  | 1 |
| c-fastmath-omp | 243.7 | 122.2 | 63.0 | 66.6 | 63.5 | 1 |
| c-native-serial | 250.4 |  |  |  |  | 1 |
| c-native-omp | 248.9 | 124.5 | 63.6 | 64.7 | 66.5 | 1 |
| c-clang-serial | 243.8 |  |  |  |  | 1 |
| c-clang-omp | 246.2 | 123.4 | 61.9 | 75.5 | 77.2 | 1 |
| cpp-thread | 240.8 | 120.7 | 61.2 | 70.9 | 71.0 | 1 |
| rust-rayon | 252.1 | 126.4 | 63.3 | 62.7 | 64.2 | 1 |
| zig-safe | 271.8 | 137.1 | 71.6 | 80.4 | 85.2 | 1 |
| zig-fast | 271.9 | 138.3 | 71.2 | 79.3 | 84.2 | 1 |
| go | 253.2 | 126.9 | 63.7 | 69.0 | 67.0 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 304.3 | 152.7 | 149.8 | 150.4 | 150.9 | 1 |
| sword-native | 302.9 | 151.9 | 149.9 | 150.7 | 151.2 | 1 |
| sword-without-walked | 304.8 | 153.0 | 149.8 | 150.0 | 151.4 | 1 |
| sword-without-walked-mut | 304.1 | 152.6 | 149.9 | 150.2 | 152.1 | 1 |
| sword-without-captures | 304.8 | 152.9 | 149.9 | 151.0 | 151.7 | 1 |
| sword-without-versioned | 312.0 | 157.5 | 152.9 | 153.7 | 154.6 | 1 |
| sword-without-split | 304.2 | 152.6 | 149.9 | 150.2 | 151.4 | 1 |
| sword-without-deferred | 304.6 | 152.7 | 149.8 | 150.0 | 151.5 | 1 |
| sword-without-lanes | 304.8 | 152.9 | 149.8 | 150.6 | 151.8 | 1 |
| sword-without-steady | 304.3 | 152.7 | 149.8 | 150.1 | 152.3 | 1 |
| c-serial | 73.7 |  |  |  |  | 1 |
| c-restrict | 73.6 |  |  |  |  | 1 |
| c-omp | 129.9 | 65.2 | 58.5 | 60.5 | 61.6 | 1 |
| c-fastmath-serial | 72.3 |  |  |  |  | 1 |
| c-fastmath-omp | 72.9 | 36.5 | 36.5 | 37.6 | 37.8 | 1 |
| c-native-serial | 73.7 |  |  |  |  | 1 |
| c-native-omp | 130.1 | 65.2 | 58.4 | 59.7 | 61.1 | 1 |
| c-clang-serial | 310.0 |  |  |  |  | 1 |
| c-clang-omp | 316.4 | 154.9 | 152.2 | 152.3 | 154.8 | 1 |
| cpp-thread | 130.7 | 66.0 | 59.6 | 68.1 | 66.9 | 1 |
| rust-rayon | 309.6 | 155.5 | 151.3 | 151.6 | 151.8 | 1 |
| zig-safe | 305.7 | 155.0 | 153.8 | 162.5 | 165.0 | 1 |
| zig-fast | 304.7 | 154.5 | 153.5 | 162.6 | 165.1 | 1 |
| go | 529.8 | 265.8 | 169.7 | 178.3 | 177.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 130.4 | 71.7 | 45.9 | 53.7 | 52.0 | 1 |
| sword-native | 127.9 | 76.1 | 57.2 | 48.4 | 58.0 | 1 |
| sword-without-walked | 138.2 | 72.2 | 46.1 | 46.4 | 46.0 | 1 |
| sword-without-walked-mut | 125.1 | 69.3 | 51.5 | 44.3 | 48.6 | 1 |
| sword-without-captures | 116.2 | 71.0 | 48.2 | 49.0 | 45.2 | 1 |
| sword-without-versioned | 213.4 | 110.2 | 78.9 | 80.8 | 76.9 | 1 |
| sword-without-split | 118.5 | 59.1 | 50.3 | 49.6 | 47.2 | 1 |
| sword-without-deferred | 111.2 | 66.9 | 49.9 | 49.1 | 48.2 | 1 |
| sword-without-lanes | 139.0 | 75.2 | 50.0 | 48.9 | 49.6 | 1 |
| sword-without-steady | 131.0 | 66.4 | 49.2 | 44.8 | 46.8 | 1 |
| c-serial | 114.6 |  |  |  |  | 1 |
| c-restrict | 120.6 |  |  |  |  | 1 |
| c-omp | 124.6 | 71.9 | 59.2 | 59.4 | 53.7 | 1 |
| c-fastmath-serial | 59.6 |  |  |  |  | 1 |
| c-fastmath-omp | 59.2 | 41.0 | 38.4 | 34.3 | 31.2 | 1 |
| c-native-serial | 136.3 |  |  |  |  | 1 |
| c-native-omp | 104.6 | 71.7 | 60.1 | 54.2 | 54.4 | 1 |
| c-clang-serial | 131.8 |  |  |  |  | 1 |
| c-clang-omp | 126.6 | 78.1 | 62.6 | 55.9 | 49.6 | 1 |
| cpp-thread | 105.7 | 74.5 | 57.2 | 56.9 | 54.8 | 1 |
| rust-rayon | 117.9 | 58.0 | 41.8 | 45.2 | 45.4 | 1 |
| zig-safe | 189.5 | 115.5 | 89.7 | 80.0 | 86.0 | 1 |
| zig-fast | 182.8 | 113.2 | 82.2 | 88.1 | 85.6 | 1 |
| go | 159.3 | 98.2 | 67.9 | 68.4 | 70.1 | 1 |

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
| c-omp | 6 | 1 | 1 | 1 | 1 |
| c-lanes | 1 |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 |
| c-fastmath-omp | 11 | 1 | 2 | 2 | 1 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 |
| c-native-omp | 9 | 1 | 1 | 1 | 1 |
| c-native-lanes | 1 |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 |
| rust-rayon | 23 | 1 | 1 | 1 | 1 |
| rust-slices |  |  | 1 |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 |
| zig-fast | 5 | 1 | 1 | 1 | 1 |
| go | 5 | 1 | 1 | 2 | 1 |
