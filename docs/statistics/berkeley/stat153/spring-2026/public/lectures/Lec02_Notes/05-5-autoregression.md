---
title: 5 Autoregression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec02_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Autoregression

**Source:** [`public/lectures/Lec02_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Another flavor of dataset we might see is data that comes from an autoregressive process. Autoregression = regression or prediction based on past values of the same time series (“auto”).

This might look something like:

_xt_ = 1 _._ 5 _xt−_ 1 _−_ 0 _._ 75 _xt−_ 2 + _wt_

You will see what this looks like in Lab 1. Because the data at _t_ relies on _t −_ 1 and _t −_ 2 (the prior two data points), this is an AR(2) process. Generating data in this way can result in oscillatory behavior.

---

[← 4 Moving average](04-4-moving-average.md) · [Up: contents](index.md) · [6 Random Walk →](06-6-random-walk.md)
