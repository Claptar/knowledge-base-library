---
title: Betweeness clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Betweeness clustering

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Repeat until max(betweeness) < threshold:

   - Compute betweeness

   - Remove edge with highest betweeness

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Schaeffer, Satu Elisa. "Graph Clustering." _Computer Science Review_ 1, no. 1 (2007): 27-64.

Markov clustering (MCL)

- Goal:  produce sharp partitions

- Intuition: A random walk will spend more time within a cluster than passing between clusters.

- Concisely explained here: Enright _et al._ NAR (2002) http://www.ncbi.nlm.nih.gov/pmc/articles/PMC101833

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Schaeffer, Satu Elisa. "Graph Clustering." _Computer Science Review_ 1, no. 1 (2007): 27-64.

---

[← Betweeness clustering](23-betweeness-clustering.md) · [Up: contents](index.md) · [Adjacency Matrix →](25-adjacency-matrix.md)
