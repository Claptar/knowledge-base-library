---
title: 2 The Box-Jenkins Time Series Modeling Strategy
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 The Box-Jenkins Time Series Modeling Strategy

**Source:** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Box and Jenkins popularized the following strategy for modeling an observed time series _y_ 1 _, . . . , yn_ :

1. Generally _y_ 1 _, . . . , yn_ will exhibit various kinds of trends. Preprocess the data to transform it to another series _xt_ which does not have any discernible trends.

2. Fit an ARMA(p, q) model for appropriate _p_ and _q_ to the transformed data _xt_ .

The preprocessing in the first step above is usually done in one of the following two ways:

1. **Differencing** . The first difference of _{yt}_ is given by _∇yt_ := _yt − yt−_ 1 for _t_ = 2 _, . . . , n_ . The second difference is given by

   - _∇_<sup>2</sup> _yt_ = _∇_ ( _∇yt_ )


Higher order differences _∇_<sup>_k_</sup> _yt_ are defined recursively. Note that the length of the time series comes down after each successive differencing. For example, _∇yt_ has length _n−_ 1, _∇_<sup>2</sup> _yt_ has length _n −_ 2 and so on. Differencing usually eliminates increasing/decreasing trends. Usually one or two orders of differencing is enough to take care of increasing/decreasing trends.

2. **Seasonal Differencing** . Seasonal differencing is used to eliminate seasonal trends. Suppose we have a dataset having seasonal trends with period _s_ (for example, for monthly datasets, _s_ = 12). The seasonal first difference of _yt_ with period _s_ is defined as


Note that _∇syt_ is a time series of length _n − s_ . The second order seasonal difference is


and higher order seasonal differences are defined recursively. Seasonal differences eliminate seasonal trends. Usually, in datasets having seasonal and increasing/decreasing

2

trends, one first takes a seasonal difference. This often eliminates seasonality and might also eliminate the linear trend. If a linear trend still persists, one takes a regular difference of the seasonal differenced series. This will often give a series with no trend and seasonality.

To the transformed data _xt_ , one fits an ARMA(p, q) model which can be done via the `ARIMA` function from the statsmodels library. The order _p_ and _q_ can be determined via a model selection criterion such as AIC or BIC.

---

[← 1 ARMA( p , q ) Model](01-1-arma-p-q-model.md) · [Up: contents](index.md) · [3 ARIMA models →](03-3-arima-models.md)
