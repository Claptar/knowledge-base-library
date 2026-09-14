---
title: Examples
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Examples

**Source:** [`reader/bayes-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Beta-Binomial

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

### Normal Mean

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

[← Special Cases and Examples](02-special-cases-and-examples.md) · [Up: contents](index.md) · [Conjugate Priors →](04-conjugate-priors.md)
