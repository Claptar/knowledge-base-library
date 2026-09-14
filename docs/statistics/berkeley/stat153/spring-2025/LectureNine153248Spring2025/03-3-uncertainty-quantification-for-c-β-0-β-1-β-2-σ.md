---
title: 3 Uncertainty Quantification for c, β 0 , β 1 , β 2 , σ
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Uncertainty Quantification for c, β 0 , β 1 , β 2 , σ

**Source:** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For this, we use Bayesian analysis. Our prior for _β_ 0 _, β_ 1 _, β_ 2 _, σ_ is the same as the one used for linear regression:


for a large _C_ .

For the parameter _c_ , we also use a uniform prior. The range of values of _c_ is 1 _,_ 2 _, . . . , n_ . But actually there is no reason to allow _c_ = 1 and _c_ = _n_ as explained below.

When _c_ = 1, the variable ReLU( _t − c_ ) simply becomes _t − c_ = _t −_ 1 so that the nonlinear term ReLU( _t − c_ ) can be absorbed with the other terms as:


In other words, when _c_ = 1, the model reverts to the simple linear trend model (it is no longer a broken stick regression model). On the other hand, when _c_ = _n_ , we simply have ReLU( _t − c_ ) = 0 (because _t_ = 1 _, . . . , n_ is always smaller than _n_ ) so the term ReLU( _t − c_ ) has no effect when _c_ = _n_ .

Our range of values is therefore _c_ = 2 _, . . . , n_ . The prior for _c_ will be taken to be


With these priors, calculate the posterior distributions, exactly as in the case of the sinusoidal model. This leads to the following. The posterior distribution of _c_ is:


2

In other words, this is a discrete distribution with pmf:


The denominator above is simply the sum of the numerator values for all _c_ = 2 _, . . . , n −_ 1. In particular, the denominator does not depend on the particular value of _c_ anymore and is a constant. We can also write:


for _c_ = 2 _, . . . , n −_ 1.

Given _c_ , as remarked before, the model is just a linear regression model with _X_ -matrix given by _Xc_ . Therefore, by results from linear regression (see Problem 4 in Homework 1), the posterior density of _σ_ given the data as well as _c_ is characterized by:


Finally, the posterior distribution of _β_ given the data as well as _c_ and _σ_ is


where

---

[← 2 Estimation of c, β 0 , β 1 , β 2 , σ](02-2-estimation-of-c-β-0-β-1-β-2-σ.md) · [Up: contents](index.md) · [4 Posterior Sampling for Uncertainty Quantification →](04-4-posterior-sampling-for-uncertainty-quantification.md)
