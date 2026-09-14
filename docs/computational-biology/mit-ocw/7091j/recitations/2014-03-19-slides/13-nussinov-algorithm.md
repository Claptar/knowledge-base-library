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

1. _i_ , _j_ are a base pair, added on to a structure for _i_ +1 ... _j_ –1

- The score we add for the base pair _i_ , _j_ is independent of any details of the opLmal structure on _i_ + 1... _j_ – 1

- Similarly, the opLmal structure on _i_ + 1... _j_ – 1 and its score _S_ ( _i_ + 1, _j_ – 1) are unaffected by whether _i_ , _j_ are base paired or not (or anything else that happens in the rest of the sequence)

- Therefore, _S_ ( _i_ , _j_ ) is just _S_ ( _i_ + 1, _j_ – 1) plus one, if _i_ , _j_ can base pair.


<!-- Start of picture text -->
S ( i  + 1, j  – 1)<br>S ( i , j ) = S ( i  + 1, j  – 1) +1 [if  i , j  base pair]<br>i  + 1  j –1<br>i  j<br><!-- End of picture text -->


<!-- Start of picture text -->
1.  i , j pair<br><!-- End of picture text -->

17

---

[← Nussinov algorithm](12-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov algorithm →](14-nussinov-algorithm.md)
