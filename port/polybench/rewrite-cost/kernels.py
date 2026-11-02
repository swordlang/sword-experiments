"""The nine PolyBench kernels whose Sword port adds work, twice each in C
with OpenMP: as the C has them, the parallel loop the port's README names
marked, and rewritten the way the Sword port is (the copy, the transpose,
the split loop), the same loops marked. The ratio of the two is what the
rewrite costs, with the language out of it.

    python3 -I kernels.py <polybench> <out dir>

Prints each kernel and the directory of its header, for run.sh.
"""
import os
import re
import sys

P = "#pragma omp parallel for"

K = {}

K["lu"] = (
"""void kernel_lu(int n, DATA_TYPE POLYBENCH_2D(A,N,N,n,n))
{
  int i, j, k;
  for (i = 0; i < _PB_N; i++) {
    for (j = 0; j < i; j++) {
      for (k = 0; k < j; k++)
        A[i][j] -= A[i][k] * A[k][j];
      A[i][j] /= A[j][j];
    }
    %(P)s private(k)
    for (j = i; j < _PB_N; j++)
      for (k = 0; k < i; k++)
        A[i][j] -= A[i][k] * A[k][j];
  }
}""",
"""void kernel_lu(int n, DATA_TYPE POLYBENCH_2D(A,N,N,n,n))
{
  int i, j, k;
  static DATA_TYPE cur[N];
  for (i = 0; i < _PB_N; i++) {
    for (j = 0; j < i; j++) {
      for (k = 0; k < j; k++)
        A[i][j] -= A[i][k] * A[k][j];
      A[i][j] /= A[j][j];
    }
    for (j = 0; j < _PB_N; j++)
      cur[j] = A[i][j];
    %(P)s private(k)
    for (j = i; j < _PB_N; j++)
      for (k = 0; k < i; k++)
        cur[j] -= A[i][k] * A[k][j];
    for (j = i; j < _PB_N; j++)
      A[i][j] = cur[j];
  }
}""")

LUDCMP_TAIL = """
  for (i = 0; i < _PB_N; i++) {
    w = b[i];
    for (j = 0; j < i; j++)
      w -= A[i][j] * y[j];
    y[i] = w;
  }
  for (i = _PB_N - 1; i >= 0; i--) {
    w = y[i];
    for (j = i + 1; j < _PB_N; j++)
      w -= A[i][j] * x[j];
    x[i] = w / A[i][i];
  }
}"""

K["ludcmp"] = (
"""void kernel_ludcmp(int n, DATA_TYPE POLYBENCH_2D(A,N,N,n,n),
    DATA_TYPE POLYBENCH_1D(b,N,n), DATA_TYPE POLYBENCH_1D(x,N,n),
    DATA_TYPE POLYBENCH_1D(y,N,n))
{
  int i, j, k;
  DATA_TYPE w;
  for (i = 0; i < _PB_N; i++) {
    for (j = 0; j < i; j++) {
      w = A[i][j];
      for (k = 0; k < j; k++)
        w -= A[i][k] * A[k][j];
      A[i][j] = w / A[j][j];
    }
    %(P)s private(k, w)
    for (j = i; j < _PB_N; j++) {
      w = A[i][j];
      for (k = 0; k < i; k++)
        w -= A[i][k] * A[k][j];
      A[i][j] = w;
    }
  }""" + LUDCMP_TAIL,
"""void kernel_ludcmp(int n, DATA_TYPE POLYBENCH_2D(A,N,N,n,n),
    DATA_TYPE POLYBENCH_1D(b,N,n), DATA_TYPE POLYBENCH_1D(x,N,n),
    DATA_TYPE POLYBENCH_1D(y,N,n))
{
  int i, j, k;
  DATA_TYPE w;
  static DATA_TYPE cur[N];
  for (i = 0; i < _PB_N; i++) {
    for (j = 0; j < i; j++) {
      w = A[i][j];
      for (k = 0; k < j; k++)
        w -= A[i][k] * A[k][j];
      A[i][j] = w / A[j][j];
    }
    for (j = 0; j < _PB_N; j++)
      cur[j] = A[i][j];
    %(P)s private(k, w)
    for (j = i; j < _PB_N; j++) {
      w = cur[j];
      for (k = 0; k < i; k++)
        w -= A[i][k] * A[k][j];
      cur[j] = w;
    }
    for (j = i; j < _PB_N; j++)
      A[i][j] = cur[j];
  }""" + LUDCMP_TAIL)

