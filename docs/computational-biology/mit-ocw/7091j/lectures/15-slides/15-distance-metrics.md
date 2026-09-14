---
title: Distance Metrics
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Distance Metrics

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
3.5<br>3<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0<br>0  2  4  6<br>Time<br>Expression<br><!-- End of picture text -->

28

## Expression data as multidimensional vectors

**expression in experiment 2**


<!-- Start of picture text -->
Gene B<br>XB,2<br>Gene A<br>XA,2<br>XA,1 XB,1<br><!-- End of picture text -->

XA =(   1, 0.5,    -1, 0.25, …) XB =(0.2, 0.4, -1.2, 0.05, …) …

**expression in experiment 1**

###### **What is a natural way to compare these vectors?**

29

---

[← Clustering](14-clustering.md) · [Up: contents](index.md) · [Euclidean →](16-euclidean.md)
