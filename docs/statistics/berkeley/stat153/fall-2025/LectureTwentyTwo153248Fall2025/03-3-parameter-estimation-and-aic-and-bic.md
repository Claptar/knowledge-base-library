---
title: 3 Parameter Estimation, and AIC and BIC
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Parameter Estimation, and AIC and BIC

**Source:** [`LectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For parameter estimation in ARMA( _p_ , _q_ ) models, we simply use the `ARIMA` function from `statsmodels` . This uses maximum likelihood estimation. Writing the likelihood for ARMA models is not easy, and the function uses some ideas from state space modeling (and the Kalman filter) for writing the likelihood. We will not go into the details of this. It should be noted that, quite often, the `arima` function will give warnings and errors while fitting ARMA models. We will be ignoring these messages.

The AIC and BIC for a fitted ARMA( _p_ , _q_ ) model are calculated as:

_AIC_ = ( _−_ 2) _×_ maximized log-likelihood + 2 _×_ number of parameters

_BIC_ = ( _−_ 2) _×_ maximized log-likelihood + (log _n_ ) _×_ number of parameters

3

These can be used for model selection. Models with smaller values of AIC and BIC are preferred. The first term in the definition of AIC and BIC determines the quality of fit to the data, and the second term penalizes model complexity thereby guarding against overfitting.

Generally log _n_ will be larger than 2 so BIC will lead to sparser models (i.e., models with fewer number of parameters) compared to AIC.

---

[← 2 ACF and PACF of ARMA( p , q ) models](02-2-acf-and-pacf-of-arma-p-q-models.md) · [Up: contents](index.md) · [4 The Box-Jenkins Time Series Modeling Strategy →](04-4-the-box-jenkins-time-series-modeling-strategy.md)
