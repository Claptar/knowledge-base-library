---
title: 1 Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Multiple Linear Regression

**Source:** [`LectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In multiple linear regression, we have one response variable _y_ and _m_ covariates _x_ 1 _, . . . , xm_ ( _m_ = 1 corresponds to simple linear regression). We observe data on _n_ instances or subjects for all these variables: ( _yi, xi_ 1 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ .

The following vector-matrix notation is very standard:


Note the presence of the column of ones in the _X_ -matrix. This notation is used not just to write formulae for linear regression, but also in code. For example, the OLS function in `statsmodels` uses the syntax `sm.OLS(y, X).fit()` to fit the linear regression model, where _y_ ( _n ×_ 1 vector) and _X_ ( _n ×_ ( _m_ + 1) matrix) are defined above.

The multiple linear regression model (with normal errors) is given by:


In the time series context, the model (1) arises in the following ways:

1. **Regression with functions of time** : Suppose we want to fit a quadratic function of time to the data. We can do this via the model (1) with _x_ 1 being the time variable, and _x_ 2 being the squared time i.e., _xi_ 1 = _i_ and _xi_ 2 = _i_<sup>2</sup> . Suppose we want to fit a simple sinusoidal function to the data. We can do this via (1) with _xi_ 1 = cos(2 _πi/_ 12) and _xi_ 2 = sin(2 _πi/_ 12).

2. **AutoRegression (AR)** : If we take _xij_ = _yi−j_ , then we get the AR model:

_yt_ = _β_ 0 + _β_ 1 _yt−_ 1 + _· · ·_ + _βmyt−m_ + _ϵt._

1

The idea here is that we are using the _m_ most recent values of the time series to predict the next observation. AR models are very commonly used and they work quite well for time series.

Let us focus for now on regression using functions of time. We shall study AutoRegression in detail later.

Our goal is to use the observed data (in _y, X_ ) to obtain estimates along with uncertainty interals for the parameters _β_ 0 _, . . . , βm_ . There are two broad principles for doing this: frequentist and Bayesian.

---

[Up: contents](index.md) · [2 Frequentist Inference for Linear Regression →](02-2-frequentist-inference-for-linear-regression.md)
