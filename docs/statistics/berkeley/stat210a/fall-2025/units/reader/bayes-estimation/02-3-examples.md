---
title: 3 Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Examples

## 3.1 Beta-Binomial {.anchored number="3.1" anchor-id="beta-binomial"}

- $X|\theta \sim \text{Binomial}(n, \theta)$, $\theta \in [0,1]$
- $\theta \sim \text{Beta}(\alpha, \beta)$, $\alpha, \beta > 0$

The marginal distribution of $X$ is called Beta-Binomial.

Posterior:

$$
\pi(\theta|x) \propto \theta^x (1-\theta)^{n-x} \cdot \theta^{\alpha-1}(1-\theta)^{\beta-1} \propto \theta^{x+\alpha-1}(1-\theta)^{n-x+\beta-1}
$$

Therefore, $\theta|X \sim \text{Beta}(x+\alpha, n-x+\beta)$

$$
\EE[\theta|X] = \frac{x+\alpha}{n+\alpha+\beta}
$$

Interpret $\alpha+\beta$ as pseudo-trials and $\alpha$ as pseudo-successes.

## 3.2 Normal Mean {.anchored number="3.2" anchor-id="normal-mean"}

- $X_i|\theta \sim N(\theta, \sigma^2)$, $\sigma^2$ known
- $\theta \sim N(\mu, \tau^2)$

Posterior:

$$
\pi(\theta|x) \propto \exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\theta)^2\right) \exp\left(-\frac{1}{2\tau^2}(\theta-\mu)^2\right)
$$

Complete the square:

$$
\theta|X \sim N\left(\frac{\frac{n}{\sigma^2}\bar{x} + \frac{1}{\tau^2}\mu}{\frac{n}{\sigma^2} + \frac{1}{\tau^2}}, \frac{1}{\frac{n}{\sigma^2} + \frac{1}{\tau^2}}\right)
$$

$$
\EE[\theta|X] = \frac{\frac{n}{\sigma^2}\bar{x} + \frac{1}{\tau^2}\mu}{\frac{n}{\sigma^2} + \frac{1}{\tau^2}} = w\bar{x} + (1-w)\mu
$$

where $w = \frac{n\tau^2}{n\tau^2 + \sigma^2}$

If $\frac{1}{\tau^2} = k$, interpret as $k$ pseudo-observations with mean $\mu$.

---

[← 1 Bayes Risk and Bayes Estimator](01-1-bayes-risk-and-bayes-estimator.md) · [Up: contents](index.md) · [4 Conjugate Priors →](03-4-conjugate-priors.md)
