---
title: The 1/2 correction for binomial approximation
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The 1/2 correction for binomial approximation

**Source:** `lectures/20-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Fix _p_ , where 0 _< p <_ 1

- _Xi_ : Bernoulli( _p_ )

- _Sn_ = _X_ 1 + _· · ·_ + _Xn_ : Binomial( _n, p_ )

   - **P** ( _Sn ≤_ 21) = **P** ( _Sn <_ 22) _,_ because _Sn_ is integer

   - Compromise: consider **P** ( _Sn ≤_ 21 _._ 5)

- mean _np_ , variance _np_ (1 _− p_ )

- _−→_ standard normal

- _−_

- CDF of ~~￿~~ _np_<sup>_Sn_</sup> (1<sup>_−np_</sup> _p_ )

---

[← Apply to binomial](03-apply-to-binomial.md) · [Up: contents](index.md) · [Example →](05-example.md)
