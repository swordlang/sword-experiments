## sum

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 3.5 | 1.6 | 0.8 | 1.1 | 1.0 | 1 |
| sword-native | 3.5 | 1.6 | 0.8 | 1.1 | 1.4 | 1 |
| sword-without-walked | 4.5 | 2.7 | 1.1 | 1.4 | 1.4 | 1 |
| sword-without-walked-mut | 3.4 | 1.8 | 0.9 | 0.9 | 1.4 | 1 |
| sword-without-captures | 3.5 | 1.7 | 0.9 | 1.3 | 1.1 | 1 |
| sword-without-versioned | 3.4 | 1.6 | 0.7 | 0.9 | 1.3 | 1 |
| sword-without-split | 3.0 | 1.5 | 0.7 | 1.1 | 1.2 | 1 |
| sword-without-deferred | 3.5 | 1.6 | 0.9 | 1.0 | 1.2 | 1 |
| sword-without-lanes | 6.5 | 3.4 | 1.7 | 2.2 | 2.0 | 1 |
| sword-without-steady | 3.4 | 1.7 | 0.8 | 1.1 | 1.2 | 1 |
| c-serial | 6.6 |  |  |  |  | 1 |
| c-restrict | 6.6 |  |  |  |  | 1 |
| c-omp | 6.8 | 3.4 | 1.7 | 1.8 | 2.2 | 7 |
| c-lanes | 3.9 |  |  |  |  | 1 |
| c-lanes-omp | 4.0 | 1.8 | 0.9 | 1.3 | 1.1 | 1 |
| c-fastmath-serial | 6.8 |  |  |  |  | 1 |
| c-fastmath-omp | 6.5 | 3.3 | 1.7 | 2.4 | 2.0 | 7 |
| c-native-serial | 6.3 |  |  |  |  | 1 |
| c-native-omp | 6.6 | 3.3 | 1.7 | 1.7 | 2.0 | 7 |
| c-native-lanes | 3.1 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.8 | 1.5 | 0.7 | 1.1 | 1.0 | 1 |
| c-clang-serial | 6.5 |  |  |  |  | 1 |
| c-clang-omp | 6.6 | 3.3 | 1.6 | 2.4 | 2.1 | 5 |
| cpp-thread | 6.5 | 3.2 | 1.8 | 2.6 | 2.5 | 5 |
| rust-rayon | 6.6 | 3.3 | 1.7 | 1.7 | 1.7 | 9 |
| zig-safe | 6.8 | 3.5 | 2.2 | 2.7 | 2.9 | 5 |
| zig-fast | 6.9 | 3.5 | 2.2 | 2.7 | 2.8 | 5 |
| go | 6.6 | 3.4 | 1.7 | 1.8 | 1.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 1.9 | 1.6 | 1.7 | 1.6 | 1.6 | 1 |
| sword-native | 2.2 | 1.6 | 1.6 | 1.6 | 1.7 | 1 |
| sword-without-walked | 2.8 | 1.7 | 1.5 | 1.6 | 1.7 | 1 |
| sword-without-walked-mut | 1.9 | 1.7 | 1.6 | 1.6 | 1.7 | 1 |
| sword-without-captures | 1.9 | 1.7 | 1.6 | 1.6 | 1.6 | 1 |
| sword-without-versioned | 1.9 | 1.6 | 1.5 | 1.6 | 1.6 | 1 |
| sword-without-split | 2.0 | 1.6 | 1.7 | 1.6 | 1.7 | 1 |
| sword-without-deferred | 2.0 | 1.6 | 1.6 | 1.6 | 1.6 | 1 |
| sword-without-lanes | 8.2 | 4.1 | 2.1 | 2.2 | 2.4 | 1 |
| sword-without-steady | 2.0 | 1.6 | 1.7 | 1.8 | 1.7 | 1 |
| c-serial | 8.2 |  |  |  |  | 1 |
| c-restrict | 8.2 |  |  |  |  | 1 |
| c-omp | 8.2 | 4.1 | 2.1 | 2.1 | 2.7 | 8 |
| c-lanes | 2.3 |  |  |  |  | 1 |
| c-lanes-omp | 2.3 | 1.6 | 1.5 | 1.6 | 1.8 | 1 |
| c-fastmath-serial | 2.2 |  |  |  |  | 1 |
| c-fastmath-omp | 8.2 | 4.1 | 2.1 | 2.1 | 2.7 | 7 |
| c-native-serial | 8.2 |  |  |  |  | 1 |
| c-native-omp | 8.2 | 4.1 | 2.1 | 2.9 | 2.7 | 7 |
| c-native-lanes | 2.2 |  |  |  |  | 1 |
| c-native-lanes-omp | 2.2 | 1.5 | 1.6 | 1.6 | 1.8 | 1 |
| c-clang-serial | 8.2 |  |  |  |  | 1 |
| c-clang-omp | 8.2 | 4.1 | 2.1 | 3.1 | 3.2 | 5 |
| cpp-thread | 8.3 | 4.2 | 2.2 | 3.3 | 3.2 | 5 |
| rust-rayon | 8.2 | 4.1 | 2.1 | 2.1 | 2.2 | 9 |
| zig-safe | 8.4 | 4.4 | 2.7 | 3.5 | 3.7 | 5 |
| zig-fast | 8.4 | 4.4 | 2.7 | 3.5 | 3.9 | 5 |
| go | 8.2 | 4.2 | 3.0 | 3.0 | 3.0 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 2.0 | 2.0 | 1.6 | 1.8 | 1.7 | 1 |
| sword-native | 2.0 | 2.0 | 1.8 | 1.9 | 1.7 | 1 |
| sword-without-walked | 3.9 | 2.6 | 2.3 | 2.0 | 2.0 | 1 |
| sword-without-walked-mut | 2.0 | 1.7 | 1.7 | 1.7 | 1.7 | 1 |
| sword-without-captures | 1.9 | 1.7 | 1.6 | 1.9 | 1.8 | 1 |
| sword-without-versioned | 2.0 | 1.8 | 1.8 | 1.8 | 1.8 | 1 |
| sword-without-split | 1.9 | 1.9 | 2.0 | 1.7 | 1.9 | 1 |
| sword-without-deferred | 1.9 | 1.7 | 1.6 | 1.7 | 1.8 | 1 |
| sword-without-lanes | 10.5 | 6.3 | 4.0 | 4.2 | 4.5 | 1 |
| sword-without-steady | 1.8 | 1.8 | 1.7 | 1.7 | 1.6 | 1 |
| c-serial | 10.4 |  |  |  |  | 1 |
| c-restrict | 10.7 |  |  |  |  | 1 |
| c-omp | 10.4 | 6.8 | 5.2 | 4.3 | 4.1 | 5 |
| c-lanes | 1.7 |  |  |  |  | 1 |
| c-lanes-omp | 1.8 | 1.7 | 1.7 | 1.8 | 1.8 | 1 |
| c-fastmath-serial | 1.8 |  |  |  |  | 1 |
| c-fastmath-omp | 1.7 | 1.8 | 1.7 | 1.8 | 1.7 | 5 |
| c-native-serial | 11.0 |  |  |  |  | 1 |
| c-native-omp | 10.5 | 6.9 | 5.3 | 4.1 | 4.3 | 5 |
| c-native-lanes | 1.9 |  |  |  |  | 1 |
| c-native-lanes-omp | 1.8 | 1.6 | 1.7 | 1.7 | 1.8 | 1 |
| c-clang-serial | 10.9 |  |  |  |  | 1 |
| c-clang-omp | 10.5 | 5.5 | 5.7 | 4.9 | 4.9 | 5 |
| cpp-thread | 11.2 | 6.2 | 5.7 | 4.6 | 4.3 | 5 |
| rust-rayon | 10.7 | 6.0 | 4.4 | 3.9 | 5.9 | 9 |
| zig-safe | 10.6 | 6.9 | 5.5 | 5.3 | 4.9 | 5 |
| zig-fast | 10.8 | 6.2 | 5.4 | 4.3 | 5.0 | 5 |
| go | 10.4 | 6.8 | 5.2 | 4.5 | 5.4 | 5 |

