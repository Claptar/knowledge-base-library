---
title: 4 Moving average
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Moving average

**Source:** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One way of smoothing a time series (including white noise) is to average the value at a time point _t_ with its neighbors _t −_ 1 and _t_ + 1 (or an even larger window from _t − p_ to _t_ + _p_ ). For example:

_vt_ = 3<sup><u>1</u>(</sup><sup>_wt−_1 +</sup><sup>_wt_+</sup><sup>_wt_+1)</sup> or more generally


This is inherently a low-pass filter (lets low frequency signals pass, gets rid of high frequency). It preserves trends slower than _∼ n_ samples, and suppresses oscillations with period ≲ _n_ samples.

### **When do we use this?**

We might use this to reveal trends in noisy time series data, remove fluctuations we consider “noise”, or do simple online smoothing (especially if we choose the window to include only data in the past). However, this is the most basic form of smoothing and is typically replaced by more complex methods such as exponential moving averages, Kalman filters, median filter, etc.

---

[← 3 White noise](03-3-white-noise.md) · [Up: contents](index.md) · [5 Autoregression →](05-5-autoregression.md)
