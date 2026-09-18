---
title: Today
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Today

* **Reading**: Chapter 1.3-1.7 – Shumway and Stoffer

* Autocovariance, autocorrelation, cross-covariance, cross-correlation
* Stationarity

### Covariance of linear combinations of random variables

If we have random variables $U=\displaystyle\sum_{j=1}^m a_j X_j$ and $V=\displaystyle\sum_{k=1}^r b_k Y_k$ that are linear combinations of (finite variance) random variables ${X_j}$ and ${Y_k}$, then the covariance of these is:

$\operatorname{cov}(U,V) = \displaystyle\sum_{j=1}^m \displaystyle\sum_{k=1}^r a_j b_k \operatorname{cov}(X_j, Y_k)$

### Autocovariance of a random walk

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

## Autocorrelation function

We can calculate the autocorrelation function (ACF) as:

$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\gamma(s,s)\gamma(t,t)}}$

This measures the linear predictability of the time series at time $t$ ($x_t$) using $x_s$. The Cauchy-Schwarz inequality states that:

$\operatorname{cov}(x,y) \leq \sqrt{\operatorname{Var}(x)\operatorname{Var}(y)}$

We can also extend this to looking at the linear predictability of one time series to another, by extending into the concepts of *cross-covariance* and *cross-correlation*.

## Cross-covariance

Between two time series $x_t$ and $y_t$:

$\gamma_xy(s,t) = \operatorname{cov}(x_s,y_t) = \mathbb{E}[(x_s-\mu_{xs})(y_t-\mu_{yt})]$

This tells us how the values in $y$ relate to the values in $x$ over time.

Let's think about a simple example:

$y_t = x_{t-2}$

What is $\gamma_{xy}(k)$ (for lag $k$)? At what lag is $\gamma_{xy}$ maximized?

We can also have the normalized version:

## Cross-correlation

$\rho_{xy}(s,t) = \frac{\gamma_xy(s,t)}{\sqrt{\gamma_x(s,s)\gamma_y(t,t)}}$

This is bounded such that $-1 \leq \rho(s,t) \leq 1$

---

[Up: contents](index.md) · [Stationarity →](02-stationarity.md)
