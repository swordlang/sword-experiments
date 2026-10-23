"""Figures for the article and the poster, from results/: python figures.py

Writes results/figures/*.png (300 dpi, for a Word document) and *.svg (for a
poster), labelled in English. FIGURES_LANG=pt writes the same figures labelled
in Portuguese, the language of the COBRIC article, into results/figures/pt/.
Everything is read from the CSVs that analyze.py reads; nothing here is typed
in by hand.
"""
import csv
import os
import struct

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import MaxNLocator  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
LANG = os.environ.get("FIGURES_LANG", "en")
if LANG not in ("en", "pt"):
    raise SystemExit("FIGURES_LANG is en or pt, not %r" % LANG)
OUT = os.path.join(RESULTS, "figures", *(["pt"] if LANG == "pt" else []))


def tr(en, pt):
    return pt if LANG == "pt" else en


def count(n):
    """A count as the language writes it: 12,345 or 12.345."""
    return f"{n:,}".replace(",", tr(",", "."))

C_COLOR = "#c0392b"
SWORD_COLOR = "#2c3e50"
LIGHT = "#95a5a6"

PLATFORM_NAMES = {
    "macos-arm64": "macOS, Apple M4",
    "linux-arm64-docker": tr("Linux arm64 (VM on the M4)", "Linux arm64 (VM no M4)"),
    "gh-linux-x86_64": "Linux x86-64 (GitHub)",
    "gh-linux-arm64": "Linux arm64 (GitHub)",
    "gh-macos-arm64": "macOS M1 (GitHub)",
    "macos-arm64-atomic": tr("macOS, Apple M4, atomic reduction",
                             "macOS, Apple M4, redução atômica"),
}

# Runs that are not another machine but the same one done differently: the M4
# with libomp forced to an atomic reduction, which only E1b asks about. Counted
# as a platform anywhere else it would be the M4 twice.
VARIANTS = {"macos-arm64-atomic"}

METHOD_NAMES = {
    "c-serial": "C serial",
    "c-omp": "C OpenMP",
    "c-ompkahan": "C OpenMP + Kahan",
    "c-thread": tr("C, a generator per thread", "C, gerador por thread"),
    "c-index": tr("C, a generator by index", "C, gerador por índice"),
    "c-philox": "C, Philox",
    "sword-plain": "Sword reduce(+)",
    "sword-kahan": "Sword Kahan",
    "sword-exact": tr("Sword exact", "Sword exata"),
    "sword-mix": "Sword, splitmix",
}


def rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def platforms(variants=False):
    return sorted(p for p in os.listdir(RESULTS)
                  if os.path.isfile(os.path.join(RESULTS, p, "env.txt"))
                  and (variants or p not in VARIANTS))


def ordered(bits):
    b = int(bits, 16)
    return b if b < 1 << 63 else (1 << 63) - b


def reference(platform, dataset):
    with open(os.path.join(RESULTS, platform, "reference.csv")) as f:
        for line in f:
            name, bits, _ = line.strip().split(",")
            if name.replace(".bin", "") == dataset:
                return bits
    raise KeyError(dataset)


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=300)
    fig.savefig(os.path.join(OUT, name + ".svg"))
    plt.close(fig)


def color(method):
    return SWORD_COLOR if method.startswith("sword") else C_COLOR


def distinct_everywhere():
    """How many different answers each method gave over every platform and
    thread count."""
    names = platforms()
    panels = [(tr("E1: sum of 10⁷ doubles (mixed data)",
                  "E1: soma de 10⁷ doubles (dados mistos)"), "sum.csv", "mixed"),
              ("E2: Monte Carlo, ∫₀¹ e^(−x²) dx", "mc.csv", None)]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    for ax, (title, file, dataset) in zip(axes, panels):
        seen = {}
        for p in names:
            for r in rows(os.path.join(RESULTS, p, file)):
                if dataset and r["data"] != dataset:
                    continue
                if r["method"] == "c-serial":
                    continue
                seen.setdefault(r["method"], set()).add(r["bits"])
        methods = list(seen)
        counts = [len(seen[m]) for m in methods]
        bars = ax.barh([METHOD_NAMES[m] for m in methods], counts,
                       color=[color(m) for m in methods])
        for bar, n in zip(bars, counts):
            ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                    str(n), va="center", fontsize=9)
        ax.invert_yaxis()
        ax.set_title(title, fontsize=10)
        ax.set_xlabel(tr("different results in %d runs",
                         "resultados diferentes em %d execuções") %
                      (len(names) * 8))
        ax.set_xlim(0, max(counts) + 2)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.suptitle(tr("%d platforms × 8 thread counts (1 to 16)",
                    "%d plataformas × 8 números de threads (1 a 16)") % len(names),
                 fontsize=10, y=0.98)
    save(fig, tr("f1-distinct-results", "f1-resultados-distintos"))


