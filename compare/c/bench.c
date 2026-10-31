// The five kernels of the comparison in C.
//
//   serial    plain loops, one thread
//   restrict  the same loops with every pointer restrict-qualified
//   omp       #pragma omp parallel for, the way it is usually written
//
//   bench <kernel> serial|restrict|omp <threads> [reps]
//
// Prints: kernel,method,threads,check,median_ns
#include <math.h>
#include <omp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

enum {
  SumN = 10000000,
  SaxpyN = 10000000,
  GridW = 2048,
  GridSteps = 10,
  MandelW = 2000,
  MandelIter = 256,
  Bodies = 4096,
  BodySteps = 4,
};

// splitmix64 of seed + i, scaled to [0, 1): every language draws the same bits.
static double unit(uint64_t seed, uint64_t i) {
  uint64_t z = seed + i + 0x9e3779b97f4a7c15ULL;
  z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
  z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
  z ^= z >> 31;
  return (double)(z >> 11) / 9007199254740992.0;
}

static void fill(uint64_t seed, double *xs, long n) {
  for (long i = 0; i < n; i++) xs[i] = unit(seed, i);
}

// The checksum of an array is its sum in index order, outside the timing.
static double total(const double *xs, long n) {
  double s = 0.0;
  for (long i = 0; i < n; i++) s += xs[i];
  return s;
}

static double sum_serial(const double *xs, long n) {
  double s = 0.0;
  for (long i = 0; i < n; i++) s += xs[i];
  return s;
}

static double sum_omp(const double *xs, long n) {
  double s = 0.0;
#pragma omp parallel for reduction(+ : s) schedule(static)
  for (long i = 0; i < n; i++) s += xs[i];
  return s;
}

static void saxpy_serial(double a, const double *x, double *y, long n) {
  for (long i = 0; i < n; i++) y[i] = a * x[i] + y[i];
}

static void saxpy_restrict(double a, const double *restrict x, double *restrict y, long n) {
  for (long i = 0; i < n; i++) y[i] = a * x[i] + y[i];
}

static void saxpy_omp(double a, const double *x, double *y, long n) {
#pragma omp parallel for schedule(static)
  for (long i = 0; i < n; i++) y[i] = a * x[i] + y[i];
}

static void step_serial(long w, const double *a, double *b) {
  for (long i = 0; i < w; i++)
    for (long j = 0; j < w; j++) {
      long k = i * w + j;
      if (i == 0 || j == 0 || i == w - 1 || j == w - 1)
        b[k] = a[k];
      else
        b[k] = 0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w]);
    }
}

static void step_restrict(long w, const double *restrict a, double *restrict b) {
  for (long i = 0; i < w; i++)
    for (long j = 0; j < w; j++) {
      long k = i * w + j;
      if (i == 0 || j == 0 || i == w - 1 || j == w - 1)
        b[k] = a[k];
      else
        b[k] = 0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w]);
    }
}

static void step_omp(long w, const double *a, double *b) {
#pragma omp parallel for schedule(static)
  for (long i = 0; i < w; i++)
    for (long j = 0; j < w; j++) {
      long k = i * w + j;
      if (i == 0 || j == 0 || i == w - 1 || j == w - 1)
        b[k] = a[k];
      else
        b[k] = 0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w]);
    }
}

static long row(long w, long i, int max) {
  long count = 0;
  double cy = 2.5 * (double)i / (double)w - 1.25;
  for (long j = 0; j < w; j++) {
    double cx = 2.5 * (double)j / (double)w - 2.0;
    double zr = 0.0, zi = 0.0;
    int it = 0;
    while (it < max && zr * zr + zi * zi <= 4.0) {
      double t = zr * zr - zi * zi + cx;
      zi = 2.0 * zr * zi + cy;
      zr = t;
      it++;
    }
    count += it;
  }
  return count;
}

static long mandel_serial(long w, int max) {
  long count = 0;
  for (long i = 0; i < w; i++) count += row(w, i, max);
  return count;
}

