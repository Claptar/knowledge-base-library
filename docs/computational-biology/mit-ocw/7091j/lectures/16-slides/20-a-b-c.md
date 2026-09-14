---
title: A B C
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A B C

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Simulated Annealing Solution: •Initialize T and  subgraph Gn with score Sn •Repeat while •Pick a neighboring node v to add to the subgraph

- •Score new subgraph -> Stest •If Sn<Stest: keep new subgraph

- •Else keep new subgraph with P=exp[-(Stest-Sn)/T]

•Modify T according to “cooling schedule.”

---

[← A B C](19-a-b-c.md) · [Up: contents](index.md) · [Clustering Graphs →](21-clustering-graphs.md)
