---
title: 2 ACF and PACF of ARMA( p , q ) models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 ACF and PACF of ARMA( p , q ) models

**Source:** [`LectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For a causal stationary time series model, we can define ACF and PACF. The ACF is simply defined as:

_ACF_ ( _h_ ) = correlation between _yt_ and _yt_ + _h._

The PACF is defined as (it can be shown that the quantity below does not depend on _t_ if _{yt}_ is stationary):

_PACF_ ( _h_ ) = partial correlation between _yt_ and _yt_ + _h_ after removing the effect of _yt_ +1 _, . . . , yt_ + _h−_ 1 _._

We will not go into the formal definition of partial correlation between two random variables _X_ 1 and _X_ 2 after removing the effect of _Z_ 1 _, . . . , Zm_ (see e.g., `https://en.wikipedia.org/ wiki/Partial_correlation` ).

The key facts are:

1. For the MA( _q_ ) model, _ACF_ ( _h_ ) is exactly zero for _h > q_ . So ACF( _h_ ) can be used to determine the value of _q_ for the MA model.

2. For the AR( _p_ ) model, _PACF_ ( _h_ ) is exactly zero for _h > p_ . So PACF( _h_ ) can be used to determine the value of _p_ for the AR model.

3. For an ARMA( _p_ , _q_ ) model with both _p ≥_ 1 and _q ≥_ 1, neither the ACF nor the PACF cuts off after a certain lag. For such models, ACF and PACF are not useful for determining _p_ and _q_ . There are inbuilt functions `arma acf` and `arma` ~~`p`~~ `acf` for computing the ACF and PACF of causal stationary ARMA processes. These can be used to get an idea of the behaviour of the ACF and PACF for ARMA processes.

4. Given observed data _y_ 1 _, . . . , yn_ that is supposedly generated from a stationary time series model, we can estimate _ACF_ ( _h_ ) and _PACF_ ( _h_ ) for every _h_ . These estimates are called Sample ACF and Sample PACF respectively. These can be obtained from inbuilt functions in `statsmodels` . These are useful for determining _q_ (in order to use an MA( _q_ ) model) or _p_ (in order to use an AR( _p_ ) model). But they are not useful for determining both _p_ and _q_ in order to use an ARMA( _p_ , _q_ ) model.

Instead of using sample ACF and PACF, we use automatic model selection criteria such as AIC and BIC to determine _p_ and _q_ while using ARMA( _p_ , _q_ ) models.

---

[← 1 ARMA( p , q ) models](01-1-arma-p-q-models.md) · [Up: contents](index.md) · [3 Parameter Estimation, and AIC and BIC →](03-3-parameter-estimation-and-aic-and-bic.md)
