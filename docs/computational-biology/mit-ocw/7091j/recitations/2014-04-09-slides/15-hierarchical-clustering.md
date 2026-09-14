---
title: Hierarchical Clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hierarchical Clustering

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- ( **repeat   unKl   only   1   cluster   leT** )   –   calculate   distances   between each   pair   of   clusters,   merge   the   two   closest   into   single   cluster – how   do   we   do   this   for   clusters   with   more   than   1   point?


<!-- Start of picture text -->
1<br>dsingle<br>dcentroid<br>5<br>dcomplete<br>7<br>2<br>4<br>3<br>6<br>centroid<br><!-- End of picture text -->

Let   cluster **A** contain   the   set   of   points _i_ and   cluster **B** contains   the   set   of   points _j_ ,   then   the distance   between **A** and **B** is: Op'on   (1): **Single   or   complete   linkage**

Calculate   all   distances   d _ij_ between   points _i_ in   A and   all   points _j_ in   other   cluster   B,   and consider   dist(A,B)   =   min(d _ij_ )   for   single   linkage,   dist(A,B)   =   max(d _ij_ )   for   complete   linkage Op'on   (2): **Centroid   linkage**

For   clusters   A   and   B,   compute   the   “centroid”   or   geometric   center   of   the   points   in   the cluster   AC   and   BC,   and   dist(A,B)   =   dist(AC,   BC)

---

[← Hierarchical Clustering](14-hierarchical-clustering.md) · [Up: contents](index.md) · [Hierarchical Clustering →](16-hierarchical-clustering.md)
