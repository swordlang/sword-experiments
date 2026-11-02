// The kernels of the comparison in Rust, with rayon's parallel iterators: the
// five of E4, and hist, scan and sort of E5.
//
//   bench <kernel> <threads> [reps] [slices]
//
// With "slices" the stencil takes each row's neighbours as slices and zips
// them, the form that lets the compiler drop the bounds checks; it prints
// rust-slices.
//
// Prints: kernel,method,threads,check,median_ns
use rayon::prelude::*;
use std::time::Instant;

const SUM_N: usize = 10_000_000;
const SAXPY_N: usize = 10_000_000;
const GRID_W: usize = 2048;
const GRID_STEPS: usize = 10;
const MANDEL_W: usize = 2000;
const MANDEL_ITER: u32 = 256;
const BODIES: usize = 4096;
const BODY_STEPS: usize = 4;
const HIST_N: usize = 10_000_000;
const BINS: usize = 64;
const SCAN_N: usize = 10_000_000;
const SORT_N: usize = 1_000_000;
const SORT_KEYS: f64 = 1000.0;

// splitmix64 of seed + i, scaled to [0, 1): every language draws the same bits.
fn unit(seed: u64, i: u64) -> f64 {
    let mut z = seed.wrapping_add(i).wrapping_add(0x9e3779b97f4a7c15);
    z = (z ^ (z >> 30)).wrapping_mul(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)).wrapping_mul(0x94d049bb133111eb);
    z ^= z >> 31;
    (z >> 11) as f64 / 9007199254740992.0
}

fn fill(seed: u64, xs: &mut [f64]) {
    for (i, x) in xs.iter_mut().enumerate() {
        *x = unit(seed, i as u64);
    }
}

// The checksum of an array is its sum in index order, outside the timing.
fn total(xs: &[f64]) -> f64 {
    let mut s = 0.0;
    for &x in xs {
        s += x;
    }
    s
}

// A histogram per piece of work rayon hands out, merged as the pieces finish.
fn hist(xs: &[f64]) -> Vec<f64> {
    xs.par_iter()
        .fold(
            || vec![0.0; BINS],
            |mut h, &x| {
                h[(x * 64.0) as usize] += x;
                h
            },
        )
        .reduce(
            || vec![0.0; BINS],
            |mut a, b| {
                for j in 0..BINS {
                    a[j] += b[j];
                }
                a
            },
        )
}

// rayon has no scan; the usual one is two passes over one block per thread.
fn scan(xs: &[f64], out: &mut [f64]) {
    let block = xs.len().div_ceil(rayon::current_num_threads());
    let totals: Vec<f64> = xs.par_chunks(block).map(|c| c.iter().sum()).collect();
    let mut carry = vec![0.0; totals.len()];
    for k in 1..totals.len() {
        carry[k] = carry[k - 1] + totals[k - 1];
    }
    out.par_chunks_mut(block)
        .zip(xs.par_chunks(block))
        .zip(carry.par_iter())
        .for_each(|((o, x), &c)| {
            let mut s = c;
            for (o, &x) in o.iter_mut().zip(x) {
                s += x;
                *o = s;
            }
        });
}

#[derive(Clone, Copy)]
struct Rec {
    key: u32,
    id: u32,
}

fn sort_recs(xs: &mut [Rec]) {
    xs.par_sort_unstable_by_key(|r| r.key);
}

fn fnv(c: u64, w: u64) -> u64 {
    (c ^ w).wrapping_mul(1099511628211)
}

fn sum(xs: &[f64]) -> f64 {
    xs.par_iter().sum()
}

fn saxpy(a: f64, x: &[f64], y: &mut [f64]) {
    y.par_iter_mut().zip(x.par_iter()).for_each(|(y, &x)| *y = a * x + *y);
}

