---
title: The Viterbi Algorithm
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Viterbi Algorithm

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
0.2  I G<br>0.8  0.9<br>Island ( I )  Genome ( G )  C G A T<br>0.1<br><!-- End of picture text -->

Often, we want to infer the most likely sequence of hidden states _S_ for a particular sequence of observed values _O_ (e.g. bases); in other words, find that maximizes -what is the optimal parse for the following sequence?  GTGCCTA -we're going to find this recursively, e.g. we find optimal parse of the first two bases GT in terms of paths up to the first base, G

What is the optimal parse for the first base, G?

- if first state is I?

P( _X_ 1 = G | _S_ 1 = I) = P1(I) * PE(G | S=I) = (0.1)*(0.4) = 0.04 - if first state is G? P( _X_ 1 = G | _S_ 1 = G) = P1(G) * PE(G | S=G) = (0.9)*(0.1) = 0.09

Therefore, the optimal parse for the first base is state G (note this doesn't yet consider the rest of the sequence!)

20

---

[← Using HMMs as generative models](17-using-hmms-as-generative-models.md) · [Up: contents](index.md) · [Using HMMs as generative models →](19-using-hmms-as-generative-models.md)