## saxpy

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 6.9 | 3.5 | 1.9 | 1.8 | 2.2 | 1 |
| sword-native | 6.8 | 3.5 | 2.0 | 1.9 | 2.0 | 1 |
| sword-without-walked | 6.6 | 3.7 | 1.9 | 1.9 | 2.0 | 1 |
| sword-without-walked-mut | 6.9 | 3.5 | 1.9 | 2.0 | 2.0 | 1 |
| sword-without-captures | 9.5 | 5.5 | 2.8 | 2.9 | 3.1 | 1 |
| sword-without-versioned | 6.8 | 3.4 | 1.7 | 2.0 | 1.9 | 1 |
| sword-without-split | 6.6 | 3.7 | 2.0 | 2.0 | 2.2 | 1 |
| sword-without-deferred | 6.9 | 3.6 | 1.9 | 2.0 | 2.1 | 1 |
| sword-without-lanes | 6.8 | 3.7 | 2.0 | 2.1 | 2.0 | 1 |
| sword-without-steady | 6.9 | 3.5 | 1.9 | 1.9 | 2.5 | 1 |
| c-serial | 6.8 |  |  |  |  | 1 |
| c-restrict | 6.7 |  |  |  |  | 1 |
| c-omp | 7.1 | 3.6 | 2.0 | 2.8 | 2.5 | 1 |
| c-fastmath-serial | 6.6 |  |  |  |  | 1 |
| c-fastmath-omp | 6.8 | 3.7 | 2.0 | 2.7 | 2.4 | 1 |
| c-native-serial | 6.8 |  |  |  |  | 1 |
| c-native-omp | 6.7 | 3.5 | 2.1 | 2.7 | 2.4 | 1 |
| c-clang-serial | 7.3 |  |  |  |  | 1 |
| c-clang-omp | 7.1 | 3.9 | 1.9 | 2.8 | 2.7 | 1 |
| cpp-thread | 7.2 | 3.7 | 2.3 | 2.9 | 3.1 | 1 |
| rust-rayon | 7.3 | 3.6 | 1.9 | 2.0 | 2.2 | 1 |
| zig-safe | 11.5 | 6.1 | 3.3 | 4.3 | 4.5 | 1 |
| zig-fast | 9.1 | 4.9 | 2.8 | 3.7 | 3.8 | 1 |
| go | 7.4 | 3.8 | 2.1 | 2.1 | 2.1 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 4.5 | 3.8 | 3.6 | 3.9 | 3.8 | 1 |
| sword-native | 4.5 | 3.7 | 3.9 | 4.0 | 3.7 | 1 |
| sword-without-walked | 4.5 | 3.8 | 3.8 | 3.8 | 3.7 | 1 |
| sword-without-walked-mut | 4.5 | 3.8 | 3.9 | 3.8 | 4.0 | 1 |
| sword-without-captures | 8.1 | 4.4 | 4.2 | 4.3 | 4.3 | 1 |
| sword-without-versioned | 4.5 | 3.7 | 3.9 | 3.9 | 3.8 | 1 |
| sword-without-split | 4.5 | 3.7 | 3.8 | 3.7 | 3.8 | 1 |
| sword-without-deferred | 4.2 | 3.6 | 3.5 | 3.6 | 3.7 | 1 |
| sword-without-lanes | 4.5 | 3.7 | 3.7 | 3.6 | 3.9 | 1 |
| sword-without-steady | 4.5 | 3.8 | 3.9 | 3.7 | 3.9 | 1 |
| c-serial | 4.6 |  |  |  |  | 1 |
| c-restrict | 4.7 |  |  |  |  | 1 |
| c-omp | 4.6 | 3.7 | 3.8 | 3.9 | 3.9 | 1 |
| c-fastmath-serial | 4.3 |  |  |  |  | 1 |
| c-fastmath-omp | 4.5 | 3.7 | 3.7 | 3.9 | 3.8 | 1 |
| c-native-serial | 4.1 |  |  |  |  | 1 |
| c-native-omp | 4.5 | 3.7 | 3.7 | 3.7 | 3.8 | 1 |
| c-clang-serial | 4.3 |  |  |  |  | 1 |
| c-clang-omp | 4.5 | 3.8 | 3.8 | 3.9 | 3.9 | 1 |
| cpp-thread | 4.9 | 4.0 | 4.0 | 4.2 | 4.1 | 1 |
| rust-rayon | 4.5 | 4.0 | 4.1 | 4.2 | 4.4 | 1 |
| zig-safe | 8.7 | 4.6 | 4.7 | 5.0 | 5.3 | 1 |
| zig-fast | 6.6 | 4.2 | 4.0 | 4.6 | 4.7 | 1 |
| go | 5.6 | 3.9 | 3.9 | 4.1 | 3.9 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 4.9 | 4.7 | 4.7 | 4.7 | 4.7 | 1 |
| sword-native | 4.9 | 4.9 | 4.7 | 4.9 | 5.2 | 1 |
| sword-without-walked | 4.9 | 4.7 | 4.9 | 5.3 | 4.8 | 1 |
| sword-without-walked-mut | 4.9 | 4.9 | 4.7 | 5.2 | 5.1 | 1 |
| sword-without-captures | 9.0 | 6.4 | 5.4 | 5.1 | 4.8 | 1 |
| sword-without-versioned | 4.7 | 4.6 | 4.9 | 4.8 | 5.9 | 1 |
| sword-without-split | 4.7 | 4.6 | 4.7 | 4.7 | 5.5 | 1 |
| sword-without-deferred | 4.8 | 5.0 | 4.7 | 5.3 | 4.7 | 1 |
| sword-without-lanes | 4.8 | 5.0 | 6.2 | 5.1 | 5.4 | 1 |
| sword-without-steady | 6.5 | 5.9 | 5.2 | 5.3 | 5.1 | 1 |
| c-serial | 6.3 |  |  |  |  | 1 |
| c-restrict | 6.0 |  |  |  |  | 1 |
| c-omp | 5.6 | 5.4 | 5.1 | 5.1 | 5.8 | 1 |
| c-fastmath-serial | 6.4 |  |  |  |  | 1 |
| c-fastmath-omp | 6.1 | 5.1 | 5.6 | 5.0 | 5.0 | 1 |
| c-native-serial | 5.3 |  |  |  |  | 1 |
| c-native-omp | 5.5 | 5.3 | 5.6 | 4.8 | 4.7 | 1 |
| c-clang-serial | 6.6 |  |  |  |  | 1 |
| c-clang-omp | 5.2 | 5.6 | 5.4 | 5.2 | 5.0 | 1 |
| cpp-thread | 5.1 | 5.1 | 5.1 | 5.0 | 5.1 | 1 |
| rust-rayon | 5.4 | 5.4 | 5.1 | 5.0 | 5.8 | 1 |
| zig-safe | 11.0 | 8.5 | 6.2 | 6.1 | 6.6 | 1 |
| zig-fast | 9.9 | 7.3 | 5.4 | 5.8 | 5.6 | 1 |
| go | 8.1 | 6.0 | 6.7 | 5.1 | 4.7 | 1 |

