## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.7 | 1.9 | 0.9 | 1.0 | 1.0 | 1 |
| sword-native | 3.4 | 1.7 | 0.9 | 1.2 | 1.5 | 1 |
| sword-without-walked | 4.5 | 2.6 | 1.3 | 1.3 | 1.4 | 1 |
| sword-without-walked-mut | 3.7 | 1.9 | 0.9 | 1.5 | 1.3 | 1 |
| sword-without-captures | 3.5 | 1.7 | 0.8 | 1.1 | 1.1 | 1 |
| sword-without-versioned | 3.8 | 1.7 | 0.8 | 1.1 | 1.1 | 1 |
| sword-without-split | 3.3 | 1.7 | 0.9 | 1.1 | 1.2 | 1 |
| sword-without-deferred | 3.7 | 1.8 | 0.8 | 1.0 | 1.0 | 1 |
| sword-without-lanes | 6.4 | 3.5 | 1.7 | 1.9 | 2.2 | 1 |
| sword-without-steady | 3.5 | 1.8 | 0.9 | 0.9 | 1.0 | 1 |
| c-serial | 6.4 |  |  |  |  | 1 |
| c-restrict | 6.3 |  |  |  |  | 1 |
| c-omp | 6.4 | 3.2 | 1.6 | 2.3 | 2.1 | 6 |
| c-lanes | 3.5 |  |  |  |  | 1 |
| c-lanes-omp | 3.7 | 1.8 | 1.0 | 1.3 | 1.2 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.4 | 3.2 | 1.6 | 2.2 | 2.4 | 5 |
| c-nofma-serial | 6.6 |  |  |  |  | 1 |
| c-nofma-omp | 6.7 | 3.4 | 1.7 | 2.2 | 2.1 | 8 |
| c-native-serial | 6.5 |  |  |  |  | 1 |
| c-native-omp | 6.5 | 3.3 | 1.6 | 1.9 | 2.2 | 6 |
| c-native-lanes | 3.8 |  |  |  |  | 1 |
| c-native-lanes-omp | 4.0 | 2.1 | 1.0 | 1.2 | 1.2 | 1 |
| c-clang-serial | 6.4 |  |  |  |  | 1 |
| c-clang-omp | 6.4 | 3.4 | 1.7 | 2.5 | 2.1 | 5 |
| cpp-thread | 6.7 | 3.4 | 1.8 | 2.6 | 2.6 | 5 |
| rust-rayon | 6.6 | 3.3 | 1.6 | 1.7 | 1.7 | 10 |
| zig-safe | 6.6 | 3.5 | 2.2 | 2.7 | 2.8 | 5 |
| zig-fast | 6.6 | 3.5 | 2.1 | 2.7 | 2.8 | 5 |
| go | 6.5 | 3.3 | 1.8 | 1.8 | 1.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.4 | 2.0 | 1.6 | 1.6 | 1.7 | 1 |
| sword-native | 3.0 | 1.8 | 1.5 | 1.6 | 1.7 | 1 |
| sword-without-walked | 4.6 | 2.5 | 1.8 | 1.8 | 1.9 | 1 |
| sword-without-walked-mut | 3.6 | 2.0 | 1.6 | 1.8 | 1.7 | 1 |
| sword-without-captures | 3.6 | 2.0 | 1.6 | 1.7 | 1.7 | 1 |
| sword-without-versioned | 3.5 | 2.0 | 1.6 | 1.7 | 1.7 | 1 |
| sword-without-split | 3.6 | 1.9 | 1.7 | 1.7 | 1.8 | 1 |
| sword-without-deferred | 3.5 | 2.1 | 1.5 | 1.8 | 1.9 | 1 |
| sword-without-lanes | 9.5 | 4.8 | 2.4 | 2.5 | 2.6 | 1 |
| sword-without-steady | 3.6 | 2.0 | 1.6 | 1.7 | 1.8 | 1 |
| c-serial | 9.5 |  |  |  |  | 1 |
| c-restrict | 9.5 |  |  |  |  | 1 |
| c-omp | 9.5 | 4.8 | 2.4 | 3.1 | 3.1 | 5 |
| c-lanes | 3.8 |  |  |  |  | 1 |
| c-lanes-omp | 3.8 | 2.0 | 1.6 | 1.8 | 2.0 | 1 |
| c-fastmath-serial | 3.4 |  |  |  |  | 1 |
| c-fastmath-omp | 9.5 | 4.8 | 2.4 | 2.5 | 3.0 | 7 |
| c-nofma-serial | 9.5 |  |  |  |  | 1 |
| c-nofma-omp | 9.5 | 4.8 | 2.4 | 2.5 | 2.9 | 5 |
| c-native-serial | 9.5 |  |  |  |  | 1 |
| c-native-omp | 9.5 | 4.8 | 2.4 | 3.0 | 3.1 | 7 |
| c-native-lanes | 3.9 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.9 | 2.1 | 1.6 | 1.6 | 1.8 | 1 |
| c-clang-serial | 9.5 |  |  |  |  | 1 |
| c-clang-omp | 9.6 | 4.8 | 2.4 | 3.7 | 3.7 | 5 |
| cpp-thread | 9.6 | 4.9 | 2.6 | 3.8 | 4.0 | 5 |
| rust-rayon | 9.5 | 4.8 | 2.5 | 2.5 | 2.6 | 10 |
| zig-safe | 9.8 | 5.2 | 3.1 | 4.1 | 4.4 | 5 |
| zig-fast | 9.8 | 5.2 | 3.2 | 4.1 | 4.5 | 5 |
| go | 9.6 | 4.9 | 3.4 | 3.4 | 3.4 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1.9 | 1.9 | 1.8 | 1.9 | 1.9 | 1 |
| sword-native | 1.9 | 1.8 | 2.1 | 1.7 | 1.8 | 1 |
| sword-without-walked | 3.9 | 3.0 | 2.4 | 2.1 | 2.1 | 1 |
| sword-without-walked-mut | 2.3 | 2.3 | 2.0 | 2.1 | 1.9 | 1 |
| sword-without-captures | 2.4 | 1.9 | 2.1 | 1.9 | 2.0 | 1 |
| sword-without-versioned | 2.5 | 2.3 | 1.9 | 2.4 | 1.9 | 1 |
| sword-without-split | 2.0 | 2.3 | 1.9 | 2.3 | 2.2 | 1 |
| sword-without-deferred | 2.5 | 2.0 | 1.8 | 1.8 | 1.7 | 1 |
| sword-without-lanes | 11.1 | 6.4 | 4.2 | 4.3 | 5.0 | 1 |
| sword-without-steady | 2.2 | 2.0 | 1.9 | 1.7 | 1.8 | 1 |
| c-serial | 11.6 |  |  |  |  | 1 |
| c-restrict | 11.9 |  |  |  |  | 1 |
| c-omp | 12.8 | 7.8 | 5.8 | 5.4 | 4.9 | 5 |
| c-lanes | 2.0 |  |  |  |  | 1 |
| c-lanes-omp | 2.1 | 1.9 | 1.8 | 1.7 | 2.0 | 1 |
| c-fastmath-serial | 2.2 |  |  |  |  | 1 |
| c-fastmath-omp | 2.0 | 1.9 | 2.0 | 2.0 | 1.9 | 5 |
| c-nofma-serial | 11.6 |  |  |  |  | 1 |
| c-nofma-omp | 11.6 | 6.9 | 5.7 | 5.1 | 4.4 | 5 |
| c-native-serial | 11.8 |  |  |  |  | 1 |
| c-native-omp | 11.1 | 6.1 | 5.5 | 4.4 | 4.9 | 5 |
| c-native-lanes | 2.3 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.2 | 2.2 | 1.8 | 1.8 | 1.8 | 1 |
| c-clang-serial | 11.5 |  |  |  |  | 1 |
| c-clang-omp | 11.0 | 7.3 | 5.7 | 5.3 | 5.0 | 5 |
| cpp-thread | 11.8 | 7.2 | 5.6 | 5.4 | 4.9 | 5 |
| rust-rayon | 10.8 | 6.1 | 4.4 | 4.9 | 4.6 | 12 |
| zig-safe | 12.4 | 6.9 | 6.3 | 5.4 | 5.5 | 5 |
| zig-fast | 11.5 | 6.9 | 6.1 | 5.1 | 5.2 | 5 |
| go | 11.0 | 7.0 | 5.2 | 9.1 | 4.8 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.1 | 3.9 | 2.1 | 2.1 | 2.2 | 1 |
| sword-native | 6.9 | 3.6 | 2.0 | 2.1 | 2.3 | 1 |
| sword-without-walked | 7.2 | 3.6 | 2.0 | 2.1 | 2.3 | 1 |
| sword-without-walked-mut | 6.7 | 3.6 | 2.1 | 2.0 | 2.3 | 1 |
| sword-without-captures | 11.9 | 6.5 | 3.4 | 3.5 | 3.5 | 1 |
| sword-without-versioned | 7.1 | 3.8 | 2.2 | 2.1 | 2.3 | 1 |
| sword-without-split | 6.6 | 3.6 | 2.1 | 2.1 | 2.2 | 1 |
| sword-without-deferred | 7.0 | 3.6 | 2.0 | 2.1 | 2.2 | 1 |
| sword-without-lanes | 7.1 | 3.7 | 2.0 | 2.1 | 2.4 | 1 |
| sword-without-steady | 6.9 | 3.6 | 2.0 | 2.1 | 2.2 | 1 |
| c-serial | 6.7 |  |  |  |  | 1 |
| c-restrict | 6.8 |  |  |  |  | 1 |
| c-omp | 7.0 | 3.7 | 2.1 | 2.5 | 2.4 | 1 |
| c-fastmath-serial | 6.8 |  |  |  |  | 1 |
| c-fastmath-omp | 7.4 | 3.7 | 2.1 | 2.7 | 2.6 | 1 |
| c-nofma-serial | 6.9 |  |  |  |  | 1 |
| c-nofma-omp | 6.9 | 4.0 | 2.2 | 3.1 | 2.4 | 1 |
| c-native-serial | 7.0 |  |  |  |  | 1 |
| c-native-omp | 6.9 | 3.9 | 2.2 | 3.0 | 2.5 | 1 |
| c-clang-serial | 6.9 |  |  |  |  | 1 |
| c-clang-omp | 6.7 | 3.5 | 2.0 | 2.8 | 2.2 | 1 |
| cpp-thread | 7.7 | 4.2 | 2.4 | 3.0 | 3.0 | 1 |
| rust-rayon | 6.8 | 3.7 | 2.0 | 2.1 | 2.4 | 1 |
| zig-safe | 11.1 | 5.9 | 3.3 | 4.3 | 4.3 | 1 |
| zig-fast | 9.2 | 4.9 | 2.9 | 3.7 | 3.7 | 1 |
| go | 8.2 | 4.1 | 2.4 | 2.4 | 2.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.1 | 4.2 | 4.6 | 4.2 | 4.9 | 1 |
| sword-native | 5.5 | 4.4 | 4.3 | 4.4 | 4.6 | 1 |
| sword-without-walked | 6.1 | 4.4 | 4.3 | 4.4 | 4.5 | 1 |
| sword-without-walked-mut | 6.0 | 4.3 | 4.3 | 4.4 | 4.4 | 1 |
| sword-without-captures | 8.7 | 5.2 | 4.4 | 4.4 | 4.4 | 1 |
| sword-without-versioned | 6.1 | 4.2 | 4.4 | 4.5 | 4.6 | 1 |
| sword-without-split | 6.0 | 4.4 | 4.6 | 4.7 | 4.9 | 1 |
| sword-without-deferred | 6.1 | 4.5 | 4.4 | 4.7 | 4.5 | 1 |
| sword-without-lanes | 6.2 | 4.5 | 4.4 | 4.3 | 4.5 | 1 |
| sword-without-steady | 6.0 | 4.7 | 4.3 | 4.2 | 4.3 | 1 |
| c-serial | 5.8 |  |  |  |  | 1 |
| c-restrict | 5.7 |  |  |  |  | 1 |
| c-omp | 6.9 | 4.4 | 4.1 | 4.5 | 4.4 | 1 |
| c-fastmath-serial | 5.5 |  |  |  |  | 1 |
| c-fastmath-omp | 6.9 | 4.3 | 4.5 | 4.3 | 4.4 | 1 |
| c-nofma-serial | 5.5 |  |  |  |  | 1 |
| c-nofma-omp | 6.8 | 4.7 | 4.2 | 4.4 | 4.4 | 1 |
| c-native-serial | 5.7 |  |  |  |  | 1 |
| c-native-omp | 7.0 | 4.4 | 4.1 | 4.2 | 4.3 | 1 |
| c-clang-serial | 5.9 |  |  |  |  | 1 |
| c-clang-omp | 6.0 | 4.4 | 4.3 | 4.9 | 4.7 | 1 |
| cpp-thread | 7.2 | 4.6 | 4.2 | 4.5 | 4.9 | 1 |
| rust-rayon | 6.3 | 4.7 | 4.5 | 4.9 | 4.9 | 1 |
| zig-safe | 10.8 | 5.8 | 5.6 | 6.2 | 6.8 | 1 |
| zig-fast | 8.7 | 5.0 | 4.9 | 5.3 | 5.9 | 1 |
| go | 7.3 | 4.5 | 4.2 | 4.4 | 4.4 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 8.3 | 6.0 | 6.2 | 6.1 | 5.2 | 1 |
| sword-native | 8.0 | 6.9 | 5.5 | 5.5 | 5.5 | 1 |
| sword-without-walked | 6.4 | 5.6 | 5.2 | 5.1 | 5.4 | 1 |
| sword-without-walked-mut | 6.5 | 5.5 | 5.9 | 5.6 | 5.9 | 1 |
| sword-without-captures | 15.0 | 8.4 | 6.0 | 6.4 | 5.8 | 1 |
| sword-without-versioned | 6.3 | 5.3 | 5.5 | 5.4 | 5.4 | 1 |
| sword-without-split | 7.6 | 5.7 | 5.3 | 5.7 | 5.8 | 1 |
| sword-without-deferred | 8.3 | 6.2 | 5.4 | 5.8 | 5.2 | 1 |
| sword-without-lanes | 6.8 | 5.4 | 5.1 | 5.6 | 5.5 | 1 |
| sword-without-steady | 7.5 | 5.9 | 5.3 | 5.8 | 5.6 | 1 |
| c-serial | 5.5 |  |  |  |  | 1 |
| c-restrict | 5.7 |  |  |  |  | 1 |
| c-omp | 6.8 | 7.1 | 5.6 | 5.6 | 5.7 | 1 |
| c-fastmath-serial | 5.2 |  |  |  |  | 1 |
| c-fastmath-omp | 5.6 | 5.9 | 5.6 | 5.2 | 5.4 | 1 |
| c-nofma-serial | 6.2 |  |  |  |  | 1 |
| c-nofma-omp | 6.4 | 5.5 | 5.2 | 5.5 | 5.2 | 1 |
| c-native-serial | 5.8 |  |  |  |  | 1 |
| c-native-omp | 6.0 | 5.9 | 5.2 | 6.4 | 5.9 | 1 |
| c-clang-serial | 7.5 |  |  |  |  | 1 |
| c-clang-omp | 7.8 | 6.6 | 5.4 | 6.2 | 6.1 | 1 |
| cpp-thread | 6.1 | 5.7 | 5.6 | 5.7 | 5.9 | 1 |
| rust-rayon | 5.8 | 5.2 | 5.5 | 5.6 | 6.0 | 1 |
| zig-safe | 11.4 | 8.7 | 8.2 | 7.1 | 7.3 | 1 |
| zig-fast | 10.0 | 8.3 | 7.3 | 6.4 | 6.5 | 1 |
| go | 10.3 | 7.9 | 7.2 | 6.0 | 6.1 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 78.5 | 39.5 | 20.0 | 23.4 | 24.8 | 1 |
| sword-native | 64.8 | 33.0 | 16.5 | 18.7 | 22.5 | 1 |
| sword-without-walked | 78.4 | 40.2 | 19.9 | 22.6 | 26.6 | 1 |
| sword-without-walked-mut | 79.5 | 40.2 | 19.8 | 24.5 | 25.5 | 1 |
| sword-without-captures | 87.7 | 44.5 | 22.0 | 26.1 | 27.0 | 1 |
| sword-without-versioned | 77.8 | 40.0 | 19.7 | 23.5 | 24.8 | 1 |
| sword-without-split | 91.2 | 46.0 | 23.1 | 27.5 | 28.8 | 1 |
| sword-without-deferred | 77.7 | 39.6 | 19.8 | 23.6 | 24.7 | 1 |
| sword-without-lanes | 77.7 | 40.2 | 19.5 | 23.8 | 25.0 | 1 |
| sword-without-steady | 78.2 | 40.0 | 19.7 | 22.1 | 25.5 | 1 |
| sword-rows | 23.3 | 11.6 | 5.7 | 7.6 | 8.6 | 1 |
| sword-rows-without-steady | 22.9 | 11.4 | 6.0 | 8.0 | 8.7 | 1 |
| c-serial | 55.2 |  |  |  |  | 1 |
| c-restrict | 54.5 |  |  |  |  | 1 |
| c-omp | 51.8 | 25.7 | 12.9 | 16.3 | 14.7 | 1 |
| c-fastmath-serial | 55.1 |  |  |  |  | 1 |
| c-fastmath-omp | 52.3 | 25.5 | 12.6 | 15.0 | 14.3 | 1 |
| c-nofma-serial | 56.0 |  |  |  |  | 1 |
| c-nofma-omp | 52.6 | 25.8 | 13.0 | 16.4 | 14.9 | 1 |
| c-native-serial | 44.3 |  |  |  |  | 1 |
| c-native-omp | 44.4 | 21.2 | 10.6 | 13.5 | 12.5 | 1 |
| c-clang-serial | 50.2 |  |  |  |  | 1 |
| c-clang-omp | 49.5 | 25.4 | 12.4 | 18.6 | 15.8 | 1 |
| cpp-thread | 58.0 | 28.7 | 15.2 | 18.7 | 20.3 | 1 |
| rust-rayon | 91.8 | 46.2 | 23.4 | 23.3 | 23.6 | 1 |
| rust-slices | 21.4 | 10.8 | 5.5 | 5.6 | 6.0 | 1 |
| zig-safe | 94.2 | 48.4 | 27.6 | 35.3 | 36.6 | 1 |
| zig-fast | 43.0 | 22.3 | 14.3 | 18.6 | 20.8 | 1 |
| go | 79.1 | 39.1 | 19.9 | 23.0 | 21.7 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 96.9 | 43.2 | 40.2 | 41.7 | 43.4 | 1 |
| sword-native | 84.8 | 41.8 | 40.1 | 41.1 | 42.9 | 1 |
| sword-without-walked | 84.7 | 43.9 | 40.0 | 41.3 | 42.0 | 1 |
| sword-without-walked-mut | 83.8 | 42.4 | 40.1 | 41.0 | 43.2 | 1 |
| sword-without-captures | 88.8 | 47.4 | 42.9 | 44.2 | 45.5 | 1 |
| sword-without-versioned | 87.3 | 43.8 | 40.0 | 41.1 | 42.1 | 1 |
| sword-without-split | 98.4 | 51.9 | 48.3 | 48.8 | 49.5 | 1 |
| sword-without-deferred | 86.1 | 42.9 | 40.1 | 41.0 | 42.4 | 1 |
| sword-without-lanes | 89.4 | 47.7 | 41.7 | 41.9 | 43.1 | 1 |
| sword-without-steady | 84.6 | 42.2 | 40.1 | 41.2 | 43.8 | 1 |
| sword-rows | 33.2 | 16.9 | 14.1 | 13.9 | 16.1 | 1 |
| sword-rows-without-steady | 32.5 | 18.4 | 13.9 | 14.3 | 15.3 | 1 |
| c-serial | 37.4 |  |  |  |  | 1 |
| c-restrict | 39.6 |  |  |  |  | 1 |
| c-omp | 36.2 | 22.5 | 19.9 | 19.0 | 19.8 | 1 |
| c-fastmath-serial | 48.1 |  |  |  |  | 1 |
| c-fastmath-omp | 47.8 | 24.2 | 21.2 | 23.0 | 23.1 | 1 |
| c-nofma-serial | 37.8 |  |  |  |  | 1 |
| c-nofma-omp | 37.5 | 20.0 | 18.2 | 19.2 | 21.1 | 1 |
| c-native-serial | 41.5 |  |  |  |  | 1 |
| c-native-omp | 37.4 | 20.2 | 18.0 | 19.7 | 20.8 | 1 |
| c-clang-serial | 50.8 |  |  |  |  | 1 |
| c-clang-omp | 52.4 | 23.0 | 22.3 | 30.3 | 26.0 | 1 |
| cpp-thread | 51.8 | 28.0 | 22.8 | 29.1 | 28.0 | 1 |
| rust-rayon | 108.2 | 54.5 | 48.4 | 48.9 | 49.1 | 1 |
| rust-slices | 28.3 | 17.4 | 13.6 | 14.6 | 14.5 | 1 |
| zig-safe | 82.9 | 44.4 | 45.4 | 55.6 | 56.7 | 1 |
| zig-fast | 42.4 | 23.8 | 23.3 | 27.6 | 35.2 | 1 |
| go | 91.6 | 47.2 | 41.6 | 40.7 | 41.3 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 46.4 | 38.1 | 29.8 | 28.3 | 29.6 | 1 |
| sword-native | 58.9 | 48.0 | 32.9 | 29.7 | 29.3 | 1 |
| sword-without-walked | 52.1 | 39.8 | 26.5 | 28.1 | 28.9 | 1 |
| sword-without-walked-mut | 64.1 | 49.8 | 32.3 | 31.4 | 31.2 | 1 |
| sword-without-captures | 101.3 | 61.9 | 32.7 | 32.4 | 38.9 | 1 |
| sword-without-versioned | 61.7 | 39.5 | 33.5 | 30.2 | 27.6 | 1 |
| sword-without-split | 82.7 | 51.8 | 37.6 | 37.8 | 40.3 | 1 |
| sword-without-deferred | 50.5 | 36.9 | 25.7 | 28.7 | 29.1 | 1 |
| sword-without-lanes | 59.5 | 38.1 | 27.3 | 25.7 | 28.8 | 1 |
| sword-without-steady | 47.4 | 47.3 | 33.2 | 30.8 | 24.7 | 1 |
| sword-rows | 39.6 | 32.5 | 20.5 | 22.4 | 20.5 | 1 |
| sword-rows-without-steady | 29.6 | 24.4 | 21.6 | 20.0 | 19.6 | 1 |
| c-serial | 46.4 |  |  |  |  | 1 |
| c-restrict | 52.5 |  |  |  |  | 1 |
| c-omp | 51.1 | 35.8 | 31.4 | 26.7 | 25.0 | 1 |
| c-fastmath-serial | 49.8 |  |  |  |  | 1 |
| c-fastmath-omp | 45.2 | 40.7 | 26.2 | 26.5 | 26.7 | 1 |
| c-nofma-serial | 45.5 |  |  |  |  | 1 |
| c-nofma-omp | 43.7 | 35.4 | 27.4 | 28.5 | 25.0 | 1 |
| c-native-serial | 45.1 |  |  |  |  | 1 |
| c-native-omp | 49.0 | 31.7 | 24.8 | 30.9 | 27.0 | 1 |
| c-clang-serial | 48.1 |  |  |  |  | 1 |
| c-clang-omp | 46.2 | 36.6 | 33.0 | 33.7 | 32.5 | 1 |
| cpp-thread | 50.9 | 37.8 | 31.4 | 30.7 | 32.6 | 1 |
| rust-rayon | 107.4 | 55.8 | 42.5 | 37.4 | 45.7 | 1 |
| rust-slices | 41.1 | 23.3 | 25.3 | 20.8 | 23.1 | 1 |
| zig-safe | 98.4 | 83.1 | 67.2 | 62.4 | 57.6 | 1 |
| zig-fast | 49.0 | 37.1 | 28.9 | 26.6 | 29.0 | 1 |
| go | 83.2 | 61.3 | 50.6 | 48.7 | 46.6 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.7 | 346.6 | 173.6 | 176.4 | 176.8 | 1 |
| sword-native | 683.9 | 342.1 | 171.5 | 172.8 | 174.8 | 1 |
| sword-without-walked | 692.3 | 346.4 | 173.7 | 175.2 | 176.5 | 1 |
| sword-without-walked-mut | 692.8 | 346.6 | 173.7 | 175.9 | 176.2 | 1 |
| sword-without-captures | 692.7 | 346.5 | 173.6 | 176.1 | 175.9 | 1 |
| sword-without-versioned | 692.9 | 346.7 | 173.7 | 175.5 | 176.7 | 1 |
| sword-without-split | 692.7 | 346.6 | 173.9 | 175.8 | 177.8 | 1 |
| sword-without-deferred | 692.7 | 346.5 | 173.9 | 176.3 | 176.2 | 1 |
| sword-without-lanes | 692.7 | 346.5 | 173.8 | 177.0 | 176.5 | 1 |
| sword-without-steady | 692.7 | 346.5 | 173.8 | 175.7 | 175.8 | 1 |
| c-serial | 647.7 |  |  |  |  | 1 |
| c-restrict | 647.1 |  |  |  |  | 1 |
| c-omp | 635.5 | 318.3 | 159.5 | 159.4 | 159.7 | 1 |
| c-fastmath-serial | 626.6 |  |  |  |  | 1 |
| c-fastmath-omp | 627.6 | 314.0 | 157.3 | 157.3 | 157.4 | 1 |
| c-nofma-serial | 697.1 |  |  |  |  | 1 |
| c-nofma-omp | 697.3 | 348.7 | 174.8 | 174.8 | 174.8 | 1 |
| c-native-serial | 648.9 |  |  |  |  | 1 |
| c-native-omp | 645.6 | 325.5 | 163.3 | 162.4 | 163.0 | 1 |
| c-clang-serial | 770.4 |  |  |  |  | 1 |
| c-clang-omp | 768.5 | 384.8 | 193.1 | 193.3 | 193.1 | 1 |
| cpp-thread | 853.9 | 427.3 | 214.2 | 229.0 | 217.3 | 1 |
| rust-rayon | 693.0 | 347.2 | 174.1 | 173.9 | 174.2 | 1 |
| zig-safe | 682.9 | 342.3 | 171.9 | 184.7 | 174.1 | 1 |
| zig-fast | 897.1 | 448.9 | 225.2 | 242.5 | 229.2 | 1 |
| go | 677.9 | 339.3 | 170.3 | 180.6 | 174.7 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 838.6 | 420.0 | 230.9 | 233.6 | 235.1 | 1 |
| sword-native | 830.5 | 416.1 | 224.8 | 226.8 | 227.6 | 1 |
| sword-without-walked | 838.9 | 420.0 | 230.9 | 232.4 | 234.1 | 1 |
| sword-without-walked-mut | 838.6 | 420.1 | 230.8 | 233.0 | 234.4 | 1 |
| sword-without-captures | 838.5 | 420.2 | 230.9 | 232.6 | 233.5 | 1 |
| sword-without-versioned | 838.5 | 420.0 | 230.9 | 232.3 | 233.9 | 1 |
| sword-without-split | 838.7 | 420.1 | 231.4 | 233.7 | 233.5 | 1 |
| sword-without-deferred | 838.4 | 420.0 | 230.9 | 232.4 | 234.5 | 1 |
| sword-without-lanes | 838.6 | 419.9 | 230.9 | 235.0 | 234.5 | 1 |
| sword-without-steady | 838.5 | 420.7 | 231.1 | 233.5 | 234.4 | 1 |
| c-serial | 798.5 |  |  |  |  | 1 |
| c-restrict | 798.5 |  |  |  |  | 1 |
| c-omp | 798.5 | 400.0 | 212.1 | 212.2 | 212.5 | 1 |
| c-fastmath-serial | 794.4 |  |  |  |  | 1 |
| c-fastmath-omp | 794.6 | 397.9 | 213.0 | 213.2 | 213.2 | 1 |
| c-nofma-serial | 831.6 |  |  |  |  | 1 |
| c-nofma-omp | 832.6 | 417.5 | 226.6 | 226.7 | 227.1 | 1 |
| c-native-serial | 798.5 |  |  |  |  | 1 |
| c-native-omp | 798.9 | 399.9 | 212.1 | 212.2 | 212.4 | 1 |
| c-clang-serial | 823.7 |  |  |  |  | 1 |
| c-clang-omp | 824.4 | 413.2 | 225.4 | 225.8 | 225.9 | 1 |
| cpp-thread | 799.0 | 400.7 | 212.5 | 232.9 | 217.4 | 1 |
| rust-rayon | 830.1 | 416.0 | 227.5 | 227.6 | 227.5 | 1 |
| zig-safe | 835.7 | 418.7 | 227.4 | 247.2 | 232.2 | 1 |
| zig-fast | 833.4 | 418.0 | 226.1 | 242.3 | 230.8 | 1 |
| go | 827.0 | 414.7 | 224.2 | 234.2 | 228.2 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1109.2 | 589.1 | 384.6 | 379.6 | 397.0 | 1 |
| sword-native | 1075.5 | 558.7 | 473.8 | 407.5 | 393.6 | 1 |
| sword-without-walked | 1078.0 | 561.7 | 376.0 | 387.4 | 370.3 | 1 |
| sword-without-walked-mut | 1100.0 | 594.8 | 367.1 | 394.7 | 415.2 | 1 |
| sword-without-captures | 1118.5 | 562.7 | 377.9 | 355.5 | 344.1 | 1 |
| sword-without-versioned | 1070.0 | 543.9 | 431.2 | 394.2 | 392.2 | 1 |
| sword-without-split | 1161.3 | 593.5 | 402.8 | 406.0 | 406.7 | 1 |
| sword-without-deferred | 1192.2 | 562.2 | 366.3 | 369.8 | 424.4 | 1 |
| sword-without-lanes | 1022.2 | 497.0 | 405.9 | 415.4 | 362.4 | 1 |
| sword-without-steady | 967.0 | 516.3 | 380.0 | 356.0 | 415.7 | 1 |
| c-serial | 833.1 |  |  |  |  | 1 |
| c-restrict | 958.9 |  |  |  |  | 1 |
| c-omp | 956.5 | 507.1 | 335.6 | 404.7 | 324.6 | 1 |
| c-fastmath-serial | 852.5 |  |  |  |  | 1 |
| c-fastmath-omp | 877.2 | 404.5 | 286.1 | 269.9 | 288.0 | 1 |
| c-nofma-serial | 1048.1 |  |  |  |  | 1 |
| c-nofma-omp | 1064.6 | 552.2 | 375.0 | 371.5 | 363.3 | 1 |
| c-native-serial | 918.9 |  |  |  |  | 1 |
| c-native-omp | 925.5 | 527.3 | 368.8 | 365.7 | 376.8 | 1 |
| c-clang-serial | 822.6 |  |  |  |  | 1 |
| c-clang-omp | 826.4 | 474.8 | 314.8 | 387.6 | 306.8 | 1 |
| cpp-thread | 877.2 | 481.8 | 414.3 | 318.4 | 317.6 | 1 |
| rust-rayon | 999.9 | 537.3 | 451.0 | 359.6 | 358.5 | 1 |
| zig-safe | 933.0 | 561.4 | 367.2 | 372.8 | 383.6 | 1 |
| zig-fast | 993.2 | 519.9 | 368.7 | 360.9 | 352.3 | 1 |
| go | 963.4 | 515.5 | 367.5 | 365.4 | 382.5 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.8 | 125.7 | 63.5 | 67.6 | 67.0 | 1 |
| sword-native | 246.9 | 123.6 | 62.1 | 65.8 | 66.6 | 1 |
| sword-without-walked | 251.7 | 126.0 | 63.1 | 65.7 | 67.9 | 1 |
| sword-without-walked-mut | 251.8 | 126.0 | 63.2 | 66.5 | 67.0 | 1 |
| sword-without-captures | 251.5 | 126.0 | 64.0 | 66.5 | 68.0 | 1 |
| sword-without-versioned | 270.6 | 135.6 | 68.9 | 69.5 | 71.0 | 1 |
| sword-without-split | 251.7 | 125.8 | 62.8 | 65.8 | 68.1 | 1 |
| sword-without-deferred | 251.7 | 126.0 | 63.3 | 66.4 | 68.0 | 1 |
| sword-without-lanes | 251.7 | 126.0 | 64.2 | 66.9 | 68.8 | 1 |
| sword-without-steady | 251.1 | 126.0 | 63.1 | 66.2 | 66.9 | 1 |
| c-serial | 237.6 |  |  |  |  | 1 |
| c-restrict | 237.7 |  |  |  |  | 1 |
| c-omp | 238.6 | 119.5 | 60.0 | 65.4 | 63.0 | 1 |
| c-fastmath-serial | 237.8 |  |  |  |  | 1 |
| c-fastmath-omp | 244.3 | 122.2 | 61.3 | 65.2 | 65.6 | 1 |
| c-nofma-serial | 242.6 |  |  |  |  | 1 |
| c-nofma-omp | 268.4 | 134.2 | 67.3 | 72.9 | 72.0 | 1 |
| c-native-serial | 250.4 |  |  |  |  | 1 |
| c-native-omp | 248.8 | 124.5 | 62.4 | 67.0 | 66.2 | 1 |
| c-clang-serial | 242.7 |  |  |  |  | 1 |
| c-clang-omp | 246.5 | 123.4 | 61.9 | 66.9 | 68.7 | 1 |
| cpp-thread | 240.4 | 120.5 | 61.4 | 71.8 | 70.7 | 1 |
| rust-rayon | 238.8 | 120.0 | 60.3 | 60.8 | 61.8 | 1 |
| zig-safe | 271.9 | 136.9 | 71.6 | 80.1 | 85.4 | 1 |
| zig-fast | 271.9 | 136.9 | 71.4 | 80.9 | 84.3 | 1 |
| go | 252.3 | 126.4 | 63.7 | 67.7 | 67.1 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 304.8 | 153.1 | 150.0 | 150.7 | 151.4 | 1 |
| sword-native | 302.8 | 151.8 | 149.9 | 150.3 | 151.2 | 1 |
| sword-without-walked | 304.3 | 152.7 | 149.9 | 151.2 | 150.9 | 1 |
| sword-without-walked-mut | 305.0 | 153.0 | 149.9 | 150.4 | 151.2 | 1 |
| sword-without-captures | 304.6 | 152.7 | 149.9 | 150.0 | 151.3 | 1 |
| sword-without-versioned | 312.0 | 156.5 | 152.9 | 153.9 | 154.9 | 1 |
| sword-without-split | 305.0 | 152.9 | 149.9 | 150.7 | 151.5 | 1 |
| sword-without-deferred | 304.8 | 153.0 | 150.0 | 150.1 | 151.2 | 1 |
| sword-without-lanes | 304.1 | 152.6 | 150.0 | 151.0 | 151.6 | 1 |
| sword-without-steady | 304.8 | 153.0 | 150.0 | 150.5 | 151.2 | 1 |
| c-serial | 73.5 |  |  |  |  | 1 |
| c-restrict | 73.4 |  |  |  |  | 1 |
| c-omp | 130.0 | 65.2 | 58.4 | 59.1 | 60.5 | 1 |
| c-fastmath-serial | 73.0 |  |  |  |  | 1 |
| c-fastmath-omp | 73.0 | 36.6 | 36.5 | 37.3 | 38.0 | 1 |
| c-nofma-serial | 75.0 |  |  |  |  | 1 |
| c-nofma-omp | 129.8 | 65.1 | 59.0 | 59.8 | 61.3 | 1 |
| c-native-serial | 73.7 |  |  |  |  | 1 |
| c-native-omp | 130.1 | 65.2 | 58.5 | 58.9 | 60.2 | 1 |
| c-clang-serial | 310.2 |  |  |  |  | 1 |
| c-clang-omp | 316.6 | 155.3 | 152.4 | 154.6 | 173.7 | 1 |
| cpp-thread | 130.6 | 66.0 | 59.6 | 68.1 | 66.0 | 1 |
| rust-rayon | 312.3 | 156.8 | 151.1 | 151.5 | 151.8 | 1 |
| zig-safe | 304.8 | 154.4 | 153.8 | 162.2 | 165.1 | 1 |
| zig-fast | 304.6 | 154.2 | 153.4 | 162.4 | 164.4 | 1 |
| go | 529.4 | 265.7 | 165.1 | 174.1 | 172.1 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 96.0 | 67.5 | 45.2 | 48.6 | 40.9 | 1 |
| sword-native | 93.2 | 60.5 | 46.2 | 48.9 | 47.2 | 1 |
| sword-without-walked | 89.0 | 62.2 | 48.2 | 48.0 | 51.8 | 1 |
| sword-without-walked-mut | 124.0 | 60.1 | 38.3 | 39.8 | 47.5 | 1 |
| sword-without-captures | 93.3 | 62.5 | 50.1 | 42.8 | 43.0 | 1 |
| sword-without-versioned | 139.1 | 97.0 | 72.9 | 68.9 | 69.6 | 1 |
| sword-without-split | 95.0 | 62.7 | 55.4 | 53.6 | 50.6 | 1 |
| sword-without-deferred | 101.2 | 60.6 | 43.0 | 50.6 | 44.4 | 1 |
| sword-without-lanes | 90.2 | 61.9 | 48.1 | 39.6 | 48.0 | 1 |
| sword-without-steady | 92.1 | 62.6 | 48.4 | 49.3 | 49.2 | 1 |
| c-serial | 84.6 |  |  |  |  | 1 |
| c-restrict | 85.4 |  |  |  |  | 1 |
| c-omp | 84.2 | 70.2 | 52.0 | 48.1 | 37.2 | 1 |
| c-fastmath-serial | 45.5 |  |  |  |  | 1 |
| c-fastmath-omp | 45.5 | 33.4 | 32.9 | 18.0 | 23.2 | 1 |
| c-nofma-serial | 100.9 |  |  |  |  | 1 |
| c-nofma-omp | 89.1 | 68.0 | 49.2 | 52.5 | 51.3 | 1 |
| c-native-serial | 85.1 |  |  |  |  | 1 |
| c-native-omp | 84.6 | 69.4 | 57.9 | 54.7 | 45.3 | 1 |
| c-clang-serial | 87.5 |  |  |  |  | 1 |
| c-clang-omp | 85.2 | 68.6 | 47.0 | 49.6 | 50.5 | 1 |
| cpp-thread | 86.4 | 71.0 | 54.5 | 54.0 | 38.4 | 1 |
| rust-rayon | 88.6 | 56.8 | 42.8 | 42.2 | 40.7 | 1 |
| zig-safe | 139.6 | 97.6 | 73.8 | 72.1 | 75.4 | 1 |
| zig-fast | 133.0 | 97.9 | 77.4 | 54.4 | 75.0 | 1 |
| go | 155.3 | 70.7 | 66.0 | 58.6 | 63.9 | 1 |

