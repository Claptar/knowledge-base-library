---
title: 4 The Box-Jenkins Time Series Modeling Strategy
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 The Box-Jenkins Time Series Modeling Strategy

**Source:** [`LectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Box and Jenkins popularized the following strategy for modeling an observed time series _y_ 1 _, . . . , yn_ :

1. Generally _y_ 1 _, . . . , yn_ will exhibit various kinds of trends. Preprocess the data to transform it to another series _xt_ which does not have any discernible trends.

2. Fit an ARMA(p, q) model for appropriate _p_ and _q_ to the transformed data _xt_ .

The preprocessing in the first step above is usually done by taking differences (either for the original data or for its logarithms). The first difference of _{yt}_ is given by _∇yt_ := _yt − yt−_ 1 for _t_ = 2 _, . . . , n_ . The second difference is given by


Higher order differences _∇_<sup>_k_</sup> _yt_ are defined recursively. Note that the length of the time series comes down after each successive differencing. For example, _∇yt_ has length _n −_ 1, _∇_<sup>2</sup> _yt_ has length _n−_ 2 and so on. Differencing usually eliminates increasing/decreasing trends. Usually one or two orders of differencing is enough to take care of increasing/decreasing trends.

To the transformed data _xt_ , one fits an ARMA(p, q) model which can be done via the `ARIMA` function from the statsmodels library. The order _p_ and _q_ can be determined via a model selection criterion such as AIC or BIC.

---

[← 3 Parameter Estimation, and AIC and BIC](03-3-parameter-estimation-and-aic-and-bic.md) · [Up: contents](index.md) · [5 ARIMA models →](05-5-arima-models.md)
