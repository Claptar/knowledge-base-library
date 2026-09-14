---
title: 2 AR (Auto-Regressive) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 AR (Auto-Regressive) Models

**Source:** [`LectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe time series _y_ 1 _, . . . , yn_ . AR models are simply linear regression models where the covariates are chosen to be past (or lagged) values of _yt_ .

The AR model of order _p_ (referred to by _AR_ ( _p_ )) is given by


for _t_ = _p_ + 1 _, . . . , n_ . In matrix notation,


where


This regression model is called AutoRegression because the responses as well as the covariates are both formed from the same time series: the time series _yt_ is regressed on its own lagged values _yt−_ 1 _, . . . , yt−p_ .

The parameters _ϕ_ 0 _, . . . , ϕp_ are estimated in the usual way by minimizing _∥Y − Xβ∥_<sup>2</sup> . Let the estimates by _ϕ_<sup>ˆ</sup> 0 _, . . . , ϕ_<sup>ˆ</sup> _p_ .

1

AR models are useful for predicting future values of the time series. For predicting _yn_ +1, we plug _t_ = _n_ + 1 in (1) to get


Note that _yn, yn−_ 1 _, . . . , yn_ +1 _−p_ are all observed and they are the last _p_ observations. For predicting _yn_ +2, we plug _t_ = _n_ + 2 in (1) to get


In the above, _yn_ +1 is not observed. But we can replace it by the predicted value _y_ ˆ _n_ +1. This gives


More generally, we predict _yn_ + _i_ by the recursion


where the recursion is initialized with


We will look at AR models in more details in the coming lectures. Today, we shall provide a motivation for their use through the sunspots dataset. This was how the AR models were originally invented by Yule [1].

---

[← 1 Auto or Lagged Regression](01-1-auto-or-lagged-regression.md) · [Up: contents](index.md) · [3 AR Models for the Sunspots Data →](03-3-ar-models-for-the-sunspots-data.md)
