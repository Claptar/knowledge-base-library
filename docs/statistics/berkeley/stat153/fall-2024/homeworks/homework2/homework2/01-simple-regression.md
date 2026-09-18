---
title: Simple regression
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) — berkeley-stat153 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Simple regression

```r
knitr::opts_chunk$set(cache = TRUE, autodep = TRUE, cache.comments = TRUE)
```

\raggedright

The total number of points possible for this homework is 39. The number of
points for each question is written below, and questions marked as "bonus" are
optional (points awarded for bonus problems can be used to earn back points that
you may have lost on other parts of this homework but will not put you above
full credit). Submit the **knitted pdf file** from this Rmd to Gradescope.

If you collaborated with anybody for this homework, put their names here:

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

## Multiple regression

5. (2 pts)
In class, we claimed that the multiple regression coefficients, with respect to
responses $y_i$ and feature vectors $x_i \in \mathbb{R}^p$, $i = 1,\dots,n$, can
be written in two ways: the first is

$$
\hat\beta = \bigg( \sum_{i=1}^n x_i x_i^T \bigg)^{-1} \sum_{i=1}^n x_i y_i.
]
The second is
[
\hat\beta = (X^T X)^{-1} X^T y,
$$

where $X \in \mathbb{R}^{n \times p}$ is a feature matrix, with $i^{\text{th}}$
row $x_i$, and $y \in \mathbb{R}^n$ is a response vector, with $i^{\text{th}}$
component $y_i$. Prove that these two expressions are equivalent.

6. (Bonus)
Derive the population and sample multiple regression coefficients by solving the
corresponding least squares problem (differentiating the criterion with respect
to each $\beta_j$, setting equal to zero, and solving). For the sample least
squares coefficient, deriving either representation in Q5 will be fine.

---

[Up: contents](index.md) · [Covariance calculations →](02-covariance-calculations.md)
