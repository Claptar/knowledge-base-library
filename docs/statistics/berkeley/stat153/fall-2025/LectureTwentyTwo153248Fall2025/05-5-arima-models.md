---
title: 5 ARIMA models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 ARIMA models

**Source:** [`LectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

ARIMA stands for AutoRegressive Integrated Moving Average. ARIMA is essentially differencing plus ARMA.

**Definition 5.1** (ARIMA) **.** _A time series model yt is said to be ARIMA(p, d, q) if_


ARIMA models are fit by the function `ARIMA()` in `statsmodels` . The mean _µ_ above is taken to be zero by default when the order parameter _d_ in `ARIMA` is strictly larger than zero.

When _d_ = 1, the ARIMA( _p_ , 1, _q_ ) model becomes:


4

Define a process _ηt_ by _yt_ = _y_ 0 + _µt_ + _ηt_ (in other words, _ηt_ = _yt − y_ 0 _− µt_ ). Then

_∇yt_ = _yt − yt−_ 1 = ( _y_ 0 + _µt_ + _ηt_ ) _−_ ( _y_ 0 + _µ_ ( _t −_ 1) + _ηt−_ 1) = _µ_ + ( _ηt − ηt−_ 1) = _µ_ + _∇ηt._

Plugging this into (5), we get


In other words, (5) is equivalent to:


When _µ̸_ = 0, the term _y_ 0 + _µt_ represents a deterministic linear trend in _yt_ . However many real-world time series (e.g., macroeconomic variables such as GNP or GDP) are unlikely to exhibit an exact deterministic linear trend. For this reason, the default behavior of the `ARIMA` function in `statsmodels` sets _µ_ = 0 in (5). To fit it with _µ̸_ = 0, one must specify the argument `trend = ’t’` .

5

---

[← 4 The Box-Jenkins Time Series Modeling Strategy](04-4-the-box-jenkins-time-series-modeling-strategy.md) · [Up: contents](index.md)
