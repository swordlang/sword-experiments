// The kernels of the comparison in Go: one goroutine per block of the range,
// partial sums combined in block order. The five of E4, and hist, scan and
// sort of E5.
//
//	bench <kernel> <threads> [reps]
//
// Prints: kernel,method,threads,check,median_ns
package main

import (
	"fmt"
	"math"
	"os"
	"runtime"
	"sort"
	"strconv"
	"sync"
	"time"
)

const (
	sumN       = 10000000
	saxpyN     = 10000000
	gridW      = 2048
	gridSteps  = 10
	mandelW    = 2000
	mandelIter = 256
	bodies     = 4096
	bodySteps  = 4
	histN      = 10000000
	bins       = 64
	scanN      = 10000000
	sortN      = 1000000
	sortKeys   = 1000
)

var threads = 1

// splitmix64 of seed + i, scaled to [0, 1): every language draws the same bits.
func unit(seed, i uint64) float64 {
	z := seed + i + 0x9e3779b97f4a7c15
	z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9
	z = (z ^ (z >> 27)) * 0x94d049bb133111eb
	z ^= z >> 31
	return float64(z>>11) / 9007199254740992.0
}

func fill(seed uint64, xs []float64) {
	for i := range xs {
		xs[i] = unit(seed, uint64(i))
	}
}

// The checksum of an array is its sum in index order, outside the timing.
func total(xs []float64) float64 {
	s := 0.0
	for _, x := range xs {
		s += x
	}
	return s
}

// blocks calls body(lo, hi, k) on block k of [0, n), one goroutine per block.
func blocks(n int, body func(lo, hi, k int)) {
	var wg sync.WaitGroup
	for k := 0; k < threads; k++ {
		wg.Add(1)
		go func(k int) {
			defer wg.Done()
			body(n*k/threads, n*(k+1)/threads, k)
		}(k)
	}
	wg.Wait()
}

// A histogram per goroutine, added together in block order.
func hist(xs []float64) []float64 {
	part := make([][]float64, threads)
	blocks(len(xs), func(lo, hi, k int) {
		h := make([]float64, bins)
		for _, x := range xs[lo:hi] {
			h[int(x*64.0)] += x
		}
		part[k] = h
	})
	h := make([]float64, bins)
	for _, p := range part {
		for j := range h {
			h[j] += p[j]
		}
	}
	return h
}

// Each block totals itself, the totals are carried across in order, and each
// block is written from its carry.
func scan(xs, out []float64) {
	carry := make([]float64, threads+1)
	blocks(len(xs), func(lo, hi, k int) {
		s := 0.0
		for _, x := range xs[lo:hi] {
			s += x
		}
		carry[k+1] = s
	})
	for k := 1; k <= threads; k++ {
		carry[k] += carry[k-1]
	}
	blocks(len(xs), func(lo, hi, k int) {
		s := carry[k]
		for i := lo; i < hi; i++ {
			s += xs[i]
			out[i] = s
		}
	})
}

type rec struct {
	key, id uint32
}

// sort.Slice on each block, then neighbouring blocks merged, the left one
// first on a tie.
func sortRecs(xs []rec) {
	bounds := make([]int, threads+1)
	for k := range bounds {
		bounds[k] = len(xs) * k / threads
	}
	blocks(len(xs), func(lo, hi, k int) {
		part := xs[lo:hi]
		sort.Slice(part, func(i, j int) bool { return part[i].key < part[j].key })
	})
	tmp := make([]rec, len(xs))
	for width := 1; width < threads; width *= 2 {
		var wg sync.WaitGroup
		for k := 0; k+width < threads; k += 2 * width {
			lo, mid, hi := bounds[k], bounds[k+width], bounds[min(k+2*width, threads)]
			wg.Add(1)
			go func() {
				defer wg.Done()
				i, j, o := lo, mid, lo
				for i < mid && j < hi {
					if xs[j].key < xs[i].key {
						tmp[o] = xs[j]
						j++
					} else {
						tmp[o] = xs[i]
						i++
					}
					o++
				}
				o += copy(tmp[o:], xs[i:mid])
				copy(tmp[o:], xs[j:hi])
				copy(xs[lo:hi], tmp[lo:hi])
			}()
		}
		wg.Wait()
	}
}

func fnv(c, w uint64) uint64 {
	return (c ^ w) * 1099511628211
}

func sum(xs []float64) float64 {
	part := make([]float64, threads)
	blocks(len(xs), func(lo, hi, k int) {
		s := 0.0
		for _, x := range xs[lo:hi] {
			s += x
		}
		part[k] = s
	})
	s := 0.0
	for _, p := range part {
		s += p
	}
	return s
}

func saxpy(a float64, x, y []float64) {
	blocks(len(y), func(lo, hi, _ int) {
		for i := lo; i < hi; i++ {
			y[i] = a*x[i] + y[i]
		}
	})
}

func step(w int, a, b []float64) {
	blocks(w, func(lo, hi, _ int) {
		for i := lo; i < hi; i++ {
			for j := 0; j < w; j++ {
				k := i*w + j
				if i == 0 || j == 0 || i == w-1 || j == w-1 {
					b[k] = a[k]
				} else {
					b[k] = 0.25 * (a[k-1] + a[k+1] + a[k-w] + a[k+w])
				}
			}
		}
	})
}

func row(w, i, max int) int {
	count := 0
	cy := 2.5*float64(i)/float64(w) - 1.25
	for j := 0; j < w; j++ {
		cx := 2.5*float64(j)/float64(w) - 2.0
		zr, zi := 0.0, 0.0
		it := 0
		for it < max && zr*zr+zi*zi <= 4.0 {
			t := zr*zr - zi*zi + cx
			zi = 2.0*zr*zi + cy
			zr = t
			it++
		}
		count += it
	}
	return count
}