## stencil

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 79.2 | 40.1 | 19.9 | 24.4 | 25.1 | 1 |
| sword-native | 63.3 | 32.4 | 15.8 | 19.0 | 22.1 | 1 |
| sword-without-walked | 77.3 | 40.5 | 20.0 | 23.6 | 24.5 | 1 |
| sword-without-walked-mut | 81.1 | 40.5 | 20.3 | 23.1 | 25.6 | 1 |
| sword-without-captures | 87.7 | 45.1 | 21.9 | 25.3 | 27.4 | 1 |
| sword-without-versioned | 78.6 | 39.6 | 19.9 | 23.0 | 25.4 | 1 |
| sword-without-split | 91.1 | 46.5 | 23.2 | 26.6 | 28.5 | 1 |
| sword-without-deferred | 77.9 | 39.0 | 19.6 | 23.0 | 25.3 | 1 |
| sword-without-lanes | 78.9 | 39.2 | 19.9 | 22.5 | 25.9 | 1 |
| sword-without-steady | 78.7 | 39.4 | 19.8 | 22.6 | 25.0 | 1 |
| sword-rows | 24.1 | 11.9 | 6.2 | 8.9 | 9.5 | 1 |
| c-serial | 54.8 |  |  |  |  | 1 |
| c-restrict | 55.0 |  |  |  |  | 1 |
| c-omp | 50.8 | 25.6 | 12.6 | 16.0 | 15.3 | 1 |
| c-fastmath-serial | 55.0 |  |  |  |  | 1 |
| c-fastmath-omp | 53.2 | 25.4 | 12.7 | 16.5 | 15.6 | 1 |
| c-native-serial | 44.0 |  |  |  |  | 1 |
| c-native-omp | 44.0 | 21.9 | 10.5 | 13.6 | 13.0 | 1 |
| c-clang-serial | 49.1 |  |  |  |  | 1 |
| c-clang-omp | 50.4 | 24.6 | 12.3 | 18.7 | 15.7 | 1 |
| cpp-thread | 58.4 | 29.4 | 16.0 | 18.6 | 20.3 | 1 |
| rust-rayon | 93.0 | 46.9 | 23.8 | 23.4 | 24.0 | 1 |
| rust-slices | 23.1 | 11.6 | 6.0 | 6.2 | 6.6 | 1 |
| zig-safe | 95.7 | 49.3 | 28.2 | 36.1 | 37.3 | 1 |
| zig-fast | 43.5 | 23.5 | 15.5 | 19.7 | 22.7 | 1 |
| go | 80.6 | 39.8 | 20.4 | 22.7 | 23.4 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 79.5 | 39.8 | 35.1 | 36.2 | 37.5 | 1 |
| sword-native | 84.6 | 39.8 | 35.8 | 35.9 | 37.4 | 1 |
| sword-without-walked | 79.3 | 41.3 | 35.2 | 35.8 | 37.6 | 1 |
| sword-without-walked-mut | 84.2 | 42.2 | 37.2 | 38.8 | 39.1 | 1 |
| sword-without-captures | 88.1 | 46.3 | 38.7 | 39.6 | 40.0 | 1 |
| sword-without-versioned | 80.1 | 39.8 | 35.5 | 36.5 | 36.9 | 1 |
| sword-without-split | 96.0 | 49.7 | 41.4 | 42.5 | 44.4 | 1 |
| sword-without-deferred | 83.9 | 40.9 | 35.1 | 36.2 | 37.4 | 1 |
| sword-without-lanes | 78.3 | 41.5 | 35.1 | 35.9 | 36.9 | 1 |
| sword-without-steady | 78.9 | 42.5 | 35.7 | 36.4 | 37.8 | 1 |
| sword-rows | 39.1 | 20.6 | 15.1 | 15.4 | 16.5 | 1 |
| c-serial | 47.9 |  |  |  |  | 1 |
| c-restrict | 45.6 |  |  |  |  | 1 |
| c-omp | 47.8 | 25.6 | 18.9 | 20.1 | 19.5 | 1 |
| c-fastmath-serial | 54.2 |  |  |  |  | 1 |
| c-fastmath-omp | 48.0 | 26.4 | 20.4 | 19.6 | 22.2 | 1 |
| c-native-serial | 45.0 |  |  |  |  | 1 |
| c-native-omp | 49.3 | 25.0 | 18.9 | 18.3 | 20.5 | 1 |
| c-clang-serial | 51.6 |  |  |  |  | 1 |
| c-clang-omp | 48.7 | 25.7 | 18.0 | 32.8 | 23.1 | 1 |
| cpp-thread | 58.2 | 27.4 | 20.5 | 25.7 | 26.2 | 1 |
| rust-rayon | 114.7 | 46.9 | 44.0 | 45.1 | 45.2 | 1 |
| rust-slices | 42.8 | 21.5 | 14.8 | 15.9 | 16.7 | 1 |
| zig-safe | 74.2 | 39.4 | 37.0 | 45.3 | 45.9 | 1 |
| zig-fast | 52.0 | 29.3 | 23.2 | 28.8 | 31.4 | 1 |
| go | 76.5 | 38.4 | 33.7 | 31.2 | 32.6 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 41.5 | 32.6 | 21.5 | 22.1 | 24.4 | 1 |
| sword-native | 51.5 | 37.1 | 26.6 | 24.2 | 20.7 | 1 |
| sword-without-walked | 52.6 | 38.4 | 24.9 | 22.2 | 17.3 | 1 |
| sword-without-walked-mut | 56.4 | 32.3 | 22.5 | 17.1 | 22.7 | 1 |
| sword-without-captures | 71.9 | 47.4 | 31.1 | 30.2 | 30.5 | 1 |
| sword-without-versioned | 54.3 | 34.5 | 25.1 | 21.7 | 15.1 | 1 |
| sword-without-split | 72.9 | 52.5 | 30.9 | 25.1 | 27.3 | 1 |
| sword-without-deferred | 42.5 | 29.7 | 25.3 | 16.0 | 19.3 | 1 |
| sword-without-lanes | 47.3 | 27.4 | 20.1 | 20.3 | 20.5 | 1 |
| sword-without-steady | 43.2 | 25.1 | 16.4 | 18.2 | 20.7 | 1 |
| sword-rows | 31.7 | 24.3 | 18.5 | 17.7 | 22.1 | 1 |
| c-serial | 43.6 |  |  |  |  | 1 |
| c-restrict | 45.1 |  |  |  |  | 1 |
| c-omp | 43.0 | 20.8 | 20.6 | 19.3 | 19.6 | 1 |
| c-fastmath-serial | 43.5 |  |  |  |  | 1 |
| c-fastmath-omp | 44.9 | 22.2 | 26.3 | 19.0 | 16.0 | 1 |
| c-native-serial | 35.8 |  |  |  |  | 1 |
| c-native-omp | 38.7 | 19.8 | 20.2 | 20.7 | 16.3 | 1 |
| c-clang-serial | 41.7 |  |  |  |  | 1 |
| c-clang-omp | 43.4 | 22.6 | 25.2 | 19.0 | 19.7 | 1 |
| cpp-thread | 37.4 | 19.2 | 21.2 | 16.6 | 17.6 | 1 |
| rust-rayon | 82.2 | 48.3 | 32.7 | 34.8 | 30.0 | 1 |
| rust-slices | 26.7 | 22.5 | 17.8 | 19.8 | 21.8 | 1 |
| zig-safe | 88.2 | 58.1 | 50.4 | 36.6 | 35.5 | 1 |
| zig-fast | 40.0 | 31.5 | 22.1 | 22.1 | 20.0 | 1 |
| go | 87.7 | 40.5 | 43.4 | 36.4 | 33.4 | 1 |

