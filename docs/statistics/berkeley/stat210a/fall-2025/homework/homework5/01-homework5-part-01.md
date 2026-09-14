---
title: Homework5 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework5.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework5.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework5 Part 01 —

**Source:** [`homework/homework5.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework5.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Ridge regression).

Consider the *Gaussian linear model* where $$y_i = x_i' \beta + \varepsilon_i, \quad \text{ with } \varepsilon_i \overset{\text{i.i.d.}}{\sim}N(0,\sigma^2) \;\text{ for } i =1, \ldots n,$$ where $\beta \in \mathbb{R}^d$ is unknown, and the covariate vectors $x_i \in \mathbb{R}^d$ are fixed and known. Assume the error variance $\sigma^2>0$ is also known. We observe the response vector $y \in \mathbb{R}^n$.

1.  Assume that $d \leq n$, and the design matrix $\mathbf{X}$ (the $n \times d$ matrix whose $i$th row is $x_i'$) has full column rank. Show that the OLS estimator $\hat\beta = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'y$ is the UMVU estimator of $\beta$.

    **Note:** Remember that the design matrix $\mathbf{X}$ is not data in the same sense $y$ is; it is more like a known parameter.

2.  Now consider Bayesian estimation with the prior $\beta \sim N(\mu, \tau^2 I_d)$. Under the same prior as in part (b), find the posterior distribution of $\beta$. Does it matter whether $d > n$, or whether $\mathbf{X}$ has full column rank?

3.  Suppose that $\mathbf{X}\gamma = 0$ for some nonzero $\gamma \in \mathbb{R}^d$ whose entries are all nonzero. Show that no unbiased estimator exists for any $\beta_j$. In your opinion, should this give us any reason for concern about the Bayes estimator? (The subjective part of the question will be graded leniently).

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
