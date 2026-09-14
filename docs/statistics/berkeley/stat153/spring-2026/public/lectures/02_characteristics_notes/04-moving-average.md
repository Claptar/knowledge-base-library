---
title: Moving average
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Moving average

**Source:** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

One way of smoothing a time series (including white noise) is to average the value at a time point $t$ with its neighbors $t-1$ and $t+1$ (or an even larger window from $t-p$ to $t+p$). For example:

$v_t = \frac{1}{3}(w_{t-1}+w_t+w_{t+1})$

or more generally

$v_t = \frac{1}{n} \displaystyle\sum_{k=-\frac{n-1}{2}}^{\frac{n-1}{2}} w_{t+k}$ for odd $n$

This is inherently a low-pass filter (lets low frequency signals pass, gets rid of high frequency). It preserves trends slower than $\sim n$ samples, and suppresses oscillations with period $\lesssim n$ samples.

**When do we use this?**

We might use this to reveal trends in noisy time series data, remove fluctuations we consider "noise", or do simple online smoothing (especially if we choose the window to include only data in the past). However, this is the most basic form of smoothing and is typically replaced by more complex methods such as exponential moving averages, Kalman filters, median filter, etc.

---

[← White noise](03-white-noise.md) · [Up: contents](index.md) · [Autoregression →](05-autoregression.md)
