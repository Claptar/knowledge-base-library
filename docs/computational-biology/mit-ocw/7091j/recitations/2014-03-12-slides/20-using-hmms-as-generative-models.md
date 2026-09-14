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
0.2  I G<br>0.8  0.9<br>Island ( I )  Genome ( G )  C G A T<br>0.1<br><!-- End of picture text -->

What is the most likely parse for the following sequence?  GTGCCTA

Now consider the possible ways of being in state I in position 2:


<!-- Start of picture text -->
S 1 S 2 (1)  S 1 = G:   P( S 1,  S 2,  X 1,  X 2) = 0.09 * PT(I | G) * PE(T | I)<br>= 0.09 * 0.1 * 0.1 = 0.0009<br>G T<br>G 0.09  0.0324<br>(1)<br>(2)  S 1 = I:     P( S 1,  S 2,  X 1,  X 2) = 0.04 * PT(I | I) * PE(T | I)<br>= 0.04 * 0.8 * 0.1 = 0.0032<br>I 0.04 0.0032<br>(2)<br>probability of the optimal parse  ending with state  I  at<br>22<br>position 2 is { S 1=I,  S 2=I }<br><!-- End of picture text -->

---

[← Using HMMs as generative models](19-using-hmms-as-generative-models.md) · [Up: contents](index.md) · [Using HMMs as generative models →](21-using-hmms-as-generative-models.md)
