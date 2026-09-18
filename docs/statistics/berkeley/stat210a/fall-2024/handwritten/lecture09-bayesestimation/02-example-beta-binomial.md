---
title: 'Example: Beta-Binomial'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example: Beta-Binomial

$$
\begin{aligned}
X \mid \theta &\sim \operatorname{Binom}(n, \theta) = \theta^x (1-\theta)^{n-x} \binom{n}{x} \\
\theta &\sim \operatorname{Beta}(\alpha, \beta) = \theta^{\alpha-1} (1-\theta)^{\beta-1} \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
\end{aligned}
$$

$\theta$ is r.v. here; $\frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ normalizing const.

Marginal dist. of $X$ called **Beta-Binomial**

**Posterior**:

$$
\begin{aligned}
\lambda(\theta \mid x) &= \lambda(\theta) p_\theta(x) / q(x) \\
&\propto_\theta \theta^{\alpha-1} (1-\theta)^{\beta-1} \theta^x (1-\theta)^{n-x} \quad (\text{we can drop factors that don't depend on } \theta) \\
&= \theta^{x+\alpha-1} (1-\theta)^{n-x+\beta-1}
\end{aligned}
$$

$\Rightarrow \theta \mid X=x \sim \operatorname{Beta}(x+\alpha, \, n-x+\beta)$

$$
\mathbb{E}[\theta \mid X] = \frac{X + \alpha}{n + \alpha + \beta}
$$

Convex combo of $\frac{X}{n}, \frac{\alpha}{\alpha+\beta}$:

$$
= \frac{X}{n} \cdot \frac{n}{n+\alpha+\beta} + \frac{\alpha}{\alpha+\beta} \cdot \frac{\alpha+\beta}{n+\alpha+\beta}
$$

where $\frac{X}{n}$ is UMVU, $\frac{\alpha}{\alpha+\beta}$ is Prior Expectation, and $\frac{\alpha+\beta}{n+\alpha+\beta} = \left(1 - \frac{n}{n+\alpha+\beta}\right)$

Interp.: $k = \alpha+\beta$ "pseudo-trials," $\alpha$ successes
(Recall $\frac{X+3}{n+6}$ from Lec. 2)

---

---

[← Frequentist Motivation](01-frequentist-motivation.md) · [Up: contents](index.md) · [Example: Normal mean →](03-example-normal-mean.md)
