---
title: de Bruijn graph
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# de Bruijn graph

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Choose _k_ smaller than read length _L_ – Each read has _L-k_ +1 _k_ mers

   - For each of these _k_ mers, consider its

   - two ( _k-1_ )mers (prefix and suffix)


- These ( _k-1_ )mers are the nodes of the graph

- Connect the prefix ( _k_ -1)mer node to the

- suffix ( _k_ -1)mer node with a directed arrow

- The edges are _k_ mers from the input reads

   - If a _k_ mer is present in multiple times in your reads, can draw one arrow weighted with the number of occurrences of that _k_ mer in all of the reads

26

---

[← de Bruijn graph](12-de-bruijn-graph.md) · [Up: contents](index.md) · [de Bruijn graph →](14-de-bruijn-graph.md)
