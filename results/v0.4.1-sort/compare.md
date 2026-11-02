## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.6 | 1.3 | 0.6 | 1.1 | 0.7 | 1 |
| sword-native | 2.4 | 1.3 | 0.7 | 0.8 | 0.9 | 1 |
| sword-without-walked | 4.1 | 2.1 | 1.0 | 1.2 | 1.4 | 1 |
| sword-without-walked-mut | 2.5 | 1.3 | 0.6 | 0.9 | 0.9 | 1 |
| sword-without-captures | 2.4 | 1.2 | 0.6 | 0.8 | 0.8 | 1 |
| sword-without-versioned | 2.5 | 1.3 | 0.6 | 0.9 | 0.9 | 1 |
| sword-without-split | 2.6 | 1.2 | 0.6 | 0.8 | 0.8 | 1 |
| sword-without-deferred | 2.3 | 1.2 | 0.6 | 0.9 | 0.8 | 1 |
| sword-without-lanes | 6.3 | 3.2 | 1.6 | 1.8 | 2.2 | 1 |
| sword-without-steady | 2.4 | 1.3 | 0.7 | 0.9 | 0.8 | 1 |
| c-serial | 6.5 |  |  |  |  | 1 |
| c-restrict | 6.4 |  |  |  |  | 1 |
| c-omp | 6.3 | 3.2 | 1.6 | 1.6 | 2.0 | 8 |
| c-lanes | 3.0 |  |  |  |  | 1 |
| c-lanes-omp | 3.0 | 1.5 | 0.7 | 1.1 | 1.0 | 1 |
| c-fastmath-serial | 6.5 |  |  |  |  | 1 |
| c-fastmath-omp | 6.4 | 3.4 | 1.6 | 2.0 | 2.1 | 6 |
| c-nofma-serial | 6.3 |  |  |  |  | 1 |
| c-nofma-omp | 6.4 | 3.2 | 1.6 | 2.0 | 2.0 | 7 |
| c-native-serial | 6.3 |  |  |  |  | 1 |
| c-native-omp | 6.3 | 3.2 | 1.6 | 1.9 | 2.1 | 8 |
| c-native-lanes | 3.1 |  |  |  |  | 1 |
| c-native-lanes-omp | 3.2 | 1.5 | 0.8 | 1.2 | 1.0 | 1 |
| c-clang-serial | 6.3 |  |  |  |  | 1 |
| c-clang-omp | 6.3 | 3.2 | 1.6 | 2.5 | 2.1 | 5 |
| cpp-thread | 6.9 | 3.4 | 1.7 | 2.1 | 2.3 | 5 |
| rust-rayon | 6.5 | 3.2 | 1.6 | 1.6 | 1.7 | 10 |
| zig-safe | 6.6 | 3.4 | 2.2 | 2.6 | 2.7 | 5 |
| zig-fast | 6.8 | 3.5 | 2.0 | 2.7 | 2.7 | 5 |
| go | 6.4 | 3.3 | 1.7 | 1.7 | 2.1 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.6 | 2.2 | 1.9 | 1.9 | 1.9 | 1 |
| sword-native | 3.3 | 1.9 | 1.8 | 2.0 | 2.1 | 1 |
| sword-without-walked | 4.8 | 2.7 | 2.0 | 2.0 | 2.1 | 1 |
| sword-without-walked-mut | 3.6 | 2.1 | 1.8 | 1.8 | 1.9 | 1 |
| sword-without-captures | 4.1 | 2.3 | 2.0 | 2.3 | 2.0 | 1 |
| sword-without-versioned | 3.7 | 2.1 | 2.0 | 2.0 | 2.1 | 1 |
| sword-without-split | 3.7 | 2.4 | 2.1 | 1.9 | 1.9 | 1 |
| sword-without-deferred | 3.8 | 2.3 | 1.8 | 2.1 | 1.9 | 1 |
| sword-without-lanes | 9.5 | 4.8 | 2.5 | 2.7 | 2.8 | 1 |
| sword-without-steady | 3.6 | 2.1 | 2.1 | 1.9 | 2.2 | 1 |
| c-serial | 9.5 |  |  |  |  | 1 |
| c-restrict | 9.5 |  |  |  |  | 1 |
| c-omp | 9.6 | 4.8 | 2.5 | 3.0 | 3.1 | 8 |
| c-lanes | 4.0 |  |  |  |  | 1 |
| c-lanes-omp | 4.1 | 2.3 | 2.0 | 2.2 | 2.2 | 1 |
| c-fastmath-serial | 3.7 |  |  |  |  | 1 |
| c-fastmath-omp | 9.5 | 4.8 | 2.5 | 3.7 | 3.3 | 8 |
| c-nofma-serial | 9.6 |  |  |  |  | 1 |
| c-nofma-omp | 9.6 | 4.8 | 2.8 | 3.7 | 3.3 | 5 |
| c-native-serial | 9.5 |  |  |  |  | 1 |
| c-native-omp | 9.6 | 4.8 | 2.5 | 2.5 | 3.2 | 6 |
| c-native-lanes | 4.1 |  |  |  |  | 1 |
| c-native-lanes-omp | 4.1 | 2.5 | 2.0 | 2.1 | 2.2 | 1 |
| c-clang-serial | 9.5 |  |  |  |  | 1 |
| c-clang-omp | 9.6 | 4.8 | 2.7 | 3.8 | 3.2 | 5 |
| cpp-thread | 9.7 | 4.9 | 2.6 | 3.9 | 4.0 | 5 |
| rust-rayon | 9.5 | 4.8 | 2.5 | 2.5 | 2.6 | 10 |
| zig-safe | 9.8 | 5.2 | 3.2 | 4.0 | 4.4 | 5 |
| zig-fast | 9.8 | 5.2 | 3.2 | 4.1 | 4.5 | 5 |
| go | 9.6 | 5.0 | 3.4 | 3.5 | 3.5 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.2 | 2.4 | 1.9 | 1.7 | 1.7 | 1 |
| sword-native | 2.0 | 2.2 | 1.8 | 1.8 | 1.9 | 1 |
| sword-without-walked | 3.8 | 2.7 | 2.1 | 2.1 | 2.3 | 1 |
| sword-without-walked-mut | 2.3 | 2.0 | 1.5 | 2.1 | 1.7 | 1 |
| sword-without-captures | 2.0 | 2.1 | 2.0 | 1.8 | 1.8 | 1 |
| sword-without-versioned | 1.9 | 2.0 | 1.7 | 1.7 | 1.8 | 1 |
| sword-without-split | 1.8 | 1.8 | 1.8 | 1.7 | 1.9 | 1 |
| sword-without-deferred | 2.3 | 2.0 | 1.6 | 1.8 | 1.7 | 1 |
| sword-without-lanes | 11.2 | 5.6 | 5.2 | 5.6 | 4.7 | 1 |
| sword-without-steady | 2.0 | 2.3 | 2.0 | 1.9 | 1.6 | 1 |
| c-serial | 12.0 |  |  |  |  | 1 |
| c-restrict | 11.5 |  |  |  |  | 1 |
| c-omp | 10.6 | 5.4 | 5.4 | 4.7 | 4.3 | 5 |
| c-lanes | 1.8 |  |  |  |  | 1 |
| c-lanes-omp | 2.1 | 2.7 | 1.7 | 1.9 | 1.7 | 1 |
| c-fastmath-serial | 2.0 |  |  |  |  | 1 |
| c-fastmath-omp | 1.9 | 1.9 | 1.6 | 1.6 | 2.1 | 5 |
| c-nofma-serial | 12.8 |  |  |  |  | 1 |
| c-nofma-omp | 11.1 | 6.2 | 5.9 | 5.3 | 5.1 | 5 |
| c-native-serial | 10.1 |  |  |  |  | 1 |
| c-native-omp | 10.3 | 6.1 | 5.5 | 4.7 | 4.9 | 5 |
| c-native-lanes | 1.8 |  |  |  |  | 1 |
| c-native-lanes-omp | 1.8 | 1.7 | 1.8 | 1.6 | 2.4 | 1 |
| c-clang-serial | 10.9 |  |  |  |  | 1 |
| c-clang-omp | 11.5 | 6.8 | 5.6 | 5.0 | 4.3 | 5 |
| cpp-thread | 11.1 | 6.2 | 5.4 | 5.2 | 5.3 | 5 |
| rust-rayon | 10.8 | 6.7 | 4.2 | 4.1 | 4.4 | 10 |
| zig-safe | 11.0 | 6.9 | 5.6 | 5.4 | 5.1 | 5 |
| zig-fast | 11.0 | 5.6 | 5.8 | 4.5 | 4.6 | 5 |
| go | 12.2 | 6.1 | 4.9 | 4.5 | 4.1 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.2 | 3.3 | 1.7 | 1.7 | 1.9 | 1 |
| sword-native | 6.2 | 3.2 | 1.8 | 1.8 | 1.8 | 1 |
| sword-without-walked | 6.3 | 3.3 | 1.7 | 1.7 | 2.0 | 1 |
| sword-without-walked-mut | 6.2 | 3.2 | 1.8 | 1.8 | 2.0 | 1 |
| sword-without-captures | 11.9 | 6.4 | 3.3 | 3.4 | 3.6 | 1 |
| sword-without-versioned | 6.2 | 3.4 | 1.8 | 1.7 | 2.0 | 1 |
| sword-without-split | 6.1 | 3.2 | 1.7 | 1.8 | 1.9 | 1 |
| sword-without-deferred | 6.3 | 3.2 | 1.8 | 1.9 | 1.9 | 1 |
| sword-without-lanes | 6.1 | 3.1 | 1.7 | 1.7 | 1.9 | 1 |
| sword-without-steady | 5.9 | 3.2 | 1.7 | 1.7 | 1.8 | 1 |
| c-serial | 5.9 |  |  |  |  | 1 |
| c-restrict | 5.9 |  |  |  |  | 1 |
| c-omp | 6.1 | 3.4 | 1.9 | 2.8 | 2.4 | 1 |
| c-fastmath-serial | 6.2 |  |  |  |  | 1 |
| c-fastmath-omp | 6.1 | 3.4 | 1.9 | 2.7 | 2.3 | 1 |
| c-nofma-serial | 5.9 |  |  |  |  | 1 |
| c-nofma-omp | 6.5 | 3.6 | 1.9 | 2.9 | 2.4 | 1 |
| c-native-serial | 6.1 |  |  |  |  | 1 |
| c-native-omp | 6.1 | 3.4 | 1.8 | 2.6 | 2.2 | 1 |
| c-clang-serial | 6.2 |  |  |  |  | 1 |
| c-clang-omp | 6.1 | 3.2 | 1.7 | 2.4 | 2.5 | 1 |
| cpp-thread | 7.0 | 3.9 | 2.2 | 2.2 | 2.6 | 1 |
| rust-rayon | 6.4 | 3.3 | 1.7 | 1.8 | 2.1 | 1 |
| zig-safe | 11.6 | 5.9 | 3.3 | 4.1 | 4.4 | 1 |
| zig-fast | 9.2 | 4.9 | 2.7 | 3.6 | 3.6 | 1 |
| go | 7.4 | 3.8 | 2.1 | 2.2 | 2.1 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.4 | 5.3 | 5.1 | 5.3 | 5.5 | 1 |
| sword-native | 6.1 | 5.1 | 5.3 | 5.2 | 5.2 | 1 |
| sword-without-walked | 6.6 | 5.1 | 5.1 | 5.2 | 5.2 | 1 |
| sword-without-walked-mut | 6.6 | 5.3 | 5.0 | 5.2 | 5.1 | 1 |
| sword-without-captures | 9.0 | 5.5 | 5.2 | 5.2 | 5.3 | 1 |
| sword-without-versioned | 6.7 | 5.3 | 5.2 | 5.2 | 5.1 | 1 |
| sword-without-split | 6.5 | 5.1 | 5.2 | 5.0 | 5.0 | 1 |
| sword-without-deferred | 6.9 | 5.2 | 5.2 | 5.1 | 5.2 | 1 |
| sword-without-lanes | 6.4 | 5.1 | 5.2 | 5.2 | 5.1 | 1 |
| sword-without-steady | 6.6 | 5.2 | 5.2 | 5.3 | 5.2 | 1 |
| c-serial | 6.7 |  |  |  |  | 1 |
| c-restrict | 6.5 |  |  |  |  | 1 |
| c-omp | 7.6 | 5.3 | 5.3 | 5.4 | 5.4 | 1 |
| c-fastmath-serial | 6.4 |  |  |  |  | 1 |
| c-fastmath-omp | 7.6 | 5.4 | 4.9 | 5.2 | 5.5 | 1 |
| c-nofma-serial | 6.3 |  |  |  |  | 1 |
| c-nofma-omp | 7.4 | 5.4 | 5.2 | 5.2 | 5.4 | 1 |
| c-native-serial | 6.5 |  |  |  |  | 1 |
| c-native-omp | 7.3 | 5.3 | 5.4 | 5.5 | 5.6 | 1 |
| c-clang-serial | 6.5 |  |  |  |  | 1 |
| c-clang-omp | 6.6 | 5.1 | 5.3 | 5.4 | 5.5 | 1 |
| cpp-thread | 7.7 | 5.4 | 5.3 | 5.5 | 5.9 | 1 |
| rust-rayon | 6.8 | 5.4 | 5.4 | 5.5 | 5.7 | 1 |
| zig-safe | 11.3 | 6.3 | 6.0 | 6.6 | 7.0 | 1 |
| zig-fast | 9.1 | 6.1 | 5.8 | 6.2 | 6.1 | 1 |
| go | 7.9 | 5.5 | 5.4 | 5.4 | 5.3 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.1 | 4.7 | 4.7 | 4.5 | 5.1 | 1 |
| sword-native | 6.2 | 5.3 | 4.7 | 5.2 | 5.1 | 1 |
| sword-without-walked | 5.5 | 5.2 | 5.3 | 5.4 | 4.8 | 1 |
| sword-without-walked-mut | 6.1 | 5.4 | 5.1 | 4.9 | 5.2 | 1 |
| sword-without-captures | 9.5 | 6.6 | 5.3 | 5.3 | 5.3 | 1 |
| sword-without-versioned | 6.5 | 4.9 | 5.0 | 5.0 | 4.7 | 1 |
| sword-without-split | 5.6 | 5.0 | 4.8 | 4.8 | 5.1 | 1 |
| sword-without-deferred | 6.0 | 5.2 | 4.8 | 4.9 | 5.1 | 1 |
| sword-without-lanes | 5.4 | 4.9 | 5.1 | 5.1 | 5.2 | 1 |
| sword-without-steady | 6.0 | 5.3 | 5.3 | 4.8 | 4.9 | 1 |
| c-serial | 5.7 |  |  |  |  | 1 |
| c-restrict | 5.8 |  |  |  |  | 1 |
| c-omp | 5.6 | 5.3 | 5.3 | 5.3 | 5.4 | 1 |
| c-fastmath-serial | 5.0 |  |  |  |  | 1 |
| c-fastmath-omp | 6.9 | 5.0 | 5.6 | 4.7 | 4.6 | 1 |
| c-nofma-serial | 5.2 |  |  |  |  | 1 |
| c-nofma-omp | 5.1 | 5.5 | 4.7 | 5.3 | 4.6 | 1 |
| c-native-serial | 5.1 |  |  |  |  | 1 |
| c-native-omp | 4.9 | 5.2 | 4.6 | 4.6 | 4.6 | 1 |
| c-clang-serial | 6.5 |  |  |  |  | 1 |
| c-clang-omp | 6.5 | 5.2 | 4.8 | 5.4 | 5.0 | 1 |
| cpp-thread | 5.2 | 5.1 | 4.9 | 5.1 | 5.1 | 1 |
| rust-rayon | 6.2 | 5.2 | 4.8 | 4.9 | 6.1 | 1 |
| zig-safe | 12.3 | 7.7 | 7.2 | 6.6 | 6.3 | 1 |
| zig-fast | 11.3 | 5.6 | 5.8 | 5.1 | 5.9 | 1 |
| go | 8.2 | 5.2 | 5.8 | 5.1 | 4.8 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 76.5 | 38.6 | 19.4 | 22.7 | 24.9 | 1 |
| sword-native | 62.3 | 31.4 | 15.7 | 19.8 | 20.3 | 1 |
| sword-without-walked | 76.8 | 38.4 | 19.4 | 23.8 | 24.2 | 1 |
| sword-without-walked-mut | 77.4 | 38.9 | 19.6 | 23.1 | 25.1 | 1 |
| sword-without-captures | 86.3 | 43.3 | 21.8 | 25.9 | 27.7 | 1 |
| sword-without-versioned | 76.7 | 39.0 | 19.4 | 22.2 | 25.2 | 1 |
| sword-without-split | 89.5 | 44.9 | 22.6 | 26.6 | 27.3 | 1 |
| sword-without-deferred | 76.5 | 38.9 | 19.4 | 24.2 | 24.0 | 1 |
| sword-without-lanes | 76.5 | 38.8 | 19.3 | 22.1 | 25.1 | 1 |
| sword-without-steady | 76.7 | 39.0 | 19.4 | 23.1 | 24.0 | 1 |
| sword-rows | 20.8 | 11.1 | 5.5 | 7.2 | 8.2 | 1 |
| sword-rows-without-steady | 21.3 | 11.3 | 5.6 | 9.0 | 8.0 | 1 |
| c-serial | 52.1 |  |  |  |  | 1 |
| c-restrict | 52.2 |  |  |  |  | 1 |
| c-omp | 49.8 | 24.4 | 12.2 | 16.5 | 14.4 | 1 |
| c-fastmath-serial | 52.4 |  |  |  |  | 1 |
| c-fastmath-omp | 49.7 | 24.5 | 12.3 | 16.3 | 14.5 | 1 |
| c-nofma-serial | 53.0 |  |  |  |  | 1 |
| c-nofma-omp | 49.5 | 24.5 | 12.2 | 15.2 | 14.3 | 1 |
| c-native-serial | 40.7 |  |  |  |  | 1 |
| c-native-omp | 40.2 | 20.0 | 10.0 | 13.2 | 11.7 | 1 |
| c-clang-serial | 46.2 |  |  |  |  | 1 |
| c-clang-omp | 48.7 | 24.2 | 12.4 | 17.9 | 16.8 | 1 |
| cpp-thread | 54.8 | 27.3 | 14.8 | 18.5 | 19.6 | 1 |
| rust-rayon | 90.9 | 45.5 | 23.0 | 23.1 | 23.4 | 1 |
| rust-slices | 20.6 | 10.2 | 5.2 | 5.4 | 5.9 | 1 |
| zig-safe | 93.2 | 47.6 | 27.0 | 33.7 | 35.2 | 1 |
| zig-fast | 41.1 | 21.7 | 13.6 | 17.8 | 20.5 | 1 |
| go | 77.1 | 38.7 | 19.6 | 22.5 | 21.7 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 87.8 | 44.3 | 40.3 | 41.5 | 42.5 | 1 |
| sword-native | 83.2 | 42.3 | 40.1 | 41.5 | 42.3 | 1 |
| sword-without-walked | 88.4 | 44.6 | 41.1 | 41.1 | 42.4 | 1 |
| sword-without-walked-mut | 87.0 | 42.7 | 40.1 | 41.7 | 42.6 | 1 |
| sword-without-captures | 90.3 | 46.4 | 43.6 | 44.6 | 45.6 | 1 |
| sword-without-versioned | 88.0 | 45.1 | 40.1 | 42.2 | 42.3 | 1 |
| sword-without-split | 97.8 | 51.2 | 47.6 | 49.9 | 50.1 | 1 |
| sword-without-deferred | 87.7 | 46.0 | 40.3 | 41.7 | 42.6 | 1 |
| sword-without-lanes | 86.9 | 44.7 | 41.5 | 42.2 | 43.0 | 1 |
| sword-without-steady | 87.8 | 44.1 | 40.9 | 41.0 | 42.4 | 1 |
| sword-rows | 34.3 | 23.5 | 19.6 | 20.7 | 21.3 | 1 |
| sword-rows-without-steady | 36.1 | 22.1 | 20.2 | 19.8 | 21.8 | 1 |
| c-serial | 41.5 |  |  |  |  | 1 |
| c-restrict | 41.0 |  |  |  |  | 1 |
| c-omp | 44.0 | 24.2 | 21.3 | 22.5 | 24.0 | 1 |
| c-fastmath-serial | 50.9 |  |  |  |  | 1 |
| c-fastmath-omp | 45.9 | 29.8 | 24.9 | 25.4 | 25.7 | 1 |
| c-nofma-serial | 41.4 |  |  |  |  | 1 |
| c-nofma-omp | 40.9 | 20.8 | 21.7 | 20.1 | 20.5 | 1 |
| c-native-serial | 38.2 |  |  |  |  | 1 |
| c-native-omp | 46.3 | 21.6 | 21.4 | 22.3 | 22.3 | 1 |
| c-clang-serial | 62.2 |  |  |  |  | 1 |
| c-clang-omp | 48.8 | 26.9 | 23.3 | 30.9 | 29.5 | 1 |
| cpp-thread | 50.1 | 26.7 | 24.7 | 30.8 | 28.3 | 1 |
| rust-rayon | 109.4 | 54.9 | 48.3 | 49.7 | 49.5 | 1 |
| rust-slices | 32.8 | 20.3 | 18.1 | 16.9 | 16.9 | 1 |
| zig-safe | 83.6 | 44.7 | 45.4 | 55.4 | 57.2 | 1 |
| zig-fast | 44.1 | 25.4 | 25.3 | 30.3 | 37.6 | 1 |
| go | 92.3 | 48.2 | 42.6 | 42.2 | 42.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 39.6 | 23.6 | 22.8 | 19.2 | 22.2 | 1 |
| sword-native | 53.3 | 26.5 | 18.4 | 19.9 | 17.8 | 1 |
| sword-without-walked | 42.1 | 24.1 | 19.7 | 23.1 | 25.2 | 1 |
| sword-without-walked-mut | 52.9 | 29.8 | 23.1 | 20.4 | 18.8 | 1 |
| sword-without-captures | 77.2 | 46.9 | 26.7 | 27.0 | 27.3 | 1 |
| sword-without-versioned | 44.2 | 27.4 | 17.1 | 20.4 | 22.7 | 1 |
| sword-without-split | 77.6 | 44.0 | 35.7 | 35.6 | 36.5 | 1 |
| sword-without-deferred | 44.0 | 26.1 | 19.4 | 19.0 | 19.0 | 1 |
| sword-without-lanes | 53.0 | 34.6 | 18.9 | 21.0 | 18.3 | 1 |
| sword-without-steady | 47.6 | 26.9 | 24.3 | 22.2 | 20.4 | 1 |
| sword-rows | 31.5 | 21.2 | 16.6 | 16.2 | 18.6 | 1 |
| sword-rows-without-steady | 30.1 | 19.0 | 16.5 | 17.0 | 17.7 | 1 |
| c-serial | 47.7 |  |  |  |  | 1 |
| c-restrict | 49.6 |  |  |  |  | 1 |
| c-omp | 42.8 | 29.7 | 26.8 | 24.0 | 18.1 | 1 |
| c-fastmath-serial | 43.0 |  |  |  |  | 1 |
| c-fastmath-omp | 43.0 | 34.4 | 31.0 | 27.5 | 26.5 | 1 |
| c-nofma-serial | 44.7 |  |  |  |  | 1 |
| c-nofma-omp | 42.6 | 25.8 | 22.3 | 17.0 | 19.8 | 1 |
| c-native-serial | 43.4 |  |  |  |  | 1 |
| c-native-omp | 41.6 | 22.7 | 21.4 | 18.3 | 18.8 | 1 |
| c-clang-serial | 45.5 |  |  |  |  | 1 |
| c-clang-omp | 45.1 | 21.7 | 26.5 | 27.1 | 22.2 | 1 |
| cpp-thread | 41.5 | 27.1 | 26.6 | 20.3 | 17.6 | 1 |
| rust-rayon | 84.0 | 43.5 | 31.9 | 31.3 | 32.1 | 1 |
| rust-slices | 28.1 | 18.7 | 21.8 | 22.3 | 25.7 | 1 |
| zig-safe | 100.1 | 52.7 | 49.9 | 44.5 | 40.2 | 1 |
| zig-fast | 38.9 | 22.6 | 21.3 | 20.8 | 20.1 | 1 |
| go | 76.5 | 42.2 | 47.1 | 44.6 | 35.7 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.8 | 346.6 | 173.6 | 176.3 | 176.0 | 1 |
| sword-native | 683.9 | 342.1 | 171.4 | 174.6 | 173.8 | 1 |
| sword-without-walked | 692.3 | 346.3 | 173.5 | 174.9 | 175.3 | 1 |
| sword-without-walked-mut | 692.7 | 346.6 | 173.6 | 177.0 | 176.0 | 1 |
| sword-without-captures | 692.6 | 346.5 | 173.7 | 176.2 | 176.0 | 1 |
| sword-without-versioned | 692.8 | 346.6 | 173.7 | 176.3 | 176.5 | 1 |
| sword-without-split | 692.7 | 346.5 | 173.8 | 175.8 | 176.4 | 1 |
| sword-without-deferred | 692.7 | 346.5 | 173.9 | 176.8 | 176.4 | 1 |
| sword-without-lanes | 692.7 | 346.5 | 173.8 | 177.1 | 176.6 | 1 |
| sword-without-steady | 692.6 | 346.5 | 173.7 | 176.0 | 176.5 | 1 |
| c-serial | 646.3 |  |  |  |  | 1 |
| c-restrict | 648.5 |  |  |  |  | 1 |
| c-omp | 641.6 | 320.2 | 160.2 | 160.0 | 159.8 | 1 |
| c-fastmath-serial | 628.3 |  |  |  |  | 1 |
| c-fastmath-omp | 629.2 | 314.7 | 157.7 | 157.7 | 157.7 | 1 |
| c-nofma-serial | 697.4 |  |  |  |  | 1 |
| c-nofma-omp | 697.2 | 348.7 | 174.6 | 174.7 | 174.8 | 1 |
| c-native-serial | 649.4 |  |  |  |  | 1 |
| c-native-omp | 657.1 | 328.0 | 164.1 | 163.7 | 163.8 | 1 |
| c-clang-serial | 770.2 |  |  |  |  | 1 |
| c-clang-omp | 769.9 | 385.5 | 193.6 | 193.6 | 193.6 | 1 |
| cpp-thread | 854.0 | 427.2 | 214.3 | 235.0 | 218.2 | 1 |
| rust-rayon | 693.0 | 347.1 | 173.9 | 174.0 | 174.1 | 1 |
| zig-safe | 684.2 | 341.7 | 172.0 | 183.4 | 175.7 | 1 |
| zig-fast | 897.0 | 448.9 | 225.2 | 240.3 | 229.1 | 1 |
| go | 678.1 | 339.2 | 170.3 | 176.7 | 173.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 838.2 | 419.7 | 230.9 | 232.7 | 234.1 | 1 |
| sword-native | 830.4 | 415.8 | 224.8 | 227.0 | 228.2 | 1 |
| sword-without-walked | 838.6 | 419.9 | 230.8 | 233.0 | 233.4 | 1 |
| sword-without-walked-mut | 838.8 | 419.9 | 230.9 | 233.4 | 234.2 | 1 |
| sword-without-captures | 838.5 | 419.9 | 231.0 | 234.2 | 233.7 | 1 |
| sword-without-versioned | 838.5 | 419.7 | 230.8 | 233.4 | 233.8 | 1 |
| sword-without-split | 838.5 | 419.9 | 230.9 | 233.3 | 234.1 | 1 |
| sword-without-deferred | 838.5 | 419.9 | 230.9 | 233.8 | 233.6 | 1 |
| sword-without-lanes | 838.2 | 419.6 | 230.8 | 234.6 | 235.1 | 1 |
| sword-without-steady | 838.7 | 419.9 | 230.9 | 232.0 | 233.7 | 1 |
| c-serial | 798.4 |  |  |  |  | 1 |
| c-restrict | 798.2 |  |  |  |  | 1 |
| c-omp | 798.4 | 399.7 | 212.0 | 212.2 | 212.5 | 1 |
| c-fastmath-serial | 793.9 |  |  |  |  | 1 |
| c-fastmath-omp | 794.7 | 397.6 | 213.1 | 213.2 | 213.2 | 1 |
| c-nofma-serial | 831.1 |  |  |  |  | 1 |
| c-nofma-omp | 833.9 | 417.5 | 226.4 | 226.9 | 226.7 | 1 |
| c-native-serial | 798.5 |  |  |  |  | 1 |
| c-native-omp | 798.6 | 399.8 | 212.4 | 212.2 | 212.3 | 1 |
| c-clang-serial | 823.6 |  |  |  |  | 1 |
| c-clang-omp | 824.2 | 413.2 | 225.4 | 225.9 | 225.8 | 1 |
| cpp-thread | 798.8 | 400.3 | 212.2 | 226.9 | 219.3 | 1 |
| rust-rayon | 829.9 | 415.8 | 227.2 | 227.1 | 227.5 | 1 |
| zig-safe | 835.4 | 418.7 | 227.2 | 247.4 | 231.3 | 1 |
| zig-fast | 832.9 | 418.0 | 226.1 | 248.0 | 230.8 | 1 |
| go | 827.4 | 414.4 | 224.6 | 232.4 | 228.3 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1035.5 | 523.2 | 358.3 | 401.3 | 368.3 | 1 |
| sword-native | 1000.8 | 538.2 | 394.2 | 365.6 | 368.2 | 1 |
| sword-without-walked | 985.8 | 518.0 | 363.2 | 356.9 | 374.0 | 1 |
| sword-without-walked-mut | 969.7 | 523.7 | 338.8 | 361.2 | 346.8 | 1 |
| sword-without-captures | 1081.3 | 514.4 | 329.0 | 354.4 | 352.5 | 1 |
| sword-without-versioned | 1047.5 | 557.9 | 328.8 | 370.0 | 378.5 | 1 |
| sword-without-split | 1121.6 | 483.7 | 326.1 | 330.4 | 338.8 | 1 |
| sword-without-deferred | 1018.1 | 486.1 | 323.9 | 363.7 | 329.4 | 1 |
| sword-without-lanes | 1047.6 | 484.3 | 376.1 | 341.1 | 383.5 | 1 |
| sword-without-steady | 980.7 | 503.4 | 373.6 | 370.3 | 365.0 | 1 |
| c-serial | 836.4 |  |  |  |  | 1 |
| c-restrict | 877.0 |  |  |  |  | 1 |
| c-omp | 841.7 | 417.6 | 288.1 | 292.1 | 281.7 | 1 |
| c-fastmath-serial | 697.7 |  |  |  |  | 1 |
| c-fastmath-omp | 689.3 | 358.5 | 230.6 | 272.3 | 233.1 | 1 |
| c-nofma-serial | 994.9 |  |  |  |  | 1 |
| c-nofma-omp | 979.5 | 480.4 | 340.6 | 352.1 | 383.0 | 1 |
| c-native-serial | 1052.9 |  |  |  |  | 1 |
| c-native-omp | 1020.6 | 522.8 | 395.2 | 363.4 | 357.9 | 1 |
| c-clang-serial | 824.8 |  |  |  |  | 1 |
| c-clang-omp | 841.6 | 411.4 | 317.9 | 300.9 | 299.6 | 1 |
| cpp-thread | 940.9 | 474.7 | 353.7 | 323.8 | 323.6 | 1 |
| rust-rayon | 1014.9 | 577.1 | 403.1 | 411.6 | 408.3 | 1 |
| zig-safe | 1276.3 | 662.6 | 430.6 | 432.7 | 390.0 | 1 |
| zig-fast | 1183.5 | 491.0 | 406.6 | 369.5 | 367.6 | 1 |
| go | 1005.7 | 527.6 | 387.1 | 386.7 | 376.1 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 251.9 | 126.0 | 63.2 | 67.0 | 67.1 | 1 |
| sword-native | 246.9 | 123.6 | 62.2 | 65.2 | 68.2 | 1 |
| sword-without-walked | 251.3 | 125.9 | 63.1 | 65.7 | 68.5 | 1 |
| sword-without-walked-mut | 250.3 | 126.0 | 63.1 | 66.2 | 67.8 | 1 |
| sword-without-captures | 246.4 | 125.4 | 64.0 | 66.5 | 69.2 | 1 |
| sword-without-versioned | 270.5 | 135.5 | 68.3 | 71.0 | 70.5 | 1 |
| sword-without-split | 251.7 | 126.1 | 63.3 | 66.1 | 67.9 | 1 |
| sword-without-deferred | 251.9 | 126.2 | 63.2 | 65.8 | 66.9 | 1 |
| sword-without-lanes | 251.6 | 126.0 | 64.1 | 66.5 | 68.0 | 1 |
| sword-without-steady | 251.4 | 126.0 | 63.4 | 67.3 | 67.4 | 1 |
| c-serial | 237.7 |  |  |  |  | 1 |
| c-restrict | 237.6 |  |  |  |  | 1 |
| c-omp | 239.6 | 119.8 | 60.2 | 64.0 | 63.5 | 1 |
| c-fastmath-serial | 237.7 |  |  |  |  | 1 |
| c-fastmath-omp | 245.0 | 122.5 | 61.5 | 66.5 | 65.8 | 1 |
| c-nofma-serial | 242.4 |  |  |  |  | 1 |
| c-nofma-omp | 268.4 | 134.3 | 67.4 | 71.0 | 71.4 | 1 |
| c-native-serial | 248.6 |  |  |  |  | 1 |
| c-native-omp | 248.8 | 124.5 | 62.5 | 63.5 | 66.0 | 1 |
| c-clang-serial | 242.7 |  |  |  |  | 1 |
| c-clang-omp | 246.6 | 123.1 | 61.7 | 89.6 | 63.6 | 1 |
| cpp-thread | 240.3 | 120.3 | 61.1 | 69.5 | 71.1 | 1 |
| rust-rayon | 238.9 | 119.7 | 60.2 | 61.1 | 61.8 | 1 |
| zig-safe | 271.8 | 136.8 | 71.3 | 80.0 | 83.5 | 1 |
| zig-fast | 271.8 | 136.8 | 71.1 | 79.9 | 84.4 | 1 |
| go | 252.9 | 126.7 | 63.8 | 69.3 | 67.8 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 304.8 | 153.9 | 149.8 | 151.1 | 152.3 | 1 |
| sword-native | 302.6 | 151.8 | 149.8 | 150.3 | 151.6 | 1 |
| sword-without-walked | 304.2 | 152.7 | 149.8 | 150.4 | 152.4 | 1 |
| sword-without-walked-mut | 304.8 | 152.9 | 149.8 | 150.6 | 152.0 | 1 |
| sword-without-captures | 304.4 | 152.7 | 149.9 | 151.1 | 151.8 | 1 |
| sword-without-versioned | 311.9 | 157.0 | 153.0 | 153.3 | 154.4 | 1 |
| sword-without-split | 304.8 | 152.8 | 149.9 | 150.9 | 151.0 | 1 |
| sword-without-deferred | 304.9 | 153.0 | 149.8 | 150.1 | 151.6 | 1 |
| sword-without-lanes | 304.1 | 152.5 | 149.9 | 150.5 | 151.7 | 1 |
| sword-without-steady | 304.7 | 153.0 | 149.8 | 150.0 | 151.4 | 1 |
| c-serial | 73.5 |  |  |  |  | 1 |
| c-restrict | 73.6 |  |  |  |  | 1 |
| c-omp | 130.0 | 65.1 | 58.4 | 59.0 | 60.7 | 1 |
| c-fastmath-serial | 73.0 |  |  |  |  | 1 |
| c-fastmath-omp | 72.9 | 36.6 | 36.5 | 37.6 | 37.6 | 1 |
| c-nofma-serial | 75.0 |  |  |  |  | 1 |
| c-nofma-omp | 129.7 | 65.1 | 59.0 | 59.7 | 60.7 | 1 |
| c-native-serial | 73.7 |  |  |  |  | 1 |
| c-native-omp | 130.1 | 65.2 | 58.4 | 59.4 | 61.3 | 1 |
| c-clang-serial | 306.5 |  |  |  |  | 1 |
| c-clang-omp | 318.4 | 153.5 | 152.1 | 153.7 | 156.4 | 1 |
| cpp-thread | 130.8 | 66.1 | 59.6 | 66.3 | 65.7 | 1 |
| rust-rayon | 312.4 | 156.6 | 151.0 | 151.3 | 151.7 | 1 |
| zig-safe | 305.1 | 154.5 | 154.0 | 162.2 | 165.9 | 1 |
| zig-fast | 304.6 | 154.3 | 153.4 | 163.3 | 164.1 | 1 |
| go | 529.5 | 265.5 | 165.6 | 175.6 | 171.8 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 94.6 | 49.0 | 34.3 | 34.4 | 31.7 | 1 |
| sword-native | 100.2 | 55.9 | 33.0 | 30.7 | 30.1 | 1 |
| sword-without-walked | 99.8 | 54.9 | 45.2 | 37.6 | 38.2 | 1 |
| sword-without-walked-mut | 124.1 | 80.0 | 41.0 | 41.5 | 40.6 | 1 |
| sword-without-captures | 109.0 | 66.0 | 45.0 | 41.5 | 38.5 | 1 |
| sword-without-versioned | 168.6 | 92.3 | 71.4 | 71.3 | 62.1 | 1 |
| sword-without-split | 112.7 | 65.7 | 37.4 | 37.9 | 36.9 | 1 |
| sword-without-deferred | 105.9 | 55.8 | 34.8 | 36.4 | 40.9 | 1 |
| sword-without-lanes | 104.6 | 63.1 | 35.6 | 38.6 | 41.4 | 1 |
| sword-without-steady | 110.5 | 69.7 | 49.8 | 44.0 | 42.3 | 1 |
| c-serial | 104.3 |  |  |  |  | 1 |
| c-restrict | 105.0 |  |  |  |  | 1 |
| c-omp | 95.1 | 46.4 | 57.5 | 42.0 | 39.7 | 1 |
| c-fastmath-serial | 47.5 |  |  |  |  | 1 |
| c-fastmath-omp | 50.8 | 36.5 | 32.3 | 23.7 | 21.9 | 1 |
| c-nofma-serial | 107.1 |  |  |  |  | 1 |
| c-nofma-omp | 95.9 | 47.1 | 39.8 | 40.7 | 39.2 | 1 |
| c-native-serial | 91.5 |  |  |  |  | 1 |
| c-native-omp | 94.9 | 48.9 | 40.9 | 35.8 | 37.5 | 1 |
| c-clang-serial | 100.3 |  |  |  |  | 1 |
| c-clang-omp | 101.8 | 49.9 | 47.4 | 38.2 | 45.0 | 1 |
| cpp-thread | 87.4 | 44.3 | 43.8 | 33.8 | 33.9 | 1 |
| rust-rayon | 92.0 | 50.8 | 39.0 | 32.5 | 49.0 | 1 |
| zig-safe | 154.8 | 99.8 | 55.2 | 52.7 | 52.4 | 1 |
| zig-fast | 141.9 | 68.2 | 51.6 | 52.1 | 52.0 | 1 |
| go | 129.1 | 60.7 | 44.8 | 46.6 | 41.6 | 1 |

