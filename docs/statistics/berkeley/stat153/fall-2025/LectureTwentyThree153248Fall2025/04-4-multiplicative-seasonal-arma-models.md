---
title: 4 Multiplicative Seasonal ARMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Multiplicative Seasonal ARMA Models

**Source:** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For the `co2` dataset (from the time series analysis textbook by Cryer and Chan), for the first and seasonal differenced data, we saw that the sample autocorrelations seem nonnegligible at lags 0, 1, 11, 12, 13 and those at all other lags seem negligible. This behaviour can be produced in a MA(13) model but that model will have 14 parameters possibly leading to overfitting.

2

We can get a much more parsimonious model for this dataset by _combining_ the MA(1) model with a seasonal MA(1) model of period 12. Specifically, consider the model _yt_ = (1 + Θ _B_<sup>12</sup> )(1 + _θB_ ) _ϵt_ = �1 + _θB_ + Θ _B_<sup>12</sup> + _θ_ Θ _B_<sup>13�</sup> _ϵt_ = _ϵt_ + _θϵt−_ 1 + Θ _ϵt−_ 12 + _θ_ Θ _ϵt−_ 13 _._

It is easy to check that model has the autocorrelation function:


and


At every other lag _h >_ 0, the autocorrelation _ρX_ ( _h_ ) equals zero. Based on this ACF (and the sample ACF calculated from the data), this model can be suitable for the first and seasonal differenced data in the co2 dataset.

More generally, we can combine, by multiplication, ARMA and seasonal ARMA models to obtain models which have special autocorrelation properties with respect to seasonal lags. The **Multiplicative Seasonal Autoregressive Moving Average Model** ARMA( _p_ , _q_ ) _×_ ( _P_ , _Q_ ) _s_ is defined via the difference equation:


The model we looked at above for the co2 dataset is ARMA(0, 1) _×_ (0, 1)12.

Another example of a multiplicative seasonal ARMA model is ARMA(0, 1) _×_ (1, 0)12 (this is same as _MA_ (1) _× AR_ (1)12)


The autocorrelation function of this model can be checked to be _ρ_ (12 _h_ ) = Φ<sup>_h_</sup> for _h ≥_ 0 and


and _ρ_ ( _h_ ) = 0 at all other lags.

When we have a dataset whose ACF and PACF show interesting patterns at seasonal lags, consider using a multiplicative seasonal ARMA model. You may use the `Statsmodels` functions `arma` ~~`a`~~ `cf` and `arma` ~~`p`~~ `acf` to understand the autocorrelation and partial autocorrelation functions of these models.

---

[← 3 Seasonal ARMA Models](03-3-seasonal-arma-models.md) · [Up: contents](index.md) · [5 SARIMA Models →](05-5-sarima-models.md)
