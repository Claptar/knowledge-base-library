---
title: 'Example: Normal mean'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example: Normal mean

$$
X \mid \theta \sim N(\theta, \sigma^2) \propto_\theta e^{-(x-\theta)^2 / 2\sigma^2}
$$

$$
\sim N(\mu, \tau^2) \propto_\theta e^{-(\theta-\mu)^2 / 2\tau^2}
$$

$$
\begin{aligned}
\lambda(\theta \mid x) &\propto_\theta \exp\left\{ -\frac{(x-\theta)^2}{2\sigma^2} - \frac{(\theta-\mu)^2}{2\tau^2} \right\} \\
&\propto_\theta \exp\left\{ \frac{x\theta}{\sigma^2} - \frac{\theta^2}{2\sigma^2} - \frac{\theta^2}{2\tau^2} + \frac{\theta\mu}{\tau^2} \right\} \\
&= \exp\left\{ \theta \underbrace{\left(\frac{x}{\sigma^2} + \frac{\mu}{\tau^2}\right)}_{b} - \theta^2 \underbrace{\left(\frac{\sigma^{-2} + \tau^{-2}}{2}\right)}_{a^2} \right\}
\end{aligned}
$$

Complete square:
$$
\begin{aligned}
a^2 \theta^2 - b\theta &= \left(\theta a - \frac{b}{2a}\right)^2 - c(a, b) \\
&= \left(\theta - \frac{b}{2a^2}\right)^2 \cdot a^2 - c(a, b)/a
\end{aligned}
$$

$$
\begin{aligned}
&\rightarrow \propto_\theta \exp\left\{ -\left(\theta - \frac{x\sigma^{-2} + \mu\tau^{-2}}{\sigma^{-2} + \tau^{-2}}\right)^2 \middle/ 2(\sigma^{-2} + \tau^{-2})^{-1} \right\} \\
&\propto_\theta N\left(\frac{x\sigma^{-2} + \mu\tau^{-2}}{\sigma^{-2} + \tau^{-2}}, \, \frac{1}{\sigma^{-2} + \tau^{-2}}\right)
\end{aligned}
$$

precision-weighted average of $x$, $\mu$:
$$
\mathbb{E}[\theta \mid X] = X \cdot \frac{\sigma^{-2}}{\sigma^{-2} + \tau^{-2}} + \mu \cdot \frac{\tau^{-2}}{\sigma^{-2} + \tau^{-2}}
$$

---

## Gaussian iid sample

$$
\theta \sim N(\mu, \tau^2), \quad X_i \mid \theta \stackrel{iid}{\sim} N(\theta, \sigma^2), \quad i = 1, \dots, n
$$

Suff. reduction $\rightsquigarrow \bar{X} \mid \theta \sim N(\theta, \frac{\sigma^2}{n})$

$$
\begin{aligned}
\Rightarrow \mathbb{E}[\theta \mid X] &= \bar{X} \cdot \frac{n\sigma^{-2}}{n\sigma^{-2} + \tau^{-2}} + \mu \cdot \frac{\tau^{-2}}{n\sigma^{-2} + \tau^{-2}} \\
&= \bar{X} \cdot \frac{n}{n + \sigma^2/\tau^2} + \mu \cdot \frac{\sigma^2/\tau^2}{n + \sigma^2/\tau^2}
\end{aligned}
$$

Interp: $k = \sigma^2/\tau^2$ pseudo-observations, mean $\mu$

If $n \gg k$, "data swamps prior"
If $n \ll k$, "prior swamps data"

[Note in both examples:
* Prior & Likelihood have similar fcn. form
* Posterior comes from same exp. fam. as prior]

If the posterior is from the same family as the prior, we say the prior is **conjugate** to the likelihood.

Most common in exp. families

---

---

[← Example: Beta-Binomial](03-example-beta-binomial.md) · [Up: contents](index.md) · [Conjugate Priors →](05-conjugate-priors.md)
