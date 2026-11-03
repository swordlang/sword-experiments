## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.6 | 1.8 | 0.8 | 1.5 | 1.3 | 1 |
| sword-native | 3.6 | 1.8 | 0.8 | 0.9 | 1.3 | 1 |
| sword-without-walked | 4.4 | 2.6 | 1.3 | 1.4 | 1.8 | 1 |
| sword-without-walked-mut | 4.0 | 1.9 | 0.8 | 1.2 | 1.4 | 1 |
| sword-without-captures | 3.3 | 1.7 | 0.9 | 1.3 | 1.4 | 1 |
| sword-without-versioned | 3.5 | 1.8 | 0.8 | 0.9 | 0.9 | 1 |
| sword-without-split | 3.3 | 1.7 | 0.8 | 1.0 | 1.0 | 1 |
| sword-without-deferred | 3.4 | 1.8 | 0.8 | 1.0 | 0.9 | 1 |
| sword-without-lanes | 6.5 | 3.3 | 1.8 | 2.2 | 2.2 | 1 |
| sword-without-steady | 3.6 | 1.7 | 0.8 | 1.0 | 1.0 | 1 |
| c-serial | 6.6 |  |  |  |  | 1 |
| c-restrict | 6.6 |  |  |  |  | 1 |
| c-omp | 6.5 | 3.2 | 1.7 | 2.1 | 2.1 | 5 |
| c-lanes | 3.8 |  |  |  |  | 1 |
| c-lanes-omp | 3.8 | 1.8 | 1.0 | 1.4 | 1.1 | 1 |
| c-fastmath-serial | 6.7 |  |  |  |  | 1 |
| c-fastmath-omp | 6.7 | 3.3 | 1.7 | 2.4 | 2.2 | 7 |
| c-nofma-serial | 6.4 |  |  |  |  | 1 |
| c-nofma-omp | 6.4 | 3.4 | 1.6 | 2.0 | 2.0 | 7 |
| c-native-serial | 6.4 |  |  |  |  | 1 |
| c-native-omp | 6.4 | 3.3 | 1.6 | 2.1 | 2.2 | 6 |
| c-native-lanes | 3.8 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.6 | 1.8 | 0.9 | 1.2 | 1.0 | 1 |
| c-clang-serial | 6.4 |  |  |  |  | 1 |
| c-clang-omp | 6.5 | 3.3 | 1.6 | 2.5 | 2.2 | 5 |
| cpp-thread | 6.7 | 3.4 | 1.8 | 2.4 | 2.3 | 5 |
| rust-rayon | 6.4 | 3.3 | 1.6 | 1.7 | 1.6 | 10 |
| zig-safe | 6.7 | 3.5 | 2.1 | 2.7 | 2.8 | 5 |
| zig-fast | 7.0 | 3.5 | 2.1 | 2.7 | 2.8 | 5 |
| go | 6.5 | 3.4 | 1.7 | 1.8 | 1.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 4.9 | 2.6 | 2.3 | 2.1 | 2.4 | 1 |
| sword-native | 3.7 | 2.2 | 1.8 | 2.0 | 1.8 | 1 |
| sword-without-walked | 7.8 | 3.9 | 2.8 | 2.8 | 3.0 | 1 |
| sword-without-walked-mut | 5.2 | 2.6 | 2.1 | 2.1 | 2.3 | 1 |
| sword-without-captures | 5.1 | 2.4 | 2.0 | 2.0 | 2.3 | 1 |
| sword-without-versioned | 5.0 | 2.3 | 2.2 | 2.0 | 2.3 | 1 |
| sword-without-split | 4.9 | 2.3 | 1.9 | 2.2 | 2.6 | 1 |
| sword-without-deferred | 5.5 | 2.7 | 2.3 | 2.1 | 2.4 | 1 |
| sword-without-lanes | 8.3 | 4.3 | 2.5 | 2.7 | 3.0 | 1 |
| sword-without-steady | 5.3 | 2.7 | 2.3 | 2.2 | 2.6 | 1 |
| c-serial | 8.3 |  |  |  |  | 1 |
| c-restrict | 8.5 |  |  |  |  | 1 |
| c-omp | 8.3 | 4.1 | 2.6 | 2.6 | 3.0 | 7 |
| c-lanes | 5.6 |  |  |  |  | 1 |
| c-lanes-omp | 5.7 | 2.8 | 2.0 | 2.4 | 2.1 | 1 |
| c-fastmath-serial | 4.4 |  |  |  |  | 1 |
| c-fastmath-omp | 8.2 | 3.9 | 2.3 | 2.8 | 2.9 | 6 |
| c-nofma-serial | 8.1 |  |  |  |  | 1 |
| c-nofma-omp | 8.1 | 4.0 | 2.4 | 3.2 | 2.8 | 6 |
| c-native-serial | 8.5 |  |  |  |  | 1 |
| c-native-omp | 8.3 | 4.1 | 2.4 | 2.6 | 3.2 | 7 |
| c-native-lanes | 5.4 |  |  |  |  | 1 |
| c-native-lanes-omp | 5.0 | 2.7 | 2.1 | 2.3 | 2.0 | 1 |
| c-clang-serial | 8.7 |  |  |  |  | 1 |
| c-clang-omp | 10.3 | 4.8 | 2.7 | 3.9 | 3.3 | 5 |
| cpp-thread | 8.3 | 4.1 | 2.6 | 3.6 | 3.5 | 5 |
| rust-rayon | 8.1 | 4.1 | 2.9 | 2.8 | 2.8 | 10 |
| zig-safe | 8.4 | 4.3 | 3.0 | 4.2 | 4.4 | 5 |
| zig-fast | 8.8 | 4.3 | 2.7 | 3.7 | 4.3 | 5 |
| go | 9.2 | 4.5 | 3.5 | 3.8 | 3.6 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.2 | 1.9 | 1.9 | 1.7 | 2.1 | 1 |
| sword-native | 2.4 | 2.0 | 1.6 | 1.6 | 1.7 | 1 |
| sword-without-walked | 3.8 | 2.0 | 2.2 | 2.1 | 2.3 | 1 |
| sword-without-walked-mut | 2.1 | 2.0 | 1.8 | 2.0 | 1.9 | 1 |
| sword-without-captures | 2.4 | 2.2 | 2.0 | 2.4 | 1.8 | 1 |
| sword-without-versioned | 2.2 | 2.1 | 2.0 | 2.0 | 1.8 | 1 |
| sword-without-split | 2.3 | 2.1 | 2.1 | 1.9 | 1.8 | 1 |
| sword-without-deferred | 2.1 | 2.3 | 2.0 | 1.9 | 1.8 | 1 |
| sword-without-lanes | 11.0 | 6.3 | 4.1 | 4.3 | 4.5 | 1 |
| sword-without-steady | 2.1 | 2.0 | 1.9 | 1.7 | 1.9 | 1 |
| c-serial | 10.6 |  |  |  |  | 1 |
| c-restrict | 11.2 |  |  |  |  | 1 |
| c-omp | 11.3 | 5.8 | 5.6 | 5.1 | 4.9 | 5 |
| c-lanes | 2.0 |  |  |  |  | 1 |
| c-lanes-omp | 2.3 | 2.1 | 1.8 | 1.9 | 2.0 | 1 |
| c-fastmath-serial | 2.2 |  |  |  |  | 1 |
| c-fastmath-omp | 2.3 | 2.2 | 1.7 | 1.9 | 2.0 | 5 |
| c-nofma-serial | 11.4 |  |  |  |  | 1 |
| c-nofma-omp | 10.6 | 6.7 | 6.7 | 4.9 | 5.1 | 5 |
| c-native-serial | 11.9 |  |  |  |  | 1 |
| c-native-omp | 11.9 | 6.8 | 5.1 | 5.2 | 5.7 | 5 |
| c-native-lanes | 2.2 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.1 | 2.2 | 1.9 | 1.9 | 2.0 | 1 |
| c-clang-serial | 11.5 |  |  |  |  | 1 |
| c-clang-omp | 11.4 | 6.9 | 5.5 | 4.3 | 4.7 | 5 |
| cpp-thread | 11.1 | 6.6 | 5.7 | 5.1 | 6.8 | 5 |
| rust-rayon | 11.0 | 6.5 | 4.7 | 4.1 | 4.4 | 12 |
| zig-safe | 10.7 | 6.9 | 5.7 | 6.1 | 5.1 | 5 |
| zig-fast | 11.7 | 7.0 | 5.6 | 5.5 | 5.1 | 5 |
| go | 10.9 | 6.9 | 5.1 | 5.0 | 4.6 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.1 | 3.8 | 2.0 | 2.0 | 2.1 | 1 |
| sword-native | 7.1 | 3.8 | 2.0 | 2.1 | 2.2 | 1 |
| sword-without-walked | 7.0 | 3.4 | 2.0 | 2.1 | 2.2 | 1 |
| sword-without-walked-mut | 6.6 | 3.6 | 2.0 | 2.0 | 2.3 | 1 |
| sword-without-captures | 11.8 | 6.4 | 3.3 | 3.6 | 3.6 | 1 |
| sword-without-versioned | 7.0 | 3.6 | 2.0 | 2.0 | 2.1 | 1 |
| sword-without-split | 6.9 | 3.7 | 2.0 | 2.0 | 2.4 | 1 |
| sword-without-deferred | 7.3 | 3.8 | 2.0 | 2.1 | 2.3 | 1 |
| sword-without-lanes | 7.1 | 3.6 | 2.0 | 2.1 | 2.2 | 1 |
| sword-without-steady | 7.1 | 3.7 | 2.0 | 2.2 | 2.2 | 1 |
| c-serial | 7.3 |  |  |  |  | 1 |
| c-restrict | 7.1 |  |  |  |  | 1 |
| c-omp | 7.1 | 3.9 | 2.1 | 2.9 | 2.5 | 1 |
| c-fastmath-serial | 7.3 |  |  |  |  | 1 |
| c-fastmath-omp | 6.9 | 3.7 | 2.2 | 3.0 | 2.5 | 1 |
| c-nofma-serial | 7.3 |  |  |  |  | 1 |
| c-nofma-omp | 7.2 | 4.1 | 2.1 | 2.9 | 2.5 | 1 |
| c-native-serial | 7.1 |  |  |  |  | 1 |
| c-native-omp | 7.1 | 3.9 | 2.1 | 2.8 | 2.4 | 1 |
| c-clang-serial | 6.9 |  |  |  |  | 1 |
| c-clang-omp | 6.7 | 3.8 | 2.0 | 2.8 | 2.5 | 1 |
| cpp-thread | 7.6 | 4.0 | 2.4 | 2.8 | 2.9 | 1 |
| rust-rayon | 7.1 | 3.6 | 2.0 | 2.1 | 2.4 | 1 |
| zig-safe | 11.5 | 6.0 | 3.3 | 4.2 | 4.3 | 1 |
| zig-fast | 9.2 | 5.2 | 2.8 | 3.8 | 3.8 | 1 |
| go | 7.9 | 4.2 | 2.3 | 2.3 | 2.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 11.1 | 5.8 | 5.2 | 5.2 | 5.2 | 1 |
| sword-native | 9.3 | 4.6 | 4.7 | 5.0 | 4.9 | 1 |
| sword-without-walked | 11.3 | 5.8 | 5.2 | 5.3 | 5.2 | 1 |
| sword-without-walked-mut | 11.2 | 5.8 | 5.2 | 5.2 | 5.3 | 1 |
| sword-without-captures | 13.9 | 7.2 | 5.7 | 5.8 | 5.8 | 1 |
| sword-without-versioned | 11.3 | 5.8 | 5.2 | 5.2 | 5.3 | 1 |
| sword-without-split | 11.2 | 5.8 | 5.2 | 5.2 | 5.3 | 1 |
| sword-without-deferred | 11.1 | 5.7 | 5.2 | 5.2 | 5.3 | 1 |
| sword-without-lanes | 11.2 | 5.8 | 5.2 | 5.2 | 5.2 | 1 |
| sword-without-steady | 11.1 | 5.8 | 5.2 | 5.3 | 5.3 | 1 |
| c-serial | 10.1 |  |  |  |  | 1 |
| c-restrict | 10.2 |  |  |  |  | 1 |
| c-omp | 11.6 | 6.3 | 5.4 | 6.1 | 5.7 | 1 |
| c-fastmath-serial | 9.8 |  |  |  |  | 1 |
| c-fastmath-omp | 11.9 | 6.3 | 5.3 | 6.0 | 5.7 | 1 |
| c-nofma-serial | 10.0 |  |  |  |  | 1 |
| c-nofma-omp | 12.1 | 6.5 | 5.4 | 5.8 | 5.9 | 1 |
| c-native-serial | 10.0 |  |  |  |  | 1 |
| c-native-omp | 11.5 | 6.0 | 5.4 | 5.9 | 5.7 | 1 |
| c-clang-serial | 11.2 |  |  |  |  | 1 |
| c-clang-omp | 11.2 | 5.7 | 5.1 | 6.1 | 6.0 | 1 |
| cpp-thread | 13.2 | 6.8 | 5.6 | 6.2 | 6.5 | 1 |
| rust-rayon | 11.3 | 5.9 | 5.3 | 5.3 | 5.6 | 1 |
| zig-safe | 15.1 | 7.9 | 6.1 | 6.9 | 8.3 | 1 |
| zig-fast | 13.9 | 7.3 | 5.8 | 6.7 | 7.4 | 1 |
| go | 13.3 | 6.6 | 5.4 | 5.6 | 5.4 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.5 | 5.4 | 5.6 | 5.4 | 5.6 | 1 |
| sword-native | 6.5 | 5.9 | 5.4 | 5.3 | 5.2 | 1 |
| sword-without-walked | 5.5 | 5.4 | 5.4 | 5.4 | 5.7 | 1 |
| sword-without-walked-mut | 6.2 | 5.8 | 5.5 | 5.7 | 5.5 | 1 |
| sword-without-captures | 12.2 | 7.5 | 6.3 | 6.6 | 7.0 | 1 |
| sword-without-versioned | 8.0 | 5.8 | 6.3 | 6.2 | 5.7 | 1 |
| sword-without-split | 5.8 | 5.5 | 5.4 | 5.4 | 5.5 | 1 |
| sword-without-deferred | 5.9 | 5.4 | 5.8 | 5.4 | 6.2 | 1 |
| sword-without-lanes | 6.1 | 5.6 | 6.1 | 5.6 | 5.3 | 1 |
| sword-without-steady | 5.6 | 6.1 | 5.4 | 5.3 | 5.3 | 1 |
| c-serial | 6.7 |  |  |  |  | 1 |
| c-restrict | 6.2 |  |  |  |  | 1 |
| c-omp | 6.3 | 6.3 | 5.6 | 5.8 | 5.8 | 1 |
| c-fastmath-serial | 6.0 |  |  |  |  | 1 |
| c-fastmath-omp | 6.0 | 5.7 | 5.5 | 5.4 | 6.4 | 1 |
| c-nofma-serial | 5.6 |  |  |  |  | 1 |
| c-nofma-omp | 5.9 | 5.6 | 5.6 | 5.9 | 5.6 | 1 |
| c-native-serial | 6.0 |  |  |  |  | 1 |
| c-native-omp | 5.9 | 5.7 | 5.0 | 5.2 | 5.7 | 1 |
| c-clang-serial | 5.8 |  |  |  |  | 1 |
| c-clang-omp | 6.8 | 5.5 | 5.6 | 5.5 | 5.6 | 1 |
| cpp-thread | 5.8 | 5.4 | 5.4 | 5.4 | 5.5 | 1 |
| rust-rayon | 5.6 | 5.2 | 5.1 | 5.2 | 5.7 | 1 |
| zig-safe | 12.5 | 8.7 | 6.7 | 6.6 | 6.9 | 1 |
| zig-fast | 8.9 | 7.9 | 6.2 | 6.2 | 6.4 | 1 |
| go | 8.3 | 6.4 | 6.2 | 5.7 | 5.9 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 77.9 | 39.0 | 19.4 | 23.2 | 25.2 | 1 |
| sword-native | 64.4 | 32.0 | 16.3 | 19.5 | 21.2 | 1 |
| sword-without-walked | 78.0 | 39.3 | 19.8 | 22.6 | 24.7 | 1 |
| sword-without-walked-mut | 79.4 | 39.9 | 19.9 | 23.4 | 24.1 | 1 |
| sword-without-captures | 87.7 | 44.3 | 22.2 | 25.4 | 27.6 | 1 |
| sword-without-versioned | 78.6 | 39.6 | 19.6 | 23.2 | 24.8 | 1 |
| sword-without-split | 91.6 | 46.1 | 22.8 | 25.7 | 29.8 | 1 |
| sword-without-deferred | 77.7 | 38.9 | 19.5 | 22.8 | 25.0 | 1 |
| sword-without-lanes | 77.6 | 38.9 | 19.6 | 22.2 | 23.9 | 1 |
| sword-without-steady | 77.4 | 39.1 | 19.6 | 22.4 | 24.5 | 1 |
| sword-rows | 22.3 | 11.2 | 5.7 | 7.5 | 8.3 | 1 |
| sword-rows-without-steady | 22.2 | 11.3 | 5.8 | 8.2 | 8.2 | 1 |
| c-serial | 54.0 |  |  |  |  | 1 |
| c-restrict | 54.2 |  |  |  |  | 1 |
| c-omp | 52.2 | 24.9 | 12.5 | 16.0 | 14.7 | 1 |
| c-fastmath-serial | 54.5 |  |  |  |  | 1 |
| c-fastmath-omp | 50.4 | 25.1 | 12.5 | 16.6 | 14.2 | 1 |
| c-nofma-serial | 55.1 |  |  |  |  | 1 |
| c-nofma-omp | 52.5 | 25.3 | 12.5 | 15.8 | 13.9 | 1 |
| c-native-serial | 42.2 |  |  |  |  | 1 |
| c-native-omp | 42.1 | 20.7 | 10.4 | 13.2 | 12.2 | 1 |
| c-clang-serial | 48.8 |  |  |  |  | 1 |
| c-clang-omp | 49.7 | 24.6 | 12.4 | 18.1 | 18.6 | 1 |
| cpp-thread | 57.0 | 28.1 | 15.5 | 19.6 | 20.3 | 1 |
| rust-rayon | 91.7 | 46.0 | 23.5 | 23.4 | 23.7 | 1 |
| rust-slices | 21.0 | 10.9 | 5.7 | 5.7 | 6.0 | 1 |
| zig-safe | 94.5 | 48.0 | 27.6 | 34.3 | 36.1 | 1 |
| zig-fast | 43.0 | 22.7 | 14.7 | 18.4 | 20.2 | 1 |
| go | 78.8 | 38.8 | 20.0 | 23.1 | 21.3 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 291.7 | 43.6 | 42.8 | 43.1 | 44.9 | 1 |
| sword-native | 87.3 | 43.7 | 42.7 | 44.1 | 45.3 | 1 |
| sword-without-walked | 88.0 | 44.3 | 42.8 | 44.1 | 45.1 | 1 |
| sword-without-walked-mut | 87.8 | 44.4 | 43.0 | 43.9 | 44.8 | 1 |
| sword-without-captures | 94.2 | 47.8 | 47.3 | 48.0 | 49.6 | 1 |
| sword-without-versioned | 88.0 | 44.3 | 42.8 | 43.9 | 44.8 | 1 |
| sword-without-split | 102.2 | 51.5 | 50.0 | 50.8 | 51.1 | 1 |
| sword-without-deferred | 87.3 | 43.9 | 42.9 | 44.1 | 45.1 | 1 |
| sword-without-lanes | 87.7 | 44.5 | 43.0 | 43.8 | 44.7 | 1 |
| sword-without-steady | 87.6 | 44.0 | 42.8 | 43.8 | 44.2 | 1 |
| sword-rows | 35.9 | 17.5 | 15.4 | 15.5 | 16.1 | 1 |
| sword-rows-without-steady | 35.7 | 17.5 | 14.9 | 15.1 | 16.3 | 1 |
| c-serial | 46.0 |  |  |  |  | 1 |
| c-restrict | 45.6 |  |  |  |  | 1 |
| c-omp | 45.1 | 22.7 | 18.7 | 21.4 | 20.4 | 1 |
| c-fastmath-serial | 47.2 |  |  |  |  | 1 |
| c-fastmath-omp | 45.5 | 22.1 | 18.8 | 20.0 | 21.7 | 1 |
| c-nofma-serial | 45.1 |  |  |  |  | 1 |
| c-nofma-omp | 45.6 | 22.4 | 18.7 | 20.3 | 20.7 | 1 |
| c-native-serial | 47.5 |  |  |  |  | 1 |
| c-native-omp | 47.0 | 22.4 | 18.7 | 21.2 | 20.9 | 1 |
| c-clang-serial | 52.6 |  |  |  |  | 1 |
| c-clang-omp | 51.8 | 25.4 | 23.8 | 31.5 | 30.9 | 1 |
| cpp-thread | 51.2 | 26.3 | 22.9 | 30.1 | 27.5 | 1 |
| rust-rayon | 115.9 | 58.2 | 47.6 | 48.7 | 48.7 | 1 |
| rust-slices | 37.7 | 18.4 | 15.2 | 15.3 | 15.7 | 1 |
| zig-safe | 92.3 | 48.5 | 48.2 | 57.7 | 57.3 | 1 |
| zig-fast | 49.0 | 25.2 | 22.4 | 28.3 | 29.9 | 1 |
| go | 88.1 | 44.2 | 40.8 | 41.8 | 42.4 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 51.2 | 32.8 | 23.7 | 26.4 | 25.0 | 1 |
| sword-native | 47.3 | 33.6 | 30.5 | 29.6 | 29.6 | 1 |
| sword-without-walked | 44.2 | 32.9 | 26.9 | 29.0 | 29.3 | 1 |
| sword-without-walked-mut | 60.2 | 37.7 | 30.2 | 31.4 | 29.4 | 1 |
| sword-without-captures | 72.6 | 52.7 | 42.8 | 40.2 | 36.4 | 1 |
| sword-without-versioned | 43.3 | 32.8 | 27.5 | 29.3 | 28.9 | 1 |
| sword-without-split | 73.2 | 51.8 | 34.2 | 38.4 | 38.0 | 1 |
| sword-without-deferred | 56.3 | 37.4 | 28.6 | 25.7 | 26.5 | 1 |
| sword-without-lanes | 40.4 | 32.6 | 30.0 | 29.1 | 25.9 | 1 |
| sword-without-steady | 42.5 | 32.5 | 26.8 | 25.1 | 28.7 | 1 |
| sword-rows | 29.2 | 25.6 | 21.1 | 19.9 | 19.8 | 1 |
| sword-rows-without-steady | 35.6 | 23.4 | 22.6 | 22.0 | 21.1 | 1 |
| c-serial | 41.6 |  |  |  |  | 1 |
| c-restrict | 41.1 |  |  |  |  | 1 |
| c-omp | 45.1 | 31.8 | 25.5 | 26.1 | 24.5 | 1 |
| c-fastmath-serial | 44.8 |  |  |  |  | 1 |
| c-fastmath-omp | 37.9 | 32.1 | 26.0 | 26.5 | 23.8 | 1 |
| c-nofma-serial | 46.6 |  |  |  |  | 1 |
| c-nofma-omp | 44.8 | 32.6 | 29.1 | 27.0 | 27.9 | 1 |
| c-native-serial | 45.9 |  |  |  |  | 1 |
| c-native-omp | 43.3 | 36.9 | 26.0 | 31.4 | 26.8 | 1 |
| c-clang-serial | 42.3 |  |  |  |  | 1 |
| c-clang-omp | 41.7 | 36.8 | 25.6 | 24.5 | 22.6 | 1 |
| cpp-thread | 44.9 | 33.8 | 27.1 | 27.8 | 26.7 | 1 |
| rust-rayon | 107.0 | 52.8 | 67.2 | 41.4 | 40.4 | 1 |
| rust-slices | 28.0 | 22.5 | 19.7 | 20.2 | 21.7 | 1 |
| zig-safe | 96.1 | 70.0 | 54.8 | 52.8 | 51.9 | 1 |
| zig-fast | 41.4 | 29.9 | 23.8 | 25.2 | 26.8 | 1 |
| go | 79.1 | 61.3 | 50.6 | 48.7 | 46.1 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.8 | 346.6 | 173.7 | 175.8 | 176.2 | 1 |
| sword-native | 683.9 | 342.1 | 171.4 | 174.1 | 173.7 | 1 |
| sword-without-walked | 692.4 | 346.4 | 173.7 | 176.0 | 175.8 | 1 |
| sword-without-walked-mut | 692.8 | 346.6 | 173.7 | 176.5 | 176.7 | 1 |
| sword-without-captures | 692.7 | 346.5 | 173.8 | 177.3 | 176.8 | 1 |
| sword-without-versioned | 692.8 | 346.6 | 173.6 | 176.0 | 176.3 | 1 |
| sword-without-split | 692.7 | 346.5 | 173.8 | 177.2 | 179.9 | 1 |
| sword-without-deferred | 692.7 | 346.6 | 173.7 | 175.9 | 176.1 | 1 |
| sword-without-lanes | 692.7 | 346.5 | 173.6 | 175.2 | 176.2 | 1 |
| sword-without-steady | 692.7 | 346.5 | 173.8 | 176.2 | 177.3 | 1 |
| c-serial | 648.0 |  |  |  |  | 1 |
| c-restrict | 646.7 |  |  |  |  | 1 |
| c-omp | 636.6 | 319.2 | 160.0 | 160.2 | 160.1 | 1 |
| c-fastmath-serial | 628.4 |  |  |  |  | 1 |
| c-fastmath-omp | 629.2 | 314.8 | 157.7 | 157.7 | 157.8 | 1 |
| c-nofma-serial | 697.2 |  |  |  |  | 1 |
| c-nofma-omp | 697.0 | 348.7 | 174.7 | 174.6 | 174.7 | 1 |
| c-native-serial | 649.4 |  |  |  |  | 1 |
| c-native-omp | 658.4 | 329.4 | 164.8 | 164.6 | 163.6 | 1 |
| c-clang-serial | 770.2 |  |  |  |  | 1 |
| c-clang-omp | 769.9 | 385.5 | 193.6 | 193.6 | 193.9 | 1 |
| cpp-thread | 853.9 | 427.3 | 214.3 | 236.2 | 217.9 | 1 |
| rust-rayon | 693.0 | 347.1 | 173.9 | 174.0 | 174.0 | 1 |
| zig-safe | 682.5 | 342.7 | 172.1 | 189.8 | 174.8 | 1 |
| zig-fast | 897.1 | 448.9 | 225.2 | 240.6 | 229.0 | 1 |
| go | 678.1 | 339.4 | 170.5 | 175.8 | 174.9 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 863.6 | 433.2 | 243.7 | 245.9 | 247.3 | 1 |
| sword-native | 826.6 | 415.7 | 234.2 | 236.0 | 237.1 | 1 |
| sword-without-walked | 863.1 | 433.2 | 242.7 | 244.7 | 246.1 | 1 |
| sword-without-walked-mut | 864.1 | 432.7 | 242.3 | 246.1 | 246.2 | 1 |
| sword-without-captures | 862.5 | 432.1 | 243.1 | 245.1 | 245.5 | 1 |
| sword-without-versioned | 863.4 | 433.6 | 243.7 | 246.2 | 246.0 | 1 |
| sword-without-split | 863.2 | 433.6 | 243.1 | 245.1 | 246.2 | 1 |
| sword-without-deferred | 864.0 | 433.1 | 243.9 | 245.5 | 245.8 | 1 |
| sword-without-lanes | 861.4 | 433.2 | 242.0 | 245.8 | 245.8 | 1 |
| sword-without-steady | 863.1 | 432.7 | 243.6 | 245.7 | 247.3 | 1 |
| c-serial | 820.6 |  |  |  |  | 1 |
| c-restrict | 819.9 |  |  |  |  | 1 |
| c-omp | 835.2 | 419.3 | 227.0 | 227.5 | 227.0 | 1 |
| c-fastmath-serial | 811.8 |  |  |  |  | 1 |
| c-fastmath-omp | 805.5 | 404.6 | 228.2 | 228.6 | 229.1 | 1 |
| c-nofma-serial | 861.2 |  |  |  |  | 1 |
| c-nofma-omp | 859.7 | 431.7 | 242.8 | 243.5 | 242.2 | 1 |
| c-native-serial | 824.0 |  |  |  |  | 1 |
| c-native-omp | 836.4 | 419.3 | 226.8 | 227.3 | 227.5 | 1 |
| c-clang-serial | 853.2 |  |  |  |  | 1 |
| c-clang-omp | 857.2 | 430.5 | 244.8 | 244.5 | 244.8 | 1 |
| cpp-thread | 839.7 | 421.9 | 227.1 | 247.8 | 231.3 | 1 |
| rust-rayon | 859.2 | 431.5 | 245.7 | 245.5 | 245.9 | 1 |
| zig-safe | 865.5 | 435.1 | 243.4 | 263.3 | 248.4 | 1 |
| zig-fast | 848.8 | 426.9 | 240.1 | 259.3 | 246.7 | 1 |
| go | 883.2 | 443.4 | 244.0 | 252.8 | 248.5 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 998.6 | 523.3 | 369.1 | 383.7 | 360.7 | 1 |
| sword-native | 1060.7 | 572.9 | 376.7 | 356.0 | 361.9 | 1 |
| sword-without-walked | 1042.5 | 506.0 | 355.3 | 361.2 | 357.3 | 1 |
| sword-without-walked-mut | 1028.8 | 503.5 | 354.2 | 423.7 | 362.4 | 1 |
| sword-without-captures | 1274.3 | 555.2 | 408.2 | 397.7 | 382.1 | 1 |
| sword-without-versioned | 1160.5 | 549.1 | 400.5 | 365.0 | 375.6 | 1 |
| sword-without-split | 1039.8 | 523.6 | 359.8 | 387.5 | 364.2 | 1 |
| sword-without-deferred | 1115.7 | 553.2 | 395.9 | 379.3 | 386.3 | 1 |
| sword-without-lanes | 1043.6 | 548.2 | 356.6 | 368.1 | 365.5 | 1 |
| sword-without-steady | 1131.0 | 561.9 | 356.3 | 363.0 | 362.4 | 1 |
| c-serial | 890.6 |  |  |  |  | 1 |
| c-restrict | 908.6 |  |  |  |  | 1 |
| c-omp | 948.8 | 434.6 | 300.8 | 398.3 | 301.3 | 1 |
| c-fastmath-serial | 778.2 |  |  |  |  | 1 |
| c-fastmath-omp | 784.9 | 394.6 | 253.7 | 255.4 | 250.2 | 1 |
| c-nofma-serial | 995.1 |  |  |  |  | 1 |
| c-nofma-omp | 1010.5 | 516.2 | 366.4 | 362.2 | 356.7 | 1 |
| c-native-serial | 967.7 |  |  |  |  | 1 |
| c-native-omp | 883.4 | 474.4 | 357.6 | 365.2 | 354.5 | 1 |
| c-clang-serial | 797.2 |  |  |  |  | 1 |
| c-clang-omp | 872.6 | 452.5 | 317.1 | 312.7 | 317.0 | 1 |
| cpp-thread | 815.5 | 424.2 | 368.2 | 311.9 | 367.8 | 1 |
| rust-rayon | 1218.7 | 634.7 | 441.3 | 427.6 | 414.7 | 1 |
| zig-safe | 1170.7 | 581.9 | 406.1 | 391.5 | 380.0 | 1 |
| zig-fast | 998.2 | 516.1 | 374.3 | 353.6 | 352.3 | 1 |
| go | 977.4 | 569.2 | 406.4 | 391.8 | 398.5 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.7 | 125.6 | 63.2 | 67.0 | 67.9 | 1 |
| sword-native | 246.9 | 123.6 | 62.1 | 64.7 | 67.6 | 1 |
| sword-without-walked | 250.7 | 125.6 | 62.7 | 65.5 | 66.9 | 1 |
| sword-without-walked-mut | 251.3 | 125.6 | 63.2 | 66.1 | 66.5 | 1 |
| sword-without-captures | 254.4 | 127.3 | 63.3 | 66.9 | 67.8 | 1 |
| sword-without-versioned | 270.7 | 135.5 | 68.2 | 71.2 | 70.9 | 1 |
| sword-without-split | 251.6 | 125.7 | 63.4 | 66.9 | 67.4 | 1 |
| sword-without-deferred | 251.7 | 125.6 | 64.1 | 66.2 | 67.3 | 1 |
| sword-without-lanes | 254.5 | 127.3 | 63.4 | 65.0 | 67.2 | 1 |
| sword-without-steady | 250.2 | 125.3 | 63.4 | 65.3 | 67.1 | 1 |
| c-serial | 237.7 |  |  |  |  | 1 |
| c-restrict | 237.6 |  |  |  |  | 1 |
| c-omp | 239.5 | 119.9 | 60.2 | 64.3 | 63.8 | 1 |
| c-fastmath-serial | 237.7 |  |  |  |  | 1 |
| c-fastmath-omp | 245.0 | 122.6 | 61.6 | 66.1 | 65.2 | 1 |
| c-nofma-serial | 242.5 |  |  |  |  | 1 |
| c-nofma-omp | 268.4 | 134.3 | 67.4 | 71.5 | 72.3 | 1 |
| c-native-serial | 248.6 |  |  |  |  | 1 |
| c-native-omp | 248.8 | 124.5 | 62.5 | 69.0 | 67.2 | 1 |
| c-clang-serial | 242.6 |  |  |  |  | 1 |
| c-clang-omp | 246.4 | 123.3 | 61.9 | 72.1 | 66.5 | 1 |
| cpp-thread | 240.4 | 120.4 | 61.3 | 71.9 | 70.8 | 1 |
| rust-rayon | 239.0 | 120.2 | 60.4 | 60.9 | 61.8 | 1 |
| zig-safe | 271.9 | 137.0 | 71.4 | 81.1 | 84.5 | 1 |
| zig-fast | 271.7 | 136.8 | 71.4 | 80.1 | 85.2 | 1 |
| go | 252.8 | 126.4 | 63.7 | 68.9 | 67.6 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 235.4 | 118.4 | 119.9 | 120.0 | 121.1 | 1 |
| sword-native | 240.5 | 120.7 | 122.6 | 122.8 | 124.4 | 1 |
| sword-without-walked | 235.4 | 118.3 | 119.6 | 120.8 | 121.5 | 1 |
| sword-without-walked-mut | 235.6 | 118.4 | 119.9 | 120.3 | 121.5 | 1 |
| sword-without-captures | 235.2 | 118.6 | 119.8 | 120.4 | 121.8 | 1 |
| sword-without-versioned | 235.8 | 118.2 | 123.0 | 123.2 | 124.1 | 1 |
| sword-without-split | 235.1 | 118.9 | 119.7 | 120.4 | 121.6 | 1 |
| sword-without-deferred | 235.1 | 118.5 | 119.6 | 120.4 | 121.4 | 1 |
| sword-without-lanes | 235.1 | 118.3 | 119.7 | 120.3 | 120.8 | 1 |
| sword-without-steady | 234.8 | 118.3 | 119.5 | 119.8 | 121.2 | 1 |
| c-serial | 112.6 |  |  |  |  | 1 |
| c-restrict | 112.5 |  |  |  |  | 1 |
| c-omp | 127.7 | 64.5 | 60.2 | 61.6 | 62.4 | 1 |
| c-fastmath-serial | 112.5 |  |  |  |  | 1 |
| c-fastmath-omp | 112.7 | 56.6 | 56.5 | 57.1 | 58.4 | 1 |
| c-nofma-serial | 112.4 |  |  |  |  | 1 |
| c-nofma-omp | 128.6 | 65.3 | 60.6 | 60.9 | 62.9 | 1 |
| c-native-serial | 112.6 |  |  |  |  | 1 |
| c-native-omp | 128.4 | 65.0 | 60.4 | 61.9 | 63.1 | 1 |
| c-clang-serial | 235.5 |  |  |  |  | 1 |
| c-clang-omp | 235.5 | 118.6 | 121.4 | 121.7 | 137.4 | 1 |
| cpp-thread | 132.9 | 67.5 | 62.6 | 69.9 | 69.6 | 1 |
| rust-rayon | 241.1 | 121.1 | 122.7 | 122.8 | 123.1 | 1 |
| zig-safe | 241.9 | 122.5 | 123.4 | 131.3 | 133.1 | 1 |
| zig-fast | 241.8 | 122.6 | 124.2 | 132.9 | 133.9 | 1 |
| go | 585.6 | 294.3 | 152.5 | 161.0 | 161.0 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 126.5 | 69.0 | 53.2 | 40.9 | 44.9 | 1 |
| sword-native | 129.8 | 60.3 | 50.3 | 49.2 | 52.6 | 1 |
| sword-without-walked | 94.6 | 61.0 | 50.6 | 48.2 | 50.7 | 1 |
| sword-without-walked-mut | 92.0 | 63.0 | 45.3 | 46.2 | 49.0 | 1 |
| sword-without-captures | 91.8 | 71.1 | 48.5 | 51.4 | 48.6 | 1 |
| sword-without-versioned | 148.0 | 92.2 | 68.8 | 69.6 | 67.3 | 1 |
| sword-without-split | 94.8 | 61.5 | 53.2 | 51.2 | 46.9 | 1 |
| sword-without-deferred | 90.8 | 61.4 | 49.5 | 48.0 | 45.4 | 1 |
| sword-without-lanes | 90.8 | 62.6 | 48.7 | 43.5 | 48.2 | 1 |
| sword-without-steady | 97.0 | 62.3 | 46.3 | 48.3 | 46.5 | 1 |
| c-serial | 105.4 |  |  |  |  | 1 |
| c-restrict | 90.5 |  |  |  |  | 1 |
| c-omp | 95.7 | 66.3 | 56.5 | 51.8 | 49.4 | 1 |
| c-fastmath-serial | 48.5 |  |  |  |  | 1 |
| c-fastmath-omp | 47.0 | 39.2 | 34.5 | 30.8 | 32.1 | 1 |
| c-nofma-serial | 96.3 |  |  |  |  | 1 |
| c-nofma-omp | 88.5 | 74.7 | 54.7 | 55.0 | 50.4 | 1 |
| c-native-serial | 88.2 |  |  |  |  | 1 |
| c-native-omp | 89.4 | 74.8 | 56.0 | 52.0 | 51.9 | 1 |
| c-clang-serial | 93.2 |  |  |  |  | 1 |
| c-clang-omp | 105.2 | 66.3 | 53.4 | 48.4 | 50.8 | 1 |
| cpp-thread | 86.2 | 72.0 | 52.2 | 51.3 | 47.5 | 1 |
| rust-rayon | 87.6 | 58.2 | 40.1 | 43.4 | 42.5 | 1 |
| zig-safe | 150.1 | 97.1 | 77.2 | 70.4 | 71.6 | 1 |
| zig-fast | 147.9 | 103.4 | 78.6 | 70.8 | 69.6 | 1 |
| go | 133.8 | 88.3 | 69.1 | 63.5 | 62.4 | 1 |

