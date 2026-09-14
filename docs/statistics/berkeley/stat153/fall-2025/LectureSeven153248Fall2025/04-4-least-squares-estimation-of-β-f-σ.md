---
title: 4 Least Squares Estimation of β, f, σ
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Least Squares Estimation of β, f, σ

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We use exactly the same method for parameter estimation as in the change of slope model. We take a bunch of possible values of _f_ , calculate the goodness of fit _RSS_ ( _f_ ) of the resulting linear regression model with fixed _f_ , and then use _f_<sup>ˆ</sup> as the minimizer of _RSS_ ( _f_ ) over _f_ . The remaining parameters ( _β_ and _σ_ ) are estimated as in usual linear regression with _f_ fixed at _f_<sup>ˆ</sup> . This algorithm is described below:

1. Take a grid of all possible values of _f_ in the range [0 _,_ 1 _/_ 2].

2. For each frequency value _f_ in the grid,

   - a) Form the matrix _Xf_

   - b) Do a regression of _y_ on _Xf_ and compute the Residual Sum of Squares _RSS_ ( _f_ )

3. Take _f_<sup>ˆ</sup> to be the grid value which minimizes _RSS_ ( _f_ ) over all the grid values.

4. Take _β_<sup>ˆ</sup> and _σ_ ˆ to be the usual regression estimates (of _β_ and _σ_ ) in the linear regression of _y_ on _Xf_ ˆ.

---

[← 3 Discrete sampling and restricting f to [0 , 1 / 2]](03-3-discrete-sampling-and-restricting-f-to-0-1-2.md) · [Up: contents](index.md) · [5 Bayesian Posterior →](05-5-bayesian-posterior.md)
