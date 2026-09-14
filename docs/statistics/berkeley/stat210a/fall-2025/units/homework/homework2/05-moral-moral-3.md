---
title: 'Moral: {#moral-3}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework2.tex
source_file: sources/berkeley-stat210a/fall-2025/units/homework/homework2.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-3}

**Source:** [`units/homework/homework2.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework/homework2.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

This exercise confirms something that we should intuitively expect to be true: that increasing the natural parameter $\eta$, which “tilts” the distribution toward larger values of $T(X)$, will also shift the distribution of $X$ to the right if $T$ is an increasing function. It also illustrates the usefulness of differential identities for understanding exponential families’ structure.

**Problem 5** (Mean parameterization of an exponential family). Consider the $s$-parameter exponential family $\mathcal{P}= \{P_\eta:\; \eta \in \Xi\}$ on $\mathcal{X}$ with densities $p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x)$ with respect to a common dominating measure $\nu$. Assume $\Xi=\Xi_1^{\circ}$, the interior of the full natural parameter space, and that $\text{Var}_\eta(a'T(X))>0$ for all $a \neq 0$ and $\eta\in \Xi$.

Define the *mean parameter* $$\mu(\eta) = \mathbb{E}_\eta[T(X)].$$ We will show that this is a one-to-one mapping, so $\mathcal{P}$ can be alternatively be parameterized by $\mu(\eta)$ instead of $\eta$. The Bernoulli, Poisson, and exponential distributions are exponential families that are most often parameterized by their means, and parameterizations of other distributions like the normal and binomial are closely related to the mean parameterization.

Throughout this problem, you may use without proof that if the variance of any statistic $S(X)$ is positive under one $P_\eta \in \mathcal{P}$ then it is positive under all $P_\eta \in \mathcal{P}$ (as an optional exercise, try to prove this).

1.  For $s=1$, show that $\eta \mapsto \mathbb{E}_\eta[T(X)]$ is a one-to-one mapping; that is, show that if $\eta_1 \neq \eta_2$ then $\mathbb{E}_{\eta_1}[T(X)] \neq \mathbb{E}_{\eta_2}[T(X)]$.

    **Hint:** You can use the differential identities.

2.  For $s>1$ and $\eta_1,\eta_2\in\Xi$, consider the subfamily whose parameter space is the line segment between $\eta_1$ and $\eta_2$. For $\theta \in [0,1]$, let $$\eta(\theta) = (1-\theta) \eta_1 + \theta \eta_2.$$ Show that this subfamily is a one-parameter exponential family on $\mathcal{X}$ with natural parameter $\theta$, and write it in standard exponential family form.

3.  Combine (a) and (b) to show that $\eta \mapsto \mathbb{E}_\eta[T(X)]$ is a one-to-one mapping for $s \geq 1$.

---

[← Moral: {#moral-2}](04-moral-moral-2.md) · [Up: contents](index.md) · [Moral: {#moral-4} →](06-moral-moral-4.md)