K["floyd-warshall"] = (
"""void kernel_floyd_warshall(int n, DATA_TYPE POLYBENCH_2D(path,N,N,n,n))
{
  int i, j, k;
  for (k = 0; k < _PB_N; k++) {
    %(P)s private(j)
    for (i = 0; i < _PB_N; i++)
      for (j = 0; j < _PB_N; j++)
        path[i][j] = path[i][j] < path[i][k] + path[k][j] ?
          path[i][j] : path[i][k] + path[k][j];
  }
}""",
"""void kernel_floyd_warshall(int n, DATA_TYPE POLYBENCH_2D(path,N,N,n,n))
{
  int i, j, k;
  static DATA_TYPE rowk[N];
  for (k = 0; k < _PB_N; k++) {
    for (j = 0; j < _PB_N; j++)
      rowk[j] = path[k][j];
    %(P)s private(j)
    for (i = 0; i < _PB_N; i++)
      for (j = 0; j < _PB_N; j++)
        path[i][j] = path[i][j] < path[i][k] + rowk[j] ?
          path[i][j] : path[i][k] + rowk[j];
  }
}""")

K["trmm"] = (
"""void kernel_trmm(int m, int n, DATA_TYPE alpha,
    DATA_TYPE POLYBENCH_2D(A,M,M,m,m), DATA_TYPE POLYBENCH_2D(B,M,N,m,n))
{
  int i, j, k;
  for (i = 0; i < _PB_M; i++) {
    %(P)s private(k)
    for (j = 0; j < _PB_N; j++) {
      for (k = i + 1; k < _PB_M; k++)
        B[i][j] += A[k][i] * B[k][j];
      B[i][j] = alpha * B[i][j];
    }
  }
}""",
"""void kernel_trmm(int m, int n, DATA_TYPE alpha,
    DATA_TYPE POLYBENCH_2D(A,M,M,m,m), DATA_TYPE POLYBENCH_2D(B,M,N,m,n))
{
  int i, j, k;
  static DATA_TYPE B0[M][N];
  for (i = 0; i < _PB_M; i++)
    for (j = 0; j < _PB_N; j++)
      B0[i][j] = B[i][j];
  %(P)s private(j, k)
  for (i = 0; i < _PB_M; i++)
    for (j = 0; j < _PB_N; j++) {
      for (k = i + 1; k < _PB_M; k++)
        B[i][j] += A[k][i] * B0[k][j];
      B[i][j] = alpha * B[i][j];
    }
}""")

K["symm"] = (
"""void kernel_symm(int m, int n, DATA_TYPE alpha, DATA_TYPE beta,
    DATA_TYPE POLYBENCH_2D(C,M,N,m,n), DATA_TYPE POLYBENCH_2D(A,M,M,m,m),
    DATA_TYPE POLYBENCH_2D(B,M,N,m,n))
{
  int i, j, k;
  DATA_TYPE temp2;
  for (i = 0; i < _PB_M; i++) {
    %(P)s private(k, temp2)
    for (j = 0; j < _PB_N; j++) {
      temp2 = 0;
      for (k = 0; k < i; k++) {
        C[k][j] += alpha * B[i][j] * A[i][k];
        temp2 += B[k][j] * A[i][k];
      }
      C[i][j] = beta * C[i][j] + alpha * B[i][j] * A[i][i] + alpha * temp2;
    }
  }
}""",
"""void kernel_symm(int m, int n, DATA_TYPE alpha, DATA_TYPE beta,
    DATA_TYPE POLYBENCH_2D(C,M,N,m,n), DATA_TYPE POLYBENCH_2D(A,M,M,m,m),
    DATA_TYPE POLYBENCH_2D(B,M,N,m,n))
{
  int i, j, k;
  DATA_TYPE temp2;
  static DATA_TYPE Ct[N][M];
  %(P)s private(k)
  for (j = 0; j < _PB_N; j++)
    for (k = 0; k < _PB_M; k++)
      Ct[j][k] = C[k][j];
  %(P)s private(i, k, temp2)
  for (j = 0; j < _PB_N; j++)
    for (i = 0; i < _PB_M; i++) {
      temp2 = 0;
      for (k = 0; k < i; k++) {
        Ct[j][k] += alpha * B[i][j] * A[i][k];
        temp2 += B[k][j] * A[i][k];
      }
      Ct[j][i] = beta * Ct[j][i] + alpha * B[i][j] * A[i][i] + alpha * temp2;
    }
  %(P)s private(j)
  for (i = 0; i < _PB_M; i++)
    for (j = 0; j < _PB_N; j++)
      C[i][j] = Ct[j][i];
}""")

