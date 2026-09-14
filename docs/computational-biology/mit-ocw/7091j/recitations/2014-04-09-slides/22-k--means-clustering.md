---
title: K-­‐means clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# K-­‐means clustering

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Goal:   Find   a   set   of _k_ clusters   that   minimizes the   distances   of   each   point   in   the   cluster   to the   cluster’s   mean

- You   must   a   priori   select _k_ ,   the   number   of clusters   to   return

- Algorithm:

– For   all   points   Xi: Repeat   un'l • Assign   Xi   to   the   cluster   with   the   closest   mean convergence (no – Recalculate   the   mean   of   each   cluster   based   on assignments change) previous   itera'on’s   assignments

30

---

[← Hierarchical Clustering](21-hierarchical-clustering.md) · [Up: contents](index.md) · [K-­‐means clustering example ( k =4) →](23-k--means-clustering-example-k-4.md)