## mandelbrot

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 692.9 | 346.6 | 173.8 | 176.0 | 176.5 | 1 |
| sword-native | 684.0 | 342.2 | 171.6 | 174.2 | 173.9 | 1 |
| sword-without-walked | 692.9 | 346.6 | 173.7 | 174.8 | 175.8 | 1 |
| sword-without-walked-mut | 692.9 | 346.6 | 173.7 | 176.4 | 177.4 | 1 |
| sword-without-captures | 692.9 | 346.6 | 173.7 | 174.5 | 176.0 | 1 |
| sword-without-versioned | 692.8 | 346.6 | 173.7 | 176.1 | 175.8 | 1 |
| sword-without-split | 692.7 | 346.6 | 173.7 | 175.7 | 176.7 | 1 |
| sword-without-deferred | 692.9 | 346.6 | 173.8 | 176.5 | 176.1 | 1 |
| sword-without-lanes | 692.9 | 346.6 | 173.7 | 175.6 | 176.5 | 1 |
| sword-without-steady | 692.8 | 346.6 | 173.8 | 175.7 | 176.9 | 1 |
| c-serial | 648.1 |  |  |  |  | 1 |
| c-restrict | 647.2 |  |  |  |  | 1 |
| c-omp | 635.9 | 317.9 | 159.4 | 159.5 | 159.5 | 1 |
| c-fastmath-serial | 626.5 |  |  |  |  | 1 |
| c-fastmath-omp | 627.6 | 314.0 | 157.3 | 157.4 | 157.6 | 1 |
| c-native-serial | 649.1 |  |  |  |  | 1 |
| c-native-omp | 651.5 | 326.4 | 163.1 | 163.1 | 163.4 | 1 |
| c-clang-serial | 770.4 |  |  |  |  | 1 |
| c-clang-omp | 768.6 | 384.8 | 193.4 | 193.7 | 193.7 | 1 |
| cpp-thread | 854.0 | 427.3 | 214.5 | 235.0 | 218.2 | 1 |
| rust-rayon | 693.0 | 347.2 | 174.4 | 173.9 | 174.2 | 1 |
| zig-safe | 683.4 | 342.9 | 171.9 | 189.9 | 175.0 | 1 |
| zig-fast | 897.2 | 449.1 | 225.3 | 246.9 | 228.5 | 1 |
| go | 678.3 | 339.6 | 170.5 | 180.6 | 173.9 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 763.3 | 381.9 | 203.2 | 204.1 | 206.2 | 1 |
| sword-native | 716.8 | 358.7 | 190.8 | 192.3 | 193.7 | 1 |
| sword-without-walked | 763.3 | 381.9 | 203.2 | 205.8 | 205.5 | 1 |
| sword-without-walked-mut | 763.0 | 381.7 | 203.6 | 205.5 | 205.4 | 1 |
| sword-without-captures | 763.0 | 381.9 | 203.5 | 204.9 | 207.7 | 1 |
| sword-without-versioned | 763.1 | 381.9 | 203.1 | 204.0 | 206.5 | 1 |
| sword-without-split | 763.3 | 381.9 | 203.4 | 205.2 | 205.6 | 1 |
| sword-without-deferred | 763.2 | 381.9 | 203.4 | 204.8 | 206.1 | 1 |
| sword-without-lanes | 762.9 | 381.9 | 203.7 | 204.5 | 206.0 | 1 |
| sword-without-steady | 763.3 | 381.9 | 203.2 | 204.4 | 205.2 | 1 |
| c-serial | 711.3 |  |  |  |  | 1 |
| c-restrict | 711.2 |  |  |  |  | 1 |
| c-omp | 712.0 | 356.4 | 176.7 | 176.8 | 177.0 | 1 |
| c-fastmath-serial | 705.4 |  |  |  |  | 1 |
| c-fastmath-omp | 710.2 | 355.6 | 177.4 | 177.7 | 177.5 | 1 |
| c-native-serial | 710.6 |  |  |  |  | 1 |
| c-native-omp | 710.6 | 355.8 | 176.5 | 176.7 | 176.8 | 1 |
| c-clang-serial | 688.3 |  |  |  |  | 1 |
| c-clang-omp | 687.7 | 344.8 | 206.6 | 206.7 | 207.2 | 1 |
| cpp-thread | 710.7 | 355.8 | 176.7 | 195.8 | 181.1 | 1 |
| rust-rayon | 713.0 | 347.9 | 214.6 | 211.4 | 211.7 | 1 |
| zig-safe | 719.4 | 360.4 | 197.3 | 215.2 | 202.0 | 1 |
| zig-fast | 718.3 | 359.9 | 189.8 | 208.1 | 194.8 | 1 |
| go | 687.0 | 349.8 | 206.4 | 209.8 | 208.3 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 957.3 | 475.3 | 356.1 | 338.2 | 365.1 | 1 |
| sword-native | 922.9 | 470.5 | 325.5 | 322.3 | 340.8 | 1 |
| sword-without-walked | 990.7 | 531.4 | 355.8 | 340.4 | 345.0 | 1 |
| sword-without-walked-mut | 966.8 | 523.6 | 348.2 | 357.8 | 328.2 | 1 |
| sword-without-captures | 995.3 | 509.6 | 345.6 | 339.7 | 362.4 | 1 |
| sword-without-versioned | 1019.3 | 504.8 | 327.5 | 326.9 | 370.1 | 1 |
| sword-without-split | 977.7 | 517.3 | 360.1 | 381.2 | 374.2 | 1 |
| sword-without-deferred | 1056.8 | 517.3 | 348.2 | 346.7 | 407.4 | 1 |
| sword-without-lanes | 1011.8 | 497.1 | 352.1 | 346.8 | 355.9 | 1 |
| sword-without-steady | 946.4 | 475.5 | 332.5 | 341.2 | 370.9 | 1 |
| c-serial | 732.7 |  |  |  |  | 1 |
| c-restrict | 759.1 |  |  |  |  | 1 |
| c-omp | 778.7 | 375.6 | 273.4 | 262.6 | 279.1 | 1 |
| c-fastmath-serial | 687.1 |  |  |  |  | 1 |
| c-fastmath-omp | 667.0 | 362.2 | 238.0 | 259.7 | 249.8 | 1 |
| c-native-serial | 958.9 |  |  |  |  | 1 |
| c-native-omp | 959.3 | 501.3 | 375.2 | 319.6 | 325.1 | 1 |
| c-clang-serial | 801.8 |  |  |  |  | 1 |
| c-clang-omp | 796.8 | 398.6 | 288.1 | 279.0 | 299.7 | 1 |
| cpp-thread | 899.5 | 445.0 | 287.6 | 281.8 | 289.5 | 1 |
| rust-rayon | 913.5 | 520.5 | 371.5 | 346.0 | 349.3 | 1 |
| zig-safe | 896.6 | 480.9 | 307.0 | 311.1 | 338.7 | 1 |
| zig-fast | 881.4 | 465.3 | 343.0 | 309.0 | 340.3 | 1 |
| go | 925.6 | 518.1 | 337.5 | 372.9 | 373.5 | 1 |