## hist

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 7.7 | 3.9 | 2.1 | 2.2 | 2.1 | 1 |
| sword-native | 7.5 | 3.8 | 1.9 | 2.6 | 2.3 | 1 |
| c-serial | 7.8 |  |  |  |  | 1 |
| c-omp | 7.9 | 4.0 | 2.0 | 2.3 | 2.5 | 10 |
| c-fastmath-serial | 7.6 |  |  |  |  | 1 |
| c-fastmath-omp | 7.7 | 4.0 | 2.0 | 2.8 | 2.5 | 10 |
| c-nofma-serial | 7.7 |  |  |  |  | 1 |
| c-nofma-omp | 7.6 | 3.9 | 1.9 | 2.2 | 2.4 | 10 |
| c-native-serial | 7.6 |  |  |  |  | 1 |
| c-native-omp | 7.7 | 3.9 | 2.0 | 2.1 | 2.4 | 11 |
| c-clang-serial | 7.7 |  |  |  |  | 1 |
| c-clang-omp | 7.7 | 4.0 | 1.9 | 2.9 | 2.4 | 7 |
| cpp-thread | 8.2 | 4.1 | 2.6 | 3.1 | 2.8 | 5 |
| rust-rayon | 7.9 | 3.9 | 1.9 | 2.0 | 2.0 | 11 |
| zig-safe | 13.2 | 8.4 | 5.3 | 4.9 | 5.4 | 5 |
| zig-fast | 8.3 | 5.0 | 3.3 | 3.4 | 3.4 | 5 |
| go | 9.0 | 4.7 | 2.4 | 2.4 | 2.4 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 13.4 | 6.7 | 5.9 | 5.9 | 6.0 | 1 |
| sword-native | 13.8 | 7.0 | 6.2 | 6.2 | 6.4 | 1 |
| c-serial | 10.5 |  |  |  |  | 1 |
| c-omp | 8.4 | 4.2 | 3.6 | 3.7 | 4.2 | 11 |
| c-fastmath-serial | 36.5 |  |  |  |  | 1 |
| c-fastmath-omp | 8.4 | 4.3 | 3.6 | 3.6 | 4.0 | 11 |
| c-nofma-serial | 10.5 |  |  |  |  | 1 |
| c-nofma-omp | 8.4 | 4.3 | 3.6 | 3.9 | 4.0 | 11 |
| c-native-serial | 10.4 |  |  |  |  | 1 |
| c-native-omp | 8.5 | 4.4 | 3.6 | 3.7 | 4.2 | 10 |
| c-clang-serial | 8.6 |  |  |  |  | 1 |
| c-clang-omp | 8.5 | 4.3 | 3.5 | 4.5 | 4.8 | 6 |
| cpp-thread | 8.5 | 4.4 | 4.9 | 4.9 | 4.4 | 5 |
| rust-rayon | 16.6 | 8.4 | 7.7 | 7.9 | 8.1 | 11 |
| zig-safe | 15.8 | 11.2 | 9.3 | 9.6 | 9.2 | 5 |
| zig-fast | 12.8 | 9.1 | 7.2 | 6.9 | 7.3 | 5 |
| go | 8.5 | 4.4 | 4.0 | 4.0 | 4.1 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.1 | 3.0 | 2.1 | 2.0 | 3.4 | 1 |
| sword-native | 6.4 | 3.0 | 2.2 | 2.3 | 2.3 | 1 |
| c-serial | 5.6 |  |  |  |  | 1 |
| c-omp | 5.7 | 2.9 | 2.8 | 2.1 | 2.2 | 6 |
| c-fastmath-serial | 5.6 |  |  |  |  | 1 |
| c-fastmath-omp | 5.4 | 2.7 | 2.8 | 2.1 | 2.3 | 6 |
| c-nofma-serial | 5.1 |  |  |  |  | 1 |
| c-nofma-omp | 5.2 | 2.7 | 2.8 | 2.1 | 2.2 | 6 |
| c-native-serial | 5.7 |  |  |  |  | 1 |
| c-native-omp | 5.6 | 2.8 | 3.0 | 2.2 | 2.7 | 7 |
| c-clang-serial | 6.3 |  |  |  |  | 1 |
| c-clang-omp | 6.3 | 2.7 | 2.8 | 2.2 | 2.3 | 5 |
| cpp-thread | 5.5 | 2.9 | 2.9 | 2.3 | 2.4 | 5 |
| rust-rayon | 5.6 | 2.9 | 1.9 | 1.9 | 2.2 | 11 |
| zig-safe | 7.1 | 4.6 | 4.5 | 3.9 | 3.8 | 5 |
| zig-fast | 4.8 | 4.0 | 4.2 | 2.5 | 3.1 | 5 |
| go | 7.3 | 3.9 | 4.3 | 3.7 | 2.7 | 5 |

