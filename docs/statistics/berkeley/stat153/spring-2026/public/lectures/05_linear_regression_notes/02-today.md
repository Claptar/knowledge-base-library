---
title: Today
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/05_linear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/05_linear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Today

**Source:** [`public/lectures/05_linear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/05_linear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

## Simple linear regression

Let's say we want to learn the relationship between two variables $y$ and $x$ - the goal is to predict $y$ given $x$. For example, we might want to predict the height of an adult man ($y$) given the height of his father ($x$). $y$ is called the response variable or dependent variable, $x$ i the covariate or independent variable. We will start with the more general scenario and then extend this concept specifically to time series.

In simple linear regression, we are predicting $y$ given one covariate $x$. In the case of multiple $x$, say $\{x_1, \dots, x_p\}$, this is called multiple regression.

For the simple case, we are predicting $y$ from one covariate $x$. For example:

$y = \beta_0 + \beta_1 x + \epsilon$

$\beta_0$ and $\beta_1$ are parameters that we will estimate from the data, where $\beta_0$ is the intercept, which corresponds to the value of $y$ when $x=0$, and $\beta_1$ represents the change in $y$ when $x$ changes by one unit.

We could observe, for example, pairs of data $(x_1, y_1), \dots, (x_n, y_n)$ where each of these samples is a pair of fathers and sons. We then might write:

$y_i = \beta_0 + \beta_1 x_i + \epsilon_i$.

We can then estimate our $\hat{\beta}_0$ and $\hat{\beta}_1$ from the data, then use these to predict the value of the response variable $\hat{y}$ (height of a new adult man) for a new covariate $x$. We will talk about how to do this using the Python library `statsmodels`, but we will also talk about how to derive the solution mathematically.

For time series regression, we often have some observed data $y_1, \dots, y_n$ that are observations for a single variable $y$. In this case, we may try two main ways of predicting $y$:

1. **Use time as a covariate** (many of the examples we've seen already do this -- for example, the DJIA data, fMRI data, population data over time)

2. **Use lagged version of $y$ as the covariate.** For this case, we might take $x_i = y_{i=1}$. In this case, we are predicting a current value based on a prior time point. This is called Lagged Regression or AutoRegression.

![Price of chicken and price of farm-bred Norwegian salmon over time, and corresponding fitted linear trend and 95% confidence intervals.](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec5_commodities.png)

## How do we estimate $\beta_0$ and $\beta_1$?

There are a couple of ways to estimate $\beta_0$ and $\beta_1$. Standard libraries such as `statsmodels` use the least squares method. In this method, we minimize the error sum of squares:

$$Q = \sum_{t=1}^n (y - \hat{y})^2 = \sum_{t=1}^n (y - \beta_0 - \beta_1 x)^2$$

### Ordinary Least Squares (OLS)

In ordinary least squares, we can solve for:

$\min_{\beta_0,\beta_1} \mathbb{E}[(y - \beta_0 - \beta_1 x)^2]$, which will be the best fitting line at the population level.

Solving this gives:

$\hat{\beta}_0 = \bar{y}-\hat{\beta}_1\bar{x}$
and
$\hat{\beta}_1=\frac{\sum_{i=1}^n (y_i-\bar{y})(x_i-\bar{x})}{\sum_{i=1}^n (x_i-\bar{x})^2}$

where

$\bar{y} = \frac{y_1+\dots+y_n}{n}$
and
$\bar{x} = \frac{x_1+\dots+x_n}{n}$

Let's look at what this looks like in `statsmodels` with an example.

---

[← Review](01-review.md) · [Up: contents](index.md)