K["gramschmidt"] = (
"""void kernel_gramschmidt(int m, int n, DATA_TYPE POLYBENCH_2D(A,M,N,m,n),
    DATA_TYPE POLYBENCH_2D(R,N,N,n,n), DATA_TYPE POLYBENCH_2D(Q,M,N,m,n))
{
  int i, j, k;
  DATA_TYPE nrm;
  for (k = 0; k < _PB_N; k++) {
    nrm = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_M; i++)
      nrm += A[i][k] * A[i][k];
    R[k][k] = SQRT_FUN(nrm);
    %(P)s
    for (i = 0; i < _PB_M; i++)
      Q[i][k] = A[i][k] / R[k][k];
    %(P)s private(i)
    for (j = k + 1; j < _PB_N; j++) {
      R[k][j] = SCALAR_VAL(0.0);
      for (i = 0; i < _PB_M; i++)
        R[k][j] += Q[i][k] * A[i][j];
      for (i = 0; i < _PB_M; i++)
        A[i][j] = A[i][j] - Q[i][k] * R[k][j];
    }
  }
}""",
"""void kernel_gramschmidt(int m, int n, DATA_TYPE POLYBENCH_2D(A,M,N,m,n),
    DATA_TYPE POLYBENCH_2D(R,N,N,n,n), DATA_TYPE POLYBENCH_2D(Q,M,N,m,n))
{
  int i, j, k;
  DATA_TYPE nrm;
  for (k = 0; k < _PB_N; k++) {
    nrm = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_M; i++)
      nrm += A[i][k] * A[i][k];
    R[k][k] = SQRT_FUN(nrm);
    %(P)s
    for (i = 0; i < _PB_M; i++)
      Q[i][k] = A[i][k] / R[k][k];
    %(P)s private(i)
    for (j = k + 1; j < _PB_N; j++) {
      R[k][j] = SCALAR_VAL(0.0);
      for (i = 0; i < _PB_M; i++)
        R[k][j] += Q[i][k] * A[i][j];
    }
    %(P)s private(j)
    for (i = 0; i < _PB_M; i++)
      for (j = k + 1; j < _PB_N; j++)
        A[i][j] = A[i][j] - Q[i][k] * R[k][j];
  }
}""")

COV_HEAD = """void kernel_covariance(int m, int n, DATA_TYPE float_n,
    DATA_TYPE POLYBENCH_2D(data,N,M,n,m), DATA_TYPE POLYBENCH_2D(cov,M,M,m,m),
    DATA_TYPE POLYBENCH_1D(mean,M,m))
{
  int i, j, k;
  %(P)s private(i)
  for (j = 0; j < _PB_M; j++) {
    mean[j] = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_N; i++)
      mean[j] += data[i][j];
    mean[j] /= float_n;
  }
  %(P)s private(j)
  for (i = 0; i < _PB_N; i++)
    for (j = 0; j < _PB_M; j++)
      data[i][j] -= mean[j];
"""

K["covariance"] = (
COV_HEAD + """  %(P)s private(j, k)
  for (i = 0; i < _PB_M; i++)
    for (j = i; j < _PB_M; j++) {
      cov[i][j] = SCALAR_VAL(0.0);
      for (k = 0; k < _PB_N; k++)
        cov[i][j] += data[k][i] * data[k][j];
      cov[i][j] /= (float_n - SCALAR_VAL(1.0));
      cov[j][i] = cov[i][j];
    }
}""",
COV_HEAD + """  static DATA_TYPE up[M][M];
  %(P)s private(j, k)
  for (i = 0; i < _PB_M; i++)
    for (j = i; j < _PB_M; j++) {
      up[i][j] = SCALAR_VAL(0.0);
      for (k = 0; k < _PB_N; k++)
        up[i][j] += data[k][i] * data[k][j];
      up[i][j] /= (float_n - SCALAR_VAL(1.0));
    }
  %(P)s private(j)
  for (i = 0; i < _PB_M; i++)
    for (j = 0; j < _PB_M; j++)
      cov[i][j] = j >= i ? up[i][j] : up[j][i];
}""")

