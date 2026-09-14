---
title: K-Means Clustering
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# K-Means Clustering

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Basic Idea

- Assume a fixed number K of clusters

- Partition points into K compact clusters

- The Algorithm

- Initialize K cluster centers randomly

- Repeatedly:

   - Assign points to nearest center

   - Move centers to center of gravity of their points

- Stop at convergence (no more reassignments)

10

---

[← Two approaches to clustering](03-two-approaches-to-clustering.md) · [Up: contents](index.md) · [K-Means Algorithm Example →](05-k-means-algorithm-example.md)