## nbody

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 247.7 | 126.0 | 64.2 | 67.1 | 68.8 | 1 |
| sword-native | 247.0 | 123.6 | 62.6 | 64.0 | 67.2 | 1 |
| sword-without-walked | 251.3 | 125.9 | 64.7 | 67.0 | 68.1 | 1 |
| sword-without-walked-mut | 252.1 | 126.1 | 63.2 | 65.9 | 67.9 | 1 |
| sword-without-captures | 251.9 | 126.1 | 64.7 | 66.3 | 69.0 | 1 |
| sword-without-versioned | 270.6 | 135.5 | 68.1 | 71.3 | 71.3 | 1 |
| sword-without-split | 251.9 | 126.1 | 64.0 | 66.4 | 67.7 | 1 |
| sword-without-deferred | 251.8 | 126.1 | 64.0 | 66.9 | 68.6 | 1 |
| sword-without-lanes | 251.6 | 126.0 | 63.3 | 66.3 | 68.1 | 1 |
| sword-without-steady | 251.8 | 126.0 | 64.0 | 67.9 | 68.0 | 1 |
| c-serial | 237.6 |  |  |  |  | 1 |
| c-restrict | 237.7 |  |  |  |  | 1 |
| c-omp | 238.7 | 119.7 | 60.0 | 63.1 | 63.7 | 1 |
| c-fastmath-serial | 237.8 |  |  |  |  | 1 |
| c-fastmath-omp | 244.4 | 122.3 | 61.4 | 64.9 | 65.8 | 1 |
| c-native-serial | 250.6 |  |  |  |  | 1 |
| c-native-omp | 248.9 | 124.5 | 62.6 | 67.4 | 65.6 | 1 |
| c-clang-serial | 243.6 |  |  |  |  | 1 |
| c-clang-omp | 246.5 | 123.4 | 61.9 | 64.8 | 64.6 | 1 |
| cpp-thread | 240.4 | 120.4 | 61.3 | 71.4 | 70.2 | 1 |
| rust-rayon | 239.0 | 119.9 | 60.2 | 61.0 | 61.9 | 1 |
| zig-safe | 272.0 | 137.2 | 71.6 | 80.3 | 85.6 | 1 |
| zig-fast | 271.8 | 137.1 | 71.7 | 80.5 | 85.0 | 1 |
| go | 252.5 | 126.8 | 63.9 | 69.9 | 67.5 | 1 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 254.0 | 127.3 | 127.0 | 127.5 | 128.7 | 1 |
| sword-native | 255.0 | 127.8 | 127.6 | 128.3 | 129.6 | 1 |
| sword-without-walked | 253.9 | 127.7 | 127.0 | 127.2 | 128.4 | 1 |
| sword-without-walked-mut | 253.9 | 127.3 | 127.0 | 127.3 | 129.0 | 1 |
| sword-without-captures | 254.2 | 127.4 | 127.0 | 127.5 | 128.5 | 1 |
| sword-without-versioned | 255.5 | 128.0 | 128.0 | 128.0 | 129.7 | 1 |
| sword-without-split | 254.0 | 127.3 | 127.0 | 127.4 | 128.6 | 1 |
| sword-without-deferred | 254.0 | 127.3 | 127.0 | 127.3 | 128.8 | 1 |
| sword-without-lanes | 254.1 | 127.3 | 127.0 | 127.3 | 129.2 | 1 |
| sword-without-steady | 254.0 | 127.3 | 127.1 | 127.4 | 128.5 | 1 |
| c-serial | 63.7 |  |  |  |  | 1 |
| c-restrict | 63.6 |  |  |  |  | 1 |
| c-omp | 115.9 | 58.1 | 53.3 | 53.8 | 55.5 | 1 |
| c-fastmath-serial | 63.6 |  |  |  |  | 1 |
| c-fastmath-omp | 63.7 | 32.0 | 31.8 | 34.1 | 32.4 | 1 |
| c-native-serial | 57.8 |  |  |  |  | 1 |
| c-native-omp | 107.1 | 53.7 | 55.1 | 56.2 | 57.2 | 1 |
| c-clang-serial | 254.9 |  |  |  |  | 1 |
| c-clang-omp | 256.9 | 128.0 | 127.3 | 131.2 | 132.5 | 1 |
| cpp-thread | 117.0 | 58.9 | 54.2 | 61.2 | 59.8 | 1 |
| rust-rayon | 256.7 | 128.7 | 128.2 | 128.7 | 128.8 | 1 |
| zig-safe | 254.7 | 128.9 | 129.5 | 138.1 | 138.7 | 1 |
| zig-fast | 255.0 | 129.1 | 129.7 | 137.7 | 139.7 | 1 |
| go | 454.8 | 228.4 | 143.0 | 151.5 | 150.2 | 1 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 95.3 | 54.8 | 41.4 | 31.6 | 35.7 | 1 |
| sword-native | 86.7 | 46.4 | 36.1 | 43.2 | 30.0 | 1 |
| sword-without-walked | 82.4 | 59.3 | 35.4 | 36.9 | 34.5 | 1 |
| sword-without-walked-mut | 88.8 | 44.8 | 29.5 | 34.9 | 29.7 | 1 |
| sword-without-captures | 82.1 | 48.9 | 32.9 | 32.6 | 37.0 | 1 |
| sword-without-versioned | 135.1 | 89.2 | 48.7 | 66.1 | 60.6 | 1 |
| sword-without-split | 90.0 | 64.0 | 39.1 | 33.5 | 43.8 | 1 |
| sword-without-deferred | 100.4 | 55.1 | 32.1 | 31.9 | 31.3 | 1 |
| sword-without-lanes | 95.9 | 65.4 | 43.1 | 31.5 | 34.7 | 1 |
| sword-without-steady | 96.1 | 46.3 | 32.4 | 31.3 | 31.1 | 1 |
| c-serial | 84.2 |  |  |  |  | 1 |
| c-restrict | 83.8 |  |  |  |  | 1 |
| c-omp | 84.0 | 44.1 | 37.7 | 32.3 | 32.4 | 1 |
| c-fastmath-serial | 45.4 |  |  |  |  | 1 |
| c-fastmath-omp | 45.4 | 24.2 | 23.2 | 17.6 | 18.5 | 1 |
| c-native-serial | 80.7 |  |  |  |  | 1 |
| c-native-omp | 80.5 | 42.9 | 36.2 | 31.3 | 31.8 | 1 |
| c-clang-serial | 92.7 |  |  |  |  | 1 |
| c-clang-omp | 85.9 | 42.6 | 37.8 | 33.2 | 32.5 | 1 |
| cpp-thread | 90.6 | 42.0 | 38.2 | 32.8 | 33.4 | 1 |
| rust-rayon | 88.3 | 45.4 | 54.9 | 56.0 | 45.6 | 1 |
| zig-safe | 144.5 | 65.1 | 50.9 | 50.7 | 53.5 | 1 |
| zig-fast | 140.8 | 70.7 | 49.5 | 54.5 | 54.3 | 1 |
| go | 116.1 | 59.1 | 44.1 | 47.3 | 42.0 | 1 |

