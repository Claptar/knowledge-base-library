---
title: K-medoids clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# K-medoids clustering

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Initialize: choose k points as cluster means

- Repeat until convergence:

   - Assignment:  place each point Xi in the cluster with the closest medoid.

   - Update: recalculate the medoid for each cluster

81

---

[← Limits of k-means](33-limits-of-k-means.md) · [Up: contents](index.md) · [Other approaches →](35-other-approaches.md)
