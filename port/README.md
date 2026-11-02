# The port: what Sword can say, and what it cannot

Two suites written again in Sword, to count how much of ordinary parallel code
goes in as it is, how much has to be written another way, and how much cannot
be written in parallel at all. Sword infers det for every function and refuses
any program with a race, and that refusal has a price; this is where it is
measured.

- **PolyBench/C 4.2.1**, all 30 kernels (`polybench/`). Loop nests over
  arrays: linear algebra, solvers, stencils, data mining, dynamic programming.
- **The Cilk-5.4.6 examples** (`cilk/`): the recursive divide-and-conquer
  programs that came with Cilk-5 and are still the usual examples of
  fork-join parallelism. Seventeen of them: bucket, cholesky, cilksort, ck,
  fft, fib, game, heat, knapsack, lu, magic, matmul, plu, queens, rectmul,
  spacemul and strassen. Left out are the tests of the runtime (hello,
  nfib, velin, test-errno, test-locks, test-void-func, testall), the random
  number library (rand), the copies built as a library (cholesky-lib,
  nfib-lib) and kalah, which reads its moves from a person.

## What is counted, decided before any kernel was written

Each kernel is first read as a C programmer with OpenMP would read it: in
each loop nest, the parallel loop is the outermost one whose iterations carry
no dependence on each other, judged by the C code alone and not by what Sword
accepts. A temporary that each iteration fills before it reads counts as
private to it, as OpenMP's `private` would make it. A loop whose only carried
dependence is a sum is not taken as parallel: a parallel sum of floats
changes the bits in C as well, and what that costs is measured in E1 and E4.
A Cilk program's parallelism is its `spawn`s. That is the parallelism the
port tries to keep. Then each kernel goes in one of four
classes, the worst of its nests deciding:

| class | meaning |
|---|---|
| **as is** | the Sword program has the same loops in the same order, the parallel ones as `parallel for`, or the same `spawn`s; only the syntax changed |
| **rewritten** | every parallel loop or spawn is kept, but only after a change of form the C does not need: indexing a row through `chunks`, splitting a body into two loops, a temporary, passing state in a struct instead of a closure. The change is written down |
| **refused** | a loop or spawn that is legal and free of races in C cannot be made parallel in Sword in any form found, and stays sequential. The reason is written down |
| **sequential** | the C code has no parallel loop at all (every loop carries a dependence); it says nothing about Sword and is not counted against it |

Two Cilk forms are counted apart from the class. A Sword task returns
nothing and writes into memory its parent hands it, so `x = spawn f(n)`
becomes `spawn f(&x, n)`; that is taken as syntax, since it is the only way a
Sword task gives a value back. A spawn in a loop gives its value into its
own slot of an array cut by `chunks(1)`, added up after the scope, and that
is taken as syntax too. `abort` stops the spawns still running, so that a
search ends at the first answer found or at a cutoff; Sword has no way to
stop a sibling task, by design, so a port of a program that aborts keeps its
spawns and lets every child run to the end. Each such program says so, and
the class is decided by its spawns alone: a spawn that cannot be kept at a
cost the program can bear without its abort counts as refused.

The program must also give the same answer as the C reference: every output
array is compared bit for bit with PolyBench's own C, built with
`-ffp-contract=off` so that neither side fuses a multiply and an add, and the
Sword program gives the same bits at one thread and at four.

A Cilk program's reference is its serial elision: the `.cilk` file with
`cilk`, `spawn`, `sync`, `inlet` and `abort` taken out, which Cilk defines to
be a C program with the same meaning on one processor, built with GCC (an
inlet becomes a nested function, which Clang does not have). The Sword port
prints what the elision prints, less its timings, with the bits of any
floating point result.

PolyBench's sizes are its `SMALL_DATASET`, enough to exercise every loop; this is
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

## Cilk

`cilk/run.sh` downloads Cilk-5.4.6 at a pinned commit, checks its SHA-256,
builds each example's serial elision with GCC and its port with Shield, and
prints `program,class,same_answer,threads_agree`. Each port names at its top
the arguments it runs with, the lines of the C's output that are its answer,
and any `// Patch:` applied to the elision first: a patch prints the bits of
a floating point result the C prints rounded, or stands in for something the
elision cannot build (a macro of Cilk's headers in strassen, `inline`
without `static` in game and cholesky). All 17 give the same answer at one
thread and at four, and 16 give the C's:

| class | programs |
|---|---|
| as is (2) | fib, magic |
| rewritten (11) | cholesky, cilksort, ck, fft, heat, knapsack, plu, queens, rectmul, spacemul, strassen |
| refused (4) | bucket, game, lu, matmul |

