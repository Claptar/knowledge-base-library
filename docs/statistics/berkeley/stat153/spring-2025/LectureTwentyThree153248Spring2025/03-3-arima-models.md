---
title: 3 ARIMA models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 ARIMA models

**Source:** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

ARIMA stands for AutoRegressive Integrated Moving Average. ARIMA is essentially differencing plus ARMA.

**Definition 3.1** (ARIMA) **.** _A time series model yt is said to be ARIMA(p, d, q) if_


ARIMA models are fit by the function `ARIMA()` in statismodels. The mean _µ_ above is taken to be zero by default when the order parameter _d_ in `ARIMA` is strictly larger than zero.

---

[← 2 The Box-Jenkins Time Series Modeling Strategy](02-2-the-box-jenkins-time-series-modeling-strategy.md) · [Up: contents](index.md) · [4 Seasonal ARMA Models →](04-4-seasonal-arma-models.md)
