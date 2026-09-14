---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework7.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework7.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework7.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework7.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

When we think carefully about how to design rejection regions, we can get surprising results. In particular, for location families with heavy tails, extreme values are not that informative for distinguishing between two smaller values of the location parameter. Concretely, $X=10^6$ doesn’t help us distinguish between $\theta_1=1$ vs. $\theta_0=0$. By contrast, if the tails are lighter ($\log p_0$ concave implies the density shrinks at least exponentially) then more extreme $X$ values always give stronger evidence for distinguishing between any two parameter values; this is what MLR means.

**Problem 3** (Some UMP tests).

Numerically find the UMP test for the following hypothesis testing problems at level $\alpha=0.05$. For each problem,

1.  derive the appropriate test on paper,

2.  numerically compute the cutoff value $c$ (and $\gamma$ if necessary), and

3.  plot the power function of the level-$\alpha$ test for an appropriate range of parameter values.

<!-- -->

1.  $X_i \overset{\text{ind.}}{\sim}\text{Pois}(a_i \lambda)$ for $i=1,\ldots,n$, where $a_1,\ldots,a_n$ are known positive constants and $\lambda > 0$ is unknown. Test $H_0:\; \lambda = 1$ vs. $H_1:\; \lambda > 1$, with $n = 5$ and $a_i = i$.

2.  $X_i \overset{\text{ind.}}{\sim}N(\theta, \sigma_i^2)$ for $i=1,\ldots,n$, where $\sigma_i^2$ are known positive constants and $\theta \in \mathbb{R}$ is unknown. Test $H_0:\; \theta = 0$ vs. $H_1:\; \theta > 0$, with $n = 20$ and $\sigma_i^2 = i$. On your power plot, also plot the power function of the (sub-optimal) test that rejects for large $\sum_i X_i$.

3.  $X_1,\ldots, X_n \overset{\text{i.i.d.}}{\sim}\text{Pareto}(\theta) = \theta x^{-(1+\theta)}$, for $\theta > 0$ and $x > 1$ (also called a power law distribution). Test $H_0:\; \theta = 1$ vs. $H_1:\; \theta < 1$, for $n = 100$. On your power plot, also plot the power function of the (sub-optimal) test that rejects for large $\sum_i X_i$.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
