// The five kernels of the comparison in Zig, with std.Thread: the range is cut
// into one block per thread, and partial sums are combined in block order.
// Built twice: -O safe keeps the bounds checks, -O fast drops them.
//
//   bench <kernel> <threads> [reps]
//
// Prints: kernel,method,threads,check,median_ns
const std = @import("std");
const builtin = @import("builtin");

const sum_n = 10_000_000;
const saxpy_n = 10_000_000;
const grid_w = 2048;
const grid_steps = 10;
const mandel_w = 2000;
const mandel_iter = 256;
const bodies = 4096;
const body_steps = 4;
const max_threads = 64;

var threads: usize = 1;

// splitmix64 of seed + i, scaled to [0, 1): every language draws the same bits.
fn unit(seed: u64, i: u64) f64 {
    var z = seed +% i +% 0x9e3779b97f4a7c15;
    z = (z ^ (z >> 30)) *% 0xbf58476d1ce4e5b9;
    z = (z ^ (z >> 27)) *% 0x94d049bb133111eb;
    z ^= z >> 31;
    return @as(f64, @floatFromInt(z >> 11)) / 9007199254740992.0;
}

fn fill(seed: u64, xs: []f64) void {
    for (xs, 0..) |*x, i| x.* = unit(seed, @intCast(i));
}

// The checksum of an array is its sum in index order, outside the timing.
fn total(xs: []const f64) f64 {
    var s: f64 = 0.0;
    for (xs) |x| s += x;
    return s;
}

// Calls ctx.run(lo, hi, k) on block k of [0, n), one thread per block.
fn blocks(n: usize, ctx: anytype) !void {
    var pool: [max_threads]std.Thread = undefined;
    for (0..threads) |k| {
        pool[k] = try std.Thread.spawn(.{}, @TypeOf(ctx.*).run, .{ ctx, n * k / threads, n * (k + 1) / threads, k });
    }
    for (pool[0..threads]) |t| t.join();
}

const Sum = struct {
    xs: []const f64,
    part: []f64,
    fn run(self: *const Sum, lo: usize, hi: usize, k: usize) void {
        var s: f64 = 0.0;
        for (self.xs[lo..hi]) |x| s += x;
        self.part[k] = s;
    }
};

fn sum(xs: []const f64) !f64 {
    var part: [max_threads]f64 = undefined;
    const ctx = Sum{ .xs = xs, .part = part[0..threads] };
    try blocks(xs.len, &ctx);
    var s: f64 = 0.0;
    for (part[0..threads]) |p| s += p;
    return s;
}

const Saxpy = struct {
    a: f64,
    x: []const f64,
    y: []f64,
    fn run(self: *const Saxpy, lo: usize, hi: usize, _: usize) void {
        for (lo..hi) |i| self.y[i] = self.a * self.x[i] + self.y[i];
    }
};

const Step = struct {
    w: usize,
    a: []const f64,
    b: []f64,
    fn run(self: *const Step, lo: usize, hi: usize, _: usize) void {
        const w = self.w;
        const a = self.a;
        for (lo..hi) |i| {
            for (0..w) |j| {
                const k = i * w + j;
                if (i == 0 or j == 0 or i == w - 1 or j == w - 1) {
                    self.b[k] = a[k];
                } else {
                    self.b[k] = 0.25 * (a[k - 1] + a[k + 1] + a[k - w] + a[k + w]);
                }
            }
        }
    }
};

fn row(w: usize, i: usize, max: u32) u64 {
    var count: u64 = 0;
    const fw: f64 = @floatFromInt(w);
    const cy = 2.5 * @as(f64, @floatFromInt(i)) / fw - 1.25;
    for (0..w) |j| {
        const cx = 2.5 * @as(f64, @floatFromInt(j)) / fw - 2.0;
        var zr: f64 = 0.0;
        var zi: f64 = 0.0;
        var it: u32 = 0;
        while (it < max and zr * zr + zi * zi <= 4.0) {
            const t = zr * zr - zi * zi + cx;
            zi = 2.0 * zr * zi + cy;
            zr = t;
            it += 1;
        }
        count += it;
    }
    return count;
}

// Rows are dealt round-robin, since the ones near the middle cost the most.
fn mandelRows(w: usize, max: u32, k: usize, part: *u64) void {
    var c: u64 = 0;
    var i = k;
    while (i < w) : (i += threads) c += row(w, i, max);
    part.* = c;
}

fn mandel(w: usize, max: u32) !u64 {
    var part: [max_threads]u64 = undefined;
    var pool: [max_threads]std.Thread = undefined;
    for (0..threads) |k| pool[k] = try std.Thread.spawn(.{}, mandelRows, .{ w, max, k, &part[k] });
    for (pool[0..threads]) |t| t.join();
    var count: u64 = 0;
    for (part[0..threads]) |c| count += c;
    return count;
}

