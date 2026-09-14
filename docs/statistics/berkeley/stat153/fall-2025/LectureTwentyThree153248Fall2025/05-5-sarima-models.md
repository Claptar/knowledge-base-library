---
title: 5 SARIMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 SARIMA Models

**Source:** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

These models are obtained by combining differencing with multiplicative seasonal ARMA models. These models are denoted by ARIMA( _p_ , _d_ , _q_ ) _×_ ( _P_ , _D_ , _Q_ ) _s_ . This means that after differencing _d_ times and seasonal differencing _D_ times (with period _s_ ), we get a multiplicative seasonal ARMA model. In other words, _{yt}_ is ARIMA( _p_ , _d_ , _q_ ) _×_ ( _P_ , _D_ , _Q_ ) _s_ if it satisfies the difference equation:


Recall that _∇_<sup>_d_</sup> _s_<sup>= (1</sup><sup>_−Bs_)</sup><sup>_d_and</sup><sup>_∇d_= (1</sup><sup>_−B_)</sup><sup>_d_denotethedifferencingoperators.</sup>

In the co2 example, we wanted to use the model ARMA(0 _,_ 1) _×_ (0 _,_ 1)12 to the seasonal and first differenced data: _∇∇_ 12 _Xt_ . In other words, we want to fit the SARIMA model with nonseasonal orders 0 _,_ 1 _,_ 1 and seasonal orders 0 _,_ 1 _,_ 1 with seasonal period 12 to the original co2 dataset. This model can be fit to the data using the function `ARIMA` with the `seasonal` ~~`o`~~ `rder` argument.

3

---

[← 4 Multiplicative Seasonal ARMA Models](04-4-multiplicative-seasonal-arma-models.md) · [Up: contents](index.md)
