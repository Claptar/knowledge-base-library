---
title: 'Example: Beta-Binomial'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example: Beta-Binomial

$$
X \mid \theta \sim \operatorname{Binom}(n, \theta) = \theta^x (1-\theta)^{n-x} \binom{n}{x}
$$

$$
\theta \sim \operatorname{Beta}(\alpha, \beta) = \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$
*($\theta$ is r.v. here; $\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ is normalizing const.)*

Marginal dist. of $X$ called **Beta-Binomial**

**Posterior**:

$$
\begin{aligned}
\lambda(\theta \mid x) &= \lambda(\theta) p_\theta(x) / q(x) \\
&\propto_\theta \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \, \theta^x (1-\theta)^{n-x} \quad \text{(we can drop factors that don't depend on } \theta\text{)} \\
&= \theta^{x + \alpha - 1} (1-\theta)^{n - x + \beta - 1}
\end{aligned}
$$

$$
\Rightarrow \theta \mid X = x \sim \operatorname{Beta}(x + \alpha, \, n - x + \beta)
$$

$$
\mathbb{E}[\theta \mid X] = \frac{x + \alpha}{n + \alpha + \beta}
$$

Convex combo of $\frac{x}{n}$, $\frac{\alpha}{\alpha + \beta}$:
$$
= \overbrace{\frac{x}{n}}^{\text{UMVU}} \cdot \frac{n}{n + \alpha + \beta} + \overbrace{\frac{\alpha}{\alpha + \beta}}^{\text{Prior Expectation}} \cdot \overbrace{\frac{\alpha + \beta}{n + \alpha + \beta}}^{\left(1 - \frac{n}{n + \alpha + \beta}\right)}
$$

Interp.: $k = \alpha + \beta$ "pseudo-trials," $\alpha$ successes
(Recall $\frac{X + 3}{n + 6}$ from Lec. 2)

---

---

[← Bayes Estimator](02-bayes-estimator.md) · [Up: contents](index.md) · [Example: Normal mean →](04-example-normal-mean.md)
