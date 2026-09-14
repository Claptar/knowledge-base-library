---
title: Q10. Linear regression with dependent errors {-}
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Q10. Linear regression with dependent errors {-}

**Source:** [`public/homework/Stat248_Homework1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Consider the linear regression model $y_t = \beta_0 + \beta_1 x_t + \epsilon_t$ for $t=1, \dots, T$ where $x_t$ is a known, fixed regressor and $\epsilon_t$ represents noise.

Assume the noise $\epsilon_t$ is weakly stationary, with $\mathbb{E}(\epsilon_t)=0$, $\operatorname{cov}(\epsilon_t, \epsilon_{t+h}) = \gamma(h)$ and $\displaystyle\sum_{h=-\infty}^\infty \left|\gamma(h)\right| < \infty$

(a) Derive the ordinary least squares (OLS) estimator $\hat{\beta_1}$ and show that it is unbiased even when the noise is temporally correlated. (4 points)

(b) Explain why assuming independent noise (and ignoring temporal correlations in the noise) can yield incorrect standard errors. (4 points)

---

[← Q9. Auto- and cross-correlation for brain data {-}](11-q9-auto--and-cross-correlation-for-brain-data.md) · [Up: contents](index.md)
