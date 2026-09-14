---
title: 1 Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Simple Linear Regression

**Source:** [`LectureThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ). In the time series context, _y_ 1 _, . . . , yn_ is the observed time series. For the covariate, we have two options:

1. _xi_ = _i_ (covariate is time)

2. _xi_ = _yi−_ 1 (covariate is lagged version of the observed time series)

For now, we focus on the first case _xi_ = _i_ (AutoRegression will be studied in detail later).

The linear regression model is:


where _β_ 0 and _β_ 1 are unknown parameters (their values are to be estimated from the data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ )) and _ϵi_ denotes the error term accounting for the deviation between _yi_ and the model equation _β_ 0 + _β_ 1 _xi_ .

We use the function `OLS` in the Python library `statsmodels` to do inference on _β_ 0 and _β_ 1 (inference refers to estimating their values, and also to obtain uncertainty intervals).

There are two main approaches for statistical inference: Frequentist and Bayesian. We shall explore how each of these work for linear regression.

---

[Up: contents](index.md) · [2 Frequentist Inference →](02-2-frequentist-inference.md)
