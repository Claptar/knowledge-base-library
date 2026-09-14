---
title: Single-cell RNA-seq
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Single-cell RNA-seq

**Source:** `recitations/2014-03-07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Bulk cell RNA-seq only captures average behavior of millions of cells, but individual cells in the population can have different behavior

- Solution: single-cell RNA-seq

   - Instead of taking an aliquot of millions of cells to prepare a library, first sort single cells into wells and then do each library prep on each individual cell

   - Each cell has its own 6nt barcode in adapter; can then pool libraries from multiple cells together to sequence on one flow cell

- Caveats:

   - Library prep with such little starting RNA from 1 cell is technically very challenging

   - Much more likely that random sampling during library prep will produce strong biases, further amplified by PCR

   - For example, if a transcript is very lowly expressed, you might have only one or a few molecules in your single cell RNA sample - easily lost due to stochastic sampling during library prep

   - Hard to interpret “negative” results of a gene or isoform not being expressed – is it actually not expressed in the cell, or did you just lose it during library prep?

27

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802 / 6.874 / HST.506 Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Topic Models �](17-topic-models.md) · [Up: contents](index.md)
