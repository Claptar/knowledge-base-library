---
title: 2 Autocorrelation function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec04_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Autocorrelation function

**Source:** [`public/lectures/Lec04_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can calculate the autocorrelation function (ACF) as:

_ρ_ ( _s, t_ ) = _<u>γ</u>_ <u>(</u> _s,t_ <u>)</u> _~~√~~ γ_ ( _s,s_ ) _γ_ ( _t,t_ )

This measures the linear predictability of the time series at time _t_ ( _xt_ ) using _xs_ . The Cauchy-Schwarz inequality states that:

cov( _x, y_ ) _≤_ √Var( _x_ ) Var( _y_ )

We can also extend this to looking at the linear predictability of one time series to another, by extending into the concepts of _cross-covariance_ and _crosscorrelation_ .

---

[← 1 Today](01-1-today.md) · [Up: contents](index.md) · [3 Cross-covariance →](03-3-cross-covariance.md)
