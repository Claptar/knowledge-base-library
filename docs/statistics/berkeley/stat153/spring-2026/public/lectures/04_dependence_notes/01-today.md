---
title: Today
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Today

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

* Autocovariance, autocorrelation, cross-covariance, cross-correlation
* Stationarity

## Covariance of linear combinations of random variables

If we have random variables $U=\displaystyle\sum_{j=1}^m a_j X_j$ and $V=\displaystyle\sum_{k=1}^r b_k Y_k$ that are linear combinations of (finite variance) random variables ${X_j}$ and ${Y_k}$, then the covariance of these is:

$\operatorname{cov}(U,V) = \displaystyle\sum_{j=1}^m \displaystyle\sum_{k=1}^r a_j b_k \operatorname{cov}(X_j, Y_k)$

## Autocovariance of a random walk

Recall that a random walk (with or without drift) is:

$x_t = \delta t + \displaystyle\sum_{i=1}^t w_i$

The $w_t$ are uncorrelated random variables.

$$
\begin{aligned}
\gamma(s,t) &= \operatorname{cov}(x_s, x_t) \\
&= \operatorname{cov}(\delta s + \displaystyle\sum_{i=1}^s w_i, \delta t + \displaystyle\sum_{i=1}^t w_i)\\
&= \sigma^2 \min(s,t)
\end{aligned}
$$

In this case, the autocovariance *does* depend on the particular $s$ and $t$ chosen.

What if we want a bounded measure?

---

[Up: contents](index.md) · [Autocorrelation function →](02-autocorrelation-function.md)
