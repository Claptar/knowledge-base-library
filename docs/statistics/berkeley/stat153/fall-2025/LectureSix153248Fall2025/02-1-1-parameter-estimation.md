---
title: 1.1 Parameter Estimation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSix153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.1 Parameter Estimation

**Source:** [`LectureSix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Least squares again is the most basic estimation procedure. The sum of squares is:


We need to minimize this over all the four variables _β_ 0 _, β_ 1 _, β_ 2 _, c_ . Using matrix notation, we can write


If we fix _c_ , then it is easy to minimize _S_ ( _β, c_ ) over _β_ . This is the same as linear regression and the minimizing _β_ is given by:


and the smallest value of _S_ ( _β, c_ ) for fixed _c_ is _S_ ( _β_<sup>ˆ</sup> ( _c_ ) _, c_ ) which is just the RSS in the multiple linear regression with fixed _c_ . We use the notation:


The least squares estimates of _β_ and _c_ can therefore be found in the following way:

1. Fix a finite set of possible values of _c_ . In this change of slope model, it is reasonable to assume that _c ∈{_ 1 _, . . . , n}_ . One can also take a finer grid of values in the range [1 _, n_ ].

2. For each value of _c_ in the chosen set, calculate _β_<sup>ˆ</sup> ( _c_ ) and define _RSS_ ( _c_ ) = _S_ ( _β_<sup>ˆ</sup> ( _c_ ) _, c_ ).

3. Take _c_ ˆ to be the value of _c_ which minimizes _RSS_ ( _c_ ).

4. Take _β_ = _β_<sup>ˆ</sup> (ˆ _c_ ).

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [1.2 Bayesian Inference →](03-1-2-bayesian-inference.md)
