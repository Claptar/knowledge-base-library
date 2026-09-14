---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework2.tex
source_file: sources/berkeley-stat210a/fall-2024/homework/homework2.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework2.tex`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/homework/homework2.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Understanding and respecting the statistical structure of a model sometimes helps us to come up with estimators that perform dramatically better than the estimator we would have naïvely thought of. Here is a case where applying the sufficiency principle helped us get a much better estimator than the sample mean.

**Problem 3** (Convexity of $A(\eta)$ and $\Xi_1$). Let $\mathcal{P}=\{p_\eta:\; \eta \in \Xi_1\}$ denote an $s$-parameter exponential family in canonical form $$p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x), \qquad A(\eta) = \log\int_{\mathcal{X}} e^{\eta'T(x)}h(x)\,d \mu(x),$$ where $\Xi_1=\{\eta:\; A(\eta) < \infty\}$ is the natural parameter space.

Recall Hölder’s inequality: if $q_1,q_2\geq 1$ with $q_1^{-1} + q_2^{-1} = 1$, and $f_1$ and $f_2$ are ($\mu$-measurable) functions from $\mathcal{X}$ to $\mathbb{R}$, then $$\|f_1f_2\|_{L^1(\mu)} \leq \|f_1\|_{L^{q_1}(\mu)}\|f_2\|_{L^{q_2}(\mu)}, \quad \text{ where } \|f\|_{L^{q}(\mu)} = \left(\int_{\mathcal{X}} |f(x)|^q\,d \mu(x)\right)^{1/q}.$$ **Note:** $q_1=q_2=2$ reduces to Cauchy-Schwarz.

1.  Show that $A(\eta):\;\mathbb{R}^s \to [0,\infty]$ is a convex function: that is, for *any* $\eta_1,\eta_2\in \mathbb{R}^s$ (not just in $\Xi_1$), and $c\in [0,1]$ then $$\begin{equation}
    \label{eq:ineq}
      A(c\eta_1 + (1-c)\eta_2) \leq c A(\eta_1) + (1-c) A(\eta_2)
    \end{equation}$$ **Hint**: try $q_1=c^{-1}$, $f_1(x)^{1/c}=e^{\eta_1'T(x)}h(x)$.

2.  Use the previous part to show that $\Xi_1\subseteq \mathbb{R}^s$ is convex.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
