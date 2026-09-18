---
title: 1 $\text{ARMA}(p, q)$ Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 $\text{ARMA}(p, q)$ Model

## Lecture Twenty Three
Spring 2025, UC Berkeley

Aditya Guntuboyina

April 17, 2025

The $\text{ARMA}(p, q)$ model is given by the equation:
$$(y_t - \mu) - \phi_1(y_{t-1} - \mu) - \dots - \phi_p(y_{t-p} - \mu) = \epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q}$$
where, as usual, $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. In backshift notation, this equation becomes
$$\phi(B)(y_t - \mu) = \theta(B)\epsilon_t \tag{1}$$
where $\phi(B)$ and $\theta(B)$ are the AR and MA polynomials:
$$\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p \quad \text{and} \quad \theta(z) = 1 + \theta_1 z + \dots + \theta_q z^q$$
applied to the backshift operator $B$. Another way of writing (1) is:
$$\phi(B)y_t = \delta + \theta(B)\epsilon_t,$$
where we now write the intercept term $\delta$ explicitly on the right hand side.

We can write the solution to (1) as
$$y_t - \mu = \frac{\theta(B)}{\phi(B)}\epsilon_t.$$
To make sense of the right hand side above, we can factorize $\phi(z)$ as:
$$\phi(z) = (1 - a_1 z)(1 - a_2 z) \dots (1 - a_p z).$$
Here $1/a_1, \dots, 1/a_p$ are the roots of $\phi(z)$. This gives
$$y_t - \mu = \frac{\theta(B)}{\prod_{k=1}^p(1 - a_k B)}\epsilon_t = \theta(B)(1 - a_1 B)^{-1}\dots(1 - a_p B)^{-1}\epsilon_t$$
Each term $(1 - a_k B)^{-1}$ can be expanded via one of the following two formulae:
$$(1 - a_k B)^{-1} = \sum_{j=0}^\infty a_k^j B^j \quad \text{or} \quad (1 - a_k B)^{-1} = -\sum_{j=1}^\infty \frac{1}{a_k^j B^j}.$$

depending on whether $|a_k| < 1$ or $|a_k| > 1$. This allows us to write $y_t - \mu$ in terms of $\{\epsilon_t\}$. If $|a_k| < 1$ for every $k$, we can write
$$y_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$$
for some $\psi_0, \psi_1, \psi_2, \dots$. This is a causal stationary process. We shall only work with $\text{ARMA}(p, q)$ models in the causal stationary regime (which corresponds to $\phi(z)$ having all roots of modulus strictly larger than 1).

$\text{ARMA}(p, q)$ is a more sophisticated model compared to pure $\text{AR}(p)$ and $\text{MA}(q)$. For $\text{AR}(p)$, the theoretical PACF becomes zero for lags $h > p$. For $\text{MA}(q)$, the theoretical ACF becomes zero for lags $h > q$. For $\text{ARMA}(p, q)$ with both $p$ and $q$ at least one, one of these is true about the ACF and PACF. It is therefore to determine an appropriate choice for $p$ and $q$ for fitting an $\text{ARMA}(p, q)$ model looking at the ACF and PACF. In practice, one usually searches over a range of $p$ and $q$ values using a model selection criterion such as AIC, BIC or Cross-Validation.

---

[Up: contents](index.md) · [2 The Box-Jenkins Time Series Modeling Strategy →](02-2-the-box-jenkins-time-series-modeling-strategy.md)
