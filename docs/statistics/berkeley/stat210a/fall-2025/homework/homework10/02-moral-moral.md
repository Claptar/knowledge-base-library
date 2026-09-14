---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework10.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework10.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework10.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework10.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

We can get interesting estimators by combining our change of basis ideas with the James–Stein estimator, to implement different sorts of inductive biases.

**Problem 2** (Confidence regions for regression).

Assume we observe $x_1,\ldots,x_n \in \mathbb{R}$, which are not all identical (for at least one pair $i$ and $j$, $x_i\neq x_j$). We also observe $$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \text{ for } \varepsilon_i \overset{\text{i.i.d.}}{\sim}N(0,\sigma^2).$$ $\beta_0,\beta_1\in \mathbb{R}$ and $\sigma^2 > 0$ are unknown. Let $\bar{x}$ represent the mean value $\frac{1}{n}\sum_i x_i$.

1.  Give an explicit expression for the $t$-based confidence interval for $\beta_1$, in terms of a quantile of a Student’s $t$ distribution with an appropriate number of degrees of freedom (feel free to break up the expression, for example by first giving an expression for $\hat\beta_1$ and then using $\hat\beta_1$ in your final expression).

2.  Define the OLS estimator $\hat\beta = \binom{\hat\beta_0}{\hat\beta_1}$. Show that $\hat\beta \sim N_2\left(\beta, \; \sigma^2(X'X)^{-1}\right)$, for the design matrix $X = [1_n, x]$. Apply this fact to find an $F$-test for the hypothesis $H_0:\;\beta=0$ vs $H_1:\;\beta \neq 0$.

3.  Invert your $F$-test to give a *confidence ellipse* for $\beta = \binom{\beta_0}{\beta_1}$. It may be convenient to represent the set as an affine transformation of the unit ball in $\mathbb{R}^2$: $$b + A \mathbb{B}_1(0) = \{b + Az:\; z\in \mathbb{R}^2, \|z\| \leq 1\}, \quad \text{ for } b \in \mathbb{R}^2, A \in \mathbb{R}^{2\times 2}.$$ Give explicit expressions for $b$ and $A$ in terms of a quantile of an appropriate $F$ distribution.

---

[← Homework10 Part 01 —](01-homework10-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