## hist

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 8.3 | 4.3 | 2.2 | 2.6 | 2.8 | 1 |
| sword-native | 7.8 | 3.9 | 2.0 | 2.4 | 2.3 | 1 |
| c-serial | 7.9 |  |  |  |  | 1 |
| c-omp | 7.8 | 3.9 | 2.2 | 2.7 | 2.7 | 10 |
| c-fastmath-serial | 8.1 |  |  |  |  | 1 |
| c-fastmath-omp | 8.2 | 4.1 | 2.1 | 2.1 | 2.6 | 10 |
| c-native-serial | 8.0 |  |  |  |  | 1 |
| c-native-omp | 8.0 | 4.0 | 2.0 | 2.0 | 2.5 | 11 |
| c-clang-serial | 8.0 |  |  |  |  | 1 |
| c-clang-omp | 7.8 | 4.1 | 2.0 | 2.9 | 2.7 | 7 |
| cpp-thread | 8.6 | 4.4 | 2.7 | 2.6 | 3.0 | 5 |
| rust-rayon | 8.2 | 4.0 | 2.1 | 2.2 | 2.2 | 10 |
| zig-safe | 13.7 | 8.1 | 5.1 | 5.0 | 5.2 | 5 |
| zig-fast | 8.2 | 5.2 | 3.2 | 3.4 | 3.5 | 5 |
| go | 9.3 | 4.7 | 2.4 | 2.4 | 2.4 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 9.8 | 4.9 | 4.7 | 4.7 | 4.8 | 1 |
| sword-native | 6.1 | 3.1 | 2.6 | 2.7 | 2.7 | 1 |
| c-serial | 6.3 |  |  |  |  | 1 |
| c-omp | 6.5 | 3.3 | 2.7 | 2.7 | 3.2 | 11 |
| c-fastmath-serial | 6.3 |  |  |  |  | 1 |
| c-fastmath-omp | 6.5 | 3.3 | 2.7 | 3.0 | 3.0 | 11 |
| c-native-serial | 6.3 |  |  |  |  | 1 |
| c-native-omp | 6.5 | 3.3 | 2.7 | 2.7 | 2.9 | 11 |
| c-clang-serial | 6.4 |  |  |  |  | 1 |
| c-clang-omp | 6.2 | 3.1 | 2.5 | 3.6 | 3.1 | 7 |
| cpp-thread | 6.6 | 3.4 | 3.8 | 3.7 | 3.7 | 5 |
| rust-rayon | 13.4 | 6.8 | 6.4 | 6.5 | 6.6 | 11 |
| zig-safe | 8.7 | 6.4 | 4.4 | 5.7 | 5.6 | 5 |
| zig-fast | 6.5 | 4.7 | 4.1 | 4.4 | 3.8 | 5 |
| go | 6.5 | 4.4 | 3.1 | 3.2 | 3.1 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 5.4 | 2.7 | 1.9 | 1.9 | 1.9 | 1 |
| sword-native | 5.3 | 2.7 | 2.1 | 2.1 | 2.2 | 1 |
| c-serial | 5.0 |  |  |  |  | 1 |
| c-omp | 5.0 | 2.6 | 2.6 | 2.1 | 2.1 | 5 |
| c-fastmath-serial | 5.1 |  |  |  |  | 1 |
| c-fastmath-omp | 4.9 | 2.6 | 2.6 | 2.1 | 2.2 | 6 |
| c-native-serial | 5.0 |  |  |  |  | 1 |
| c-native-omp | 5.9 | 2.6 | 2.8 | 2.2 | 2.2 | 5 |
| c-clang-serial | 5.4 |  |  |  |  | 1 |
| c-clang-omp | 5.2 | 2.8 | 2.8 | 2.2 | 2.3 | 6 |
| cpp-thread | 5.0 | 2.7 | 2.9 | 2.2 | 2.2 | 5 |
| rust-rayon | 5.4 | 3.1 | 2.0 | 1.9 | 2.1 | 11 |
| zig-safe | 7.0 | 4.6 | 4.2 | 3.5 | 3.4 | 5 |
| zig-fast | 4.6 | 2.8 | 2.6 | 2.1 | 2.3 | 5 |
| go | 6.2 | 3.3 | 3.1 | 2.5 | 2.4 | 5 |

