---
title: 1 Moving Average (MA) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Moving Average (MA) Models

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a positive integer _q ≥_ 1, the Moving Average model with order _q_ (denoted by MA( _q_ )) is defined by the equation:


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The MA( _q_ ) model has _q_ +2 unknown parameters which are estimated from observed data: _µ, θ_ 1 _, . . . , θq, σ_ .

The MA( _q_ ) model has been called the “Summation of Random Causes” by its inventor Slutzky in the original paper titled “The summation of random causes as the source of cyclic processes” published in Econometrica in 1937. Basically the _ϵt_ ’s can be treated as

1

random causes which are assumed to be independently and identically distributed. The actual observations _yt_ ’s are consequences of these causes. The consequence for tine _t_ depends on the cause for time _t_ as well as the causes for times _t −_ 1 _, . . . , t − q_ . These different causes affect the consequence at time _t_ differently depending on the values of _θ_ 1 _, . . . , θq_ . Note that successive observations _yt_ share some common causes leading to dependence between the successive values of _yt_ .

The simplest of these MA( _q_ ) models is MA(1) (i.e., _q_ = 1):


It is easy to check that each MA( _q_ ) model is stationary. Here is the proof for MA(1) (the proof for stationarity of MA( _q_ ) for _q ≥_ 1 is left as exercise). The mean of _yt_ is clearly E _yt_ = _µ_ which does not change with _t_ . The variance of _yt_ is


which also does not change with _t_ . The covariance between _yt_ and _yt_ +1 is

cov( _yt, yt_ +1) = cov( _µ_ + _ϵt_ + _θ_ 1 _ϵt−_ 1 _, µ_ + _ϵt_ +1 + _θ_ 1 _ϵt_ ) = cov( _ϵt, θ_ 1 _ϵt_ ) = _θ_ 1 _σ_<sup>2</sup>

which does not depend on _t_ . The covariance between _yt_ and _yt_ +2 is


Similarly, it is easy to see that the covariance between _yt_ and _yt_ + _h_ equals zero for every _h ≥_ 2. The ACVF of MA(1) is therefore


The ACF of MA(1) is:

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Stationarity of AR(1) →](03-2-stationarity-of-ar-1.md)