## scan

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 16.9 | 8.7 | 4.7 | 6.0 | 6.3 | 1 |
| sword-native | 15.2 | 8.1 | 4.3 | 4.5 | 5.8 | 1 |
| c-serial | 7.1 |  |  |  |  | 1 |
| c-omp | 13.4 | 6.8 | 3.4 | 4.0 | 4.2 | 4 |
| c-fastmath-serial | 6.8 |  |  |  |  | 1 |
| c-fastmath-omp | 13.7 | 6.8 | 3.4 | 4.2 | 4.2 | 4 |
| c-nofma-serial | 7.0 |  |  |  |  | 1 |
| c-nofma-omp | 13.6 | 6.7 | 3.4 | 4.3 | 4.6 | 4 |
| c-native-serial | 7.0 |  |  |  |  | 1 |
| c-native-omp | 13.4 | 6.7 | 3.4 | 4.7 | 4.5 | 4 |
| c-clang-serial | 6.9 |  |  |  |  | 1 |
| c-clang-omp | 13.3 | 6.8 | 3.4 | 5.1 | 5.2 | 4 |
| cpp-thread | 14.0 | 7.0 | 3.7 | 4.5 | 4.9 | 4 |
| rust-rayon | 13.0 | 7.0 | 3.6 | 3.6 | 3.6 | 4 |
| zig-safe | 15.5 | 7.8 | 4.5 | 6.0 | 6.0 | 4 |
| zig-fast | 15.2 | 7.7 | 4.4 | 5.8 | 6.3 | 4 |
| go | 13.8 | 7.0 | 3.6 | 3.6 | 4.3 | 4 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 53.2 | 26.7 | 15.6 | 16.5 | 16.4 | 1 |
| sword-native | 50.0 | 24.3 | 14.8 | 14.4 | 14.6 | 1 |
| c-serial | 9.7 |  |  |  |  | 1 |
| c-omp | 19.3 | 9.8 | 6.7 | 7.4 | 7.8 | 4 |
| c-fastmath-serial | 9.8 |  |  |  |  | 1 |
| c-fastmath-omp | 19.3 | 9.8 | 7.1 | 8.5 | 7.9 | 4 |
| c-nofma-serial | 9.7 |  |  |  |  | 1 |
| c-nofma-omp | 19.3 | 10.0 | 7.2 | 7.4 | 7.9 | 4 |
| c-native-serial | 9.7 |  |  |  |  | 1 |
| c-native-omp | 19.2 | 9.8 | 7.0 | 7.9 | 7.9 | 4 |
| c-clang-serial | 9.7 |  |  |  |  | 1 |
| c-clang-omp | 19.2 | 9.7 | 7.0 | 9.3 | 9.0 | 4 |
| cpp-thread | 19.5 | 10.2 | 7.5 | 9.1 | 8.4 | 4 |
| rust-rayon | 19.2 | 9.9 | 7.3 | 7.3 | 6.8 | 4 |
| zig-safe | 19.9 | 10.8 | 8.3 | 9.9 | 11.0 | 4 |
| zig-fast | 20.0 | 10.8 | 8.3 | 10.0 | 10.5 | 4 |
| go | 19.5 | 10.0 | 7.1 | 7.3 | 7.3 | 4 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 28.4 | 14.6 | 9.8 | 10.4 | 10.1 | 1 |
| sword-native | 24.4 | 13.0 | 10.4 | 9.7 | 12.7 | 1 |
| c-serial | 12.0 |  |  |  |  | 1 |
| c-omp | 21.8 | 12.4 | 11.2 | 9.0 | 8.9 | 4 |
| c-fastmath-serial | 10.6 |  |  |  |  | 1 |
| c-fastmath-omp | 12.7 | 8.7 | 7.4 | 6.4 | 6.1 | 5 |
| c-nofma-serial | 11.5 |  |  |  |  | 1 |
| c-nofma-omp | 23.6 | 11.5 | 11.7 | 11.0 | 8.5 | 4 |
| c-native-serial | 12.6 |  |  |  |  | 1 |
| c-native-omp | 23.5 | 11.0 | 11.4 | 10.3 | 9.9 | 4 |
| c-clang-serial | 12.8 |  |  |  |  | 1 |
| c-clang-omp | 24.0 | 14.0 | 13.3 | 10.9 | 8.6 | 4 |
| cpp-thread | 21.7 | 10.5 | 11.0 | 8.6 | 10.1 | 4 |
| rust-rayon | 22.4 | 12.8 | 12.5 | 10.9 | 9.8 | 4 |
| zig-safe | 25.2 | 14.6 | 11.5 | 9.0 | 10.9 | 4 |
| zig-fast | 25.2 | 11.9 | 13.2 | 10.5 | 10.7 | 4 |
| go | 23.1 | 12.8 | 13.5 | 12.7 | 8.7 | 4 |

