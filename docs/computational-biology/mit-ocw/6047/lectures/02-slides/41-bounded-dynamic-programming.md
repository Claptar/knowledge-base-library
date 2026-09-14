---
title: Bounded Dynamic Programming
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bounded Dynamic Programming

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**<u>Initialization:</u>**

x1 …………………………  xM F(i,0), F(0,j) undefined for i, j > k **<u>Iteration:</u>** For i = 1…M For j = max(1, i – k)…min(N, i+k) F(i – 1, j – 1)+ s(xi, yj) i, yj) , yj) j) ) F(i, j) = max F(i, j – 1) – d, if j > i – k(N) F(i – 1, j) – d, if j < i + k(N)

F(i – 1, j – 1)+ s(xi, yj) i, yj) , yj) j) ) F(i, j) = max F(i, j – 1) – d, if j > i – k(N) F(i – 1, j) – d, if j < i + k(N)

k(N)

**<u>Termination:</u>** same

Slides credit: Serafim Batzoglou

47

---

[← (4) Extensions to basic DP solution](40-4-extensions-to-basic-dp-solution.md) · [Up: contents](index.md) · [Can we do better than O(n2 )in the general case? →](42-can-we-do-better-than-o-n2-in-the-general-case.md)
