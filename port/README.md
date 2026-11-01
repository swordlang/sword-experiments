# The port: what Sword can say, and what it cannot

Two suites written again in Sword, to count how much of ordinary parallel code
goes in as it is, how much has to be written another way, and how much cannot
be written in parallel at all. Sword infers det for every function and refuses
any program with a race, and that refusal has a price; this is where it is
measured.

- **PolyBench/C 4.2.1**, all 30 kernels (`polybench/`). Loop nests over
  arrays: linear algebra, solvers, stencils, data mining, dynamic programming.
- **The Cilk programs** (`cilk/`): the recursive divide-and-conquer programs
  that came with Cilk-5 and are still the usual examples of fork-join
  parallelism.

## What is counted, decided before any kernel was written

Each kernel is first read as a C programmer with OpenMP would read it: in
each loop nest, the parallel loop is the outermost one whose iterations carry
no dependence on each other, judged by the C code alone and not by what Sword
accepts. A temporary that each iteration fills before it reads counts as
private to it, as OpenMP's `private` would make it. A loop whose only carried
dependence is a sum is not taken as parallel: a parallel sum of floats
changes the bits in C as well, and what that costs is measured in E1 and E4.
A recursive Cilk program's parallelism is its `spawn`s. That is the
parallelism the port tries to keep. Then each kernel goes in one of four
classes, the worst of its nests deciding:

| class | meaning |
|---|---|
| **as is** | the Sword program has the same loops in the same order, the parallel ones as `parallel for`, or the same `spawn`s; only the syntax changed |
| **rewritten** | every parallel loop or spawn is kept, but only after a change of form the C does not need: indexing a row through `chunks`, splitting a body into two loops, a temporary, passing state in a struct instead of a closure. The change is written down |
| **refused** | a loop or spawn that is legal and free of races in C cannot be made parallel in Sword in any form found, and stays sequential. The reason is written down |
| **sequential** | the C code has no parallel loop at all (every loop carries a dependence); it says nothing about Sword and is not counted against it |

The program must also give the same answer as the C reference: every output
array is compared bit for bit with PolyBench's own C, built with
`-ffp-contract=off` so that neither side fuses a multiply and an add, and the
Sword program gives the same bits at one thread and at four.

Sizes are PolyBench's `SMALL_DATASET`, enough to exercise every loop; this is
about what can be written, not how fast it runs. Only the kernel function is
counted; the setup and the dump are written as plain loops.

## PolyBench

`polybench/run.sh` builds each kernel both ways and prints
`kernel,class,same_bits,threads_agree`. All 30 give PolyBench's bits, and the
same bits at one thread and at four:

| class | kernels |
|---|---|
| as is (6) | atax, bicg, durbin, gesummv, jacobi-1d, mvt |
| rewritten (20) | 2mm, 3mm, adi, correlation, covariance, deriche, doitgen, fdtd-2d, floyd-warshall, gemm, gemver, gramschmidt, heat-3d, jacobi-2d, lu, ludcmp, symm, syr2k, syrk, trmm |
| refused (0) | |
| sequential (4) | cholesky, nussinov, seidel-2d, trisolv |

Each port says at its top why it is in its class. The twenty rewrites are of
four kinds, and the first is most of them:

| what C does | what Sword needs | kernels |
|---|---|---|
| a parallel loop over `i` writes row `i` of a two-dimensional array | the rows as the pieces of `a.chunks(width)`, since a parallel loop over a range may write only `a[i]` | 2mm, 3mm, fdtd-2d, gemm, gemver, heat-3d, jacobi-2d, syr2k, syrk; doitgen also makes its temporary an array of the piece's own |
| the parallel loop writes a column | the array kept or copied transposed, or a temporary and a second loop that copies across, because a slice is cut into rows and never into columns | adi, correlation, covariance, deriche, gramschmidt, symm |
| the parallel loop reads, at other places, the array it writes, places no iteration changes | a copy of what is read, taken before the loop: a row (floyd-warshall, lu, ludcmp) or the whole array (trmm), because two slices of one array count as the same memory however they are cut | floyd-warshall, lu, ludcmp, trmm |

Three classifications rest on a judgement the reader may want to check.
atax and bicg are "as is" because the C kernel has a parallel loop that
clears an output; in bicg it is the only one, and its main nest is
sequential. floyd-warshall's parallel loop is the one every parallel
Floyd–Warshall runs, but it is free of dependences only because step `k`
leaves row `k` as it is, which follows from the values (`path[k][k]` is never
negative) and not from the loops. In trmm the C's parallel loop is the inner
`j`; with a copy of `B` the Sword port runs the outer `i` in parallel
instead, which is more parallelism than the C had, bought with one more array.

deriche is in `float`. Its constants come from `expf` and `powf` in C; Sword
has neither for `f32`, so the port takes them in `f64` with `num.Exp` and
`num.Log` and rounds, and they come out with the same bits.

## Licence

The PolyBench ports are derived from PolyBench/C, and carry its notice:

```
Copyright (c) 2010-2016, Ohio State University. All rights reserved.
```

under the Ohio State University Software Distribution License that comes with
PolyBench/C (`polybench/LICENSE.txt`). The reference C is not kept here:
`polybench/run.sh` downloads PolyBench/C 4.2.1 and checks it against a pinned
SHA-256.
