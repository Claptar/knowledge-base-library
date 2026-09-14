---
title: Linear space alignment
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Linear space alignment

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

It is easy to compute F(M, N) in linear space


<!-- Start of picture text -->
F(i,j)<br><!-- End of picture text -->

Allocate ( column[1] ) Allocate ( column[2] ) For    i = 1….M

If i > 1, then: Free( column[i – 2] ) Allocate( column[ i ] ) For   j = 1…N F(i, j) = …

What about the pointers?

49

---

[← Can we do better than O(n2 )in the general case?](42-can-we-do-better-than-o-n2-in-the-general-case.md) · [Up: contents](index.md) · [Finding the best back-pointer for current column →](44-finding-the-best-back-pointer-for-current-column.md)
