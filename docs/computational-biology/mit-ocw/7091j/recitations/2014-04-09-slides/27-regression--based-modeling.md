---
title: Regression-­‐based modeling
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Regression-­‐based modeling

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Relevant   if   you   assume   a   number   of   variables (e.g.   transcrip'on   factors)   have   independent linear   effects


- βt,g>0:   Transcrip'on   factor   t   posi'vely   regulates   gene   g

- βt,g<0:   Transcrip'on   factor   t   nega'vely   regulates   gene   g

- Ojen,   we   only   want   to   consider   TFs   with   a   large   impact   on gene   expression   definitely   above   noise,   so   we   set   a   minimum threshold   for   β   or   maximum   number   of   nonzero   β   (other shrinkage   methods   possible)

35

- Nonlinear   effects   on   gene   expression

- • **Mutual   informaKon** between   pairs   of   gene expression   measurements   can   detect complex,   nonlinear   regulatory   rela'onships A

- – Feed   forward   loops


<!-- Start of picture text -->
A<br>C<br>B<br><!-- End of picture text -->

- Coopera'vity   (mul'ple   subunits   to   dimerize   or mul'merize   before   func'onal   ac'vity)

36

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Varia'ons on K-­‐means clustering](26-varia-ons-on-k--means-clustering.md) · [Up: contents](index.md)
