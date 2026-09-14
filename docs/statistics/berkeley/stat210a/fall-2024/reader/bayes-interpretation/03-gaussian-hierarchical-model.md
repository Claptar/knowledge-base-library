---
title: Gaussian Hierarchical Model
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Gaussian Hierarchical Model

**Source:** [`reader/bayes-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

$\theta_i \sim N(\mu, \tau^2)$, $X_i|\theta_i \sim N(\theta_i, \sigma^2)$

Posterior mean:
$$
\mathbb{E}[\theta_i|X] = \mathbb{E}[\mathbb{E}[\theta_i|X, \mu, \tau^2]|X] = \mathbb{E}[\frac{\tau^2}{\tau^2 + \sigma^2}X_i + \frac{\sigma^2}{\tau^2 + \sigma^2}\mu|X]
$$

Linear shrinkage estimator:
- Bayes optimal shrinkage estimated from data
- Likelihood for $\mu, \tau^2$ (marginalize over $\theta_i$):
  - $X_i|\mu, \tau^2 \sim N(\mu, \tau^2 + \sigma^2)$
  - $\bar{X} \sim N(\mu, \frac{\tau^2 + \sigma^2}{n})$
  - $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 \sim \frac{\tau^2 + \sigma^2}{n-1}\chi^2_{n-1}$

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

[← Where Does the Prior Come From?](02-where-does-the-prior-come-from.md) · [Up: contents](index.md)
