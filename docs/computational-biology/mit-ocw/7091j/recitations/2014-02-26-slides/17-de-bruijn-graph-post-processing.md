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

   - Trim off ‘dead-end’ tips

      - Tip: short chain of nodes that is disconnected on one end

      - Caused by sequencing errors in read


<!-- Start of picture text -->
Pop bubbles<br>B’&<br>A& B&<br>A&<br>Clip short, low-coverage nodes<br>B&<br><!-- End of picture text -->

Figure&adapted&from&presentaQon&by&Michael&Schatz&

---

[← de Bruijn graph post-processing](16-de-bruijn-graph-post-processing.md) · [Up: contents](index.md) · [de Bruijn graph post-processing →](18-de-bruijn-graph-post-processing.md)
