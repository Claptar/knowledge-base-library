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

- Choose _k_ smaller than read length _L_ – Tradeoff:

   - Smaller _k_ loses more long-range information for repetitive regions and could create spurious overlaps if too small.

   - But too large _k_ could eliminate edges between truly adjacent regions of genome if there are sequencing errors and/or low coverage of region.

   - Empirically, _k_ is usually in 60s

   - _k_ is odd so that no read is its reverse complement (middle base cannot be same in read and reverse complement)

25

---

[← Overlap graph](11-overlap-graph.md) · [Up: contents](index.md) · [de Bruijn graph →](13-de-bruijn-graph.md)
