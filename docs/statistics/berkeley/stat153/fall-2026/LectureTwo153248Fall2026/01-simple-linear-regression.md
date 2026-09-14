---
title: Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureTwo153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureTwo153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Simple Linear Regression

**Source:** [`LectureTwo153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureTwo153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

We want to learn the relationship between two variables $y$ and $x$, with the aim of predicting $y$ given the value of $x$. $y$ is called the response variable, and $x$ is called the covariate. For example (this was one of the original applications of regression), $y$ denotes the height of an adult man, and $x$ denotes the height of their father. The linear regression model assumes that $y$ is related to $x$ via the equation: $$\begin{equation}
\label{lin_eq}
  y = \beta_0 + \beta_1 x + \epsilon
\end{equation}$$ where $\beta_0$ and $\beta_1$ are parameters, and $\epsilon$ denotes an error term which captures deviations of $y$ from the assumed equation $\beta_0 + \beta_1 x$. The parameters $\beta_0$ and $\beta_1$ can be interpreted as follows: $\beta_0$ denotes the value of $y$ when $x = 0$ and $\beta_1$ represents the change in $y$ when $x$ changes by one unit.

We observe data $(x_1, y_1), \dots, (x_n, y_n)$ on the covariate and response variables corresponding to $n$ instances (in the height example, we have data on heights for $n$ father-son pairs). Writing the equation <a href="#lin_eq" data-reference-type="eqref" data-reference="lin_eq">[lin_eq]</a> for each individual pair $(x_i, y_i)$ we get $$\begin{equation}
\label{linmod}
  y_i = \beta_0 + \beta_1 x_i + \epsilon_i.
\end{equation}$$ The observed data $(x_1, y_1), \dots, (x_n, y_n)$ will be used to obtain estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ (as well as uncertaintly quantification) for the parameters $\beta_0$ and $\beta_1$. After obtaining these estimates, one can predict the value of the response variable for a possibly new covariate value $x_{\text{new}}$ by $\hat{\beta}_0 + \hat{\beta}_1
x_{\text{new}}$.

We will implement the equations for obtaining $\hat{\beta}_0$ and $\hat{\beta}_1$ from the observed data $(x_1, y_1), \dots, (x_n, y_n)$ using the Python library `statsmodels`. We will also study the math behind this process.

To apply linear regression, we need data on both $y$ and $x$. In the time series context, the observed data is $y_1, \dots, y_n$ which represent observations for a single variable $y$. There is no additional data on another variable $x$. In order to apply regression methods to time series, we need to create a covariate variable $x$. There are two main ways of doing it:

1.  **Time as covariate**: Here we take the time index as the covariate $x$. For example, in the time series dataset on the population of the United States for each month from January 1959 to December 2024: $n$ denotes the total number of data points, $x_i = i$ and $y_i$ denotes the observed population data for the $i^{\text{th}}$ month (first month is January 1959, second month is February 1959 and so on).

2.  **Lagged $y$ as covariate**: Here we take $x_i =
      y_{i-1}$. In other words, the covariate equals the response at the previous time point. This kind of regression is called Lagged Regression or, more commonly, AutoRegression.

For now, we shall focus on the first kind of regression (time as covariate). We shall study AutoRegression in more detail later.

---

[Up: contents](index.md) · [Estimation of $\beta0$ and $\beta1$ →](02-estimation-of-and.md)
