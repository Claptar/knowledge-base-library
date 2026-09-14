---
title: 5 The Box-Jenkins Modeling Philosophy
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 The Box-Jenkins Modeling Philosophy

**Source:** [`LectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

G. Box and G. Jenkins (two researchers who developed ARIMA models) recommended avoiding working with AR models which are **NOT** causal-stationary. Specifically, their recommendation is:

1. Only work with MA models (which are always causal stationary) and causal stationary AR models.

2. If the data are such that stationary models are not a good fit, then preprocess the data using differencing (possibly after applying a preliminary transformation such as log). After appropriate differencing, fit MA models or causal stationary AR models.

More generally Box and Jenkins recommended working with causal stationary ARMA models (after preprocessing the data). We shall look at ARMA models in the next lecture but they are given by the formula:


The left hand side resembles the AR( _p_ ) model and the right hand side resembles the MA( _q_ ) model. This is the reason why this model is called ARMA( _p_ , _q_ ). Clearly ARMA( _p_ , 0) = AR( _p_ ) and ARMA(0, _q_ ) = MA( _q_ ).

We say that _yt_ satisfies the ARIMA( _p_ , _d_ , _q_ ) model if _xt_ satisfies the ARMA( _p_ , _q_ ) model where _xt_ is the time series obtained by differencing _yt d_ times (first difference is given by _yt − yt−_ 1, second difference is ( _yt − yt−_ 1) _−_ ( _yt−_ 1 _− yt−_ 2) = _yt −_ 2 _yt−_ 1 + _yt−_ 2 and so on).

4

Note therefore that ARIMA( _p_ , 0, _q_ ) = ARMA( _p_ , _q_ ), ARIMA( _p_ , 0, 0) = AR( _p_ ) and ARIMA(0, 0, _q_ ) = MA( _q_ ).

5

---

[← 4 AR( p ) models](04-4-ar-p-models.md) · [Up: contents](index.md)
