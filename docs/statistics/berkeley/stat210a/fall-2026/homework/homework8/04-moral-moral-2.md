---
title: 'Moral: {#moral-2}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework8.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework8.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-2}

**Source:** [`homework/homework8.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework8.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Whereas Bayesian statistics is an excellent framework for incorporating a wealth of prior knowledge into our final inference, a great strength of hypothesis testing and confidence intervals is their power to let analysts remain agnostic when they want to remain agnostic. To get a Bayesian posterior distribution for the median, we would need to fully specify our prior distribution over the infinite-dimensional object $F$; but we can derive a simple frequentist confidence interval that has $90\%$ coverage for every possible $F$ without doing anything like this.

**Problem 4** (Testing with multidirectional alternatives).

Suppose $X\sim N_d(\mu,I_d)$ for unknown $\mu\in\mathbb{R}^d$. Consider testing $H_0:\; \mu=0$ vs. $H_1:\; \mu \neq 0$.

1.  Show that for any $d>1$ and $\alpha\in(0,1)$, there exists no UMP or UMPU level-$\alpha$ test.

    **Hint:** what would we do if we knew $\mu = (\theta,0,0,\ldots,0)$ for an unknown $\theta\in\mathbb{R}$?

2.  Suppose we have a prior $\Lambda_1$ for the value that $\mu$ takes under the alternative; that is, $\mu \sim \Lambda_1$ if $H_1$ is true and $\mu = 0$ if $H_0$ is true. Define the average power as $$\int_{\mathbb{R}^d} \mathbb{E}_\mu [\phi(X)] \,d\Lambda_1(\mu).$$

    If $\Lambda_1 = N(\nu, \Sigma)$, with positive definite covariance matrix $\Sigma$, find the level-$\alpha$ test that maximizes the average power. Show that the acceptance region is an ellipse centered at $0$ if $\nu = 0$.

3.  Suppose the prior $\Lambda_1$ (not necessarily multivariate Gaussian) is rotationally invariant, meaning $\Lambda_1(Q A) = \Lambda_1(A)$ where $A \subseteq \mathbb{R}^d$, $Q$ is any rotation matrix and $QA = \{Qa:\; a\in A\}$. Show that the $\chi^2$ test that rejects for large $\|X\|^2$ maximizes the average power.

---

[← Moral: {#moral-1}](03-moral-moral-1.md) · [Up: contents](index.md) · [Moral: {#moral-3} →](05-moral-moral-3.md)
