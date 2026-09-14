---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework10.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework10.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework10.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework10.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Inverting $t$- and $F$-tests is a very general tool for constructing confidence regions. Similar ideas will come up in future lectures for multivariate Gaussian random estimators.

**Problem 3** (Confidence bands for regression).

The setup for this problem is the same as for the previous problem only now we are interested in giving *confidence bands* for the regression line $f(x) = \beta_0 + \beta_1 x$. In this problem you do not need to give explicit expressions for everything, but you should be explicit enough that someone could calculate the bands based on your description.

1.  For a fixed value $x_0 \in \mathbb{R}$ (not necessarily one of the observed $x_i$ values) give a $1-\alpha$ $t$-based confidence interval for $f(x_0) = \beta_0 + \beta_1 x_0$. That is, we want to find $C_1^P(x_0), C_2^P(x_0)$ such that $$\mathbb{P}\left(C_1^P(x_0) \leq f(x_0) \leq C_2^P(x_0)\right) = 1-\alpha.$$ For each $x_0$, the coverage should be exactly $1-\alpha$. The functions $C_1^P(x), C_2^P(x)$ that we get from performing this operation on all $x$ values give a *pointwise confidence band* for the function $f(x)$.

2.  Now give a *simultaneous confidence band* around $f(x) = \beta_0 + \beta_1 x$. That is, give $C_1^S(x), C_2^S(x)$ with $$\mathbb{P}\left(C_1^S(x) \leq f(x) \leq C_2^S(x), \; \text{ for all } x\in\mathbb{R}\right) \geq 1-\alpha,$$ and show that your confidence band has this property.

    **Hint:** If all we know is that $\beta$ is in the confidence ellipse from the previous problem, what can we deduce about $f(x)$?

3.  Download the data set in `hw10.csv` from the course web site and make a scatter plot of the data. Plot the OLS regression line as well as the two confidence bands. Describe what you see. What do the bands do as $x$ goes away from the data set, and why does this make sense?

4.  **Optional:** (Not graded, no extra points) Show that the coverage of the simultaneous confidence band is *exactly* $1-\alpha$, not just greater than or equal to $1-\alpha$.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
