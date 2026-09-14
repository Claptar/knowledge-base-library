---
title: 2 Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Multiple Linear Regression

**Source:** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In multiple linear regression, we have one response variable _y_ and _m_ covariates _x_ 1 _, . . . , xm_ ( _m_ = 1 corresponds to simple linear regression). We observe data on _n_ instances or subjects for all these variables: ( _yi, xi_ 1 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . The multiple linear regression model (with normal errors) is given by:


In the time series context, the model (4) arises in the following ways:

1. **Regression with functions of time** : Suppose we want to fit a quadratic function of time to the data. We can do this via the model (4) with _x_ 1 being the time variable, and _x_ 2 being the squared time i.e., _xi_ 1 = _i_ and _xi_ 2 = _i_<sup>2</sup> . Suppose we want to fit a simple sinusoidal function to the data. We can do this via (4) with _xi_ 1 = cos(2 _πi/_ 12) and _xi_ 2 = sin(2 _πi/_ 12).

2. **AutoRegression (AR)** : If we take _xij_ = _yi−j_ , then we get the AR model:


The idea here is that we are using the _m_ most recent values of the time series to predict the next observation. AR models are very commonly used and they work quite well for time series.

3

In Bayesian inference for (4), we work with the prior


for a very large positive _C_ . The joint posterior density of _β_ 0 _, . . . , βm, σ_ is then given by


where we use the notation


for the sum of squares.

The posterior over only the coefficient parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ .


where _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ denote the least squares estimators of _β_ 0 _, . . . , βm_ (i.e., ( _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ ) minimizes _S_ ( _β_ 0 _, . . . , βm_ ) over all values of _β_ 0 _, . . . , βm_ ).

Our posterior density for _β_ 0 _, . . . , βm_ is thus:


Now we will explain why this is a multivariate _t_ -density.

4

---

[← 1 Bayesian Inference for Simple Linear Regression](01-1-bayesian-inference-for-simple-linear-regression.md) · [Up: contents](index.md) · [3 Why is (5) a t -density? →](03-3-why-is-5-a-t--density.md)