// Rows are dealt round-robin, since the ones near the middle cost the most.
func mandel(w, max int) int {
	part := make([]int, threads)
	var wg sync.WaitGroup
	for k := 0; k < threads; k++ {
		wg.Add(1)
		go func(k int) {
			defer wg.Done()
			for i := k; i < w; i += threads {
				part[k] += row(w, i, max)
			}
		}(k)
	}
	wg.Wait()
	count := 0
	for _, c := range part {
		count += c
	}
	return count
}

func nbodyStep(n int, m float64, p, v, a []float64) {
	px, py, pz := p[:n], p[n:2*n], p[2*n:]
	blocks(n, func(lo, hi, _ int) {
		for i := lo; i < hi; i++ {
			sx, sy, sz := 0.0, 0.0, 0.0
			for j := 0; j < n; j++ {
				dx, dy, dz := px[j]-px[i], py[j]-py[i], pz[j]-pz[i]
				d := dx*dx + dy*dy + dz*dz + 0.01
				f := m / (d * math.Sqrt(d))
				sx += dx * f
				sy += dy * f
				sz += dz * f
			}
			a[i], a[n+i], a[2*n+i] = sx, sy, sz
		}
	})
	blocks(3*n, func(lo, hi, _ int) {
		for i := lo; i < hi; i++ {
			v[i] += a[i] * 0.001
			p[i] += v[i] * 0.001
		}
	})
}

func main() {
	if len(os.Args) < 3 {
		fmt.Fprintln(os.Stderr, "usage: bench sum|saxpy|stencil|mandelbrot|nbody threads [reps]")
		os.Exit(2)
	}
	kernel := os.Args[1]
	threads, _ = strconv.Atoi(os.Args[2])
	reps := 5
	if len(os.Args) > 3 {
		reps, _ = strconv.Atoi(os.Args[3])
	}
	runtime.GOMAXPROCS(threads)
	times := make([]int64, reps)
	timed := func(r int, body func()) {
		t0 := time.Now()
		body()
		times[r] = time.Since(t0).Nanoseconds()
	}
	var check string

	switch kernel {
	case "sum":
		xs := make([]float64, sumN)
		fill(1, xs)
		for i := range xs {
			xs[i] = 2.0*xs[i] - 1.0
		}
		s := 0.0
		for r := 0; r < reps; r++ {
			timed(r, func() { s = sum(xs) })
		}
		check = fmt.Sprintf("%x", math.Float64bits(s))
	case "saxpy":
		x, y := make([]float64, saxpyN), make([]float64, saxpyN)
		fill(1, x)
		for r := 0; r < reps; r++ {
			fill(2, y)
			timed(r, func() { saxpy(1.5, x, y) })
		}
		check = fmt.Sprintf("%x", math.Float64bits(total(y)))
	case "stencil":
		a, b := make([]float64, gridW*gridW), make([]float64, gridW*gridW)
		for r := 0; r < reps; r++ {
			fill(1, a)
			timed(r, func() {
				for s := 0; s < gridSteps/2; s++ {
					step(gridW, a, b)
					step(gridW, b, a)
				}
			})
		}
		check = fmt.Sprintf("%x", math.Float64bits(total(a)))
	case "mandelbrot":
		n := 0
		for r := 0; r < reps; r++ {
			timed(r, func() { n = mandel(mandelW, mandelIter) })
		}
		check = strconv.Itoa(n)
	case "nbody":
		p, v, a := make([]float64, 3*bodies), make([]float64, 3*bodies), make([]float64, 3*bodies)
		for r := 0; r < reps; r++ {
			fill(1, p)
			fill(2, v)
			for i := range v {
				v[i] = 0.01 * (v[i] - 0.5)
			}
			timed(r, func() {
				for s := 0; s < bodySteps; s++ {
					nbodyStep(bodies, 1.0/bodies, p, v, a)
				}
			})
		}
		check = fmt.Sprintf("%x", math.Float64bits(total(p)))
	case "hist":
		xs := make([]float64, histN)
		fill(1, xs)
		var h []float64
		for r := 0; r < reps; r++ {
			timed(r, func() { h = hist(xs) })
		}
		c := uint64(14695981039346656037)
		for _, b := range h {
			c = fnv(c, math.Float64bits(b))
		}
		check = fmt.Sprintf("%x", c)
	case "scan":
		xs, out := make([]float64, scanN), make([]float64, scanN)
		fill(1, xs)
		for i := range xs {
			xs[i] = 2.0*xs[i] - 1.0
		}
		for r := 0; r < reps; r++ {
			timed(r, func() { scan(xs, out) })
		}
		check = fmt.Sprintf("%x", math.Float64bits(total(out)))
	case "sort":
		xs := make([]rec, sortN)
		for r := 0; r < reps; r++ {
			for i := range xs {
				xs[i] = rec{uint32(unit(1, uint64(i)) * sortKeys), uint32(i)}
			}
			timed(r, func() { sortRecs(xs) })
		}
		c := uint64(14695981039346656037)
		for _, x := range xs {
			c = fnv(c, uint64(x.id))
		}
		check = fmt.Sprintf("%x", c)
	default:
		fmt.Fprintln(os.Stderr, "unknown kernel")
		os.Exit(2)
	}
	sort.Slice(times, func(i, j int) bool { return times[i] < times[j] })
	fmt.Printf("%s,go,%d,%s,%d\n", kernel, threads, check, times[reps/2])
}
