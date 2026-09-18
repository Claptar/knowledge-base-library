---
title: Q8. Sinusoidal regression and covariance of estimators
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q8. Sinusoidal regression and covariance of estimators

Consider the sinusoidal model:

$$y_t = \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t$$

for $t = 1, \ldots, n$, where $f$ is a known frequency and $\epsilon_t \sim N(0, \sigma^2)$ i.i.d.

Q8a. Show that as $n \to \infty$, the cosine and sine regressors become orthogonal:

$$\frac{1}{n}\sum_{t=1}^n \cos(2\pi f t)\sin(2\pi f t) \to 0$$

*Hint: use the product-to-sum identity $\cos(\theta)\sin(\theta) = \frac{1}{2}\sin(2\theta)$.*

What does this imply about $\text{Cov}(\hat{\beta_1}, \hat{\beta_2})$, the covariance between the OLS estimates of $\beta_1$ and $\beta_2$? Why is this a desirable property for regression? (2 points)

Q8b. The amplitude of the sinusoidal component is $R = \sqrt{\beta_1^2 + \beta_2^2}$. A natural estimator of $R^2$ is $\hat{R}^2 = \hat{\beta_1}^2 + \hat{\beta_2}^2$, where $\hat{\beta_1}$ and $\hat{\beta_2}$ are the OLS estimates. Derive an expression for $E[\hat{R}^2]$ in terms of $R^2$, $\text{Var}(\hat{a})$, and $\text{Var}(\hat{b})$. (2 poin

Q8c. Is $\hat{R}^2$ a biased estimator of $R^2$? If so, in what direction?

Under what conditions is the bias most severe? What happens when there is no true signal ($R^2 = 0$)?

*Hint: recall that for any estimator $\hat{\theta}$, we have $E[\hat{\theta}^2] = \text{Var}(\hat{\theta}) + (E[\hat{\theta}])^2$.*

---

[← Q6. Ridge regression vs. LASSO](04-q6-ridge-regression-vs-lasso.md) · [Up: contents](index.md)
