---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework11.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework11.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework11.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework11.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

This is an example of an estimator that’s adaptive to an unknown problem parameter, in this case the ratio $\rho = \sigma^2/\tau^2$ which tells us how to choose the optimal value of some tuning parameter $\gamma^*(\rho,m,n)$. A tried and true method in statistics is to get a consistent estimator for the unknown parameter and just plug it in. Asymptotically, this very often works just as well as knowing the value of the nuisance parameter (it’s not necessarily that we don’t pay a price for not knowing $\rho$, it’s just that the price we pay might be lower order than the source of error that matters).

**Problem 2** (Some Maximum Likelihood Estimators).

Find the MLE for each model below, and find its asymptotic distribution. You do not need to check the conditions for convergence theorems; just calculate assuming they are in force.

1.  Laplace: $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}\frac{1}{2}e^{-|x-\theta|}$.

    **Note:** although the log-likelihood is non-differentiable at one point, we can still use the Fisher information as defined by $J_1(\theta) = \textnormal{Var}_\theta[\dot{\ell}_1(\theta;X_i)]$ to get the asymptotic distribution; you may assume this without proof. You may assume $n$ is odd.

2.  Binomial: $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}\text{Binom}(m,\theta)$. Find the MLE for $\theta$ and for the canonical parameter $\eta = \log\frac{\theta}{1-\theta}$.

3.  Gaussian: $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}N(\theta,\sigma^2)$. Find (i) the MLE for $\theta$ if $\sigma^2$ is known, (ii) the MLE for $\sigma^2$ if $\theta$ is known, and (iii) the MLE for $(\theta,\sigma^2)$ if neither is known.

---

[← Homework11 Part 01 —](01-homework11-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
