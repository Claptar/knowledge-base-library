---
title: 1 MA( q ) models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 MA( q ) models

**Source:** [`LectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a positive integer _q ≥_ 1, the Moving Average model with order _q_ (denoted by MA( _q_ )) is defined by the equation:


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The MA( _q_ ) model has _q_ +2 unknown parameters which are estimated from observed data: _µ, θ_ 1 _, . . . , θq, σ_ .

The MA( _q_ ) model has been called the “Summation of Random Causes” by its inventor Slutzky in the original paper titled “The summation of random causes as the source of cyclic processes” published in Econometrica in 1937. Basically the _ϵt_ ’s can be treated as random causes which are assumed to be independently and identically distributed. The actual observations _yt_ ’s are consequences of these causes. The consequence for time _t_ depends on the cause for time _t_ as well as the causes for times _t −_ 1 _, . . . , t − q_ . These different causes affect the consequence at time _t_ differently depending on the values of _θ_ 1 _, . . . , θq_ . Note that successive observations _yt_ share some common causes leading to dependence between the successive values of _yt_ .

The MA( _q_ ) model is always causal stationary (no matter what specific values its parameters _µ, θ_ 1 _, . . . , θq, σ_ take; in this respect, the MA( _q_ ) is different from AR( _p_ ) which can be causal-stationary or not depending on specific values of the parameters).

Here is how the causal stationarity of MA( _q_ ) is proved. The causality follows straight from the definition because _yt_ is written in terms of the present and past _ϵ_ -values _ϵt, ϵt−_ 1 _, . . ._ . For stationarity, we need to compute E _yt_ and cov( _yt, yt_ + _h_ ):

1. The mean of _yt_ is clearly equal to _µ_ (so it is constant in _t_ ).

1

2. The covariance between _yt_ and _yt_ + _h_ is given by:

cov( _yt, yt_ + _h_ )


Note that, in the sum<sup>�</sup><sup>_q_</sup> _j_ =0<sup>_θjϵt−j_,wetake</sup><sup>_θ_0=1.Because</sup><sup>_{ϵt}_isGaussianwhite</sup> noise, the covariance cov ( _ϵt−j, ϵt_ + _h−k_ ) equals zero unless _t−j_ = _t_ + _h−k_ i.e., _k_ = _j_ + _h_ . So we need the three conditions 0 _≤ j ≤ q_ , 0 _≤ k ≤ q_ as well as _k_ = _j_ + _h_ . If _h > q_ , it is clear that this is not possible for any _j, k_ . So we have cov( _yt, yt_ + _h_ ) equals zero when _h > q_ . When 0 _≤ h ≤ q_ , we have 0 _≤ j ≤ q_ and 0 _≤ j_ + _h ≤ q_ which implies 0 _≤ j ≤ q − h_ . We then get


We thus have:


The above covariance does not depend on _t_ which shows that the MA( _q_ ) model is stationary.

Based on the above calculation, the ACVF of MA( _q_ ) is:


The ACF _ρ_ ( _h_ ) = _γ_ ( _h_ ) _/γ_ (0) equals:


The simplest of these MA( _q_ ) models is MA(1) (i.e., _q_ = 1):


The ACF of MA(1) is:


In order to assess whether the MA( _q_ ) model is suitable for a particular dataset, a simple way is to compute the sample correlation between _yt_ and _yt_ + _h_ for each value of _h_ (in other words, the correlation between ( _at, bt_ ) _, t_ = 1 _, . . . , n − h_ where _at_ = _yt_ and _bt_ = _yt_ + _h_ ). The sample ACF is defined as a slight modification of this correlation.

2

---

[Up: contents](index.md) · [2 Sample ACF →](02-2-sample-acf.md)
