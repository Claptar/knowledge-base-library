---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 5 Library Complexity Short Read Alignment (Mapping) Foundations of Computational Systems Biology David K. Gifford

1

### Lecture 5 – Libraries and Indexing

- Library Complexity

   - How do we estimate the complexity of a sequencing library?

- Full-text Minute-size index (FM Index/BWT) – How do we convert a genome into an alternate representation that permits rapid matching of millions of sequence reads?

- Read Alignment

   - How can we use an FM index and BWT to rapidly align reads to a reference genome?

2

Library complexity is the number of unique molecules in the “library” that is sampled by finite sequencing


<!-- Start of picture text -->
Sample DNA<br>Adapters<br>Ligation<br><!-- End of picture text -->

**Library Complexity = ? Reads**


<!-- Start of picture text -->
Amplification<br><!-- End of picture text -->

**Sequencing**

**Image adapted from Mardis,** **_ARGHG_ (2008)**

3

Library complexity is the number of unique molecules in the “library” that is sampled by finite sequencing


<!-- Start of picture text -->
Sample DNA<br>Adapters<br>Ligation<br><!-- End of picture text -->

**Library Complexity = 4 Reads**


<!-- Start of picture text -->
Amplification<br><!-- End of picture text -->

**Sequencing**

**Image adapted from Mardis,** **_ARGHG_ (2008)**

4

---

[Up: contents](index.md) · [Modeling approach →](02-modeling-approach.md)