fn step(w: usize, a: &[f64], b: &mut [f64]) {
    b.par_chunks_mut(w).enumerate().for_each(|(i, row)| {
        for j in 0..w {
            let k = i * w + j;
            row[j] = if i == 0 || j == 0 || i == w - 1 || j == w - 1 {
                a[k]
            } else {
                0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w])
            };
        }
    });
}

// The same sums in the same order as step, so the same bits.
fn step_slices(w: usize, a: &[f64], b: &mut [f64]) {
    b.par_chunks_mut(w).enumerate().for_each(|(i, row)| {
        let mid = &a[i * w..(i + 1) * w];
        if i == 0 || i == w - 1 {
            row.copy_from_slice(mid);
            return;
        }
        let up = &a[(i - 1) * w..i * w];
        let down = &a[(i + 1) * w..(i + 2) * w];
        row[0] = mid[0];
        row[w - 1] = mid[w - 1];
        for ((((o, l), r), u), d) in row[1..w - 1]
            .iter_mut()
            .zip(&mid[..w - 2])
            .zip(&mid[2..])
            .zip(&up[1..w - 1])
            .zip(&down[1..w - 1])
        {
            *o = 0.25 * (l + r + u + d);
        }
    });
}

fn row(w: usize, i: usize, max: u32) -> u64 {
    let mut count = 0u64;
    let cy = 2.5 * i as f64 / w as f64 - 1.25;
    for j in 0..w {
        let cx = 2.5 * j as f64 / w as f64 - 2.0;
        let (mut zr, mut zi) = (0.0f64, 0.0f64);
        let mut it = 0u32;
        while it < max && zr * zr + zi * zi <= 4.0 {
            let t = zr * zr - zi * zi + cx;
            zi = 2.0 * zr * zi + cy;
            zr = t;
            it += 1;
        }
        count += it as u64;
    }
    count
}

fn mandel(w: usize, max: u32) -> u64 {
    (0..w).into_par_iter().map(|i| row(w, i, max)).sum()
}

fn nbody_step(n: usize, m: f64, p: &mut [f64], v: &mut [f64], a: &mut [f64]) {
    {
        let (px, rest) = p.split_at(n);
        let (py, pz) = rest.split_at(n);
        let (ax, rest) = a.split_at_mut(n);
        let (ay, az) = rest.split_at_mut(n);
        ax.par_iter_mut()
            .zip(ay.par_iter_mut())
            .zip(az.par_iter_mut())
            .enumerate()
            .for_each(|(i, ((ax, ay), az))| {
                let (mut sx, mut sy, mut sz) = (0.0f64, 0.0f64, 0.0f64);
                for j in 0..n {
                    let (dx, dy, dz) = (px[j] - px[i], py[j] - py[i], pz[j] - pz[i]);
                    let d = dx * dx + dy * dy + dz * dz + 0.01;
                    let f = m / (d * d.sqrt());
                    sx += dx * f;
                    sy += dy * f;
                    sz += dz * f;
                }
                *ax = sx;
                *ay = sy;
                *az = sz;
            });
    }
    v.par_iter_mut()
        .zip(p.par_iter_mut())
        .zip(a.par_iter())
        .for_each(|((v, p), &a)| {
            *v += a * 0.001;
            *p += *v * 0.001;
        });
}

