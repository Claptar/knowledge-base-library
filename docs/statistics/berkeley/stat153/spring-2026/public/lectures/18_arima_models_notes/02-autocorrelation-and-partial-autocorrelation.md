---
title: Autocorrelation and Partial Autocorrelation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/18_arima_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/18_arima_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Autocorrelation and Partial Autocorrelation

**Source:** [`public/lectures/18_arima_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/18_arima_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We previously discussed that the autocovariance for an AR(1) model decays away from $h=0$. On the other hand, the autocovariance for an MA(q) model is zero when $|h| > q$.

Let's look at an example of the ACF for an AR(2) model with $\phi_1=1.5$ and $\phi_2=-0.75$

![Example of the ACF for an AR(2) model with $\phi_1=1.5$ and $\phi_2=-0.75$](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/18_ACF_AR2.png)

The ACF tells us about the total correlation between $x_t$ and $x_{t-h}$, but includes indirect information through intermediate lags. For example, in an AR(1) process, $x_t$ and $x_{t-2}$ are correlated, but only because both are correlated with $x_{t-1}$. The ACF at lag 2 is nonzero even though there is no direct dependence for lag 2! So what do we do?

We can use the *partial autocorrelation function (PACF)* here. This is written as $\phi_hh$, which represents the correlation between $x_t$ and $x_{t-h}$ after regressing out the effects of $x_{t-1}, x_{t-2}, \dots, x_{t-h+1}$. This is helpful because it tells you whether lag $h$ provides additional predictive information beyond lags $1$ through $h-1$.

For random variables $X, Y$ and $Z=\{Z_1,\dots, Z_k\}$, the partial correlation between $X$ and $Y$ given $Z$ is obtained by regressing $X$ on $Z$ to obtain $\hat{X}$, regressing $Y$ on $Z$ to obtain $\hat{Y}$, and then calculating:

$$\rho_{XY|Z} = \text{corr}(X-\hat{X}, Y-\hat{Y})$$

Section 3.3.2 in your book provides more information on deriving this function.

Let's look at how that helps for the AR(2) model:

![Example of the ACF and PACF for an AR(2) model with $\phi_1=1.5$ and $\phi_2=-0.75$](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/18_PACF_AR2.png)

The following table shows how this information can be used in practice when determining if a time series has AR, MA, or ARMA components:

Function |  AR(p)    | MA(q)                | ARMA(p,q)
---------|-----------|----------------------|----------
ACF      | tails off | cuts off after lag q | tails off
PACF     | cuts off after lag p | tails off | tails off

---

[← ARMA Models](01-arma-models.md) · [Up: contents](index.md) · [Examples on real data →](03-examples-on-real-data.md)
