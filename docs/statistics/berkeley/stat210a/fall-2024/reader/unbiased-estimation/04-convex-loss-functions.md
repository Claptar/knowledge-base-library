---
title: Convex Loss Functions
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Convex Loss Functions

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Recall $f(y)$ is *convex* if for all $x_1, x_2$ and all $\gamma \in [0,1]$:

$$f(\gamma x_1 + (1-\gamma)x_2) \leq \gamma f(x_1) + (1-\gamma) f(x_2)$$ $f$ is *strictly convex* if the inequality is strict unless $x_1 = x_2$.

An key fact about convex functions is **Jensen's Inequality:** If $f$ is convex, then for *any* random variable $X$, we have

$$f(\EE[X]) \leq \EE[f(X)]$$ If $f$ is strictly convex, then the inequality is strict unless $X$ is constant.

We say a loss function $L(\theta, d)$ is (strictly) convex if is (strictly) convex as a function of the estimate $d$, its second argument, holding the parameter $\theta$ fixed.

**Example:** The best-known example of a convex loss function is the squared error loss. Recall that the corresponding risk, the MSE, can be decomposed as the sum of the bias squared and the variance:

$$
\begin{aligned}
\text{MSE}_\theta(\delta) &= \EE_\theta[(\delta(X) - g(\theta))^2] \\[5pt]
&= \text{Bias}_\theta(\delta)^2 + \text{Var}_\theta(\delta(X))
\end{aligned}
$$ If $\delta(X)$ is unbiased, then its MSE is exactly its variance, so minimizing the risk among unbiased estimators just amounts to finding one with the least variance.

---

[← Unbiased Estimation](03-unbiased-estimation.md) · [Up: contents](index.md) · [The Rao-Blackwell Theorem →](05-the-rao-blackwell-theorem.md)
