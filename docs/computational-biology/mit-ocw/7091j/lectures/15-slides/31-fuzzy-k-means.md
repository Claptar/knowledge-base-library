---
title: Fuzzy K-means
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fuzzy K-means

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

K=2

75

### **K-means**

- Initialize: choose k points as cluster means

- Repeat until convergence:

   - Assignment:  place each point Xi in the cluster with the closest mean.

   - Update: recalculate the mean for each cluster

### **Fuzzy k-means**

- Initialize: choose k points as cluster means

- Repeat until convergence:

   - Assignment:  calculate probability of each point belonging to each cluster.

   - Update: recalculate the mean for each cluster using these probabilities

76

### **K-means**


### **Fuzzy k-means**


= membership of point j in cluster i Larger values of r make the clusters more fuzzy.

Relationship to EM and Gaussian mixture models

77

---

[← Convergence](30-convergence.md) · [Up: contents](index.md) · [Example of Fuzzy K-means →](32-example-of-fuzzy-k-means.md)