const Accel = struct {
    n: usize,
    m: f64,
    p: []const f64,
    a: []f64,
    fn run(self: *const Accel, lo: usize, hi: usize, _: usize) void {
        const n = self.n;
        const px = self.p[0..n];
        const py = self.p[n .. 2 * n];
        const pz = self.p[2 * n .. 3 * n];
        for (lo..hi) |i| {
            var sx: f64 = 0.0;
            var sy: f64 = 0.0;
            var sz: f64 = 0.0;
            for (0..n) |j| {
                const dx = px[j] - px[i];
                const dy = py[j] - py[i];
                const dz = pz[j] - pz[i];
                const d = dx * dx + dy * dy + dz * dz + 0.01;
                const f = self.m / (d * @sqrt(d));
                sx += dx * f;
                sy += dy * f;
                sz += dz * f;
            }
            self.a[i] = sx;
            self.a[n + i] = sy;
            self.a[2 * n + i] = sz;
        }
    }
};

const Move = struct {
    a: []const f64,
    v: []f64,
    p: []f64,
    fn run(self: *const Move, lo: usize, hi: usize, _: usize) void {
        for (lo..hi) |i| {
            self.v[i] += self.a[i] * 0.001;
            self.p[i] += self.v[i] * 0.001;
        }
    }
};

fn since(io: std.Io, t0: std.Io.Timestamp) u64 {
    return @intCast(t0.durationTo(std.Io.Timestamp.now(io, .awake)).nanoseconds);
}

pub fn main(init: std.process.Init) !void {
    const io = init.io;
    const gpa = init.arena.allocator();
    const args = try init.minimal.args.toSlice(gpa);
    if (args.len < 3) {
        std.debug.print("usage: bench sum|saxpy|stencil|mandelbrot|nbody threads [reps]\n", .{});
        std.process.exit(2);
    }
    const kernel = args[1];
    threads = try std.fmt.parseInt(usize, args[2], 10);
    const reps: usize = if (args.len > 3) try std.fmt.parseInt(usize, args[3], 10) else 5;
    var times: [64]u64 = undefined;
    var check: u64 = 0;
    var hex = true;

    if (std.mem.eql(u8, kernel, "sum")) {
        const xs = try gpa.alloc(f64, sum_n);
        fill(1, xs);
        for (xs) |*x| x.* = 2.0 * x.* - 1.0;
        var s: f64 = 0.0;
        for (0..reps) |r| {
            const t0 = std.Io.Timestamp.now(io, .awake);
            s = try sum(xs);
            times[r] = since(io, t0);
        }
        check = @bitCast(s);
    } else if (std.mem.eql(u8, kernel, "saxpy")) {
        const x = try gpa.alloc(f64, saxpy_n);
        const y = try gpa.alloc(f64, saxpy_n);
        fill(1, x);
        for (0..reps) |r| {
            fill(2, y);
            const t0 = std.Io.Timestamp.now(io, .awake);
            try blocks(saxpy_n, &Saxpy{ .a = 1.5, .x = x, .y = y });
            times[r] = since(io, t0);
        }
        check = @bitCast(total(y));
    } else if (std.mem.eql(u8, kernel, "stencil")) {
        const a = try gpa.alloc(f64, grid_w * grid_w);
        const b = try gpa.alloc(f64, grid_w * grid_w);
        for (0..reps) |r| {
            fill(1, a);
            const t0 = std.Io.Timestamp.now(io, .awake);
            for (0..grid_steps / 2) |_| {
                try blocks(grid_w, &Step{ .w = grid_w, .a = a, .b = b });
                try blocks(grid_w, &Step{ .w = grid_w, .a = b, .b = a });
            }
            times[r] = since(io, t0);
        }
        check = @bitCast(total(a));
    } else if (std.mem.eql(u8, kernel, "mandelbrot")) {
        for (0..reps) |r| {
            const t0 = std.Io.Timestamp.now(io, .awake);
            check = try mandel(mandel_w, mandel_iter);
            times[r] = since(io, t0);
        }
        hex = false;
    } else if (std.mem.eql(u8, kernel, "nbody")) {
        const p = try gpa.alloc(f64, 3 * bodies);
        const v = try gpa.alloc(f64, 3 * bodies);
        const a = try gpa.alloc(f64, 3 * bodies);
        const m = 1.0 / @as(f64, bodies);
        for (0..reps) |r| {
            fill(1, p);
            fill(2, v);
            for (v) |*x| x.* = 0.01 * (x.* - 0.5);
            const t0 = std.Io.Timestamp.now(io, .awake);
            for (0..body_steps) |_| {
                try blocks(bodies, &Accel{ .n = bodies, .m = m, .p = p, .a = a });
                try blocks(3 * bodies, &Move{ .a = a, .v = v, .p = p });
            }
            times[r] = since(io, t0);
        }
        check = @bitCast(total(p));
    } else {
        std.debug.print("unknown kernel\n", .{});
        std.process.exit(2);
    }

    const ts = times[0..reps];
    for (1..ts.len) |i| {
        var j = i;
        while (j > 0 and ts[j - 1] > ts[j]) : (j -= 1) std.mem.swap(u64, &ts[j - 1], &ts[j]);
    }
    const method = if (builtin.mode == .safe) "zig-safe" else "zig-fast";
    var buf: [256]u8 = undefined;
    var w: std.Io.File.Writer = .init(.stdout(), io, &buf);
    const out = &w.interface;
    if (hex) {
        try out.print("{s},{s},{d},{x},{d}\n", .{ kernel, method, threads, check, ts[reps / 2] });
    } else {
        try out.print("{s},{s},{d},{d},{d}\n", .{ kernel, method, threads, check, ts[reps / 2] });
    }
    try out.flush();
}