def error_by_threads(platform="macos-arm64"):
    """Distance from the correctly rounded sum, per thread count."""
    data = [r for r in rows(os.path.join(RESULTS, platform, "sum.csv"))
            if r["data"] == "mixed"]
    ref = reference(platform, "mixed")
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for method, marker in (("c-omp", "o"), ("sword-plain", "s"),
                           ("sword-exact", "^"), ("c-ompkahan", "x")):
        rs = sorted((int(r["threads"]), abs(ordered(r["bits"]) - ordered(ref)))
                    for r in data if r["method"] == method)
        ax.plot([t for t, _ in rs], [e for _, e in rs], marker=marker,
                color=color(method), label=METHOD_NAMES[method],
                linestyle="-" if method != "c-ompkahan" else ":")
    ax.set_xscale("log", base=2)
    ax.set_xticks([1, 2, 3, 4, 6, 8, 10, 16])
    ax.set_xticklabels(["1", "2", "3", "4", "6", "8", "10", "16"])
    ax.set_xlabel("threads")
    ax.set_ylabel(tr("error (ULPs) against the exact sum",
                     "erro (ULPs) contra a soma exata"))
    ax.set_title(tr("E1: does the error change with the thread count? (%s)",
                    "E1: o erro muda com o número de threads? (%s)") %
                 PLATFORM_NAMES[platform], fontsize=10)
    ax.legend(fontsize=8)
    save(fig, tr("f2-error-by-threads", "f2-erro-por-threads"))


def time_by_threads(platform="macos-arm64"):
    data = [r for r in rows(os.path.join(RESULTS, platform, "sum.csv"))
            if r["data"] == "mixed"]
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    for method, marker in (("c-omp", "o"), ("c-ompkahan", "x"),
                           ("sword-plain", "s"), ("sword-kahan", "D"),
                           ("sword-exact", "^")):
        rs = sorted((int(r["threads"]), float(r["median_ns"]) / 1e6)
                    for r in data if r["method"] == method)
        ax.plot([t for t, _ in rs], [ms for _, ms in rs], marker=marker,
                color=color(method), label=METHOD_NAMES[method],
                linestyle=":" if method in ("c-ompkahan", "sword-kahan") else "-")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xticks([1, 2, 3, 4, 6, 8, 10, 16])
    ax.set_xticklabels(["1", "2", "3", "4", "6", "8", "10", "16"])
    ax.set_xlabel("threads")
    ax.set_ylabel(tr("time (ms, median of 7)", "tempo (ms, mediana de 7)"))
    ax.set_title(tr("E1: cost of summing 10⁷ doubles (%s)",
                    "E1: custo da soma de 10⁷ doubles (%s)") %
                 PLATFORM_NAMES[platform], fontsize=10)
    ax.legend(fontsize=8)
    save(fig, tr("f3-time-by-threads", "f3-tempo-por-threads"))


def repeatability():
    """Distinct answers in 100 identical runs, thread count fixed."""
    names = platforms(variants=True)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    threads = ["2", "4", "8", "16"]
    width = 0.8 / (len(names) + 1)
    for i, p in enumerate(names):
        data = rows(os.path.join(RESULTS, p, "repeat.csv"))
        counts = []
        for t in threads:
            got = {r["bits"] for r in data
                   if r["method"] == "c-omp" and r["threads"] == t}
            counts.append(len(got))
        xs = [k + i * width for k in range(len(threads))]
        ax.bar(xs, counts, width, label="C OpenMP — " + PLATFORM_NAMES[p],
               color=C_COLOR, alpha=0.35 + 0.65 * (i + 1) / len(names))
    sword = []
    for t in threads:
        got = set()
        for p in names:
            got |= {(p, r["bits"]) for r in rows(os.path.join(RESULTS, p, "repeat.csv"))
                    if r["method"] == "sword-plain" and r["threads"] == t}
        sword.append(max(sum(1 for q, _ in got if q == p) for p in names))
    xs = [k + len(names) * width for k in range(len(threads))]
    ax.bar(xs, sword, width, label=tr("Sword reduce(+) — all", "Sword reduce(+) — todas"),
           color=SWORD_COLOR)
    ax.set_xticks([k + len(names) * width / 2 for k in range(len(threads))])
    ax.set_xticklabels([t + " threads" for t in threads])
    ax.set_ylabel(tr("different results in 100 runs",
                     "resultados diferentes em 100 execuções"))
    ax.set_title(tr("E1b: the same configuration, run 100 times",
                    "E1b: a mesma configuração, repetida 100 vezes"), fontsize=10)
    ax.legend(fontsize=7, ncol=2)
    save(fig, tr("f4-repeatability", "f4-repetibilidade"))


