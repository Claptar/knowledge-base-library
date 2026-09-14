---
title: 3 Bayesian Inference for Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Bayesian Inference for Linear Regression

**Source:** [`LectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In Bayesian inference for (1), we work with the prior


for a very large positive _C_ . The joint posterior density of _β_ 0 _, . . . , βm, σ_ is then given by


where we use the notation


for the sum of squares.

5

The posterior over only the coefficient parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ .


where _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ denote the least squares estimators of _β_ 0 _, . . . , βm_ (i.e., ( _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ ) minimizes _S_ ( _β_ 0 _, . . . , βm_ ) over all values of _β_ 0 _, . . . , βm_ ).

Our posterior density for _β_ 0 _, . . . , βm_ is thus:


In the next lecture, we will explain why this is a multivariate _t_ -density.

6

---

[← 2 Frequentist Inference for Linear Regression](02-2-frequentist-inference-for-linear-regression.md) · [Up: contents](index.md)
