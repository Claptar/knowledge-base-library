---
title: Karp-Rabin algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Karp-Rabin algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
T=  2 3 5 9 0 2 3 1 4 1  5 2  6 7 3 9 9 2 1<br>y1 = 23,590  y7 = 31,415<br>y2 = 35,902<br>y3 = 59,023<br>x=y7  P=T[7..11]<br>P=  3 1 4 1  5<br>compute x<br>x = 31,415  for i in [1..n]:<br>compute yi<br>if x == yi:<br>print “match at S[i]”<br>(this does not actually work)<br><!-- End of picture text -->

- Key idea: – Interpret strings as numbers:  fast comparison

**.**

20

---

[← Linear-time string matching](16-linear-time-string-matching.md) · [Up: contents](index.md) · [Karp-Rabin algorithm →](18-karp-rabin-algorithm.md)
