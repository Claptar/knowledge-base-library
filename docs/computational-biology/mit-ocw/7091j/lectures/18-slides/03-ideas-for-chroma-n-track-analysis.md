---
title: Ideas for chroma/n track analysis
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ideas for chroma/n track analysis

**Source:** `lectures/18-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Hidden   Markov   Model   (ChromHMM)

- Dynamic   Bayesian   Network   (Segway)

   - Bayesian   Network   that   models   data   sampled   at intervals.      S'll   a   directed   acyclic   graph   (DAG).

   - – Can   learn   model   with   Graphical   Model   Toolkit (GMTK)

   - Can   incorporate   rela'onships   between   variables and   handle   missing   data

   - 1bp   analysis   resolu'on

Chroma'n   Structure

10


<!-- Start of picture text -->
Segway   Dynamic   Bayesian   Network<br>Black   Nodes<br>are   observed<br>Training   on<br>1%   of<br>genome<br>with   GMTK<br>Analysis   on<br>en're<br>genome<br>with   Viterbi<br><!-- End of picture text -->

Courtesy of Hoffman et al. Used with permission. Source: Hoffman, Michael M., Orion J. Buske, et al. "Segway: Simultaneous Segmentation of Multiple Functional Genomics Data Sets with Heterogeneous Patterns of Missing Data."


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Hoffman, Michael M., Orion J. Buske, et al. "Unsupervised Pattern Discovery in Human Chromatin Structure through Genomic Segmentation." _Nature Methods_ 9, no. 5 (2012): 473-6.

Chroma'n   Structure

12

---

[← Today’s Computa/onal Methods](02-today-s-computa-onal-methods.md) · [Up: contents](index.md) · [Today’s Narra/ve Arc →](04-today-s-narra-ve-arc.md)
