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

Two possible ways of being in state G in position 2: prob of optimal sequence of hidden states ending with state G at pos. 1


<!-- Start of picture text -->
S 1 S 2<br>G T<br>(1)<br>G 0.09  0.0324<br>(2)<br>I 0.04<br><!-- End of picture text -->

(1) _S_ 1 = G:   P( _S_ 1, _S_ 2, _X_ 1, _X_ 2) = 0.09 *  PT(G | G)*PE(T | G) =0.09 * 0.9 * 0.4 = 0.0324 prob of optimal sequence of hidden states ending with state I at pos. 1 (2) _S_ 1 = I:     P( _S_ 1, _S_ 2, _X_ 1, _X_ 2) = 0.04 * PT(G | I) * PE(T | G) = 0.04 * 0.2 * 0.4 = 0.0032

21

---

[← The Viterbi Algorithm](18-the-viterbi-algorithm.md) · [Up: contents](index.md) · [Using HMMs as generative models →](20-using-hmms-as-generative-models.md)