## hist

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.7 | 4.1 | 2.2 | 2.5 | 2.8 | 1 |
| sword-native | 7.6 | 4.1 | 2.1 | 2.1 | 2.3 | 1 |
| c-serial | 8.4 |  |  |  |  | 1 |
| c-omp | 7.8 | 4.2 | 2.1 | 2.1 | 2.6 | 11 |
| c-fastmath-serial | 8.1 |  |  |  |  | 1 |
| c-fastmath-omp | 7.9 | 4.0 | 2.0 | 2.1 | 2.6 | 10 |
| c-nofma-serial | 7.9 |  |  |  |  | 1 |
| c-nofma-omp | 8.0 | 4.2 | 2.1 | 2.3 | 2.6 | 11 |
| c-native-serial | 8.0 |  |  |  |  | 1 |
| c-native-omp | 8.0 | 4.1 | 2.1 | 2.2 | 2.6 | 11 |
| c-clang-serial | 7.9 |  |  |  |  | 1 |
| c-clang-omp | 7.7 | 4.0 | 2.1 | 3.0 | 2.6 | 7 |
| cpp-thread | 8.4 | 4.2 | 2.8 | 3.0 | 3.0 | 5 |
| rust-rayon | 8.2 | 4.2 | 2.1 | 2.2 | 2.4 | 10 |
| zig-safe | 13.2 | 8.3 | 5.1 | 5.0 | 5.5 | 5 |
| zig-fast | 8.4 | 5.2 | 3.2 | 3.5 | 3.7 | 5 |
| go | 9.1 | 4.7 | 2.5 | 2.5 | 2.6 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 13.3 | 6.7 | 5.9 | 6.0 | 6.1 | 1 |
| sword-native | 13.8 | 7.0 | 6.2 | 6.2 | 6.3 | 1 |
| c-serial | 10.5 |  |  |  |  | 1 |
| c-omp | 8.4 | 4.2 | 3.6 | 3.6 | 4.2 | 10 |
| c-fastmath-serial | 10.3 |  |  |  |  | 1 |
| c-fastmath-omp | 8.4 | 4.2 | 3.6 | 3.9 | 3.8 | 11 |
| c-nofma-serial | 10.4 |  |  |  |  | 1 |
| c-nofma-omp | 8.4 | 4.3 | 3.6 | 3.8 | 4.1 | 11 |
| c-native-serial | 10.7 |  |  |  |  | 1 |
| c-native-omp | 8.6 | 4.2 | 3.6 | 3.9 | 4.0 | 11 |
| c-clang-serial | 8.5 |  |  |  |  | 1 |
| c-clang-omp | 8.4 | 4.3 | 3.5 | 4.9 | 4.3 | 6 |
| cpp-thread | 8.6 | 4.3 | 4.7 | 4.7 | 4.9 | 5 |
| rust-rayon | 16.6 | 8.3 | 7.7 | 7.9 | 8.0 | 11 |
| zig-safe | 15.8 | 10.2 | 9.7 | 9.7 | 9.2 | 5 |
| zig-fast | 12.8 | 9.6 | 7.2 | 7.0 | 7.7 | 5 |
| go | 8.5 | 4.3 | 4.0 | 4.0 | 4.0 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 5.6 | 4.0 | 2.9 | 2.9 | 3.5 | 1 |
| sword-native | 6.2 | 4.3 | 3.6 | 3.4 | 3.6 | 1 |
| c-serial | 5.5 |  |  |  |  | 1 |
| c-omp | 5.5 | 4.7 | 3.7 | 3.8 | 3.8 | 7 |
| c-fastmath-serial | 5.8 |  |  |  |  | 1 |
| c-fastmath-omp | 5.7 | 4.7 | 3.7 | 3.8 | 3.6 | 7 |
| c-nofma-serial | 5.4 |  |  |  |  | 1 |
| c-nofma-omp | 5.4 | 4.6 | 3.7 | 3.8 | 3.6 | 6 |
| c-native-serial | 5.4 |  |  |  |  | 1 |
| c-native-omp | 5.5 | 4.7 | 3.7 | 3.8 | 3.7 | 7 |
| c-clang-serial | 5.5 |  |  |  |  | 1 |
| c-clang-omp | 5.5 | 4.7 | 3.7 | 3.5 | 3.6 | 6 |
| cpp-thread | 5.5 | 4.8 | 4.5 | 4.2 | 2.8 | 5 |
| rust-rayon | 5.6 | 3.3 | 3.5 | 2.9 | 2.9 | 13 |
| zig-safe | 7.2 | 9.8 | 6.9 | 7.4 | 7.5 | 5 |
| zig-fast | 4.7 | 7.2 | 5.3 | 5.2 | 4.9 | 5 |
| go | 6.6 | 5.6 | 4.5 | 4.4 | 4.1 | 5 |

