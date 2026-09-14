---
title: Asymptotic Efficiency
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/maximum-likelihood.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Asymptotic Efficiency

**Source:** [`reader/maximum-likelihood.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In the exponential family case, generalizes to a much broader class of models

Setting: $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x)$, $\theta \in \mathbb{R}^d$

$p_\theta$ smooth in $\theta$ (e.g., 2 cts integrable derives, can be relaxed)

Let $\ell_i(\theta; X) = \log p_\theta(X_i)$, $\ell_n(\theta; X) = \sum_{i=1}^n \ell_i(\theta; X)$

$S_n(\theta) = \nabla_\theta \ell_n(\theta; X)$, $J_n(\theta) = \text{Var}_\theta[\nabla_\theta \ell_n(\theta; X)] = nJ_1(\theta)$

We say an estimator is asymptotically efficient if $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, J_1^{-1}(\theta))$

Delta method for differentiable estimand $g(\theta)$:

$\sqrt{n}(g(\hat{\theta}_n) - g(\theta)) \xrightarrow{d} N(0, \nabla g(\theta)^T J_1^{-1}(\theta) \nabla g(\theta))$

Also achieves CRLB if $\hat{\theta}_n$ does, $g$ diff

---

[← Maximum Likelihood Estimation](01-maximum-likelihood-estimation.md) · [Up: contents](index.md) · [Asymptotic Distribution of MLE →](03-asymptotic-distribution-of-mle.md)
