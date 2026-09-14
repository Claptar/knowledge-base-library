---
title: Homework4 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework4.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework4 Part 01 —

**Source:** [`homework/homework4.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Complete sufficient statistic for a nonparametric family).

Consider an i.i.d. sample from the nonparametric family of *all* distributions on $\mathbb{R}$: $$X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}P,$$ Formally we can write this model as $\mathcal{P}= \left\{P^n:\; P \text{ is a probability measure on } \mathbb{R}\right\}$. Let $T(X) = (X_{(1)},\ldots,X_{(n)})$ denote the vector of order statistics.

1.  For a finite set of size $m$, $\mathcal{Y}= \{y_1,\ldots,y_m\} \subseteq \mathbb{R}$, consider the subfamily $\mathcal{P}_\mathcal{Y}$ of distributions supported on $\mathcal{Y}$: $$\mathcal{P}_\mathcal{Y}= \{P^n:\; P(\mathcal{Y}) = 1\} \subseteq \mathcal{P}.$$ Show that $T(X)$ is complete sufficient for this family.

    **Hint:** It may help to review different ways to parameterize the multinomial family.

2.  Show that the vector of order statistics $T(X) = (X_{(1)},\ldots,X_{(n)})$ is a complete sufficient statistic for $\mathcal{P}$.

3.  Next, consider the restricted subfamily $$\mathcal{Q}_k = \{P^n:\; \mathbb{E}_P[|X_1|^k] < \infty\} \subseteq \mathcal{P},$$ and define the sample mean and variance respectively as $$\overline X = \frac{1}{n}\sum_{i=1}^n X_i, \quad S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline X)^2.$$ Show that $\overline X$ is the UMVU estimator of $\mathbb{E}_P X_1$ in $\mathcal{Q}_1$, and $S^2$ is the UMVU estimator of $\text{Var}_P(X_1)$ in $\mathcal{Q}_2$.

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
