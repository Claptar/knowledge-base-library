---
title: 1 Regression with t as covariate
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Regression with t as covariate

**Source:** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The simplest and the first model that we studied was the linear regression model:


We then studied at nonlinear regression. One way to make the right hand side of (1) nonlinear in _t_ is to introduce terms involving ( _t − c_ )+ for certain knots _c_ :


Here ( _t − c_ )+ is the positive part function applied to _t − c_ 1. We shall also use the notation ReLU and _σ_ ( _·_ ) to denote this function (please do not confuse the function _σ_ ( _·_ ) with the standard deviation _σ_ of _ϵt_ ; we shall use the same notation for both but they can be easily distinguished from the context):


The unknown parameters in (2) are _β_ 0 _, . . . , βk_ +1 _, c_ 1 _, . . . , ck_ and _σ_ .

The model (2) is also a linear model but it is linear in the modified variables 1 _, t,_ ( _t − c_ 1)+ _, . . . ,_ ( _t − ck_ )+ (and nonlinear in the original variable _t_ ). The vector of these modified variables:


can be called the feature vector. The model is a linear function of the feature vectors.

We now rewrite the model (2) in a slightly different form. The time _t_ represents the covariate _xt_ here, so we write _xt_ = _t_ . We shall remove the term _t_ as it is covered by _t_ = ( _t − c_ )+ for _c_ = 0 (note that 1 _≤ t ≤ n_ ). We also write _µt_ for the mean of _yt_ . We shall also use _rt_ to denote the feature vector:


and _st_ to denote:


1

With these changes, the model (2) becomes:


In words, the univariate covariate _xt_ (which is simply _t_ ) is first converted to the _k ×_ 1 vector _st_ in a linear fastion. Then the nonlinear function _σ_ ( _·_ ) is applied to _st_ (here _σ_ ( _·_ ) is applied separately to each coordinate of _st_ ) to generate the feature vector _rt_ . Then _µt_ is a linear function of _rt_ which serves as the mean to _yt_ .

---

[Up: contents](index.md) · [2 AutoRegression →](02-2-autoregression.md)
