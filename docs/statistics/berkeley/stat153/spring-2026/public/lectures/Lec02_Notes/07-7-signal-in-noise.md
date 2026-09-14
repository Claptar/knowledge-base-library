---
title: 7 Signal in noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Signal in noise

**Source:** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More generally, we can see other examples of periodic signals contaminated by white noise. For example:

_xt_ = _A ∗_ cos(2 _πωt_ + _ϕ_ ) + _wt_

Where _A_ is the amplitude of the signal, _ω_ is the frequency of the oscillation, and _ϕ_ is a phase shift.

The ratio of the amplitude of the signal to the standard deviation of the noise determines the SNR - signal to noise ratio. The larger the SNR, the easier it is to recover our signal.

Later, we will use various forms of regression to try to recover these signals!

---

[← 6 Random Walk](06-6-random-walk.md) · [Up: contents](index.md) · [8 Next week →](08-8-next-week.md)
