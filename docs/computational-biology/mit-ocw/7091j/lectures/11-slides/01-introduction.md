---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7.91 / 20.490 / 6.874 / HST.506 7.36 / 20.390 / 6.802 C. Burge Lecture #10 March 13, 2014

RNA Secondary Structure - Biological Functions & Prediction

1

Hidden Markov Models of Genomic & Protein Features

• Hidden Markov Model terminology

- Viterbi algorithm

- Examples

   - CpG Island HMM

   - TMHMM (transmembrane helices)

2


<!-- Start of picture text -->
“Trellis” Diagram for Viterbi Algorithm<br>Position in Sequence →<br> 1  … i-2  i-1  i  i+1  i+2  …       L<br>T … A T  C  G  C  … A<br>Full set of possible transitions from position i to i+1<br>Hidden States →<br><!-- End of picture text -->

3


<!-- Start of picture text -->
“Initiation<br>Rabiner notation<br>CpG Island HMM<br>probabilities” π<br>j<br>Pgg = 0.99999 Pig = 0.001<br>Pg = 0.99, Pi = 0.01<br>Genome<br>Pii = 0.999<br>“Transition<br>probabilities” aij Pgi = 0.00001 Island<br>…<br>A      C       T       C       G      A       G      T       A<br> C  G  A  T<br>“Emission<br>Probabilities” bj(k) CpG Island:  0.3  0.3  0.2  0.2<br>Genome: 0.2  0.2  0.3  0.3<br><!-- End of picture text -->

4

### More Viterbi Examples

What is the optimal parse of the sequence for the CpG island HMM defined previously?

• (ACGT)10000

• A1000C80T1000C20A1000G60T1000

<u>Powers of 1.5:</u> N = 20 40 60 80 (1.5)<sup>N</sup> = 3x10<sup>3</sup> 1x10<sup>7</sup> 3x10<sup>10</sup> 1x10<sup>14</sup>

5

### Real World HMMs

6

#### “Profile HMM” with insertions/deletions

Of course, can have insertion/ deletion states for HMM models of DNA/RNA as well

- © Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

7

Correctly predicts ~97% of transmembrane helices according to authors

###### A. Krogh et al. _J. Mol. Biol._ 2001

- © Center for Biological Sequence Analysis. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

8

---

[Up: contents](index.md) · [Architecture of TMHMM →](02-architecture-of-tmhmm.md)