## hist

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.7 | 4.0 | 1.9 | 2.2 | 2.3 | 1 |
| sword-native | 7.4 | 3.9 | 2.0 | 2.5 | 2.2 | 1 |
| c-serial | 7.7 |  |  |  |  | 1 |
| c-omp | 7.7 | 4.0 | 2.0 | 2.1 | 2.4 | 11 |
| c-fastmath-serial | 7.6 |  |  |  |  | 1 |
| c-fastmath-omp | 7.7 | 4.0 | 2.1 | 2.2 | 2.5 | 11 |
| c-nofma-serial | 7.9 |  |  |  |  | 1 |
| c-nofma-omp | 7.7 | 3.9 | 1.9 | 2.0 | 2.5 | 11 |
| c-native-serial | 7.7 |  |  |  |  | 1 |
| c-native-omp | 7.9 | 4.0 | 2.0 | 2.1 | 2.5 | 11 |
| c-clang-serial | 7.5 |  |  |  |  | 1 |
| c-clang-omp | 7.5 | 3.8 | 1.9 | 3.0 | 2.4 | 7 |
| cpp-thread | 8.4 | 4.1 | 2.6 | 2.8 | 3.0 | 5 |
| rust-rayon | 8.0 | 4.0 | 2.0 | 1.9 | 2.1 | 10 |
| zig-safe | 13.2 | 8.4 | 5.2 | 5.1 | 5.1 | 5 |
| zig-fast | 8.1 | 5.1 | 3.2 | 3.4 | 3.6 | 5 |
| go | 9.0 | 4.6 | 2.4 | 2.5 | 2.4 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 14.4 | 7.3 | 5.9 | 5.9 | 6.1 | 1 |
| sword-native | 11.2 | 5.6 | 3.9 | 4.0 | 4.2 | 1 |
| c-serial | 12.1 |  |  |  |  | 1 |
| c-omp | 11.7 | 5.5 | 3.9 | 4.3 | 4.5 | 11 |
| c-fastmath-serial | 12.2 |  |  |  |  | 1 |
| c-fastmath-omp | 11.7 | 5.8 | 3.9 | 4.1 | 4.7 | 10 |
| c-nofma-serial | 11.9 |  |  |  |  | 1 |
| c-nofma-omp | 11.5 | 5.7 | 4.0 | 4.0 | 4.1 | 10 |
| c-native-serial | 11.8 |  |  |  |  | 1 |
| c-native-omp | 11.3 | 5.6 | 3.9 | 4.0 | 4.1 | 11 |
| c-clang-serial | 10.6 |  |  |  |  | 1 |
| c-clang-omp | 11.7 | 5.5 | 3.6 | 5.2 | 5.4 | 7 |
| cpp-thread | 11.8 | 5.7 | 7.6 | 6.1 | 5.7 | 5 |
| rust-rayon | 22.4 | 11.5 | 10.4 | 10.5 | 10.6 | 11 |
| zig-safe | 14.9 | 10.3 | 8.3 | 8.9 | 8.8 | 5 |
| zig-fast | 13.2 | 12.1 | 9.5 | 6.8 | 6.3 | 5 |
| go | 11.6 | 6.1 | 4.2 | 4.3 | 4.3 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.2 | 3.8 | 2.9 | 2.8 | 2.4 | 1 |
| sword-native | 6.2 | 4.3 | 3.4 | 3.6 | 3.0 | 1 |
| c-serial | 5.8 |  |  |  |  | 1 |
| c-omp | 5.6 | 4.6 | 4.4 | 4.1 | 3.4 | 6 |
| c-fastmath-serial | 5.8 |  |  |  |  | 1 |
| c-fastmath-omp | 7.0 | 4.6 | 3.1 | 3.8 | 3.9 | 7 |
| c-nofma-serial | 6.3 |  |  |  |  | 1 |
| c-nofma-omp | 6.1 | 4.6 | 3.7 | 3.8 | 3.6 | 7 |
| c-native-serial | 6.7 |  |  |  |  | 1 |
| c-native-omp | 6.4 | 4.7 | 3.7 | 3.9 | 3.6 | 7 |
| c-clang-serial | 5.4 |  |  |  |  | 1 |
| c-clang-omp | 5.7 | 4.4 | 3.7 | 3.8 | 3.6 | 7 |
| cpp-thread | 6.8 | 4.9 | 3.8 | 4.1 | 4.7 | 5 |
| rust-rayon | 6.4 | 4.2 | 3.4 | 2.9 | 3.0 | 13 |
| zig-safe | 8.2 | 9.6 | 7.3 | 6.8 | 5.7 | 5 |
| zig-fast | 5.0 | 4.8 | 5.2 | 5.2 | 5.6 | 5 |
| go | 6.7 | 4.9 | 5.5 | 5.1 | 3.9 | 5 |

