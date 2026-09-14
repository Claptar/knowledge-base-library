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

- Storing the _S_ ( _i_ , _j_ ) matrix requires memory proporLonal to _N_<sup>2</sup> , similar to what sequence alignment algorithms need

- However, the innermost loop of having to find opLmal potenLal bifurcaLon points _k_ means that the folding algorithm requires Lme proporLonal to _N_<sup>3</sup> , a factor of _N_ more Lme-­‐intensive than sequence alignment

   - RNA   folding calculaLons o=en require a large amount of computer power

22

---

[← Nussinov algorithm](17-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov Algorithm Example →](19-nussinov-algorithm-example.md)
