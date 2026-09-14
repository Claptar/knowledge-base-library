---
title: 2 Moving Average (MA) Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwenty153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Moving Average (MA) Models

**Source:** [`LectureTwenty153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

MA models present the simplest examples of stationary time series models that are not just white noise. Given a positive integer _q ≥_ 1, the Moving Average model with order _q_ (denoted by MA( _q_ )) is defined by the equation:


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The MA( _q_ ) model has _q_ +2 unknown parameters which are estimated from observed data: _µ, θ_ 1 _, . . . , θq, σ_ .

The MA( _q_ ) model has been called the “Summation of Random Causes” by its inventor Slutzky in the original paper titled “The summation of random causes as the source of cyclic processes” published in Econometrica in 1937. Basically the _ϵt_ ’s can be treated as random causes which are assumed to be independently and identically distributed. The actual observations _yt_ ’s are consequences of these causes. The consequence for tine _t_ depends on the cause for time _t_ as well as the causes for times _t −_ 1 _, . . . , t − q_ . These different causes affect the consequence at time _t_ differently depending on the values of _θ_ 1 _, . . . , θq_ . Note that successive observations _yt_ share some common causes leading to dependence between the successive values of _yt_ .

The mean of _yt_ is clearly equal to _µ_ (so it is constant in _t_ ). The covariance between _yt_ and _yt_ + _h_ is given by:

cov( _yt, yt_ + _h_ )


Note that, in the sum<sup>�</sup><sup>_q_</sup> _j_ =0<sup>_θjϵt−j_,wetake</sup><sup>_θ_0=1.Because</sup><sup>_{ϵt}_isGaussianwhitenoise,</sup> the covariance cov ( _ϵt−j, ϵt_ + _h−k_ ) equals zero unless _t − j_ = _t_ + _h − k_ i.e., _k_ = _j_ + _h_ . So we need the three conditions 0 _≤ j ≤ q_ , 0 _≤ k ≤ q_ as well as _k_ = _j_ + _h_ . If _h > q_ , it is clear that this is not possible for any _j, k_ . So we have cov( _yt, yt_ + _h_ ) equals zero when _h > q_ . When 0 _≤ h ≤ q_ , we have 0 _≤ j ≤ q_ and 0 _≤ j_ + _h ≤ q_ which implies 0 _≤ j ≤ q − h_ . We then get


We thus have:


The above covariance does not depend on _t_ which shows that the MA( _q_ ) model is stationary. Thus the ACVF of MA( _q_ ) is:


3

The ACF _ρ_ ( _h_ ) = _γ_ ( _h_ ) _/γ_ (0) equals:


The simplest of these MA( _q_ ) models is MA(1) (i.e., _q_ = 1):

_yt_ = _µ_ + _ϵt_ + _θϵt−_ 1 _._

The ACF of MA(1) is:

---

[← 1 Time Series Models, and Stationarity](01-1-time-series-models-and-stationarity.md) · [Up: contents](index.md) · [3 Sample ACF →](03-3-sample-acf.md)
