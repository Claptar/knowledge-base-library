---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework8.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework8.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

We see again, now in the two-sided case, that choosing the right test statistic gives better tests.

**Problem 2** (Testing in trinomial subfamilies).

Recall the problem on a previous homework on subfamilies of the trinomial distribution $$p_\pi(x) = \pi_1^{x_1}\pi_2^{x_2}\pi_3^{x_3} \cdot \frac{n!}{x_1! x_2! x_3!},$$ and recall that the probability of genotypes **aa**, **Aa**, and **AA** were $\theta^2$, $2\theta(1-\theta)$, and $(1-\theta)^2$, respectively, for an individual drawn from a well-mixed population with prevalence $\theta\in (0,1)$ for allele **a**.

You may appeal to any results from the previous homework problem that are helpful, without re-deriving them.

1.  Suppose we observe a sample of size $n = 1000$ from a well-mixed population with prevalence $\theta$, and we want to test $H_0:\;\theta \leq 0.1$ vs $H_1:\; \theta > 0.1$ at level $\alpha = 0.1$. Show that there is a UMP test for this problem, and say what the test statistic is. Give the cutoffs $c,\gamma$ and plot the power as a function of $\theta$, for an appropriate range of values.

2.  Now suppose our population is a mixture of two populations with different prevalences $\theta_1$ and $\theta_2$ for allele **a**. Define $\gamma \in [0,1]$ as the proportion of individuals from population 1, so the proportion of genotype $i=1,2,3$ is $\pi_i(\gamma) = \gamma \pi_i(1) + (1-\gamma)\pi_i(0)$. Assume that $\theta_1,\theta_2$ are known and only $\gamma$ is unknown.

    Consider testing $H_0:\;\gamma = 0$ vs $H_1:\;\gamma = \gamma_1$, for some fixed value $\gamma_1 > 0$. That is, we are testing for whether the individuals we are sampling from are coming only from population 2, or whether a nonzero fraction of them are coming from population 1. Show that the likelihood ratio test rejects for large values of the statistic $\sum_{i=1}^3 w_iX_i$, where $$w_i(\gamma_1) = \log\left(1 + \gamma_1\left(\frac{\pi_i(1)-\pi_i(0)}{\pi_i(0)}\right)\right).$$

3.  Next consider testing $H_0:\;\gamma = 0$ vs $H_1:\;\gamma >0$, when $n$ is large. Explain why no UMP test exists, and suggest instead an appropriate test for $H_0:\;\gamma = 0$ vs $H_1:\;\gamma > 0$ that prioritizes small alternative values of $\gamma$.

4.  Implement your test from part (c) when $\theta_1 = 0.7$, $\theta_2=0.05$, and $n=1000$, at level $\alpha = 0.1$, and compare its power to the Neyman–Pearson test for $H_0:\;\gamma = 0$ vs $H_1:\;\gamma = 1$. Give an explicit expression for both test statistics and comment qualitatively on how they are examining the data differently. Plot their power curves for an appropriate range of $\gamma$ values.

---

[← Homework8 Part 01 —](01-homework8-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
