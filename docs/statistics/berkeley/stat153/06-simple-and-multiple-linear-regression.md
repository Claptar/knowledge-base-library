---
title: "6. Simple and Multiple Linear Regression"
course: "Berkeley Stat 153 Fall 2024"
chapter: 6
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Simple and Multiple Linear Regression

## What this covers

How to move from a regression with one predictor to a regression with several, and how to write
and solve the resulting least-squares problem in vector and matrix form. It assumes the single-
predictor model $y = \beta_0 + \beta_1 x + \epsilon$ and the idea of fitting it by least squares;
what's new here is the bookkeeping that lets the same idea handle any number of predictors at once.

## From one predictor to several

The simple linear regression model has two parameters, an intercept and a slope:

$$y = \beta_0 + \beta_1 x + \epsilon.$$

Two standard examples: $y$ the height of an adult and $x$ the height of one of their parents, or
$y$ the price of chicken and $x$ time.

Often, though, more than one series plausibly drives $y$. *Multiple linear regression* extends the
model to $p$ predictors:

$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + w_i,$$

for observations $i = 1, \dots, n$. There are now $p+1$ coefficients $\beta_0, \dots, \beta_p$ to
estimate — one per predictor, plus the intercept.

## Writing it as a single inner product

The sum on the right is an inner product in disguise. Collect the predictors for observation $i$,
together with a leading $1$ for the intercept, into a vector

$$x_i = (1, x_{i1}, x_{i2}, \dots, x_{ip}),$$

and collect the coefficients into $\beta = (\beta_0, \beta_1, \dots, \beta_p)$. Prepending the $1$
is what lets the intercept ride along as an ordinary coefficient — it is the coefficient of a
predictor that is always $1$. The model becomes simply

$$y_i = x_i^\intercal \beta,$$

for each $i$, and estimation is the same least-squares problem regardless of how many predictors
there are:

$$\min_{\beta} \sum_{i=1}^n (y_i - x_i^\intercal \beta)^2.$$

Setting the derivative of this sum with respect to $\beta$ to zero gives the *normal equations*.
Differentiating $(y_i - x_i^\intercal\beta)^2$ term by term and summing contributes $-2x_i(y_i -
x_i^\intercal\beta)$ from each observation, so the stationary condition $\sum_i x_i(y_i -
x_i^\intercal \beta) = 0$ rearranges to $\left(\sum_i x_i x_i^\intercal\right)\beta = \sum_i x_i
y_i$, giving the estimate

$$\hat\beta = \left(\sum_{i=1}^n x_i x_i^\intercal\right)^{-1} \sum_{i=1}^n x_i y_i.$$

This is exactly the ordinary least-squares solution for simple linear regression, just written so
that it does not care how many predictors are packed into $x_i$.

## Matrix notation

The same problem is usually written by stacking the observations rather than summing over them.
Put the responses in a vector, the predictors in a matrix whose $i$-th row is $x_i$, and the
coefficients in a vector:

$$\underset{n\times 1}{y} = \underset{n \times p}{X}\ \underset{p \times 1}{\beta}, \qquad
y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}, \quad
X = \begin{bmatrix}
x_{11} & x_{12} & \cdots & x_{1p} \\
x_{21} & x_{22} & \cdots & x_{2p} \\
\vdots & & & \vdots \\
x_{n1} & x_{n2} & \cdots & x_{np}
\end{bmatrix}, \quad
\beta = \begin{bmatrix} \beta_1 \\ \beta_2 \\ \vdots \\ \beta_p \end{bmatrix}.$$

Here $n$ is the number of observations (for a time series, the number of time points) and $p$ is
the number of parameters. The columns of $X$ are the *features*. Least squares is now a single
matrix expression:

$$\min_{\beta \in \mathbb{R}^p} \lVert y - X\beta \rVert_2^2,$$

using the $\ell_2$ norm of a vector $a \in \mathbb{R}^d$, $\lVert a \rVert_2^2 = \sum_{i=1}^d
a_i^2$ — so the objective is again just the sum of squared residuals, one term per observation.
Solving gives the closed-form estimate

$$\underset{p\times 1}{\hat\beta} = \underset{p\times p}{(X^\intercal X)^{-1}}\ \underset{p\times
n}{X^\intercal}\ \underset{n \times 1}{y}.$$

This is the same $\hat\beta$ as above, just with the sums $\sum_i x_i x_i^\intercal$ and $\sum_i
x_i y_i$ written as the matrix products $X^\intercal X$ and $X^\intercal y$.

## When the solution exists

The formula needs $X^\intercal X$ to be invertible, which requires the columns of $X$ — the
features — to be linearly independent. That in turn requires $p \le n$: there can be no more
features than observations. If $p > n$, or if two features are collinear, $X^\intercal X$ is
singular and the formula breaks down. This case is not hopeless — it can be handled with
regularization — but that is a later topic, not covered here.

## The finger-tapping demo

The lecture's worked example was collected live in class rather than given as a dataset: a finger
tapping task, of the kind used clinically to assess fine motor speed, coordination and brain
function, in which the number of taps a person makes is recorded over a period of time. Two
questions organize looking at the resulting series: whether the tap rate stays roughly steady over
time, or whether it declines, showing fatigue. The class then discussed what external factors
might influence the tapping rate, and which of them would be sensible additional columns of $X$ in
a multiple regression model for the data — the demo motivates multiple regression by asking, for a
real series, which extra predictors are worth adding.

## Sources

- Slides: `07_multiple_linear_regression_notes`, parts 1–2 ("Simple and multiple linear
  regression", "Matrix notation"), Berkeley STAT 153, Spring 2026.
- No lecture transcript, written notes, or problem set were supplied for this lecture.
- The lecture's assigned reading, referred to but not contained in the supplied material: Chapter
  2 of Shumway and Stoffer.
- The finger-tapping data-collection website referenced in the slides
  (`stat153.berkeley.edu/spring-2026/lectures/07_finger-tap.html`) was not supplied, so its actual
  data and any fitted model are not reproduced here.

---

[← 5. OLS and MLE in Regression](05-ols-and-mle-in-regression.md) · [Contents](index.md) · [7. Sinusoidal Nonlinear Regression →](07-sinusoidal-nonlinear-regression.md)
