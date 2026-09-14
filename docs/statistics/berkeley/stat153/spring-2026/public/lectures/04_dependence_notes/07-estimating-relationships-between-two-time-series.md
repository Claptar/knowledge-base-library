---
title: Estimating relationships between two time series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Estimating relationships between two time series

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We can use cross-correlation to estimate relationships between two series $x_t$ and $y_t$. For signals that are jointly weakly stationary:

$\hat{\rho}_{xy}(h) = \frac{\hat{\gamma_{xy}}(h)}{\sqrt{\hat{\gamma_x}(0)\hat{\gamma_y}(0)}}$

Here is an example of the autocorrelation functions for the Southern Oscillation Index, fish recruitment, and their relationship (cross-correlation function):

![SOI and fish recruitment](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec4_SOI.png)


![Sample ACFs and CCFs of Southern Oscillation Index and fish recruitment](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec4_acf_soi.png)

---

[← Estimating covariance of a single time series](06-estimating-covariance-of-a-single-time-series.md) · [Up: contents](index.md) · [Next time →](08-next-time.md)