## scan

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 16.0 | 8.3 | 4.6 | 5.5 | 6.1 | 1 |
| sword-native | 16.5 | 9.2 | 4.6 | 5.5 | 6.0 | 1 |
| c-serial | 7.0 |  |  |  |  | 1 |
| c-omp | 13.9 | 7.0 | 3.7 | 3.9 | 4.8 | 4 |
| c-fastmath-serial | 7.0 |  |  |  |  | 1 |
| c-fastmath-omp | 13.6 | 7.1 | 3.5 | 4.6 | 4.4 | 4 |
| c-native-serial | 7.1 |  |  |  |  | 1 |
| c-native-omp | 14.0 | 7.0 | 3.5 | 3.9 | 4.8 | 4 |
| c-clang-serial | 7.0 |  |  |  |  | 1 |
| c-clang-omp | 13.6 | 7.1 | 3.5 | 5.5 | 4.6 | 4 |
| cpp-thread | 14.0 | 7.2 | 4.0 | 5.4 | 5.0 | 4 |
| rust-rayon | 14.0 | 6.9 | 3.7 | 3.7 | 3.7 | 4 |
| zig-safe | 15.2 | 8.0 | 4.7 | 6.1 | 6.7 | 4 |
| zig-fast | 14.9 | 7.6 | 4.6 | 5.9 | 6.3 | 4 |
| go | 13.7 | 6.9 | 3.8 | 4.7 | 5.0 | 4 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 27.5 | 13.8 | 8.4 | 8.9 | 9.5 | 1 |
| sword-native | 27.5 | 13.8 | 8.4 | 8.7 | 9.4 | 1 |
| c-serial | 8.3 |  |  |  |  | 1 |
| c-omp | 16.5 | 8.3 | 5.8 | 6.4 | 5.8 | 4 |
| c-fastmath-serial | 8.3 |  |  |  |  | 1 |
| c-fastmath-omp | 16.5 | 8.3 | 5.7 | 6.0 | 6.3 | 4 |
| c-native-serial | 8.2 |  |  |  |  | 1 |
| c-native-omp | 16.5 | 8.3 | 5.9 | 6.2 | 6.7 | 4 |
| c-clang-serial | 8.3 |  |  |  |  | 1 |
| c-clang-omp | 16.5 | 8.3 | 5.9 | 7.1 | 7.7 | 4 |
| cpp-thread | 16.7 | 8.5 | 6.0 | 7.5 | 7.4 | 4 |
| rust-rayon | 16.5 | 8.4 | 5.8 | 5.9 | 6.0 | 4 |
| zig-safe | 17.0 | 9.0 | 7.0 | 8.7 | 9.0 | 4 |
| zig-fast | 17.0 | 9.0 | 7.1 | 8.8 | 9.2 | 4 |
| go | 16.5 | 8.3 | 5.9 | 6.1 | 6.1 | 4 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 20.0 | 11.8 | 8.6 | 9.3 | 7.7 | 1 |
| sword-native | 22.6 | 11.4 | 8.6 | 8.6 | 8.7 | 1 |
| c-serial | 10.1 |  |  |  |  | 1 |
| c-omp | 20.4 | 10.5 | 10.4 | 7.9 | 8.7 | 4 |
| c-fastmath-serial | 9.9 |  |  |  |  | 1 |
| c-fastmath-omp | 11.5 | 6.7 | 7.0 | 5.7 | 5.6 | 5 |
| c-native-serial | 10.3 |  |  |  |  | 1 |
| c-native-omp | 20.4 | 10.9 | 10.9 | 8.1 | 8.2 | 4 |
| c-clang-serial | 11.6 |  |  |  |  | 1 |
| c-clang-omp | 20.7 | 10.1 | 10.4 | 8.0 | 8.0 | 4 |
| cpp-thread | 21.1 | 10.5 | 11.2 | 8.4 | 9.0 | 4 |
| rust-rayon | 20.7 | 11.4 | 11.2 | 9.7 | 9.1 | 4 |
| zig-safe | 19.2 | 10.0 | 10.1 | 7.9 | 8.5 | 4 |
| zig-fast | 19.2 | 10.1 | 11.0 | 9.2 | 8.8 | 4 |
| go | 19.0 | 10.3 | 8.6 | 8.7 | 8.5 | 4 |

