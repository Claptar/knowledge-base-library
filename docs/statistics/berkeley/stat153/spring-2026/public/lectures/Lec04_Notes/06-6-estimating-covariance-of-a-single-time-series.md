---
title: 6 Estimating covariance of a single time series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec04_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Estimating covariance of a single time series

**Source:** [`public/lectures/Lec04_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Much of the time we don’t have multiple samples of our time series, so we can’t estimate _µt_ separately for each _t_ . If we assume stationarity, _µt_ = _µ_ , so we can use the sample mean instead of _µt_ :

_n−h γ_ ˆ( _h_ ) = _n_<sup><u>1</u></sup> ∑( _xt_ + _h − x_ ¯)( _xt − x_ ¯), _t_ =1 where _x_ ¯ = _n_ <u>1</u> ∑ _nt_ =1<sup>_xt_isthesamplemean.</sup> Also, _γ_ ˆ( _−h_ ) = _γ_ ˆ( _h_ ) for _h_ = 0 _,_ 1 _, . . . , n −_ 1.

This is nice because we can always calculate the sample autocovariance. However, whether it is interpretable or meaningful will depend on whether the stationarity assumption is approximately true.

---

[← 5 Stationarity](05-5-stationarity.md) · [Up: contents](index.md) · [7 Estimating relationships between two time series →](07-7-estimating-relationships-between-two-time-series.md)
