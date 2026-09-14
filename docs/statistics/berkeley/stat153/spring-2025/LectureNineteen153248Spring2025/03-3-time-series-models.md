---
title: 3 Time Series Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNineteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNineteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Time Series Models

**Source:** [`LectureNineteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNineteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Before proceeding further, let us take a general look at time series models (especially the models that we have already considered), and introduce the concept of “Stationarity”. Stationarity is an important property that some time series models satisfy while others do not.

We have already seen many models for observed time series data _y_ 1 _, . . . , yn_ . These models describe the distribution of _y_ 1 _, . . . , yn_ in terms of various parameters. Even though, the observed data only corresponds to times _t_ = 1 _, . . . , n_ , it makes sense for the model to describe the distribution of _yt_ for all _t_ past and present i.e., _t_ = _. . . , −_ 3 _, −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ . This is because one may be interested in predicting the values of _yt_ for unobserved times.

All of our models have error terms _ϵt_ that we assume are i.i.d Gaussian _N_ (0 _, σ_<sup>2</sup> ). This ensures that the whole time series _{yt}_ is jointly Gaussian. Gaussianity ensures that the behavior of the time series model is characterized by means (expectations) and covariances.

**Example 3.1.** _yt_ = _β_ 0 + _β_ 1 _t_ + _ϵt. The means are given by:_


_and covariances are:_


_So the mean changes with t, variance is constant and there is no correlation between different time points._

4

**Example 3.2.** _yt_ = _β_ 0 + _β_ 1 cos(2 _πft_ ) + _β_ 2 sin(2 _πft_ ) + _ϵt The means are given by:_


_and covariances are:_


_Again the mean changes with t, variance is constant and there is no correlation between different time points._

**Example 3.3.** _Consider the Spectrum model:_


_with β_ 11 _, β_ 21 _, β_ 12 _, β_ 22 _, . . . , β_ 1 _m, β_ 2 _m all independent with_


_For this model,_ E _yt_ = _β_ 0 _so that the mean is constant over time (unlike the previous two models). The covariance is given by_

_cov_ ( _yt_ 1 _, yt_ 2)


_This model incorporates dependence between yt at different time points t (unlike the previous two models). Further, the covariance between yt_ 1 _and yt_ 2 _only depends on the distance |t_ 1 _−t_ 2 _| between the two time points._

---

[← 2 Prediction Standard Errors](02-2-prediction-standard-errors.md) · [Up: contents](index.md) · [4 Stationarity →](04-4-stationarity.md)
