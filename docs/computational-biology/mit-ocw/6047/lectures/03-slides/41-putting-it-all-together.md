---
title: Putting it all together
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Putting it all together

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- FUNDAMENTAL-PREPROCESSING(S): Z2,l,r = explicitly compare S[1..] with S[2..] **for** k in 2..n:

**if** k > r:  Zk,l,r = explicitly compare S[1..] with S[k..] **if** k <= r:

**if** Zk’<(r-k): Zk = Zk’ **else** :

Zk = explicitly compare S[r+1..] with S[(r-k)+1..] l = k

r = l+Zk

46

---

[← Computing Zk given Z1 .. Zk-1](40-computing-zk-given-z1-zk-1.md) · [Up: contents](index.md) · [Correctness of Z computation →](42-correctness-of-z-computation.md)
