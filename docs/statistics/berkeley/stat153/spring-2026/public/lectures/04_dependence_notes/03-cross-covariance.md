---
title: Cross-covariance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Cross-covariance

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Between two time series $x_t$ and $y_t$:

$\gamma_xy(s,t) = \operatorname{cov}(x_s,y_t) = \mathbb{E}[(x_s-\mu_{xs})(y_t-\mu_{yt})]$

This tells us how the values in $y$ relate to the values in $x$ over time.

Let's think about a simple example:

$y_t = x_{t-2}$

What is $\gamma_{xy}(k)$ (for lag $k$)? At what lag is $\gamma_{xy}$ maximized?

We can also have the normalized version:

---

[← Autocorrelation function](02-autocorrelation-function.md) · [Up: contents](index.md) · [Cross-correlation →](04-cross-correlation.md)
