---
title: Doubts about unbiasedness
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Doubts about unbiasedness

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The last example raises the question: why should we require zero bias? There can be good reasons for this: it's nice to be able to say your estimator is correct on average, especially if the estimand is strongly contested by different parties. But we shouldn't take this constraint too seriously because in some cases the UMVUE can be inadmissible, or even ridiculous in cases where other approaches work well.

**Example:** Suppose we observe a multivariate Gaussian vector with an unknown location parameter, $X \sim N_d(\mu, I_d)$ for  $\mu \in \RR^d$, where $I_d$ is the identity matrix, and we want to estimate $g(\mu) = \|\mu\|^2$.

Since $X$, the complete sufficient statistic for this family, is a natural estimator for $\mu$, we can start with $\|X\|^2$ and try to make it unbiased. If we write $X = \mu + Z$ where $Z \sim N_d(0,I_d)$, then we have
$$
\begin{aligned}
\EE_\mu \|X\|^2 &= \sum_j \EE (Z_j + \mu_j)^2\\
&= \sum_j \mu_j^2 + 2\mu_j\EE Z_j + \EE Z_j^2\\
&= \|\mu\|^2 + d,
\end{aligned}
$$
since each cross-term is zero and $\EE Z_j^2 = \Var(Z_j) = 1$. As a result, we can get an unbiased estimator by subtracting off the bias, namely $\delta(X) = \|X\|^2-d$. But this estimator has the very odd property that it can be negative: if $d=10$ and $\|X\|^2=5$, which can happen, we are giving the estimate $-5$ for the non-negative estimand $\|\mu\|^2$. This may not seem like a big deal when we are just doing frequentist calculations, but imagine the authors' embarrassment if such an estimate actually found its way into a journal paper!

From a dry decision theory perspective, we can also recognize this estimator as inadmissible for any reasonable loss function: whenever the estimate is zero, we will always be getting closer to the estimand if we replace it with zero; that is, $\delta_+(X) = (\|X\|^2-d)_+$ will strictly dominate $\delta(X)$, for any reasonable loss function.

There are even sillier examples of UMVU estimators, as we see next.

**Example:** Suppose we observe $X \sim \text{Bin}(1000, \theta)$, and want to estimate $g(\theta) = \PP_\theta(X \geq 500)$. What is the UMVU estimator?

!!! important "Important"

---

[← Finding the UMVUE](05-finding-the-umvue.md) · [Up: contents](index.md) · [Expand for answer →](07-expand-for-answer.md)
