---
title: Homework12 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework12.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework12.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework12 Part 01 —

**Source:** [`homework/homework12.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework12.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Score test with nuisance parameters). Consider a testing problem with $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}p_{\theta,\zeta}(x)$ with parameter of interest $\theta \in \mathbb{R}$ and nuisance parameter $\zeta\in \mathbb{R}$. That is, we are testing $H_0:\theta = \theta_0$ vs. $H_1:\; \theta \neq \theta_0$, and $\zeta$ is unknown; let $\zeta_0$ denote its true value. Then there is a version of the score test where we plug in an estimator for $\zeta$, but we must use a corrected version of the variance.

Let $\hat\zeta_0$ denote the maximum likelihood estimator of $\zeta$ under the null: $$\hat\zeta_0(\theta_0) = \arg\max_{\zeta\in\mathbb{R}} \;\;\ell(\theta_0,\zeta; X).$$ Assume $\hat\zeta_0$ is consistent under the null hypothesis.

Let $J(\theta,\zeta)$ denote the full-sample Fisher Information (omitting the usual $n$ subscript), and assume it is continuous and positive-definite everywhere.

1.  Use Taylor expansions informally to show that, for large $n$, $$%\frac{\partial}{\partial\theta} \ell(\theta,\zeta)\big|_{\theta_0,\hat\zeta_0}
    \frac{\partial}{\partial\theta} \ell(\theta_0,\hat\zeta_0)
    \approx \frac{\partial}{\partial\theta}\ell(\theta_0,\zeta_0)
    - \frac{\frac{\partial^2}{\partial\theta\partial\zeta} \ell(\theta_0,\zeta_0)}
    {\frac{\partial^2}{\partial\zeta^2} \ell(\theta_0,\zeta_0)} \;\frac{\partial}{\partial\zeta} \ell(\theta_0,\zeta_0).$$ (Note: the LHS should be read as $[\frac{\partial}{\partial\theta} \ell(\theta,\zeta)]\big|_{\theta_0,\hat\zeta_0}$, and **not** $\frac{d}{d\theta_0} [\ell(\theta_0,\hat\zeta_0(\theta_0))]$).

2.  Using part (a), conclude that $$\left(J_{11} - \frac{J_{12}^2}{J_{22}}\right)^{-1/2}
    \frac{\partial}{\partial\theta} \ell(\theta_0,\hat\zeta_0) \Rightarrow N(0,1) \quad \text{ as } n \to\infty$$ where $J = J(\theta_0,\hat\zeta_0)$. Compare this to the score test statistic we would use if $\zeta_0$ were known rather than estimated. (Note: you may assume without proof that the approximation error in part (a) is negligible; i.e. you may take the “$\approx$” as an exact equality).

---

[Up: contents](index.md) · [Moral →](02-moral.md)
