---
title: Autocorrelation function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Autocorrelation function

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We can calculate the autocorrelation function (ACF) as:

$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\gamma(s,s)\gamma(t,t)}}$

This measures the linear predictability of the time series at time $t$ ($x_t$) using $x_s$. The Cauchy-Schwarz inequality states that:

$\operatorname{cov}(x,y) \leq \sqrt{\operatorname{Var}(x)\operatorname{Var}(y)}$

We can also extend this to looking at the linear predictability of one time series to another, by extending into the concepts of *cross-covariance* and *cross-correlation*.

---

[← Today](01-today.md) · [Up: contents](index.md) · [Cross-covariance →](03-cross-covariance.md)
