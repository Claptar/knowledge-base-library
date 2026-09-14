---
title: de Bruijn graph post-processing
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# de Bruijn graph post-processing

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Before traversing the graph:

   - Pop bubbles

      - Bubble:  two paths that are redundant by starting and ending at the same nodes and contain similar sequences

      - Caused by sequencing error or biological variation

      - More complicated heuristics of how to pop them; for our purposes, manually inspect for sequencing error and pop

31

---

[← de Bruijn graph post-processing](17-de-bruijn-graph-post-processing.md) · [Up: contents](index.md) · [de Bruijn graph post-processing →](19-de-bruijn-graph-post-processing.md)
