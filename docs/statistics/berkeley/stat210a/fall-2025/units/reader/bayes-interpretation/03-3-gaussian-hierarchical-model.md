---
title: 3 Gaussian Hierarchical Model
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/bayes-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Gaussian Hierarchical Model

$\theta_i \sim N(\mu, \tau^2)$, $X_i|\theta_i \sim N(\theta_i, \sigma^2)$

Posterior mean:

$$
\mathbb{E}[\theta_i|X] = \mathbb{E}[\mathbb{E}[\theta_i|X, \mu, \tau^2]|X] = \mathbb{E}[\frac{\tau^2}{\tau^2 + \sigma^2}X_i + \frac{\sigma^2}{\tau^2 + \sigma^2}\mu|X]
$$

Linear shrinkage estimator: - Bayes optimal shrinkage estimated from data - Likelihood for $\mu, \tau^2$ (marginalize over $\theta_i$): - $X_i|\mu, \tau^2 \sim N(\mu, \tau^2 + \sigma^2)$ - $\bar{X} \sim N(\mu, \frac{\tau^2 + \sigma^2}{n})$ - $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 \sim \frac{\tau^2 + \sigma^2}{n-1}\chi^2_{n-1}$

Define $B = \tau^2 + \sigma^2$:

$$
\delta(x) = \mathbb{E}[\mathbb{E}[\theta_i|X, B]|X] = \mathbb{E}[\frac{B - \sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar{X}|X]
$$

Conjugate prior:

$$
\pi(B|\lambda, \nu) \propto B^{-\nu/2-2}\exp(-\frac{\lambda}{2B})
$$

$$
B|X \sim \text{InvGamma}(\frac{n+\nu}{2}, \frac{\lambda + (n-1)S^2}{2})
$$

$$
\mathbb{E}[\frac{1}{B}|X] = \frac{n+\nu}{\lambda + (n-1)S^2}
$$

$$
\delta_i(x) = \frac{(n-3)S^2}{(n-1)S^2 + \lambda}X_i + \frac{\lambda + 2S^2}{(n-1)S^2 + \lambda}\bar{X}
$$

Might want to truncate prior to $[\sigma^2, \infty)$ if $\lambda$ small.

---

[← 2 Where Does the Prior Come From?](02-2-where-does-the-prior-come-from.md) · [Up: contents](index.md)
