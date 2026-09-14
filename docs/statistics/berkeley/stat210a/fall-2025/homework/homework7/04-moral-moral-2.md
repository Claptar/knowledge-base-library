---
title: 'Moral: {#moral-2}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework7.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework7.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-2}

**Source:** [`homework/homework7.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework7.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Once again, when we use the right test we often can deliver noticeably better power than if we chose an *ad hoc* test.

**Problem 4** (Bayesian hypothesis testing).

Consider a univariate Gaussian problem with $X\mid \theta \sim N(\theta, 1)$, where $\theta=0$ under the null hypothesis and $\theta\sim \Lambda_1$ under the alternative hypothesis (assume $\Lambda_1(\{0\})=0$). In addition let $\pi_0$ denote the *a priori* probability that the null hypothesis is true; therefore the full prior is a mixture between a point mass at 0 and $\Lambda_1$.

1.  Compute the posterior probability that the null hypothesis is true, i.e. $$\pi_{\text{post}}(x; \Lambda_1, \pi_0) = \mathbb{P}(\theta = 0 \mid X=x).$$

2.  If $\pi_0=0.5$ and $X = x$, how small could the posterior null probability be?

    That is, find $$\pi_{\text{post}}^*(x) = \min_{\Lambda_1} \pi_{\text{post}}(x; \Lambda_1, 0.5),$$ as a function of $x$, for $x>0$. Give the minimizing prior $\Lambda_1$, which also depends on $x$.

    **Note:** This is not an optimization problem the analyst is going to solve. Any given analyst will use their own actual prior to calculate their own posterior probability. We are just getting a lower bound on how small the analyst’s posterior null probability could be.

3.  Now restrict $\Lambda_1 = N(0,\tau^2)$ for $\tau > 0$, a subclass of “realistic” priors an analyst might use if they were initially unsure about what alternative value to focus on. Compute $\pi_{\text{post}}$ as a function of $\tau^2$ and $x$.

    Continuing to assume the analyst puts $0.5$ prior on the null and the alternative, now how small could the analyst’s posterior probability be? That is, find $$\pi_{\text{post},N}^*(x) = \min_{\tau^2>0} \pi_{\text{post}}(x; N(0,\tau^2), 0.5),$$ and give the minimizing value of $\tau^2$, both as functions of $x$, for $x > 1$.

4.  Now assume we observe a value of $X$ such that the two-sided $p$-value $p(X)$ (i.e., $p(x) = \mathbb{P}_0(|X|>|x|)$) takes the values $0.05, 0.01, 0.005$, or $0.001$. Numerically compute $\pi_{\text{post}}^*$ and $\pi_{\text{post},N}^*$ for each value and make a small table. In words, interpret the results.

---

[← Moral: {#moral-1}](03-moral-moral-1.md) · [Up: contents](index.md) · [Moral: {#moral-3} →](05-moral-moral-3.md)
