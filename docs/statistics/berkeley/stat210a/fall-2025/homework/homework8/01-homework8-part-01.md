---
title: Homework8 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework8.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework8 Part 01 —

**Source:** [`homework/homework8.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Some two-tailed tests).

Consider testing $H_0:\,\theta = \theta_0$ vs $H_1:\,\theta \neq \theta_0$ in a one-parameter exponential family of the form $p_\theta(x) = e^{\theta T(x) - A(\theta)}h(x)$. We stated in class that among all *unbiased, level-$\alpha$* tests, the one that rejects for extreme (i.e., large or small) values of $T(X)$ is uniformly most powerful (simultaneously maximizes power for all alternatives).

The equal-tailed level-$\alpha$ test that rejects for extreme values of $T(X)$ does not satisfy as interesting an optimality property but it is also a competitive test. Depending on the distribution, the equal-tailed test and the UMPU test may or may not coincide.

Numerically find the equal-tailed and UMPU test for the following hypothesis testing problems at level $\alpha=0.05$. For each problem,

1.  derive the appropriate tests (leaving the cutoff values abstract), and

2.  numerically compute the cutoff values $c$ (no $\gamma$ necessary since these are continuous problems)

<!-- -->

1.  $X_i \overset{\text{ind.}}{\sim}N(\theta, \sigma_i^2)$ for $i=1,\ldots,n$, where $\sigma_i^2$ are known positive constants and $\theta \in \mathbb{R}$ is unknown. Test $H_0:\; \theta = 0$ vs. $H_1:\; \theta \neq 0$, with $n = 20$ and $\sigma_i^2 = i$. On your power plot, also plot the power function of the (sub-optimal) test that rejects for extreme values of $\sum_i X_i$.

2.  $X_1,\ldots, X_n \overset{\text{i.i.d.}}{\sim}\text{Pareto}(\theta) = \theta x^{-(1+\theta)}$, for $\theta > 0$ and $x > 1$ (also called a power law distribution). Test $H_0:\; \theta = 1$ vs. $H_1:\; \theta \neq 1$, for $n = 100$. On your power plot, also plot the power function of the (sub-optimal) test that rejects for large $\sum_i X_i$.

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
