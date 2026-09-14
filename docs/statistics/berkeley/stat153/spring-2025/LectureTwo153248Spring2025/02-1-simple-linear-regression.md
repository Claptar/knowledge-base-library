---
title: 1 Simple Linear Regression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Simple Linear Regression

**Source:** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ). _xi_ denotes the covariate value and _yi_ denotes the response value for the _i_<sup>th</sup> observation. In the time series context, in our initial applications, we shall apply linear regression with time as the covariate. For example, in the time series dataset on the population of the United States for each month from January 1959 to December 2024: _n_ denotes the total number of data points, _xi_ = _i_ and _yi_ denotes the observed population data for the _i_<sup>th</sup> month (first month is January 1959, second month is February 1959 and so on).

In the linear regression model, it is assumed that _x_ 1 _, . . . , xn_ are fixed deterministic values, and that the response values _y_ 1 _, . . . , yn_ satisfy the model equation:


Another way of writing the model is:


There are three parameters in this model: _β_ 0 _, β_ 1 and _σ_<sup>2</sup> .

We discuss frequentist and Bayesian approaches for estimating the parameters (as well as uncertainty quantification) from the observed data. A key role in both approaches will be played by the likelihood function which is the joint density of the observations given the

1

parameter values. The likelihood function is given by:


where


Note again that we are assuming that _x_ 1 _, . . . , xn_ are fixed.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Frequentist Inference →](03-2-frequentist-inference.md)
