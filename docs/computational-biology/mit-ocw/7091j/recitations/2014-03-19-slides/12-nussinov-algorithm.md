---
title: Nussinov algorithm
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Nussinov algorithm

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Look at one conLguous sub-­‐sequence from posiLon _i_ to posiLon _j_ in our complete sequence of length _N_ , and calculate the score of the best structure for just that sub-­‐sequence

- This opLmal score (call it _S_ ( _i_ , _j_ )) can be defined recursively in terms of opLma l scores of smaller sub-­‐sequences

- Four possible ways that a structure of nested base pairs on _i_ ... _j_ can be constructed

   1. _i_ , _j_ are a base pair, added on to a structure for _i_ +1 ... _j_ –1

   2. _i_ is unpaired, added on to a structure for _i_ +1 ... _j_

   3. _j_ is unpaired, added on to a structure for _i ._ .. _j_ –1

   4. _i_ , _j_ are paired, but not to each other; the structure for _i_ ... _j_ adds together sub-­‐structures for two sub-­‐sequences, _i ._ .. _k_ and _k_ +1 ... _j_ (a bifurcaLon)


<!-- Start of picture text -->
S ( i  + 1, j  – 1)  S ( i  + 1, j )<br>S ( i , j  – 1)<br>S ( i , k )  S ( k  + 1, j )<br>i  + 1  j  – 1<br>i  j  i  i  + 1  j i  j  – 1  j i  k  k  + 1  j<br><!-- End of picture text -->

1. _i_ , _j_ pair

4. Bifurcation

2. _i_ unpaired

3. _j_ unpaired

16

---

[← Mutual InformaLon (MI)](11-mutual-informalon-mi.md) · [Up: contents](index.md) · [Nussinov algorithm →](13-nussinov-algorithm.md)
