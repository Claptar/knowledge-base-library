---
title: Homework2 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework2.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework2.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework2 Part 01 —

**Source:** [`homework/homework2.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework2.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Uniform location-scale family).

Let $X_1, \ldots, X_n\overset{\text{i.i.d.}}{\sim}\text{Unif}[\mu-\sigma, \mu + \sigma]$, with $\mu\in\mathbb{R}$ and $\sigma > 0$ unknown.

1.  Show that $T(X) = (X_{(1)}, X_{(n)})$ is minimal sufficient.

2.  Suppose that we wish to estimate $\mu$ under the squared error loss. The sample mean $\overline{X}$ may appear to be a reasonable estimator of $\mu$, but we might worry about the fact that it is not a function of $T(X)$.

    Guided by the sufficiency principle, we could instead consider the estimator $$\delta^*(X) = \frac{X_{(1)} + X_{(n)}}{2}.$$ Use Monte Carlo simulation to simulate the distribution of both estimators for $\mu = 0, \sigma = 1, n = 1000$. Report the root mean squared error (RMSE), defined as $\sqrt{\textnormal{MSE}}$ (as calculated by Monte Carlo).

    For each estimator, plot a histogram of simulated estimates. You can either put both histograms on the same plot, or in side-by-side plots. If you do the latter, it might be more enlightening to use the same range for the horizontal and vertical axes in both plots, so the differences between the histograms are more evident. Include your code.

3.  In the previous part, we only compared the two estimators for one setting of the parameters $\mu,\sigma$. Show that, for both estimators, the MSE for generic $(\mu,\sigma)$ does not depend on $\mu$, and is proportional to $\sigma^2$. That is, show that $$\textnormal{MSE}(\mu, \sigma; \delta) = \sigma^2 \textnormal{MSE}(0,1; \delta), \quad \text{for } \delta = \overline{X}, \delta^*.$$ Complete the argument to conclude that $\overline{X}$ is inadmissible whenever $\textnormal{MSE}(0,1;\delta^*) < \textnormal{MSE}(0,1;\overline{X})$.

4.  (**Optional:** Not graded, no extra points) In this and the next optional parts, you will calculate the MSE analytically using some nice manipulations.

    If $B \sim \text{Beta}(\alpha,\beta)$ then its density is proportional to $x^{\alpha-1}(1-x)^{\beta-1}$ on $x\in [0,1]$.

    If $U_1,\ldots,U_n \overset{\text{i.i.d.}}{\sim}U[0,1]$, show that $$U_{(n)} \sim \text{Beta}(n,1), \quad\text{ which has density } p(x) = n x^{n-1},$$ and $$U_{(1)}/U_{(n)} \sim \text{Beta}(1,n-1) \quad\text{ which has density } p(x) = (n-1)(1-x)^{n-2},$$ independently of $U_{(n)}$.

    **Hint:** For the first part, start by writing down the CDF of $U_{(n)}$.

    **Hint:** For the second part, you may use without proof the fact that, conditional on $U_{(n)} = u$, the remaining $n-1$ values are i.i.d. $\text{Unif}[0,u]$, then proceed similarly to what you did for the first part.

5.  (**Optional:** Not graded, no extra points) Compute the MSE of each estimator as a function of $n, \mu,$ and $\sigma$, and show that $\delta^*$ strictly dominates $\overline{X}$ for $n > 2$ (the estimators coincide for $n=2$). What happens to the ratio of their MSE’s as $n\to\infty$?

    **Hint:** The results from the previous part should be useful. You may use without proof that $\text{Beta}(\alpha,\beta)$ has mean $\frac{\alpha}{\alpha+\beta}$ and variance $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha + \beta + 1)}$.

---

[Up: contents](index.md) · [Moral →](02-moral.md)
