---
title: Hypergeometric Test
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hypergeometric Test

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Say you have already chosen the Na items of set A – now you just need to choose set B. Then probability of observing exactly _k_ items overlapping among _Na_ and _Nb_ size groups drawn from _N_ total items is:

- <u>#</u> total ways of choosing B, <u>given</u> _k_ must overlap with A

   - # total ways of choosing B w/o any constraints


_− − −_ <u>(choose</u> _k_ from A to be in B’s overlap)(choose _nb k_ of B that don’t overlap, from <u>pool</u> of _N na_ non-A’s) (choose any _nb_ for B)


<!-- Start of picture text -->
− −<br>− −<br>nka Nnb nka<br>= ) P ( k ;  na, nb, N ) =<br>N<br>nb<br><!-- End of picture text -->

30

---

[← Likelihood ratio test](15-likelihood-ratio-test.md) · [Up: contents](index.md) · [Hypergeometric Test →](17-hypergeometric-test.md)
