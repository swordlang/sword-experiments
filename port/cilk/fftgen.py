"""Translate fft.cilk's machine-generated codelets (fft_base_R, the column
body of fft_twiddle_R) into Sword functions on fixed arrays.

usage: python3 -I fftgen.py fft.cilk >> fft.sword, after the hand-written part
"""
import re
import sys

src = open(sys.argv[1]).read()
V = r'(?:[ri]\d+_\d+|tmpr|tmpi|wr|wi)'
C = r'(\d+\.\d+(?:e[+-]?\d+)?)'


def expr(e):
    e = e.strip()
    m = re.fullmatch(r'\(' + C + r' \* \((' + V + r') ([+-]) (' + V + r')\)\)', e)
    if m:
        # double * float: the sum is taken in float, the product in double
        return 'f32(%s * f64(%s %s %s))' % (m[1], m[2], m[3], m[4])
    m = re.fullmatch(r'\(\(' + C + r' \* (' + V + r')\) ([+-]) \(' + C + r' \* (' + V + r')\)\)', e)
    if m:
        return 'f32(%s * f64(%s) %s %s * f64(%s))' % (m[1], m[2], m[3], m[4], m[5])
    if re.search(r'\d\.\d', e):
        raise SystemExit('unknown shape: ' + e)
    return e


def body(text, reads, writes):
    names = set()
    out = []
    for line in text.split('\n'):
        s = line.strip()
        m = re.fullmatch(r'REAL (.*);', s)
        if m:
            names.update(x.strip() for x in m[1].split(','))
            continue
        m = re.fullmatch(r'(c_re|c_im)\((\w+)\[(?:(\d+) \* \w+|(\d+))\]\) = (.*);', s)
        if m:
            field = 're' if m[1] == 'c_re' else 'im'
            k = m[3] or m[4]
            assert m[2] == writes, s
            out.append('o[%s].%s = %s' % (k, field, expr(m[5])))
            continue
        m = re.fullmatch(r'(' + V + r') = (c_re|c_im)\((\w+)\[(?:(\d+) \* (\w+)|(\d+))\]\);', s)
        if m:
            field = 're' if m[2] == 'c_re' else 'im'
            arr, k, by = m[3], m[4] or m[6], m[5]
            if arr == 'W':
                out.append('%s = w[%s * l1].%s' % (m[1], k, field))
            else:
                assert arr == reads, s
                out.append('%s = a[%s].%s' % (m[1], k, field))
            continue
        m = re.fullmatch(r'(' + V + r') = (.*);', s)
        if m:
            out.append('%s = %s' % (m[1], expr(m[2])))
            continue
        if s in ('', '{', '}') or s.startswith('jp = in + i'):
            continue
        raise SystemExit('unknown statement: ' + s)
    return names, out


def func(name):
    i = src.index('\n' + name)
    j = src.index('\n{', i)
    depth, k = 0, j + 1
    while True:
        if src[k] == '{':
            depth += 1
        elif src[k] == '}':
            depth -= 1
            if depth == 0:
                return src[j + 2:k]
        k += 1


print('// What follows is fft.cilk\'s machine-generated code, translated by')
print('// fftgen.py statement by statement.')
for r in (2, 4, 8, 16, 32):
    names, lines = body(func('static void fft_base_%d(' % r), 'in', 'out')
    print('\nfunc base%d(a [%d]Cx) [%d]Cx {' % (r, r, r))
    print('    mut o := [%d]Cx{}' % r)
    for n in sorted(names):
        print('    mut %s := f32(0.0)' % n)
    for l in lines:
        print('    ' + l)
    print('    return o')
    print('}')

    t = func('static cilk void fft_twiddle_%d(' % r)
    start = t.index('jp = in + i;')
    stop = t.index('} else {')
    names, lines = body(t[start:stop], 'jp', 'kp')
    print('\nfunc twiddle%d(a [%d]Cx, w []Cx, l1 i64) [%d]Cx {' % (r, r, r))
    print('    mut o := [%d]Cx{}' % r)
    for n in sorted(names | {'wr', 'wi', 'tmpr', 'tmpi'}):
        print('    mut %s := f32(0.0)' % n)
    for l in lines:
        print('    ' + l)
    print('    return o')
    print('}')