## scan

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 18.3 | 9.5 | 4.9 | 5.8 | 6.7 | 1 |
| sword-native | 15.7 | 8.1 | 4.3 | 5.0 | 6.0 | 1 |
| c-serial | 7.3 |  |  |  |  | 1 |
| c-omp | 13.9 | 6.9 | 3.9 | 4.2 | 4.7 | 4 |
| c-fastmath-serial | 7.3 |  |  |  |  | 1 |
| c-fastmath-omp | 13.4 | 6.9 | 3.6 | 4.6 | 4.4 | 4 |
| c-nofma-serial | 7.2 |  |  |  |  | 1 |
| c-nofma-omp | 13.7 | 7.5 | 3.7 | 4.8 | 4.6 | 4 |
| c-native-serial | 7.1 |  |  |  |  | 1 |
| c-native-omp | 13.5 | 6.8 | 3.8 | 3.9 | 4.6 | 4 |
| c-clang-serial | 6.9 |  |  |  |  | 1 |
| c-clang-omp | 13.4 | 7.0 | 3.8 | 5.6 | 4.5 | 4 |
| cpp-thread | 14.1 | 7.0 | 3.9 | 4.9 | 5.2 | 4 |
| rust-rayon | 14.3 | 7.2 | 3.6 | 3.8 | 3.8 | 4 |
| zig-safe | 15.9 | 8.0 | 4.7 | 5.9 | 6.4 | 4 |
| zig-fast | 15.1 | 7.7 | 4.5 | 5.8 | 6.2 | 4 |
| go | 14.2 | 7.4 | 3.8 | 4.4 | 4.3 | 4 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 53.1 | 26.2 | 15.4 | 16.1 | 15.7 | 1 |
| sword-native | 50.0 | 24.8 | 14.6 | 14.6 | 15.3 | 1 |
| c-serial | 9.7 |  |  |  |  | 1 |
| c-omp | 19.3 | 9.7 | 6.7 | 8.4 | 7.3 | 4 |
| c-fastmath-serial | 9.7 |  |  |  |  | 1 |
| c-fastmath-omp | 19.2 | 9.7 | 6.7 | 6.9 | 7.5 | 4 |
| c-nofma-serial | 9.7 |  |  |  |  | 1 |
| c-nofma-omp | 19.3 | 9.8 | 6.7 | 7.1 | 7.6 | 4 |
| c-native-serial | 9.8 |  |  |  |  | 1 |
| c-native-omp | 19.2 | 9.7 | 6.7 | 7.3 | 7.7 | 4 |
| c-clang-serial | 9.7 |  |  |  |  | 1 |
| c-clang-omp | 19.2 | 9.6 | 6.7 | 10.6 | 8.9 | 4 |
| cpp-thread | 19.5 | 10.0 | 7.2 | 8.8 | 8.5 | 4 |
| rust-rayon | 19.1 | 9.8 | 6.7 | 6.7 | 6.7 | 4 |
| zig-safe | 19.9 | 10.6 | 8.0 | 9.8 | 10.2 | 4 |
| zig-fast | 19.8 | 10.6 | 8.1 | 9.9 | 10.4 | 4 |
| go | 19.4 | 9.9 | 6.9 | 7.3 | 7.2 | 4 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 24.1 | 14.7 | 11.1 | 10.4 | 10.5 | 1 |
| sword-native | 22.2 | 12.4 | 9.2 | 9.4 | 9.5 | 1 |
| c-serial | 10.6 |  |  |  |  | 1 |
| c-omp | 20.8 | 15.9 | 10.9 | 11.4 | 11.7 | 4 |
| c-fastmath-serial | 14.2 |  |  |  |  | 1 |
| c-fastmath-omp | 12.5 | 9.9 | 9.8 | 8.5 | 6.1 | 5 |
| c-nofma-serial | 11.7 |  |  |  |  | 1 |
| c-nofma-omp | 22.1 | 14.3 | 14.4 | 10.6 | 9.9 | 4 |
| c-native-serial | 10.8 |  |  |  |  | 1 |
| c-native-omp | 21.3 | 11.6 | 10.6 | 10.4 | 9.9 | 4 |
| c-clang-serial | 11.0 |  |  |  |  | 1 |
| c-clang-omp | 20.7 | 13.6 | 10.9 | 8.8 | 9.3 | 4 |
| cpp-thread | 22.3 | 11.8 | 11.9 | 11.2 | 9.2 | 4 |
| rust-rayon | 25.2 | 14.7 | 12.3 | 10.5 | 9.8 | 4 |
| zig-safe | 22.7 | 14.2 | 11.8 | 11.9 | 11.5 | 4 |
| zig-fast | 23.9 | 15.0 | 11.9 | 10.9 | 9.6 | 4 |
| go | 21.8 | 15.8 | 10.7 | 10.4 | 9.7 | 4 |