heat is the one whose answer is not the C's, and only because its initial
grid is made with `sin` and `exp`: glibc's `sin` differs from `num.Sin` by one
unit in the last place at 13 of its 613 arguments. `cilk/libm/heat.sh` builds
the elision again with the values `std/num` gives in place of glibc's, and
then the bits are the same.

Each port says at its top why it is in its class. What the rewrites change,
by kind:

| what the C does | what Sword needs | programs |
|---|---|---|
| spawns on halves or quadrants of an array that are not runs of it: half of the columns, a quadrant stored a row after another | the array stored so that they are runs (Z order of blocks in cholesky and lu, quadrant order in spacemul, which the C already has), or a parallel loop over the whole blocks, each finding its own work, or a temporary laid out in the order the tasks write, copied across by rows | cholesky, fft, plu, rectmul, strassen |
| a task reads a part of an array that its siblings write other parts of | a copy of what it reads, taken before the spawns, because two pieces of one slice are the same memory to a task that is not given both | cholesky, plu |
| two arrays cut side by side, a run of each to one task, or one cut where its values say | the two held as one array of pairs (fft), or the recursion rewritten as levels whose pieces find their place by binary search (cilksort) | cilksort, fft |
| a search whose spawns share state: a bound, a killer table, an inlet that updates the parent | an atomic for the bound (knapsack), the heuristic dropped below the root (ck), the answers taken in order after the scope | ck, knapsack, queens |
| spawns on halves of the rows, and rows allocated in parallel with one `malloc` each | the halves as chunks of the rows, rounded up where the C rounds down; the grid one allocation, made before | heat |

Four are refused, each for one reason. In matmul and lu, a spawn writes half
of the columns of a block, which is two runs apart in any layout that also
keeps the halves of the rows; no form was found that hands it to a task,
so those halves run one after the other. bucket inserts each element into
the bucket its value names, under that bucket's lock, and places each run of
buckets where a prefix sum says: both write where the data says, and run in
sequence, while the prefix sum's tree keeps its parallelism a level at a
time. game is the one program whose spawns rest on abort: without it a
spawned move searches with the window its parent had, and spawning every
move did not find the first one in two minutes, against a fifth of a second
for the whole elision; the port spawns at the top three plies only. ck
aborts as game does, but spawns only after its first move has narrowed the
window, and there the whole game takes under two seconds at four threads.

Three classifications rest on a judgement the reader may want to check. ck
leaves out a heuristic, a table of killer moves every task reads and writes
without a lock, which is a race in the C; the port argues at its top why
no score or move it prints depends on it, and all 1871 lines of its answer
are the C's. In rectmul and spacemul every element of A and B is 1, so any
order of the additions gives the same bits; they are checked all the same,
but the check says less than elsewhere. fft's own input gives a transform
that is nearly all zeros, so `cilk/fftsizes.sh` compares it with the
elision at twelve sizes, chosen to reach every codelet and the general
radix, on an input that is not: all twelve give the C's bits at one thread
and at four. fft's codelets are translated statement by statement by
`cilk/fftgen.py`.

Writing these ports met three things in the checker that cost a rewrite
without protecting anything. The same two spawns written in both arms of an
`if`, each writing the same result, are refused as two writes, though only
one arm runs (rectmul chooses the halves before the scope instead). A
parallel loop over pieces takes no reduction (rectmul and spacemul count
their flops in a second walk). And a function whose tasks read one slice
and write another cannot be handed two slices taken from one array of
slices, although they are different memory, because the checker sees one
root (bucket copies the levels of its tree instead).

## Licence

The PolyBench ports are derived from PolyBench/C, and carry its notice:

```
Copyright (c) 2010-2016, Ohio State University. All rights reserved.
```

under the Ohio State University Software Distribution License that comes with
PolyBench/C (`polybench/LICENSE.txt`). The reference C is not kept here:
`polybench/run.sh` downloads PolyBench/C 4.2.1 and checks it against a pinned
SHA-256.

The Cilk ports are derived from the Cilk-5.4.6 examples, which are under the
GNU General Public License, version 2 or later, and so are they
(`cilk/COPYING`); every port says so at its top. The scripts beside them
(`run.sh`, `fftsizes.sh`, `fftgen.py`, `elision.h`, `libm/`) are written
for this repository and take nothing from Cilk's code. The Cilk sources are not kept here
either: `cilk/run.sh` downloads them and checks them against a pinned
SHA-256.
