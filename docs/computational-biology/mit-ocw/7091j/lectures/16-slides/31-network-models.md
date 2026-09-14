---
title: Network Models
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Network Models

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Structure of network

   - Coexpression

   - Mutual information

   - Physical/genetic interactions

- Analysis of network

   - Ad hoc

   - Shortest path

   - Clustering

   - Optimization


A B C


How do we find modules associated with specific data? Example: paint a PPI network with expression data. Try to find connected components that have overall high expression. (Example: Ideker et al. (2002) Bioinformatics).


A B C


Active subgraph problem: Can reveal hidden components of a biological response.


<!-- Start of picture text -->
A B C<br><!-- End of picture text -->


Where did we see something similar?


- The annotation problem attempts to label the entire graph.

- The active subnet problem searches for a part of the graph that is enriched in a label.


A B C


• **Steiner Tree Problem:** Find the smallest tree connecting all the vertices of in a set of interest (terminals).

•Downside:  will include all terminals, including false positives.

###### **Interactome**

###### **Experimental hits**


###### **Naïve methods**

---

[← Example](30-example.md) · [Up: contents](index.md) · [16 slides Part 32 — →](32-16-slides-part-32.md)