## scan

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 17.3 | 8.9 | 4.8 | 5.6 | 6.4 | 1 |
| sword-native | 15.2 | 8.3 | 4.2 | 4.6 | 5.8 | 1 |
| c-serial | 7.1 |  |  |  |  | 1 |
| c-omp | 13.4 | 6.6 | 3.4 | 3.7 | 4.4 | 4 |
| c-fastmath-serial | 7.2 |  |  |  |  | 1 |
| c-fastmath-omp | 13.3 | 7.0 | 3.5 | 4.2 | 4.5 | 4 |
| c-nofma-serial | 7.0 |  |  |  |  | 1 |
| c-nofma-omp | 13.1 | 7.0 | 3.3 | 4.5 | 4.4 | 4 |
| c-native-serial | 6.8 |  |  |  |  | 1 |
| c-native-omp | 13.2 | 6.8 | 3.3 | 4.3 | 4.3 | 4 |
| c-clang-serial | 6.9 |  |  |  |  | 1 |
| c-clang-omp | 13.3 | 6.8 | 3.5 | 5.1 | 4.7 | 4 |
| cpp-thread | 14.3 | 7.1 | 3.8 | 4.0 | 5.1 | 4 |
| rust-rayon | 13.3 | 7.0 | 3.5 | 3.7 | 3.6 | 4 |
| zig-safe | 15.6 | 7.9 | 4.7 | 5.9 | 6.3 | 4 |
| zig-fast | 14.4 | 7.7 | 4.9 | 5.6 | 5.9 | 4 |
| go | 14.5 | 7.0 | 3.6 | 4.0 | 4.0 | 4 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 33.4 | 16.8 | 12.3 | 12.8 | 13.6 | 1 |
| sword-native | 32.2 | 16.1 | 11.6 | 12.2 | 12.6 | 1 |
| c-serial | 12.3 |  |  |  |  | 1 |
| c-omp | 20.7 | 9.9 | 7.0 | 7.3 | 8.1 | 4 |
| c-fastmath-serial | 12.3 |  |  |  |  | 1 |
| c-fastmath-omp | 20.5 | 9.8 | 7.1 | 8.6 | 7.8 | 4 |
| c-nofma-serial | 12.5 |  |  |  |  | 1 |
| c-nofma-omp | 20.7 | 9.9 | 7.1 | 7.4 | 8.1 | 4 |
| c-native-serial | 12.3 |  |  |  |  | 1 |
| c-native-omp | 20.8 | 9.8 | 7.3 | 7.8 | 8.0 | 4 |
| c-clang-serial | 12.4 |  |  |  |  | 1 |
| c-clang-omp | 21.0 | 10.0 | 7.4 | 9.0 | 8.6 | 4 |
| cpp-thread | 21.5 | 9.9 | 7.9 | 9.4 | 9.9 | 4 |
| rust-rayon | 21.2 | 10.3 | 8.1 | 7.8 | 8.1 | 4 |
| zig-safe | 22.0 | 10.9 | 8.1 | 11.1 | 10.6 | 4 |
| zig-fast | 21.9 | 11.0 | 8.7 | 10.9 | 11.2 | 4 |
| go | 21.5 | 11.2 | 8.1 | 8.6 | 8.1 | 4 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 24.5 | 16.1 | 10.5 | 10.8 | 10.6 | 1 |
| sword-native | 23.2 | 12.9 | 9.1 | 9.3 | 9.7 | 1 |
| c-serial | 11.0 |  |  |  |  | 1 |
| c-omp | 20.7 | 13.9 | 10.6 | 10.8 | 9.8 | 4 |
| c-fastmath-serial | 10.3 |  |  |  |  | 1 |
| c-fastmath-omp | 12.7 | 9.1 | 7.2 | 8.0 | 7.4 | 5 |
| c-nofma-serial | 11.2 |  |  |  |  | 1 |
| c-nofma-omp | 21.5 | 13.9 | 10.9 | 10.5 | 10.2 | 4 |
| c-native-serial | 10.4 |  |  |  |  | 1 |
| c-native-omp | 20.8 | 14.4 | 11.1 | 10.8 | 10.2 | 4 |
| c-clang-serial | 10.8 |  |  |  |  | 1 |
| c-clang-omp | 21.4 | 13.9 | 11.5 | 10.4 | 9.9 | 4 |
| cpp-thread | 21.9 | 14.3 | 12.2 | 11.3 | 10.6 | 4 |
| rust-rayon | 21.8 | 14.5 | 14.1 | 13.6 | 10.2 | 4 |
| zig-safe | 24.5 | 15.1 | 14.0 | 12.7 | 14.1 | 4 |
| zig-fast | 23.9 | 14.8 | 13.5 | 13.1 | 11.4 | 4 |
| go | 22.7 | 13.6 | 10.9 | 10.3 | 10.1 | 4 |

