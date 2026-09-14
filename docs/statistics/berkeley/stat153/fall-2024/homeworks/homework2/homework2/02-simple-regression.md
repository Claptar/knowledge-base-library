---
title: Simple regression
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Simple regression

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

1. (2 pts)
Derive the population least squares coefficients, which solve
$$
\min_{\beta_1, \beta_0} \, \mathbb{E} \big[ (y - \beta_0 - \beta_1 x)^2 \big],
$$
by differentiating the criterion with respect to each $\beta_j$, setting equal
to zero, and solving. Repeat the calculation but without intercept (without the
$\beta_0$ coefficient in the model).

2. (2 pts)
As in Q1, now derive the sample least squares coefficients, which solve
$$
\min_{\beta_1, \beta_0} \, \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.
$$
Again, repeat the calculation but without intercept (no $\beta_0$ in the model).

3. (2 pts)
Prove or disprove: in the model without intercept, the regression coefficient of
$x$ on $y$ is the inverse of that from the regression of $y$ on $x$. Answer the
question for both the population version and the sample version.

4. (3 pts)
Consider the following hypothetical. Let $y$ be the height of a child and $x$ be
the height of their parent, and consider a regression of $y$ on $x$, performed
in a large population. Suppose that we estimate the regression coefficients
separately for male and female parents (two separate regressions) and we find
that the slope coefficient from the former regression $\hat\beta_1^{\text{dad}}$
is smaller than that from the latter $\hat\beta_1^{\text{mom}}$. Suppose however
that we find (in this same population) the sample correlation between a father's
height and their child's height is *larger* than that between a mother's height
and their child's height. What is a plausible explanation for what is happening
here?

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Multiple regression →](03-multiple-regression.md)