fn timed(body: impl FnOnce()) -> u128 {
    let t0 = Instant::now();
    body();
    t0.elapsed().as_nanos()
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("usage: bench sum|saxpy|stencil|mandelbrot|nbody threads [reps]");
        std::process::exit(2);
    }
    let kernel = args[1].as_str();
    let threads: usize = args[2].parse().expect("threads");
    let reps: usize = args.get(3).map_or(5, |r| r.parse().expect("reps"));
    let slices = args.get(4).is_some_and(|v| v == "slices");
    if slices && kernel != "stencil" {
        eprintln!("slices is a stencil method");
        std::process::exit(2);
    }
    let step = if slices { step_slices } else { step };
    rayon::ThreadPoolBuilder::new()
        .num_threads(threads)
        .build_global()
        .expect("thread pool");
    let mut times = vec![0u128; reps];

    let check = match kernel {
        "sum" => {
            let mut xs = vec![0.0; SUM_N];
            fill(1, &mut xs);
            for x in xs.iter_mut() {
                *x = 2.0 * *x - 1.0;
            }
            let mut s = 0.0;
            for t in times.iter_mut() {
                *t = timed(|| s = sum(&xs));
            }
            format!("{:x}", s.to_bits())
        }
        "saxpy" => {
            let mut x = vec![0.0; SAXPY_N];
            let mut y = vec![0.0; SAXPY_N];
            fill(1, &mut x);
            for t in times.iter_mut() {
                fill(2, &mut y);
                *t = timed(|| saxpy(1.5, &x, &mut y));
            }
            format!("{:x}", total(&y).to_bits())
        }
        "stencil" => {
            let mut a = vec![0.0; GRID_W * GRID_W];
            let mut b = vec![0.0; GRID_W * GRID_W];
            for t in times.iter_mut() {
                fill(1, &mut a);
                *t = timed(|| {
                    for _ in 0..GRID_STEPS / 2 {
                        step(GRID_W, &a, &mut b);
                        step(GRID_W, &b, &mut a);
                    }
                });
            }
            format!("{:x}", total(&a).to_bits())
        }
        "mandelbrot" => {
            let mut n = 0;
            for t in times.iter_mut() {
                *t = timed(|| n = mandel(MANDEL_W, MANDEL_ITER));
            }
            n.to_string()
        }
        "nbody" => {
            let mut p = vec![0.0; 3 * BODIES];
            let mut v = vec![0.0; 3 * BODIES];
            let mut a = vec![0.0; 3 * BODIES];
            for t in times.iter_mut() {
                fill(1, &mut p);
                fill(2, &mut v);
                for x in v.iter_mut() {
                    *x = 0.01 * (*x - 0.5);
                }
                *t = timed(|| {
                    for _ in 0..BODY_STEPS {
                        nbody_step(BODIES, 1.0 / BODIES as f64, &mut p, &mut v, &mut a);
                    }
                });
            }
            format!("{:x}", total(&p).to_bits())
        }
        "hist" => {
            let mut xs = vec![0.0; HIST_N];
            fill(1, &mut xs);
            let mut h = vec![0.0; BINS];
            for t in times.iter_mut() {
                *t = timed(|| h = hist(&xs));
            }
            let c = h.iter().fold(14695981039346656037u64, |c, b| fnv(c, b.to_bits()));
            format!("{:x}", c)
        }
        "scan" => {
            let mut xs = vec![0.0; SCAN_N];
            let mut out = vec![0.0; SCAN_N];
            fill(1, &mut xs);
            for x in xs.iter_mut() {
                *x = 2.0 * *x - 1.0;
            }
            for t in times.iter_mut() {
                *t = timed(|| scan(&xs, &mut out));
            }
            format!("{:x}", total(&out).to_bits())
        }
        "sort" => {
            let mut xs = vec![Rec { key: 0, id: 0 }; SORT_N];
            for t in times.iter_mut() {
                for (i, x) in xs.iter_mut().enumerate() {
                    *x = Rec { key: (unit(1, i as u64) * SORT_KEYS) as u32, id: i as u32 };
                }
                *t = timed(|| sort_recs(&mut xs));
            }
            let c = xs.iter().fold(14695981039346656037u64, |c, r| fnv(c, r.id as u64));
            format!("{:x}", c)
        }
        _ => {
            eprintln!("unknown kernel");
            std::process::exit(2);
        }
    };
    times.sort();
    let method = if slices { "rust-slices" } else { "rust-rayon" };
    println!("{},{},{},{},{}", kernel, method, threads, check, times[reps / 2]);
}