## sort

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 170.7 | 87.8 | 47.2 | 49.9 | 51.8 | 1 |
| sword-native | 169.8 | 87.5 | 47.1 | 50.5 | 50.7 | 1 |
| c-serial | 63.8 |  |  |  |  | 1 |
| c-omp | 63.9 | 32.5 | 17.1 | 19.3 | 19.6 | 1 |
| c-fastmath-serial | 63.7 |  |  |  |  | 1 |
| c-fastmath-omp | 63.7 | 32.2 | 16.8 | 18.6 | 19.2 | 1 |
| c-nofma-serial | 64.1 |  |  |  |  | 1 |
| c-nofma-omp | 64.0 | 32.6 | 17.1 | 19.0 | 19.4 | 1 |
| c-native-serial | 63.4 |  |  |  |  | 1 |
| c-native-omp | 63.1 | 31.9 | 16.9 | 19.2 | 18.3 | 1 |
| c-clang-serial | 66.8 |  |  |  |  | 1 |
| c-clang-omp | 75.7 | 35.3 | 20.1 | 28.0 | 29.5 | 1 |
| c-stable | 51.7 |  |  |  |  | 1 |
| c-stable-omp | 51.7 | 26.5 | 14.8 | 16.4 | 16.0 | 1 |
| c-symmerge | 127.8 |  |  |  |  | 1 |
| c-symmerge-omp | 127.4 | 66.1 | 36.9 | 40.9 | 41.0 | 1 |
| cpp-thread | 28.4 | 14.9 | 8.8 | 10.5 | 11.4 | 5 |
| rust-rayon | 11.7 | 6.5 | 4.0 | 4.1 | 4.2 | 1 |
| zig-safe | 15.1 | 9.3 | 6.7 | 8.1 | 9.9 | 5 |
| zig-fast | 9.4 | 6.1 | 4.6 | 5.9 | 7.3 | 5 |
| go | 58.5 | 33.8 | 18.8 | 20.6 | 21.6 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 265.4 | 135.6 | 98.1 | 99.9 | 102.4 | 1 |
| sword-native | 257.5 | 131.5 | 94.7 | 97.1 | 99.8 | 1 |
| c-serial | 109.7 |  |  |  |  | 1 |
| c-omp | 109.8 | 55.1 | 36.6 | 37.8 | 37.7 | 1 |
| c-fastmath-serial | 110.1 |  |  |  |  | 1 |
| c-fastmath-omp | 110.5 | 55.2 | 36.5 | 36.7 | 36.5 | 1 |
| c-nofma-serial | 110.3 |  |  |  |  | 1 |
| c-nofma-omp | 110.1 | 55.1 | 36.6 | 36.9 | 37.3 | 1 |
| c-native-serial | 109.4 |  |  |  |  | 1 |
| c-native-omp | 109.9 | 55.0 | 36.4 | 37.7 | 38.2 | 1 |
| c-clang-serial | 116.5 |  |  |  |  | 1 |
| c-clang-omp | 116.2 | 60.3 | 39.6 | 44.8 | 48.1 | 1 |
| c-stable | 87.6 |  |  |  |  | 1 |
| c-stable-omp | 87.4 | 44.6 | 30.1 | 31.6 | 32.9 | 1 |
| c-symmerge | 196.7 |  |  |  |  | 1 |
| c-symmerge-omp | 196.8 | 101.0 | 74.6 | 76.1 | 77.3 | 1 |
| cpp-thread | 49.9 | 26.3 | 19.2 | 21.8 | 22.6 | 5 |
| rust-rayon | 8.8 | 4.8 | 4.2 | 4.3 | 4.4 | 1 |
| zig-safe | 17.0 | 10.9 | 10.9 | 13.5 | 15.5 | 5 |
| zig-fast | 11.1 | 9.5 | 10.6 | 12.9 | 16.2 | 5 |
| go | 86.2 | 49.2 | 34.0 | 36.8 | 37.4 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 195.0 | 117.0 | 86.2 | 86.4 | 86.6 | 1 |
| sword-native | 218.4 | 130.1 | 95.5 | 93.8 | 94.7 | 1 |
| c-serial | 45.5 |  |  |  |  | 1 |
| c-omp | 45.7 | 31.5 | 24.6 | 26.1 | 28.2 | 5 |
| c-fastmath-serial | 47.9 |  |  |  |  | 1 |
| c-fastmath-omp | 48.5 | 32.9 | 28.1 | 29.0 | 31.3 | 5 |
| c-nofma-serial | 46.8 |  |  |  |  | 1 |
| c-nofma-omp | 46.5 | 32.3 | 34.0 | 33.0 | 31.3 | 5 |
| c-native-serial | 44.9 |  |  |  |  | 1 |
| c-native-omp | 43.2 | 28.5 | 26.0 | 25.5 | 28.1 | 5 |
| c-clang-serial | 43.8 |  |  |  |  | 1 |
| c-clang-omp | 44.3 | 29.4 | 23.7 | 26.7 | 27.0 | 5 |
| c-stable | 70.5 |  |  |  |  | 1 |
| c-stable-omp | 70.7 | 42.0 | 32.8 | 32.4 | 33.2 | 1 |
| c-symmerge | 167.9 |  |  |  |  | 1 |
| c-symmerge-omp | 162.9 | 96.1 | 70.6 | 71.6 | 71.1 | 1 |
| cpp-thread | 32.7 | 21.9 | 18.8 | 20.0 | 22.1 | 5 |
| rust-rayon | 11.3 | 7.8 | 6.3 | 6.4 | 6.1 | 1 |
| zig-safe | 15.5 | 13.3 | 11.9 | 13.0 | 13.7 | 5 |
| zig-fast | 10.3 | 11.4 | 11.8 | 13.6 | 15.6 | 5 |
| go | 68.1 | 41.9 | 33.9 | 35.6 | 36.1 | 5 |

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
| c-omp | 7 | 1 | 1 | 1 | 1 | 21 | 4 | 6 |
| c-lanes | 1 |  |  |  |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 | 1 | 1 | 2 |
| c-fastmath-omp | 13 | 1 | 2 | 2 | 1 | 21 | 8 | 6 |
| c-nofma-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-nofma-omp | 7 | 1 | 1 | 1 | 1 | 23 | 4 | 6 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-native-omp | 7 | 1 | 1 | 1 | 1 | 23 | 4 | 6 |
| c-native-lanes | 1 |  |  |  |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 | 10 | 4 | 6 |
| c-stable |  |  |  |  |  |  |  | 1 |
| c-stable-omp |  |  |  |  |  |  |  | 1 |
| c-symmerge |  |  |  |  |  |  |  | 1 |
| c-symmerge-omp |  |  |  |  |  |  |  | 1 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 10 |
| rust-rayon | 24 | 1 | 1 | 1 | 1 | 30 | 4 | 1 |
| rust-slices |  |  | 1 |  |  |  |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| zig-fast | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| go | 5 | 1 | 1 | 2 | 1 | 5 | 4 | 5 |
