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

4. _i_ , _j_ are paired, but not to each other; the structure for _i_ ... _j_ adds together sub-­‐structures for two sub-­‐sequences, _i ._ .. _k_ and _k_ +1 ... _j_ (a bifurcaLon)

- the

- -­‐ We deal with puOng two independent sub-­‐structures together, opLmal score _S_ ( _i_ , _k_ ) is independent of anything going on in _k_ +1 ... _j_ , and vice versa

- -­‐ Must consider all possible _k_ ’s   between _i_ and _j_

_S_ ( _i_ , _j_ ) =<sup>max</sup> **_i_ <** **_k_ <** **_j_**<sup>_S_(</sup><sup>_i_,</sup><sup>_k_) +</sup><sup>_S_(</sup><sup>_k_+ 1,</sup><sup>_j_)</sup>


<!-- Start of picture text -->
S ( i , k )  S ( k  + 1, j )<br>i k  k  + 1  j<br><!-- End of picture text -->

4. Bifurcation

19

---

[← Nussinov algorithm](14-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov algorithm →](16-nussinov-algorithm.md)
