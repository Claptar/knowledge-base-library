---
title: Two main approaches
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Two main approaches

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Overlap layout consensus (string graph) – Plus: Retain entire read and its long-range position implications

      - Drawback: computationally expensive / slow

   - de Bruijn graph

      - Plus: Computationally more tractable

      - Minus:

         - Graphs get messy (bubble, tips) and must use heuristics to trace path through graph

         - Lose longer-range position information: have 100bp reads and _k_ =30

- -Lose the fact that these two 30mers are separated by 40bp


21

---

[← Some caveats](08-some-caveats.md) · [Up: contents](index.md) · [Overlap graph →](10-overlap-graph.md)
