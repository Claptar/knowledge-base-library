---
title: 5 Stationarity
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec04_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Stationarity

**Source:** [`public/lectures/Lec04_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Recall that for a moving average, the autocovariance _γv_ ( _s, t_ ) depends only on the time separation between _s_ and _t_ (also called the _lag_ ). This is important because this implies the concept of _stationarity_ .

A _strictly stationary_ time series is one where every collection of values has identical probabilistic behavior to the time-shifted set:

_{xt, xt_ 2 _, . . . , xtk }_ = _d {xt_ 1+ _h, xt_ 2+ _h, . . . , xtk_ + _h}_

(that is, same mean, variance, higher-order moments for all _t_ ). Examples: iid process

This is not true for most applications and is too strict of a definition. So instead, we will introduce the concept of weak stationarity. In your book this is just called “stationary” as short hand.

2

## **5.1 Weakly stationary**

A weakly stationary time series _xt_ is a finite variance process where:

- The mean function is constant and doesn’t depend on _t_

- The autocovariance function _γ_ ( _s, t_ ) depends on _s_ and _t_ only through their difference _|s − t|_ .

This is convenient because we can then estimate things about time series where we don’t have multiple repeated observations (and thus we can’t actually estimate the variability for a given time sample directly). In a stationary time series, the mean function is independent of time, so we have:

_µt_ = _µ_

We can also simplify the autocovariance function so that it is only dependent on the time shift / lag. For example, if _s_ = _t_ + _h_ , _h_ is the _lag_ between _s_ and _t_ . We then have:

_γ_ ( _t_ + _h, t_ ) = cov( _xt_ + _h, xt_ ) = cov( _xh, x_ 0) = _γ_ ( _h,_ 0) = _γ_ ( _h_ )

The autocovariance of a (weakly) stationary time series is thus: _γ_ ( _h_ ) = cov( _xt_ + _h, xt_ ) = E[( _xt_ + _h − µ_ )( _xt − µ_ )]

- In your lab, you will look at the stationarity of white noise (strictly stationary), moving average (weakly stationary), random walks (not stationary), and linear trends (not stationary).

- If mean and/or autocovariance change with time, your time series is not stationary

---

[← 4 Cross-correlation](04-4-cross-correlation.md) · [Up: contents](index.md) · [6 Estimating covariance of a single time series →](06-6-estimating-covariance-of-a-single-time-series.md)
