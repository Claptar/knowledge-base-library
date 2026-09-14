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

2. _i_ is unpaired, added on to a structure for _i+1 ._ .. _j_

- In case 2, the opLmal score _S_ ( _i_ + 1, _j_ ) is independent of the addiLon of an unpaired base _i_ , so _S_ ( _i_ + 1, _j_ ) + 0 is the score of the opLmal structure on _i_ , _j_ condiLonal on _i_ being unpaired

   3. _j_ is unpaired, added on to a structure for _i ._ .. _j_ –1

- Case 3 is the same thing, but condiLonal on _j_ being unpaired


<!-- Start of picture text -->
S ( i  + 1, j )<br>S ( i , j  – 1)<br>S ( i , j ) =  S ( i  + 1, j )<br>S ( i , j ) = S( i , j  – 1)<br>i  i  + 1  j i  j  – 1  j<br><!-- End of picture text -->

2. _i_ unpaired

3. _j_ unpaired

18

---

[← Nussinov algorithm](13-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov algorithm →](15-nussinov-algorithm.md)
