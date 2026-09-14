---
title: Homework10 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework10.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework10.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework10 Part 01 —

**Source:** [`homework/homework10.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework10.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (James-Stein estimator with regression-based shrinkage).

Consider estimating $\theta \in \mathbb{R}^n$ in the model $Y \sim N_n(\theta, \sigma^2 I_n)$. In the standard James-Stein estimator, we shrink all the estimates toward zero, but it might make more sense to shrink them towards the average value $\overline{Y}$ (as we explored in a previous problem) or towards some other value based on observed side information.

Suppose that we have side information about each parameter $\theta_i$, represented by covariate vectors $x_1,\ldots,x_n \in \mathbb{R}^d$. Assume the design matrix $X \in \mathbb{R}^{n\times d}$, whose $i$th row is $x_i'$, has full column rank. Suppose that we expect $\theta_i$ is not too far from $x_i'\beta$ for some $\beta\in \mathbb{R}^d$. But unlike the usual linear regression setup, we will not assume $\theta_i = x_i'\beta$ exactly, we just want to shrink our estimate toward $x_i'\beta$.

1.  Assume the error variance $\sigma^2 = 1$ is known. Find an estimator $\delta(Y)$ for $\theta$ that strictly dominates $\delta_0(Y) = Y$ whenever $n - d \geq 3$, $$\text{MSE}(\theta; \delta) < \text{MSE}(\theta; \delta_0), \quad \text{for all } \theta \in \mathbb{R}^n,$$ and for which $\text{MSE}(X\beta; \delta) = d + 2$, for any $\beta\in \mathbb{R}^d$.

    In the special case of “intercept-only” regression ($d=1$ and $x_i=1$ for all $i$), your estimator should reduce to the version of the James-Stein estimator that shrinks toward $\overline{Y}$ (but you do not have to show this).

    **Hint:** The problem will become easier after an appropriate change of basis; think about how the estimator operates on different subspaces.

2.  Continue to assume the error variance $\sigma^2 = 1$ is known. Suppose we are unsure of whether $\theta = X\beta$ exactly. Suggest an appropriate test of the hypothesis $H_0:\;\theta = X\beta$ vs $H_1:\; \theta \neq X\beta$, treating $\beta \in \mathbb{R}^d$ as an unknown nuisance parameter.

3.  **Optional:** (Not graded, no extra points) Now suppose that the error variance $\sigma^2>0$ is unknown, but we have $r > 1$ replicates for each $i$; that is, we observe $Y_{i,k} \overset{\text{ind.}}{\sim}N(\theta_i, \sigma^2)$ for $i=1,\ldots,n$ and $k=1,\ldots,r$. Modify your test from the previous part for $H_0:\;\theta = X\beta$ vs $H_1:\; \theta \neq X\beta$.

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
