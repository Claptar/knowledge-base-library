---
title: 2 ARIMA models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 ARIMA models

**Source:** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

ARIMA stands for AutoRegressive Integrated Moving Average. ARIMA is essentially differencing plus ARMA.

**Definition 2.1** (ARIMA) **.** _A time series model yt is said to be ARIMA(p, d, q) if_


_texti.i.d ∼ where ϵt N_ (0 _, σ_<sup>2</sup> ) _._

ARIMA models are fit by the function `ARIMA()` in statismodels. The mean _µ_ above is taken to be zero by default when the order parameter _d_ in `ARIMA` is strictly larger than zero.

---

[← 1 The Box-Jenkins Time Series Modeling Strategy](01-1-the-box-jenkins-time-series-modeling-strategy.md) · [Up: contents](index.md) · [3 Seasonal ARMA Models →](03-3-seasonal-arma-models.md)