// Rows near the middle cost far more than the edges, hence dynamic.
static long mandel_omp(long w, int max) {
  long count = 0;
#pragma omp parallel for reduction(+ : count) schedule(dynamic)
  for (long i = 0; i < w; i++) count += row(w, i, max);
  return count;
}

static void accel_serial(long n, double m, const double *px, const double *py,
                         const double *pz, double *ax, double *ay, double *az) {
  for (long i = 0; i < n; i++) {
    double sx = 0.0, sy = 0.0, sz = 0.0;
    for (long j = 0; j < n; j++) {
      double dx = px[j] - px[i], dy = py[j] - py[i], dz = pz[j] - pz[i];
      double d = dx * dx + dy * dy + dz * dz + 0.01;
      double f = m / (d * sqrt(d));
      sx += dx * f;
      sy += dy * f;
      sz += dz * f;
    }
    ax[i] = sx;
    ay[i] = sy;
    az[i] = sz;
  }
}

static void accel_restrict(long n, double m, const double *restrict px,
                           const double *restrict py, const double *restrict pz,
                           double *restrict ax, double *restrict ay, double *restrict az) {
  for (long i = 0; i < n; i++) {
    double sx = 0.0, sy = 0.0, sz = 0.0;
    for (long j = 0; j < n; j++) {
      double dx = px[j] - px[i], dy = py[j] - py[i], dz = pz[j] - pz[i];
      double d = dx * dx + dy * dy + dz * dz + 0.01;
      double f = m / (d * sqrt(d));
      sx += dx * f;
      sy += dy * f;
      sz += dz * f;
    }
    ax[i] = sx;
    ay[i] = sy;
    az[i] = sz;
  }
}

static void accel_omp(long n, double m, const double *px, const double *py,
                      const double *pz, double *ax, double *ay, double *az) {
#pragma omp parallel for schedule(static)
  for (long i = 0; i < n; i++) {
    double sx = 0.0, sy = 0.0, sz = 0.0;
    for (long j = 0; j < n; j++) {
      double dx = px[j] - px[i], dy = py[j] - py[i], dz = pz[j] - pz[i];
      double d = dx * dx + dy * dy + dz * dz + 0.01;
      double f = m / (d * sqrt(d));
      sx += dx * f;
      sy += dy * f;
      sz += dz * f;
    }
    ax[i] = sx;
    ay[i] = sy;
    az[i] = sz;
  }
}

static void move_serial(long n, double dt, const double *a, double *v, double *p) {
  for (long i = 0; i < n; i++) {
    v[i] += a[i] * dt;
    p[i] += v[i] * dt;
  }
}

static void move_restrict(long n, double dt, const double *restrict a, double *restrict v,
                          double *restrict p) {
  for (long i = 0; i < n; i++) {
    v[i] += a[i] * dt;
    p[i] += v[i] * dt;
  }
}

static void move_omp(long n, double dt, const double *a, double *v, double *p) {
#pragma omp parallel for schedule(static)
  for (long i = 0; i < n; i++) {
    v[i] += a[i] * dt;
    p[i] += v[i] * dt;
  }
}

static double now_ns(void) {
  struct timespec t;
  clock_gettime(CLOCK_MONOTONIC, &t);
  return t.tv_sec * 1e9 + t.tv_nsec;
}

static int cmp(const void *a, const void *b) {
  double x = *(const double *)a, y = *(const double *)b;
  return (x > y) - (x < y);
}

static uint64_t bits(double v) {
  uint64_t b;
  memcpy(&b, &v, 8);
  return b;
}

