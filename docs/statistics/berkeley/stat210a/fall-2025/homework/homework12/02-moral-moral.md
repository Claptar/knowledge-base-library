---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework12.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework12.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework12.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework12.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

The score test can be carried out with nuisance parameters, but the fact that we estimate the nuisance parameter affects the distribution of the test statistic in a way that we need to take into account.

**Problem 2** (Poisson score test). Suppose that for $i=1,\ldots,x_n$ we observe a real covariate $x_i \in \mathbb{R}$ (fixed and known) and a Poisson response $Y_i \sim \text{Pois}(\lambda_i)$. We assume that $\lambda_i = \alpha + \beta x_i$, with the restriction that $\lambda_i \geq 0$ for all $i$, but with $\alpha, \beta \in \mathbb{R}$ otherwise unrestricted. Assume that $$\lim_{n \to \infty} \frac{\sum_{i=1}^n |x_i - \bar{x}_n|^3}{\left(\sum_{i=1}^n (x_i-\bar{x}_n)^2\right)^{3/2}} = 0,$$ where $\bar{x}_n = n^{-1}\sum_{i=1}^n x_i$. We observe the first $n$ pairs $(x_i,y_i)$ and our goal is to test the hypothesis $H_0:\; \beta = 0$ vs. $H_1:\; \beta > 0$. Assume that there are at least 3 distinct values represented among $x_1,\ldots,x_n$.

1.  Show that this model is a curved exponential family.

2.  Derive the score test statistic for $H_0$ vs $H_1$. Give the test statistic and asymptotic rejection cutoff.

3.  Show that your test statistic is indeed asymptotically normally distributed, and find an asymptotically valid rejection cutoff.

    **Hint**: It may help to use the *Lyapunov CLT*, which applies to sums of independent random variables that are not necessarily identically distributed: Suppose $Z_1,Z_2,\ldots$ is a sequence of random variables with $Z_i \sim (\mu_i, \sigma_i^2)$, for $\sigma_i^2 < \infty$. Define $s_n^2 = \sum_{i=1}^n \sigma_i^2$. If for some $\delta > 0$, we have $$\lim_{n \to \infty} \frac{1}{s_n^{2+\delta}} \sum_{i=1}^n \mathbb{E}\left[|Z_i - \mu_i|^{2+\delta}\right] = 0,$$ then $s_n^{-1}\sum_{i=1}^n (Z_i - \mu_i) \Rightarrow N(0,1)$.

    **Hint**: It may also help to start by assuming $\bar{x} = 0$, and then generalize your result.

4.  Suppose $n$ is small, so we don’t want to rely on the asymptotic normality. Explain how we could find a finite-sample exact conditional cutoff for the score test from part (b) (it is not necessary to give a closed form for the test, or to prove any optimality property).

---

[← Homework12 Part 01 —](01-homework12-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
