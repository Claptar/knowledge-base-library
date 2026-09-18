---
title: 3 Discrete sampling and restricting $f$ to $[0, 1/2]$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Discrete sampling and restricting $f$ to $[0, 1/2]$

Often in time series analysis, we work with equally spaced time points and assume that the time variable $t$ takes the values $1, \dots, n$ (where $n$ is the sample size). It turns out that if we consider the sinusoid (2) and restrict the time $t$ to $1, \dots, n$, then we can always constrain the frequency parameter $f$ to $[0, 1/2]$. This is a consequence of the following result.

**Fact 3.1.** *For every $f \in (-\infty, \infty)$ and $\phi \in (-\infty, \infty)$, there exists $f_0 \in [0, 1/2]$ and $\phi_0 \in (-\infty, \infty)$ such that*
$$s(t) = \beta_0 + R \cos(2\pi f t + \phi) = \beta_0 + R \cos(2\pi f_0 t + \phi_0) \quad \text{for all } t = 1, \dots, n.$$

*Proof.* Consider the following three cases.
1. If $f < 0$, then we can write $\cos(2\pi f t + \phi) = \cos(2\pi(-f)t - \phi)$. Clearly, $-f \ge 0$.
2. If $f \ge 1$, then we write (below $[f]$ is the largest integer less than or equal to $f$):
$$\cos(2\pi f t + \phi) = \cos(2\pi [f]t + 2\pi(f - [f])t + \phi) = \cos(2\pi(f - [f])t + \phi),$$
because $\cos(\cdot)$ is periodic with period $2\pi$. Clearly $0 \le f - [f] < 1$.
3. If $f \in [1/2, 1)$, then
$$\cos(2\pi f t + \phi) = \cos(2\pi t - 2\pi(1 - f)t + \phi) = \cos(2\pi(1 - f)t - \phi)$$
because $\cos(2\pi t - x) = \cos x$ for all integers $t$. Clearly $0 < 1 - f \le 1/2$.

Thus the sinusoid $R \cos(2\pi f t + \phi)$ equals $R \cos(2\pi f_0 t + \phi_0)$ at all integers $t$ for some $0 \le f_0 \le 1/2$ and a phase $\phi_0$ that is possibly different from $\phi$. $\square$

From now on, when we discuss sinusoids $s(t) = \beta_0 + R \cos(2\pi f t + \phi)$ in the context of $t = 1, \dots, n$, we shall assume that the frequency parameter $f$ is restricted to $[0, 1/2]$. Note also the behavior of the sinusoid for the two frequency extremes $f = 0$ and $f = 1/2$. When $f = 0$, the sinusoid $s(t)$ is simply a constant function equal to $\beta_0 + R \cos(\phi)$. When $f = 1/2$, we have
$$s(t) = \beta_0 + R \cos(\pi t + \phi) = \beta_0 + R(\cos \phi) \cos(\pi t) = \beta_0 + R(-1)^t \cos \phi.$$
This sinusoid exhibits the maximum possible oscillation going back and forth between $\beta_0 + R \cos \phi$ and $\beta_0 - R \cos \phi$.

## 4 Least Squares Estimation of $\beta, f, \sigma$

We use exactly the same method for parameter estimation as in the change of slope model. We take a bunch of possible values of $f$, calculate the goodness of fit $RSS(f)$ of the resulting linear regression model with fixed $f$, and then use $\hat{f}$ as the minimizer of $RSS(f)$ over $f$. The remaining parameters ($\beta$ and $\sigma$) are estimated as in usual linear regression with $f$ fixed at $\hat{f}$. This algorithm is described below:

1. Take a grid of all possible values of $f$ in the range $[0, 1/2]$.
2. For each frequency value $f$ in the grid,
   a) Form the matrix $X_f$
   b) Do a regression of $y$ on $X_f$ and compute the Residual Sum of Squares $RSS(f)$
3. Take $\hat{f}$ to be the grid value which minimizes $RSS(f)$ over all the grid values.
4. Take $\hat{\beta}$ and $\hat{\sigma}$ to be the usual regression estimates (of $\beta$ and $\sigma$) in the linear regression of $y$ on $X_{\hat{f}}$.

---

[← 2 The Sinusoid](02-2-the-sinusoid.md) · [Up: contents](index.md) · [5 Bayesian Posterior →](04-5-bayesian-posterior.md)
