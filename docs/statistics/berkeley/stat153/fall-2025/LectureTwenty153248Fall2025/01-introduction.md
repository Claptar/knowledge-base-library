---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **STAT 153 & 248 - Time Series Lecture Twenty**

**Fall 2025, UC Berkeley**

Aditya Guntuboyina

November 06, 2025

In the last lecture, we introduced the notion of stationary time series models, and also started discussing stationarity of AutoRegressive models.

A time series model _{yt}_ is said to be stationary if:

1. E _yt_ does not change with _t_

2. var( _yt_ ) does not change with _t_

3. cov( _yt, yt_ + _h_ ) does not change with _t_ for every _h_ .

For a stationary time series, the AutoCovariance Function (ACVF) is defined as


By stationarity,


Note also that _γ_ (0) equals the variance of _yt_ . The Autocorrelation Function (ACF) is given by:


An important class of stationary time series models are the Moving Average Models.

---

[Up: contents](index.md) · [1 Moving Average (MA) Models →](02-1-moving-average-ma-models.md)