## sort

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 171.2 | 87.9 | 47.3 | 50.6 | 51.8 | 1 |
| sword-native | 170.6 | 87.4 | 47.2 | 49.9 | 51.8 | 1 |
| c-serial | 64.1 |  |  |  |  | 1 |
| c-omp | 64.1 | 32.5 | 17.2 | 19.2 | 18.7 | 1 |
| c-fastmath-serial | 63.9 |  |  |  |  | 1 |
| c-fastmath-omp | 63.8 | 32.4 | 17.0 | 19.2 | 18.0 | 1 |
| c-nofma-serial | 63.9 |  |  |  |  | 1 |
| c-nofma-omp | 64.0 | 32.5 | 17.1 | 19.2 | 19.0 | 1 |
| c-native-serial | 63.1 |  |  |  |  | 1 |
| c-native-omp | 63.2 | 32.1 | 17.1 | 19.3 | 19.6 | 1 |
| c-clang-serial | 66.1 |  |  |  |  | 1 |
| c-clang-omp | 66.5 | 35.1 | 20.0 | 27.9 | 25.4 | 1 |
| cpp-thread | 28.5 | 14.9 | 8.9 | 10.9 | 11.3 | 5 |
| rust-rayon | 11.6 | 6.5 | 4.0 | 4.1 | 4.2 | 1 |
| zig-safe | 15.1 | 9.3 | 6.8 | 8.2 | 9.9 | 5 |
| zig-fast | 9.4 | 6.1 | 4.8 | 6.3 | 7.7 | 5 |
| go | 58.4 | 33.7 | 18.8 | 20.2 | 21.3 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 224.6 | 115.6 | 82.2 | 84.4 | 86.6 | 1 |
| sword-native | 223.8 | 114.1 | 81.8 | 83.5 | 85.1 | 1 |
| c-serial | 113.8 |  |  |  |  | 1 |
| c-omp | 114.0 | 56.6 | 36.0 | 35.4 | 34.3 | 1 |
| c-fastmath-serial | 113.8 |  |  |  |  | 1 |
| c-fastmath-omp | 114.0 | 56.5 | 35.9 | 35.5 | 35.4 | 1 |
| c-nofma-serial | 112.4 |  |  |  |  | 1 |
| c-nofma-omp | 113.1 | 56.0 | 34.1 | 34.7 | 34.3 | 1 |
| c-native-serial | 113.7 |  |  |  |  | 1 |
| c-native-omp | 113.7 | 56.3 | 36.4 | 35.5 | 34.2 | 1 |
| c-clang-serial | 105.5 |  |  |  |  | 1 |
| c-clang-omp | 105.6 | 54.5 | 36.0 | 48.3 | 41.4 | 1 |
| cpp-thread | 40.9 | 21.3 | 14.5 | 17.3 | 17.3 | 5 |
| rust-rayon | 9.4 | 5.1 | 4.4 | 4.5 | 4.6 | 1 |
| zig-safe | 18.5 | 11.3 | 11.4 | 13.6 | 16.5 | 5 |
| zig-fast | 11.9 | 9.3 | 10.4 | 13.1 | 15.8 | 5 |
| go | 73.3 | 42.5 | 29.4 | 32.0 | 33.0 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 206.2 | 116.8 | 90.2 | 86.4 | 88.1 | 1 |
| sword-native | 221.5 | 130.6 | 93.9 | 93.9 | 93.2 | 1 |
| c-serial | 42.9 |  |  |  |  | 1 |
| c-omp | 43.3 | 29.5 | 23.6 | 26.2 | 28.0 | 5 |
| c-fastmath-serial | 43.2 |  |  |  |  | 1 |
| c-fastmath-omp | 42.8 | 29.0 | 25.0 | 25.6 | 29.0 | 5 |
| c-nofma-serial | 42.5 |  |  |  |  | 1 |
| c-nofma-omp | 44.0 | 33.2 | 27.9 | 28.7 | 29.9 | 5 |
| c-native-serial | 43.3 |  |  |  |  | 1 |
| c-native-omp | 44.8 | 29.2 | 23.3 | 25.9 | 27.8 | 5 |
| c-clang-serial | 44.6 |  |  |  |  | 1 |
| c-clang-omp | 42.7 | 29.6 | 24.4 | 26.1 | 28.7 | 5 |
| cpp-thread | 32.9 | 22.3 | 19.2 | 19.5 | 21.7 | 5 |
| rust-rayon | 11.1 | 7.5 | 6.3 | 5.2 | 5.5 | 1 |
| zig-safe | 15.2 | 13.2 | 10.9 | 10.2 | 11.1 | 5 |
| zig-fast | 10.0 | 9.5 | 11.6 | 13.5 | 14.9 | 5 |
| go | 66.7 | 42.4 | 33.2 | 35.4 | 33.9 | 5 |