COR_HEAD = """void kernel_correlation(int m, int n, DATA_TYPE float_n,
    DATA_TYPE POLYBENCH_2D(data,N,M,n,m), DATA_TYPE POLYBENCH_2D(corr,M,M,m,m),
    DATA_TYPE POLYBENCH_1D(mean,M,m), DATA_TYPE POLYBENCH_1D(stddev,M,m))
{
  int i, j, k;
  DATA_TYPE eps = SCALAR_VAL(0.1);
  %(P)s private(i)
  for (j = 0; j < _PB_M; j++) {
    mean[j] = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_N; i++)
      mean[j] += data[i][j];
    mean[j] /= float_n;
  }
  %(P)s private(i)
  for (j = 0; j < _PB_M; j++) {
    stddev[j] = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_N; i++)
      stddev[j] += (data[i][j] - mean[j]) * (data[i][j] - mean[j]);
    stddev[j] /= float_n;
    stddev[j] = SQRT_FUN(stddev[j]);
    stddev[j] = stddev[j] <= eps ? SCALAR_VAL(1.0) : stddev[j];
  }
  %(P)s private(j)
  for (i = 0; i < _PB_N; i++)
    for (j = 0; j < _PB_M; j++) {
      data[i][j] -= mean[j];
      data[i][j] /= SQRT_FUN(float_n) * stddev[j];
    }
"""

K["correlation"] = (
COR_HEAD + """  %(P)s private(j, k)
  for (i = 0; i < _PB_M - 1; i++) {
    corr[i][i] = SCALAR_VAL(1.0);
    for (j = i + 1; j < _PB_M; j++) {
      corr[i][j] = SCALAR_VAL(0.0);
      for (k = 0; k < _PB_N; k++)
        corr[i][j] += (data[k][i] * data[k][j]);
      corr[j][i] = corr[i][j];
    }
  }
  corr[_PB_M - 1][_PB_M - 1] = SCALAR_VAL(1.0);
}""",
COR_HEAD + """  static DATA_TYPE up[M][M];
  %(P)s private(j, k)
  for (i = 0; i < _PB_M; i++)
    for (j = i + 1; j < _PB_M; j++) {
      up[i][j] = SCALAR_VAL(0.0);
      for (k = 0; k < _PB_N; k++)
        up[i][j] += (data[k][i] * data[k][j]);
    }
  %(P)s private(j)
  for (i = 0; i < _PB_M; i++)
    for (j = 0; j < _PB_M; j++)
      corr[i][j] = j > i ? up[i][j] : j < i ? up[j][i] : SCALAR_VAL(1.0);
}""")

DER_HEAD = """void kernel_deriche(int w, int h, DATA_TYPE alpha,
    DATA_TYPE POLYBENCH_2D(imgIn, W, H, w, h), DATA_TYPE POLYBENCH_2D(imgOut, W, H, w, h),
    DATA_TYPE POLYBENCH_2D(y1, W, H, w, h), DATA_TYPE POLYBENCH_2D(y2, W, H, w, h))
{
  int i, j;
  DATA_TYPE xm1, tm1, ym1, ym2, xp1, xp2, tp1, tp2, yp1, yp2;
  DATA_TYPE k, a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, c1, c2;
  k = (SCALAR_VAL(1.0)-EXP_FUN(-alpha))*(SCALAR_VAL(1.0)-EXP_FUN(-alpha))/(SCALAR_VAL(1.0)+SCALAR_VAL(2.0)*alpha*EXP_FUN(-alpha)-EXP_FUN(SCALAR_VAL(2.0)*alpha));
  a1 = a5 = k;
  a2 = a6 = k*EXP_FUN(-alpha)*(alpha-SCALAR_VAL(1.0));
  a3 = a7 = k*EXP_FUN(-alpha)*(alpha+SCALAR_VAL(1.0));
  a4 = a8 = -k*EXP_FUN(SCALAR_VAL(-2.0)*alpha);
  b1 = POW_FUN(SCALAR_VAL(2.0),-alpha);
  b2 = -EXP_FUN(SCALAR_VAL(-2.0)*alpha);
  c1 = c2 = 1;
  %(P)s private(j, ym1, ym2, xm1)
  for (i = 0; i < _PB_W; i++) {
    ym1 = ym2 = xm1 = SCALAR_VAL(0.0);
    for (j = 0; j < _PB_H; j++) {
      y1[i][j] = a1*imgIn[i][j] + a2*xm1 + b1*ym1 + b2*ym2;
      xm1 = imgIn[i][j]; ym2 = ym1; ym1 = y1[i][j];
    }
  }
  %(P)s private(j, yp1, yp2, xp1, xp2)
  for (i = 0; i < _PB_W; i++) {
    yp1 = yp2 = xp1 = xp2 = SCALAR_VAL(0.0);
    for (j = _PB_H - 1; j >= 0; j--) {
      y2[i][j] = a3*xp1 + a4*xp2 + b1*yp1 + b2*yp2;
      xp2 = xp1; xp1 = imgIn[i][j]; yp2 = yp1; yp1 = y2[i][j];
    }
  }
  %(P)s private(j)
  for (i = 0; i < _PB_W; i++)
    for (j = 0; j < _PB_H; j++)
      imgOut[i][j] = c1 * (y1[i][j] + y2[i][j]);
"""