def load_bits(platform, impl, fn):
    path = os.path.join(RESULTS, platform, "bits", "%s-%s-%s.bin" % (platform, impl, fn))
    raw = open(path, "rb").read()
    return struct.unpack("<%dQ" % (len(raw) // 8), raw)


def cross_platform(a="gh-linux-x86_64", b="macos-arm64"):
    fns = ["sin", "cos", "exp", "log"]
    libm, num = [], []
    for fn in fns:
        x, y = load_bits(a, "libm", fn), load_bits(b, "libm", fn)
        libm.append(sum(1 for p, q in zip(x, y) if p != q))
        x, y = load_bits(a, "num", fn), load_bits(b, "num", fn)
        num.append(sum(1 for p, q in zip(x, y) if p != q))
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ks = range(len(fns))
    bars = ax.bar([k - 0.2 for k in ks], libm, 0.4, color=C_COLOR,
                  label=tr("the system's C library (libm)",
                           "biblioteca C do sistema (libm)"))
    ax.bar([k + 0.2 for k in ks], num, 0.4, color=SWORD_COLOR, label="Sword std/num")
    for bar, n in zip(bars, libm):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.1, count(n),
                ha="center", fontsize=8)
    for k, n in zip(ks, num):
        ax.text(k + 0.2, 1.2, str(n), ha="center", fontsize=8, color=SWORD_COLOR)
    ax.set_yscale("symlog", linthresh=1)
    ax.set_xticks(list(ks))
    ax.set_xticklabels(fns)
    ax.set_ylabel(tr("different results (of 10⁶)", "resultados diferentes (de 10⁶)"))
    ax.set_title(tr("E3: the same arguments on %s and %s",
                    "E3: os mesmos argumentos em %s e %s") %
                 (PLATFORM_NAMES[a], PLATFORM_NAMES[b]), fontsize=9)
    ax.legend(fontsize=8)
    save(fig, tr("f5-functions-across-platforms", "f5-funcoes-entre-plataformas"))


def function_cost(platform="macos-arm64"):
    data = {r["fn"]: float(r["ns_per_call"]) for r in rows(os.path.join(RESULTS, platform, "math.csv"))}
    fns = [("sin", "sin\n[−1000, 1000]"), ("sinnear", "sin\n[−π/4, π/4]"),
           ("cos", "cos"), ("exp", "exp\n[−700, 700]"), ("expunit", "exp\n[−1, 0]"),
           ("log", "log")]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ks = range(len(fns))
    ax.bar([k - 0.2 for k in ks], [data["libm-" + f] for f, _ in fns], 0.4,
           color=C_COLOR, label="libm")
    ax.bar([k + 0.2 for k in ks], [data["num-" + f] for f, _ in fns], 0.4,
           color=SWORD_COLOR, label="Sword std/num")
    ax.set_xticks(list(ks))
    ax.set_xticklabels([label for _, label in fns], fontsize=8)
    ax.set_ylabel(tr("ns per call", "ns por chamada"))
    ax.set_title(tr("E3: cost of the elementary functions (%s)",
                    "E3: custo das funções elementares (%s)") % PLATFORM_NAMES[platform],
                 fontsize=10)
    ax.legend(fontsize=8)
    save(fig, tr("f6-function-cost", "f6-custo-das-funcoes"))


def main():
    distinct_everywhere()
    error_by_threads()
    time_by_threads()
    repeatability()
    cross_platform()
    function_cost()
    print("figures in", OUT)


if __name__ == "__main__":
    main()
