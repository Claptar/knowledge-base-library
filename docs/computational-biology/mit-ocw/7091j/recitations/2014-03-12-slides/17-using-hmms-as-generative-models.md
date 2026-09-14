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

We want to generate a DNA sequence of length _L_ that could be observed from this model

- **(1)** choose initial state from _P_ 1( _S_ )

- **(2)** emit first base of sequence according to current state and _P_ E( _X_ | _S_ ) for 1 < _i_ < _L:_

   - **(3)** choose state at position _i_ according to transition matrix and state at position _i_ – 1, e.g. using _P_ T _(Si|Si-1)_

   - **(4)** emit base of sequence according to current state S _i_ and _P_ E( _X_ | _Si_ )

19

---

[← HMMs continued](16-hmms-continued.md) · [Up: contents](index.md) · [The Viterbi Algorithm →](18-the-viterbi-algorithm.md)
