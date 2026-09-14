---
title: Varia'ons on K-­‐means clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Varia'ons on K-­‐means clustering

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Fuzzy   k-­‐means: – Rather   than   hard   assignments   (assigning   each   point   to strictly   1   cluster),   give   soj   assignments   ui,j   (μi,j)   for   all points   1≤ _i_ ≤N,   clusters   1≤ _N j_ ≤K

• Constraint   is X _µi,j_ = 1 • Consider   these   soj   assignments   when   recalcula'ng   the _j_ =1 cluster   means: <u>P</u> _Ni_ =1<sup>_<u>µi,jXi</u>_</sup> _Y_ ˆ _j_ = ~~P~~ _Ni_ =1<sup>_µi,j_</sup>

- k-­‐medioids:   restrict   ourselves   to   the   actual   data points

   - Rather   than   the   mean   (which   likely   doesn’t correspond   exactly   to   any   data   point),   have   the cluster   center   be   the   data   point   closest   to   the   mean

34

---

[← K-­‐means clustering](25-k--means-clustering.md) · [Up: contents](index.md) · [Regression-­‐based modeling →](27-regression--based-modeling.md)