int main(int argc, char **argv) {
  if (argc < 4) {
    fprintf(stderr, "usage: bench sum|saxpy|stencil|mandelbrot|nbody serial|restrict|omp threads [reps]\n");
    return 2;
  }
  const char *kernel = argv[1], *method = argv[2];
  int threads = atoi(argv[3]);
  int reps = argc > 4 ? atoi(argv[4]) : 5;
  int m = !strcmp(method, "serial") ? 0 : !strcmp(method, "restrict") ? 1 : 2;
  omp_set_num_threads(threads);
  double *times = malloc(reps * sizeof *times);
  uint64_t check = 0;
  int hex = 1;

  if (!strcmp(kernel, "sum")) {
    double *xs = malloc(SumN * sizeof *xs), s = 0.0;
    fill(1, xs, SumN);
    for (long i = 0; i < SumN; i++) xs[i] = 2.0 * xs[i] - 1.0;
    for (int r = 0; r < reps; r++) {
      double t0 = now_ns();
      s = m == 2 ? sum_omp(xs, SumN) : sum_serial(xs, SumN);
      times[r] = now_ns() - t0;
    }
    check = bits(s);
  } else if (!strcmp(kernel, "saxpy")) {
    double *x = malloc(SaxpyN * sizeof *x), *y = malloc(SaxpyN * sizeof *y);
    fill(1, x, SaxpyN);
    for (int r = 0; r < reps; r++) {
      fill(2, y, SaxpyN);
      double t0 = now_ns();
      if (m == 0) saxpy_serial(1.5, x, y, SaxpyN);
      else if (m == 1) saxpy_restrict(1.5, x, y, SaxpyN);
      else saxpy_omp(1.5, x, y, SaxpyN);
      times[r] = now_ns() - t0;
    }
    check = bits(total(y, SaxpyN));
  } else if (!strcmp(kernel, "stencil")) {
    double *a = malloc(GridW * GridW * sizeof *a), *b = malloc(GridW * GridW * sizeof *b);
    void (*step)(long, const double *, double *) =
        m == 0 ? step_serial : m == 1 ? step_restrict : step_omp;
    for (int r = 0; r < reps; r++) {
      fill(1, a, GridW * GridW);
      double t0 = now_ns();
      for (int s = 0; s < GridSteps / 2; s++) {
        step(GridW, a, b);
        step(GridW, b, a);
      }
      times[r] = now_ns() - t0;
    }
    check = bits(total(a, GridW * GridW));
  } else if (!strcmp(kernel, "mandelbrot")) {
    long n = 0;
    for (int r = 0; r < reps; r++) {
      double t0 = now_ns();
      n = m == 2 ? mandel_omp(MandelW, MandelIter) : mandel_serial(MandelW, MandelIter);
      times[r] = now_ns() - t0;
    }
    check = n;
    hex = 0;
  } else if (!strcmp(kernel, "nbody")) {
    long n = Bodies;
    double *p = malloc(3 * n * sizeof *p), *v = malloc(3 * n * sizeof *v),
           *a = malloc(3 * n * sizeof *a), mass = 1.0 / n;
    for (int r = 0; r < reps; r++) {
      fill(1, p, 3 * n);
      fill(2, v, 3 * n);
      for (long i = 0; i < 3 * n; i++) v[i] = 0.01 * (v[i] - 0.5);
      double t0 = now_ns();
      for (int s = 0; s < BodySteps; s++) {
        if (m == 0) {
          accel_serial(n, mass, p, p + n, p + 2 * n, a, a + n, a + 2 * n);
          move_serial(3 * n, 0.001, a, v, p);
        } else if (m == 1) {
          accel_restrict(n, mass, p, p + n, p + 2 * n, a, a + n, a + 2 * n);
          move_restrict(3 * n, 0.001, a, v, p);
        } else {
          accel_omp(n, mass, p, p + n, p + 2 * n, a, a + n, a + 2 * n);
          move_omp(3 * n, 0.001, a, v, p);
        }
      }
      times[r] = now_ns() - t0;
    }
    check = bits(total(p, 3 * n));
  } else {
    fprintf(stderr, "unknown kernel\n");
    return 2;
  }
  qsort(times, reps, sizeof *times, cmp);
  printf(hex ? "%s,c-%s,%d,%llx,%.0f\n" : "%s,c-%s,%d,%llu,%.0f\n", kernel, method, threads,
         (unsigned long long)check, times[reps / 2]);
  return 0;
}