## sort

**gh-linux-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 169.9 | 87.2 | 47.1 | 50.1 | 51.1 | 1 |
| sword-native | 170.4 | 87.3 | 47.2 | 50.2 | 50.8 | 1 |
| c-serial | 64.2 |  |  |  |  | 1 |
| c-omp | 64.2 | 32.4 | 18.8 | 18.9 | 20.3 | 1 |
| c-fastmath-serial | 64.1 |  |  |  |  | 1 |
| c-fastmath-omp | 63.8 | 32.3 | 17.1 | 19.2 | 19.2 | 1 |
| c-native-serial | 63.2 |  |  |  |  | 1 |
| c-native-omp | 63.0 | 32.0 | 17.2 | 19.4 | 18.6 | 1 |
| c-clang-serial | 66.4 |  |  |  |  | 1 |
| c-clang-omp | 66.4 | 35.1 | 19.8 | 28.6 | 29.3 | 1 |
| cpp-thread | 28.5 | 14.9 | 9.0 | 10.9 | 11.7 | 5 |
| rust-rayon | 11.7 | 6.5 | 4.0 | 4.2 | 4.2 | 1 |
| zig-safe | 15.1 | 9.5 | 6.9 | 9.1 | 10.1 | 5 |
| zig-fast | 9.5 | 6.1 | 4.8 | 6.1 | 7.6 | 5 |
| go | 58.4 | 33.9 | 19.0 | 20.8 | 20.8 | 5 |

**gh-linux-x86_64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 186.7 | 95.0 | 68.4 | 68.7 | 70.5 | 1 |
| sword-native | 189.6 | 96.6 | 69.2 | 70.2 | 69.9 | 1 |
| c-serial | 91.9 |  |  |  |  | 1 |
| c-omp | 92.0 | 45.5 | 28.7 | 28.4 | 28.8 | 1 |
| c-fastmath-serial | 92.0 |  |  |  |  | 1 |
| c-fastmath-omp | 92.0 | 45.5 | 28.6 | 30.5 | 29.1 | 1 |
| c-native-serial | 92.0 |  |  |  |  | 1 |
| c-native-omp | 92.1 | 45.5 | 28.5 | 28.9 | 28.8 | 1 |
| c-clang-serial | 94.3 |  |  |  |  | 1 |
| c-clang-omp | 94.1 | 48.4 | 31.0 | 43.6 | 39.3 | 1 |
| cpp-thread | 36.3 | 19.0 | 12.4 | 14.7 | 14.8 | 5 |
| rust-rayon | 7.7 | 4.2 | 3.6 | 3.6 | 3.7 | 1 |
| zig-safe | 12.9 | 8.1 | 8.2 | 9.8 | 11.7 | 5 |
| zig-fast | 9.3 | 7.6 | 8.3 | 10.5 | 12.8 | 5 |
| go | 62.3 | 35.9 | 24.0 | 25.7 | 27.3 | 5 |

**gh-macos-arm64**, ms

| method | 1 | 2 | 4 | 8 | 16 | answers |
|---|---:|---:|---:|---:|---:|---:|
| sword | 188.1 | 94.1 | 68.8 | 68.3 | 73.3 | 1 |
| sword-native | 200.7 | 105.3 | 78.8 | 76.2 | 76.0 | 1 |
| c-serial | 41.4 |  |  |  |  | 1 |
| c-omp | 40.9 | 24.4 | 19.5 | 21.2 | 24.1 | 5 |
| c-fastmath-serial | 40.9 |  |  |  |  | 1 |
| c-fastmath-omp | 39.3 | 23.6 | 19.3 | 22.1 | 23.5 | 5 |
| c-native-serial | 39.0 |  |  |  |  | 1 |
| c-native-omp | 42.9 | 26.2 | 20.5 | 22.7 | 24.6 | 5 |
| c-clang-serial | 39.3 |  |  |  |  | 1 |
| c-clang-omp | 39.2 | 25.6 | 21.6 | 23.2 | 26.5 | 5 |
| cpp-thread | 31.7 | 19.7 | 16.5 | 18.0 | 19.4 | 5 |
| rust-rayon | 10.2 | 5.7 | 4.3 | 4.3 | 4.4 | 1 |
| zig-safe | 13.9 | 8.5 | 9.6 | 8.7 | 9.4 | 5 |
| zig-fast | 9.4 | 7.9 | 9.6 | 11.3 | 13.3 | 5 |
| go | 65.2 | 38.9 | 28.5 | 32.1 | 27.7 | 5 |

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
| c-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-restrict | 1 | 1 | 1 | 1 | 1 |  |  |  |
| c-omp | 8 | 1 | 1 | 1 | 1 | 22 | 4 | 6 |
| c-lanes | 1 |  |  |  |  |  |  |  |
| c-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-fastmath-serial | 3 | 1 | 2 | 2 | 1 | 1 | 1 | 2 |
| c-fastmath-omp | 13 | 1 | 2 | 2 | 1 | 22 | 8 | 6 |
| c-native-serial | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| c-native-omp | 9 | 1 | 1 | 1 | 1 | 21 | 4 | 6 |
| c-native-lanes | 1 |  |  |  |  |  |  |  |
| c-native-lanes-omp | 1 |  |  |  |  |  |  |  |
| c-clang-serial | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 |
| c-clang-omp | 5 | 1 | 1 | 2 | 1 | 10 | 4 | 6 |
| cpp-thread | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 10 |
| rust-rayon | 17 | 1 | 1 | 1 | 1 | 27 | 4 | 1 |
| rust-slices |  |  | 1 |  |  |  |  |  |
| zig-safe | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| zig-fast | 5 | 1 | 1 | 1 | 1 | 5 | 4 | 5 |
| go | 5 | 1 | 1 | 2 | 1 | 5 | 4 | 5 |
