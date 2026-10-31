// The five kernels of the comparison in C++, with std::thread: the range is
// cut into one block per thread, and partial sums are combined in block order.
//
//   bench <kernel> <threads> [reps]
//
// Prints: kernel,method,threads,check,median_ns
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <thread>
#include <vector>

constexpr long SumN = 10000000;
constexpr long SaxpyN = 10000000;
constexpr long GridW = 2048;
constexpr int GridSteps = 10;
constexpr long MandelW = 2000;
constexpr int MandelIter = 256;
constexpr long Bodies = 4096;
constexpr int BodySteps = 4;

static int threads = 1;

// splitmix64 of seed + i, scaled to [0, 1): every language draws the same bits.
static double unit(uint64_t seed, uint64_t i) {
  uint64_t z = seed + i + 0x9e3779b97f4a7c15ULL;
  z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
  z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
  z ^= z >> 31;
  return static_cast<double>(z >> 11) / 9007199254740992.0;
}

static void fill(uint64_t seed, std::vector<double> &xs) {
  for (size_t i = 0; i < xs.size(); i++) xs[i] = unit(seed, i);
}

// The checksum of an array is its sum in index order, outside the timing.
static double total(const std::vector<double> &xs) {
  double s = 0.0;
  for (double x : xs) s += x;
  return s;
}

// Calls body(lo, hi, k) on block k of [0, n), one thread per block.
template <class F> static void blocks(long n, F body) {
  std::vector<std::thread> pool;
  for (int k = 0; k < threads; k++) {
    long lo = n * k / threads, hi = n * (k + 1) / threads;
    pool.emplace_back(body, lo, hi, k);
  }
  for (auto &t : pool) t.join();
}

static double sum(const std::vector<double> &xs) {
  std::vector<double> part(threads);
  blocks(xs.size(), [&](long lo, long hi, int k) {
    double s = 0.0;
    for (long i = lo; i < hi; i++) s += xs[i];
    part[k] = s;
  });
  double s = 0.0;
  for (double p : part) s += p;
  return s;
}

static void saxpy(double a, const std::vector<double> &x, std::vector<double> &y) {
  blocks(y.size(), [&](long lo, long hi, int) {
    for (long i = lo; i < hi; i++) y[i] = a * x[i] + y[i];
  });
}

static void step(long w, const std::vector<double> &a, std::vector<double> &b) {
  blocks(w, [&](long lo, long hi, int) {
    for (long i = lo; i < hi; i++)
      for (long j = 0; j < w; j++) {
        long k = i * w + j;
        if (i == 0 || j == 0 || i == w - 1 || j == w - 1)
          b[k] = a[k];
        else
          b[k] = 0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w]);
      }
  });
}

static long row(long w, long i, int max) {
  long count = 0;
  double cy = 2.5 * static_cast<double>(i) / w - 1.25;
  for (long j = 0; j < w; j++) {
    double cx = 2.5 * static_cast<double>(j) / w - 2.0;
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

// Rows are dealt round-robin, since the ones near the middle cost the most.
static long mandel(long w, int max) {
  std::vector<long> part(threads);
  std::vector<std::thread> pool;
  for (int k = 0; k < threads; k++)
    pool.emplace_back([&, k] {
      long c = 0;
      for (long i = k; i < w; i += threads) c += row(w, i, max);
      part[k] = c;
    });
  for (auto &t : pool) t.join();
  long count = 0;
  for (long c : part) count += c;
  return count;
}

static void nbody_step(long n, double m, std::vector<double> &p, std::vector<double> &v,
                       std::vector<double> &a) {
  const double *px = p.data(), *py = px + n, *pz = py + n;
  blocks(n, [&](long lo, long hi, int) {
    for (long i = lo; i < hi; i++) {
      double sx = 0.0, sy = 0.0, sz = 0.0;
      for (long j = 0; j < n; j++) {
        double dx = px[j] - px[i], dy = py[j] - py[i], dz = pz[j] - pz[i];
        double d = dx * dx + dy * dy + dz * dz + 0.01;
        double f = m / (d * std::sqrt(d));
        sx += dx * f;
        sy += dy * f;
        sz += dz * f;
      }
      a[i] = sx;
      a[n + i] = sy;
      a[2 * n + i] = sz;
    }
  });
  blocks(3 * n, [&](long lo, long hi, int) {
    for (long i = lo; i < hi; i++) {
      v[i] += a[i] * 0.001;
      p[i] += v[i] * 0.001;
    }
  });
}

static uint64_t bits(double v) {
  uint64_t b;
  std::memcpy(&b, &v, 8);
  return b;
}

int main(int argc, char **argv) {
  if (argc < 3) {
    std::fprintf(stderr, "usage: bench sum|saxpy|stencil|mandelbrot|nbody threads [reps]\n");
    return 2;
  }
  std::string kernel = argv[1];
  threads = std::atoi(argv[2]);
  int reps = argc > 3 ? std::atoi(argv[3]) : 5;
  std::vector<double> times(reps);
  uint64_t check = 0;
  bool hex = true;
  auto timed = [&](int r, auto body) {
    auto t0 = std::chrono::steady_clock::now();
    body();
    times[r] = std::chrono::duration<double, std::nano>(std::chrono::steady_clock::now() - t0).count();
  };

  if (kernel == "sum") {
    std::vector<double> xs(SumN);
    fill(1, xs);
    for (double &x : xs) x = 2.0 * x - 1.0;
    double s = 0.0;
    for (int r = 0; r < reps; r++) timed(r, [&] { s = sum(xs); });
    check = bits(s);
  } else if (kernel == "saxpy") {
    std::vector<double> x(SaxpyN), y(SaxpyN);
    fill(1, x);
    for (int r = 0; r < reps; r++) {
      fill(2, y);
      timed(r, [&] { saxpy(1.5, x, y); });
    }
    check = bits(total(y));
  } else if (kernel == "stencil") {
    std::vector<double> a(GridW * GridW), b(GridW * GridW);
    for (int r = 0; r < reps; r++) {
      fill(1, a);
      timed(r, [&] {
        for (int s = 0; s < GridSteps / 2; s++) {
          step(GridW, a, b);
          step(GridW, b, a);
        }
      });
    }
    check = bits(total(a));
  } else if (kernel == "mandelbrot") {
    long n = 0;
    for (int r = 0; r < reps; r++) timed(r, [&] { n = mandel(MandelW, MandelIter); });
    check = n;
    hex = false;
  } else if (kernel == "nbody") {
    std::vector<double> p(3 * Bodies), v(3 * Bodies), a(3 * Bodies);
    for (int r = 0; r < reps; r++) {
      fill(1, p);
      fill(2, v);
      for (double &x : v) x = 0.01 * (x - 0.5);
      timed(r, [&] {
        for (int s = 0; s < BodySteps; s++) nbody_step(Bodies, 1.0 / Bodies, p, v, a);
      });
    }
    check = bits(total(p));
  } else {
    std::fprintf(stderr, "unknown kernel\n");
    return 2;
  }
  std::sort(times.begin(), times.end());
  std::printf(hex ? "%s,cpp-thread,%d,%llx,%.0f\n" : "%s,cpp-thread,%d,%llu,%.0f\n", kernel.c_str(),
              threads, static_cast<unsigned long long>(check), times[reps / 2]);
}