## Answers across every platform and thread count

| method | sum | saxpy | stencil | mandelbrot | nbody | hist | scan | sort |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sword | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| sword-native | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| sword-without-walked | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-walked-mut | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-captures | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-versioned | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-split | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-deferred | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-lanes | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-without-steady | 1 | 1 | 1 | 1 | 1 |  |  |  |
| sword-rows |  |  | 1 |  |  |  |  |  |
| sword-rows-without-steady |  |  | 1 |  |  |  |  |  |
| c-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-restrict | 1 | 1 | 1 | 1 | 1 |  |  |  |
| c-omp | 7 | 1 | 1 | 1 | 1 | 22 | 4 | 6 |
| c-lanes | 1 |  |  |  |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 | 1 | 1 | 2 |
| c-fastmath-omp | 12 | 1 | 2 | 2 | 1 | 22 | 8 | 6 |
| c-nofma-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-nofma-omp | 8 | 1 | 1 | 1 | 1 | 22 | 4 | 6 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-native-omp | 7 | 1 | 1 | 1 | 1 | 24 | 4 | 6 |
| c-native-lanes | 1 |  |  |  |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 | 10 | 4 | 6 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 10 |
| rust-rayon | 25 | 1 | 1 | 1 | 1 | 30 | 4 | 1 |
| rust-slices |  |  | 1 |  |  |  |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| zig-fast | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| go | 5 | 1 | 1 | 2 | 1 | 5 | 4 | 5 |
