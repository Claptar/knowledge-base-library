---
title: Matrix notation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/07_multiple_linear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/07_multiple_linear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Matrix notation

**Source:** [`public/lectures/07_multiple_linear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/07_multiple_linear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We can also write this equation in a more general matrix form:

$$\underset{n\times 1}{y} = \underset{n \times p}{X} \underset{p \times 1}{\mathbb{\beta}}$$

$$
  y = \begin{bmatrix}
    y_1 \\ y_2 \\ \vdots \\ y_n
  \end{bmatrix}, \quad
  X = \begin{bmatrix}
    x_{11} & x_{12} & \cdots & x_{1p} \\
    x_{21} & x_{22} & \cdots & x_{2p} \\
    \vdots & & & \\
    x_{n1} & x_{n2} & \cdots & x_{np}
    \end{bmatrix}, \quad
  \beta = \begin{bmatrix}
    \beta_1 \\ \beta_2 \\ \vdots \\ \beta_p
    \end{bmatrix}
$$

Here $n$ might represent the number of time points and $p$ is the number of parameters. We can then write our least squares problem as:

$$\underset{{\beta \in \mathbb{R}^p}}{\min} || y - X\beta||^2_2 $$

Recall that the $\ell_2$ norm $|| \cdot ||_2$ of a vector $a \in \mathbb{R}^d$ is defined as $||a||^2_2 = \sum_{i=1}^d a_i^2$. Then, we can solve to get an estimate of $\hat{\beta}$:

$$\underset{p \times 1}{\hat{\beta}} = \underset{p \times p}{(X^\intercal X)}^{-1}\underset{p \times n}{X^\intercal} \underset{n \times 1}{y}$$

An important note here is that we assume that the columns of $X$ (sometimes called our *features*) are *linearly independent*. This can only happen for $p\leq n$ - where we have no more features than samples. Otherwise, $X \intercal X $ will not have an inverse, but we will be able to deal with this using regularization (which we will cover later).

---

[← Simple and multiple linear regression](01-simple-and-multiple-linear-regression.md) · [Up: contents](index.md) · [Finger tapping demo →](03-finger-tapping-demo.md)
