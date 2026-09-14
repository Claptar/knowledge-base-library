---
title: Limits of k-means
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Limits of k-means

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### K-means uses Euclidean distance


- Gives most weight to largest differences

- Can’t be used if data are qualitative

- Centroid usually does not represent any datum

79

###### **K-means**

- Best clustering minimizes within-cluster Euclidean distance of from centroids


###### **K-medoids**

- Best clustering minimizes within-cluster dissimilarity from medoids (exemplar)


80

---

[← Example of Fuzzy K-means](32-example-of-fuzzy-k-means.md) · [Up: contents](index.md) · [K-medoids clustering →](34-k-medoids-clustering.md)
