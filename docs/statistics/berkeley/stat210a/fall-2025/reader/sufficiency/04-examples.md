---
title: Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Examples

Some initial examples:

**Example: Normal location family** Assume we observe an i.i.d. sample from a normal distribution with unit variance and unknown mean:

$$
X_1,\ldots,X_n \simiid N(\theta,1) = \frac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2/2} = \frac{1}{\sqrt{2\pi}} e^{-x^2/2 + \theta x - \theta^2/2}
$$

The joint density function for the full data set $X = (X_1,\ldots,X_n)$ over $\RR^n$ is

$$
\begin{aligned}
p_\theta(x) &= (2\pi)^{-n/2} \cdot \prod_{i=1}^n e^{-x_i^2/2 + \theta x_i - \theta^2/2}[7pt]
&= \underbrace{e^{\theta \left(\sum_i x_i\right) -n\theta^2/2}}_{g_\theta\left(\sum_i x_i\right)}\cdot \underbrace{\frac{\prod_{i=1}^n e^{-x_i^2/2}}{(2\pi)^{-n/2}}}_{h(x)},
\end{aligned}
$$

 which by the factorization theorem shows that $\sum_i X_i$ is sufficient.

**Example: Poisson family** Next assume we observe an i.i.d. sample from a Poisson distribution with unknown mean $\theta$:

$$
X_1,\ldots,X_n \simiid \text{Pois}(\theta) = \frac{\theta^x e^{-\theta}}{x!}, \quad \text{ for } x = 0,1,\ldots
$$

 The joint pmf for the full data set $X = (X_1,\ldots,X_n)$ over $\{0,1,\ldots\}^n$ is

$$
\begin{aligned}
p_\theta(x) &= \prod_{i=1}^n \frac{\theta^{x_i}e^{-\theta}}{x_i!}[7pt]
&= \underbrace{e^{\log \theta \left(\sum_i x_i\right) -n\theta}}_{g_\theta\left(\sum_i x_i\right)}\cdot \underbrace{\left(\prod_{i=1}^n x_i!\right)^{-1}}_{h(x)},
\end{aligned}
$$

 Showing once again that $T(X) = \sum_i X_i$ is sufficient. As we’ll find out in the next lecture, there is a good reason why these calculations turned out so similarly: both of these models have what is called an *exponential family* structure.

**Example: Uniform location family** As a third example, suppose we observe an i.i.d. sample from a uniform distribution on the interval $[\theta, \theta + 1]$:

$$
X_1,\ldots, X_n \simiid U[\theta, \theta+1] = 1\{\theta \leq x \leq \theta + 1\}.
$$

 The joint density function for the full data set is

$$
p_\theta(x) = \prod_{i=1}^n 1\{\theta \leq x \leq \theta + 1\} = 1\{\theta \leq \min_i x_i\} 1\{\max_i x_i \leq \theta + 1\},
$$

so $T(X) = (\min_i X_i, \max_i X_i)$ is sufficient.

---

[← Factorization theorem](03-factorization-theorem.md) · [Up: contents](index.md) · Sufficient statistics under i.i.d. sampling →
