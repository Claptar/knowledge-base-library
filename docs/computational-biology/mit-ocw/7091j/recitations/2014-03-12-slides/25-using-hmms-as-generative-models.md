---
title: Using HMMs as generative models
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using HMMs as generative models

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
0.2  I G<br>0.8  0.9<br>Island ( I )  Genome ( G )  C G A T<br>0.1<br>What is the most likely parse for the following sequence?  GTGCCTA<br>S 1 S 2 S 3 S 4 S 5 S 6 S 7<br>G T G C C T A<br>G 0.09  0.0324 0.0029 2.61e-4 2.35e-5 1.06e-5 3.83e-6<br>I 0.04 0.0032 0.0013 4.16e-4 1.33e-4 1.06e-5 8.52e-7<br><!-- End of picture text -->

What is optimal parse of the first 3 bases GTG?

G G G We start at the highest probability for the last base, so G T G we begin our traceback from the circled point above

27

---

[← Using HMMs as generative models](24-using-hmms-as-generative-models.md) · [Up: contents](index.md) · [Midterm topics →](26-midterm-topics.md)
