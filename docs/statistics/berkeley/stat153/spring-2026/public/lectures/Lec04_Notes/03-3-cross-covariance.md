---
title: 3 Cross-covariance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec04_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Cross-covariance

**Source:** [`public/lectures/Lec04_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec04_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Between two time series _xt_ and _yt_ :

_γxy_ ( _s, t_ ) = cov( _xs, yt_ ) = E[( _xs − µxs_ )( _yt − µyt_ )]

This tells us how the values in _y_ relate to the values in _x_ over time. Let’s think about a simple example:

_yt_ = _xt−_ 2

What is _γxy_ ( _k_ ) (for lag _k_ )? At what lag is _γxy_ maximized? We can also have the normalized version:

---

[← 2 Autocorrelation function](02-2-autocorrelation-function.md) · [Up: contents](index.md) · [4 Cross-correlation →](04-4-cross-correlation.md)
