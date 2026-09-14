---
title: Homework3 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework3.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework3.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework3 Part 01 —

**Source:** [`homework/homework3.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework3.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Multinomial subfamilies).

The multinomial family is a multi-category version of the binomial, it measures the number of times each category comes up if we sample a $d$-category random variable with distribution $\pi$ on $n$ independent trials. Throughout this problem assume $d \geq 3$.

If $X \sim \text{Multinom}(n, \pi)$, with all $\pi_j > 0$ and $\sum_j \pi_j = 1$, then $X$ has density $$p_\pi(x) = \pi_1^{x_1}\pi_2^{x_2}\cdots \pi_d^{x_d} \cdot \frac{n!}{x_1! x_2! \cdots x_d!}$$

**Note:** The coordinates of $X=(X_1,\ldots,X_d)$ are neither independent nor identically distributed.

1.  Rewrite the densities as a $(d-1)$-parameter exponential family, giving an explicit form for $T(x)$, $h(x)$, $\eta$, and $A(\eta)$. Show whether $X=(X_1,\ldots,X_d)$ is complete sufficient, minimal sufficient, or neither.

2.  Suppose a certain gene has two alleles **A** and **a**, and $\theta\in (0,1)$ is the unknown prevalence of allele **a** in a well-mixed population. Then the proportion of people in the population with genotypes **aa**, **Aa**, and **AA** is $\theta^2$, $2\theta(1-\theta)$, and $(1-\theta)^2$, respectively.

    We can estimate $\theta$ by sampling $n$ independent individuals from the population and counting the number who have each genotype. These counts will have a joint multinomial distribution with probability parameter $$\pi(\theta) = (\theta^2, 2\theta(1-\theta), (1-\theta)^2).$$ Hence, scientific considerations might lead us to use the multinomial subfamily indexed by $\theta$: $$\mathcal{P}= \{\text{Multinom}(n,\pi(\theta)):\; \theta \in (0,1)\}.$$ Can $\mathcal{P}$ be written as a one-parameter exponential family? Find a minimal sufficient statistic for $\mathcal{P}$, and show whether or not it is complete.

3.  Now suppose our population is a mixture of two populations with different prevalences $\theta_1$ and $\theta_2$ for allele **a**. Define $\gamma \in (0,1)$ as the proportion of individuals from population 1. Assume that $\theta_1,\theta_2$ are known and only $\gamma$ is unknown. Since $\theta_1$ and $\theta_2$ are known it may be convenient to write the mixture probabilities as $$\pi(\gamma) = \gamma\pi^{(1)} + (1-\gamma)\pi^{(2)}, \quad \text{ for } \pi^{(k)} = (\theta_k^2, 2\theta_k(1-\theta_k), (1-\theta_k)^2), \;\;k=1,2.$$

    Now suppose that we again sample $n$ individuals from our unknown mixture, giving another one-parameter subfamily $\mathcal{Q}$ indexed by $\gamma$. Can $\mathcal{Q}$ be written as a one-parameter exponential family? Find a minimal sufficient statistic for $\mathcal{Q}$, and show whether or not it is complete.

---

[Up: contents](index.md) · [Moral →](02-moral.md)
