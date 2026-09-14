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

- Since these are the only four possible cases, the opLmal score _S_ ( _i_ , _j_ ) is just the maximum of the four possibiliLes

- We’ve   thus defined the opLmal score _S_ ( _i_ , _j_ ) recursively as a funcLon only of opLmal scores of smaller sub-­‐sequences, so we only need to remember these scores, not the combinatorial explosion of possible structures

_S_ ( _i_ , _j_ ) = max


<!-- Start of picture text -->
S ( i  + 1, j  – 1)  S ( i  + 1, j )<br>S ( i , j  – 1)<br>i  + 1  j  – 1<br>i  j i  i  + 1  j  i j  – 1  j<br><!-- End of picture text -->

_S_ ( _i_ + 1, _j_ – 1) +1 [if _i_ , _j_ base pair] _S_ ( _i_ + 1, _j_ ) S( _i_ , _j_ – 1) max **_i_ <** **_k_ <** **_j_** _S_ ( _i_ , _k_ ) + _S_ ( _k_ + 1, _j_ )


<!-- Start of picture text -->
S ( i , k )  S ( k  + 1, j )<br>i k k  + 1  j<br><!-- End of picture text -->

1. _i_ , _j_ pair

4. Bifurcation

2. _i_ unpaired

3. _j_ unpaired

20

---

[← Nussinov algorithm](15-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov algorithm →](17-nussinov-algorithm.md)