K["deriche"] = (
DER_HEAD + """  %(P)s private(i, tm1, ym1, ym2)
  for (j = 0; j < _PB_H; j++) {
    tm1 = ym1 = ym2 = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_W; i++) {
      y1[i][j] = a5*imgOut[i][j] + a6*tm1 + b1*ym1 + b2*ym2;
      tm1 = imgOut[i][j]; ym2 = ym1; ym1 = y1[i][j];
    }
  }
  %(P)s private(i, tp1, tp2, yp1, yp2)
  for (j = 0; j < _PB_H; j++) {
    tp1 = tp2 = yp1 = yp2 = SCALAR_VAL(0.0);
    for (i = _PB_W - 1; i >= 0; i--) {
      y2[i][j] = a7*tp1 + a8*tp2 + b1*yp1 + b2*yp2;
      tp2 = tp1; tp1 = imgOut[i][j]; yp2 = yp1; yp1 = y2[i][j];
    }
  }
  %(P)s private(j)
  for (i = 0; i < _PB_W; i++)
    for (j = 0; j < _PB_H; j++)
      imgOut[i][j] = c2 * (y1[i][j] + y2[i][j]);
}""",
DER_HEAD + """  static DATA_TYPE y1t[H][W], y2t[H][W];
  %(P)s private(i, tm1, ym1, ym2)
  for (j = 0; j < _PB_H; j++) {
    tm1 = ym1 = ym2 = SCALAR_VAL(0.0);
    for (i = 0; i < _PB_W; i++) {
      y1t[j][i] = a5*imgOut[i][j] + a6*tm1 + b1*ym1 + b2*ym2;
      tm1 = imgOut[i][j]; ym2 = ym1; ym1 = y1t[j][i];
    }
  }
  %(P)s private(i, tp1, tp2, yp1, yp2)
  for (j = 0; j < _PB_H; j++) {
    tp1 = tp2 = yp1 = yp2 = SCALAR_VAL(0.0);
    for (i = _PB_W - 1; i >= 0; i--) {
      y2t[j][i] = a7*tp1 + a8*tp2 + b1*yp1 + b2*yp2;
      tp2 = tp1; tp1 = imgOut[i][j]; yp2 = yp1; yp1 = y2t[j][i];
    }
  }
  %(P)s private(j)
  for (i = 0; i < _PB_W; i++)
    for (j = 0; j < _PB_H; j++)
      imgOut[i][j] = c2 * (y1t[j][i] + y2t[j][i]);
}""")


def replace_kernel(text, name, new):
    fn = "kernel_" + name.replace("-", "_")
    m = re.search(r"^(static\s+)?void\s+%s\s*\(" % fn, text, flags=re.M)
    start = m.start()
    i = text.index("{", m.end())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[:start] + "static " + new + text[j + 1:]
    raise ValueError(name)


def main():
    src, out = sys.argv[1], sys.argv[2]
    for name, (orig, rewr) in K.items():
        path = None
        for root, _, files in os.walk(src):
            if name + ".c" in files and os.path.basename(root) == name:
                path = os.path.join(root, name + ".c")
        text = open(path).read()
        d = os.path.join(out, name)
        os.makedirs(d, exist_ok=True)
        for tag, body in (("orig", orig), ("rewr", rewr)):
            with open(os.path.join(d, tag + ".c"), "w") as f:
                f.write(replace_kernel(text, name, body % {"P": P}))
        print(name, os.path.dirname(path))


main()
