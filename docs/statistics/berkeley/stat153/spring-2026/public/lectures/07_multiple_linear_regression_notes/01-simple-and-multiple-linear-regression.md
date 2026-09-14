---
title: Simple and multiple linear regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/07_multiple_linear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/07_multiple_linear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Simple and multiple linear regression

**Source:** [`public/lectures/07_multiple_linear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/07_multiple_linear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Last time we spoke about regression models where we have just two parameters, $\beta_0$ and $\beta_1$:

$$y = \beta_0 + \beta_1 x + \epsilon$$

For example, $y$ is height of an adult and $x$ is the height of their parent, or $y$ is the price of chicken and $x$ is time.

However, often we have multiple independent series that may be contributing to $y$. We can then express this through *Multiple Linear Regression*

$$y_i = \beta_0 + \beta_1 x_{i_1} + \beta_2 x_{i_2} + \cdots + \beta_n x_{i_p} + w_i$$

Here we will still be estimating $\beta_0, \dots, \beta_n$.

We can do this by rewriting the equation above as:

$$y_i = x_i^\intercal\beta,$$

for $i=1,\dots,n$. To add an intercept, we can redefine each vector $x_i$ so that it has a 1 prepended to it:

$x=(1,x_1, x_2, \dots, x_p)$

Now, the first entry of $\beta$ will be the intercept, while the rest are the coefficients for each $x_j$.

We now have the least squares problem:

$$\underset{{\beta \in \mathbb{R}^p}}{\min} \displaystyle\sum_{i=1}^n (y_i - x_i^\intercal \beta)^2$$

We can then set the derivatives equal to zero to obtain:

$$\hat{\beta} = \left( \displaystyle\sum_{i=1}^n x_i x_i^T \right)^{-1} \displaystyle\sum_{i=1}^n x_i y_i$$

---

[Up: contents](index.md) · [Matrix notation →](02-matrix-notation.md)