## sort

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 170.7 | 87.5 | 47.2 | 50.1 | 51.1 | 1 |
| sword-native | 169.8 | 87.1 | 46.9 | 49.8 | 51.0 | 1 |
| c-serial | 63.7 |  |  |  |  | 1 |
| c-omp | 63.8 | 32.4 | 17.2 | 18.8 | 19.1 | 1 |
| c-fastmath-serial | 63.6 |  |  |  |  | 1 |
| c-fastmath-omp | 63.6 | 32.1 | 16.8 | 18.6 | 18.7 | 1 |
| c-nofma-serial | 63.9 |  |  |  |  | 1 |
| c-nofma-omp | 64.0 | 32.5 | 17.1 | 19.6 | 18.7 | 1 |
| c-native-serial | 63.1 |  |  |  |  | 1 |
| c-native-omp | 63.3 | 32.0 | 16.7 | 19.1 | 18.5 | 1 |
| c-clang-serial | 66.6 |  |  |  |  | 1 |
| c-clang-omp | 75.8 | 35.3 | 20.0 | 28.6 | 29.7 | 1 |
| c-stable | 51.6 |  |  |  |  | 1 |
| c-stable-omp | 51.6 | 26.4 | 14.3 | 17.2 | 15.9 | 1 |
| c-symmerge | 127.3 |  |  |  |  | 1 |
| c-symmerge-omp | 127.5 | 66.1 | 36.8 | 41.9 | 40.2 | 1 |
| cpp-thread | 28.4 | 14.9 | 8.8 | 10.4 | 11.3 | 5 |
| rust-rayon | 11.6 | 6.5 | 4.0 | 4.1 | 4.1 | 1 |
| zig-safe | 15.1 | 9.3 | 6.7 | 8.2 | 9.7 | 5 |
| zig-fast | 9.3 | 6.0 | 4.7 | 6.3 | 7.7 | 5 |
| go | 58.4 | 33.5 | 18.6 | 20.8 | 20.6 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 227.0 | 115.7 | 82.5 | 85.2 | 86.3 | 1 |
| sword-native | 224.8 | 114.5 | 82.2 | 83.9 | 86.0 | 1 |
| c-serial | 113.9 |  |  |  |  | 1 |
| c-omp | 114.1 | 56.7 | 35.9 | 35.0 | 35.5 | 1 |
| c-fastmath-serial | 113.1 |  |  |  |  | 1 |
| c-fastmath-omp | 113.3 | 56.2 | 34.5 | 35.4 | 34.1 | 1 |
| c-nofma-serial | 114.3 |  |  |  |  | 1 |
| c-nofma-omp | 114.1 | 57.0 | 36.3 | 34.6 | 35.1 | 1 |
| c-native-serial | 114.3 |  |  |  |  | 1 |
| c-native-omp | 114.2 | 56.5 | 34.9 | 34.0 | 34.5 | 1 |
| c-clang-serial | 105.8 |  |  |  |  | 1 |
| c-clang-omp | 105.9 | 54.7 | 36.3 | 40.5 | 45.3 | 1 |
| c-stable | 67.8 |  |  |  |  | 1 |
| c-stable-omp | 67.9 | 35.2 | 26.3 | 27.2 | 27.3 | 1 |
| c-symmerge | 164.3 |  |  |  |  | 1 |
| c-symmerge-omp | 164.3 | 84.6 | 61.2 | 63.6 | 63.4 | 1 |
| cpp-thread | 41.0 | 21.8 | 15.3 | 17.7 | 18.3 | 5 |
| rust-rayon | 9.5 | 5.1 | 4.5 | 4.5 | 4.5 | 1 |
| zig-safe | 18.6 | 11.6 | 11.8 | 13.9 | 16.3 | 5 |
| zig-fast | 12.0 | 9.5 | 10.6 | 13.1 | 16.0 | 5 |
| go | 73.5 | 42.7 | 29.4 | 32.2 | 34.0 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 203.1 | 104.5 | 87.1 | 98.0 | 93.8 | 1 |
| sword-native | 233.2 | 122.7 | 82.6 | 83.6 | 89.4 | 1 |
| c-serial | 41.2 |  |  |  |  | 1 |
| c-omp | 42.0 | 25.3 | 20.3 | 23.6 | 24.6 | 5 |
| c-fastmath-serial | 41.8 |  |  |  |  | 1 |
| c-fastmath-omp | 42.8 | 25.4 | 24.1 | 26.1 | 28.6 | 5 |
| c-nofma-serial | 45.1 |  |  |  |  | 1 |
| c-nofma-omp | 46.2 | 30.1 | 21.5 | 24.0 | 26.6 | 5 |
| c-native-serial | 47.9 |  |  |  |  | 1 |
| c-native-omp | 42.2 | 25.1 | 21.9 | 23.5 | 25.7 | 5 |
| c-clang-serial | 42.4 |  |  |  |  | 1 |
| c-clang-omp | 42.0 | 25.7 | 20.1 | 23.0 | 25.0 | 5 |
| c-stable | 73.1 |  |  |  |  | 1 |
| c-stable-omp | 72.5 | 36.9 | 30.1 | 29.2 | 30.1 | 1 |
| c-symmerge | 164.1 |  |  |  |  | 1 |
| c-symmerge-omp | 158.7 | 91.5 | 68.5 | 70.7 | 68.6 | 1 |
| cpp-thread | 35.1 | 20.0 | 19.2 | 19.6 | 20.0 | 5 |
| rust-rayon | 11.4 | 6.3 | 5.1 | 5.4 | 6.2 | 1 |
| zig-safe | 15.7 | 9.2 | 10.2 | 10.9 | 10.9 | 5 |
| zig-fast | 10.2 | 9.4 | 10.7 | 13.5 | 14.0 | 5 |
| go | 65.7 | 39.7 | 32.9 | 32.9 | 30.4 | 5 |

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
| c-omp | 9 | 1 | 1 | 1 | 1 | 21 | 4 | 6 |
| c-lanes | 1 |  |  |  |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 | 1 | 1 | 2 |
| c-fastmath-omp | 13 | 1 | 2 | 2 | 1 | 21 | 8 | 6 |
| c-nofma-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-nofma-omp | 8 | 1 | 1 | 1 | 1 | 22 | 4 | 6 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-native-omp | 8 | 1 | 1 | 1 | 1 | 23 | 4 | 6 |
| c-native-lanes | 1 |  |  |  |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 | 9 | 4 | 6 |
| c-stable |  |  |  |  |  |  |  | 1 |
| c-stable-omp |  |  |  |  |  |  |  | 1 |
| c-symmerge |  |  |  |  |  |  |  | 1 |
| c-symmerge-omp |  |  |  |  |  |  |  | 1 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 10 |
| rust-rayon | 24 | 1 | 1 | 1 | 1 | 29 | 4 | 1 |
| rust-slices |  |  | 1 |  |  |  |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| zig-fast | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| go | 5 | 1 | 1 | 2 | 1 | 5 | 4 | 5 |
