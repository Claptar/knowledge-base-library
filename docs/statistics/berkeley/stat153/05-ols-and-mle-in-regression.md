---
title: "5. OLS and MLE in Regression"
course: "Berkeley Stat 153 Fall 2024"
chapter: 5
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. OLS and MLE in Regression

## What this covers

This chapter finishes the treatment of simple linear regression begun in the previous lecture. It
answers two questions: why does minimizing the sum of squared errors produce the particular formulas
for the intercept and slope, and what happens if instead of minimizing squared error we ask for the
maximum-likelihood estimates under a normal-error model? It assumes the reader already has the model
$y = \beta_0 + \beta_1 x + \epsilon$ on the table, together with the idea of fitting a line to $(x_i, y_i)$
data, from the prior lecture (the reading for both is Chapter 2 of Shumway and Stoffer).

## The model and the least-squares criterion

The working model relates a response $y$ to a single covariate $x$ through two parameters, an intercept
and a slope, plus noise:

$$y = \beta_0 + \beta_1 x + \epsilon$$

Two examples fix the idea of what $x$ and $y$ can be: $y$ could be the height of an adult and $x$ the
height of their parent, or $y$ could be the price of chicken and $x$ time.

Ordinary least squares (OLS) chooses $\beta_0, \beta_1$ to minimize the sum of squared residuals between
the observed $y_i$ and the fitted value $\hat y_i = \beta_0 + \beta_1 x_i$:

$$Q = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$$

The minimizer is found the ordinary calculus way: differentiate $Q$ with respect to each parameter and
set both derivatives to zero.

## Deriving the OLS estimates

**The intercept.** Differentiating with respect to $\beta_0$:

$$
\begin{aligned}
\frac{\partial Q}{\partial \beta_0} &= \sum_{i=1}^n 2(y_i - \beta_0 - \beta_1 x_i)(-1) \\
&= 2\sum_{i=1}^n \beta_0 + 2\sum_{i=1}^n \beta_1 x_i - 2\sum_{i=1}^n y_i \\
&= 2n\beta_0 + 2n\beta_1 \bar{x} - 2n\bar{y}
\end{aligned}
$$

Setting this to zero and solving gives

$$\beta_0 = \bar{y} - \beta_1 \bar{x}.$$

So whatever the slope turns out to be, the fitted line is forced to pass through the point of averages
$(\bar x, \bar y)$.

**The slope.** Substitute that expression for $\beta_0$ back into $Q$ before differentiating with
respect to $\beta_1$ — this is what makes the second derivative tractable:

$$
\begin{aligned}
Q &= \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\\
&= \sum_{i=1}^n (y_i - \bar{y} + \beta_1 \bar{x} - \beta_1 x_i)^2\\
\frac{\partial Q}{\partial \beta_1} &= \sum_{i=1}^n 2\big(y_i - \bar{y}) + \beta_1(\bar{x}-x_i)\big\\
&= -2\sum_{i=1}^n (y_i-\bar{y})(x_i-\bar{x}) + 2\beta_1\sum_{i=1}^n (x_i - \bar{x})^2
\end{aligned}
$$

Setting this to zero and solving:

$$\beta_1 = \frac{\sum_{i=1}^n (y_i-\bar{y})(x_i-\bar{x})}{\sum_{i=1}^n (x_i-\bar{x})^2} = \frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)}.$$

This is worth pausing on: the least-squares slope is exactly the ratio of the sample covariance of $x$
and $y$ to the sample variance of $x$. Two practical points follow. First, this identity is why the sign
of $\beta_1$ always matches the sign of the covariance. Second, computing $\bar x$ and $\bar y$ here
means the *sample* mean taken across all the observed points — in a time-series setting such as the
chicken-price example there is only one observation per time point, so there is no way to average
"within" a point; the average is necessarily across the whole run of data.

## Maximum likelihood as an alternative route to the same estimates

Least squares needs no distributional assumption on the errors — it is a purely geometric criterion.
Maximum likelihood estimation (MLE) is a different starting point that does require one: assume the
errors are i.i.d. normal,

$$\epsilon_1, \dots, \epsilon_n \overset{\text{i.i.d.}}\sim N(0,\sigma^2),$$

which is the same as saying the responses are independent normals centered at the regression line,

$$y_i \overset{\text{independent}}\sim N(\beta_0 + \beta_1 x_i, \, \sigma^2).$$

The likelihood of the data is the product of the normal densities:

$$f_{y_1,\dots, y_n \mid \beta_0,\beta_1,\sigma}(y_1,\dots,y_n) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\,\sigma} \exp\!\left(-\frac{(y_i-\beta_0-\beta_1 x_i)^2}{2\sigma^2}\right).$$

Maximizing the likelihood is easier done on the log scale, since the product turns into a sum:

$$
\begin{aligned}
\log L &= \sum_{i=1}^n \log \frac{1}{\sqrt{2\pi}\sigma} -\sum_{i=1}^n\frac{(y_i-\beta_0-\beta_1 x_i)^2}{2\sigma^2}\\
&= -\frac{n}{2}\log(2\pi) - n\log\sigma - \frac{1}{2\sigma^2}\sum_{i=1}^n (y_i-\beta_0-\beta_1 x_i)^2.
\end{aligned}
$$

Write $S(\beta_0,\beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$ for the sum of squared errors —
this is exactly the $Q$ from the least-squares section, just with the parameters left free. Differentiate
the log-likelihood with respect to each of the three unknowns $\beta_0, \beta_1, \sigma$:

$$
\begin{aligned}
\frac{\partial}{\partial \beta_0} \log L &= -\frac{1}{2\sigma^2}\frac{\partial S}{\partial\beta_0} = 0 \implies \frac{\partial S}{\partial \beta_0}= 0, \\
\frac{\partial}{\partial \beta_1} \log L &= -\frac{1}{2\sigma^2}\frac{\partial S}{\partial\beta_1} = 0 \implies \frac{\partial S}{\partial \beta_1}= 0,\\
\frac{\partial}{\partial \sigma} \log L &= -\frac{n}{\sigma}+\frac{S(\beta_0, \beta_1)}{\sigma^3}=0 \implies \sigma = \sqrt{\frac{S(\beta_0, \beta_1)}{n}}.
\end{aligned}
$$

The first two equations are, up to the constant factor $-1/2\sigma^2$, the same stationarity conditions
as the OLS derivatives. That is the point of the exercise: under a normal-error model, maximizing the
likelihood over $\beta_0, \beta_1$ is the *same optimization problem* as minimizing the sum of squared
errors, so the MLE and OLS estimates of the regression coefficients coincide. What MLE adds is a third
equation, for the noise scale $\sigma$, which least squares has no way to produce on its own.

Plugging in the fitted $\hat\beta_0, \hat\beta_1$ gives the MLE estimate of $\sigma$:

$$\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{S(\hat{\beta}_0,\hat{\beta}_1)}{n}}, \qquad \hat{\sigma}^2_{\text{MLE}}=\frac{1}{n}S(\hat{\beta}_0,\hat{\beta}_1).$$

## The bias in $\hat\sigma^2_{\text{MLE}}$

Unlike the coefficient estimators $\hat\beta_0, \hat\beta_1$, which are unbiased, $\hat\sigma^2_{\text{MLE}}$
is a **biased** estimator of $\sigma^2$: dividing by $n$ systematically underestimates the true error
variance. The standard fix is to divide by $n-p$ instead of $n$, where $p$ is the number of parameters
already estimated from the data (here $p=2$, for $\beta_0$ and $\beta_1$):

$$\hat{\sigma}^2_{\text{unbiased}}=\frac{S(\hat{\beta}_0,\hat{\beta}_1)}{n-2}.$$

The intuition is that each estimated parameter "uses up" one degree of freedom: the residuals
$y_i - \hat\beta_0 - \hat\beta_1 x_i$ are not $n$ independent quantities once $\hat\beta_0$ and $\hat\beta_1$
have been fit to the same data, so the sum of their squares is, on average, smaller than it would be if
the true $\beta_0, \beta_1$ were known. Dividing by $n-2$ rather than $n$ corrects for this. The lecture
notes flag that this bias is worth watching via simulation, and that it resurfaces later when
regularization is introduced — both points to keep in mind going forward, though neither the simulation
nor the regularization discussion is contained in these notes. The immediate next step, also flagged but
not covered here, is extending the model from one covariate to several: multiple linear regression.

## A note on assumptions

It is worth being precise about which assumptions are doing the work at each stage. Fitting $\beta_0$
and $\beta_1$ by least squares requires **no assumption whatsoever** about the true relationship between
$x$ and $y$ — the model does not need to actually be linear for OLS to produce a fitted line, and that
line can still be useful for prediction or for interpretability even when it is not the "best" or most
correct description of the data-generating process. Linear models are often used simply because they are
convenient to interpret, not because they are asserted to be true.

The assumptions become necessary only at the next stage: if the goal is **inference** — confidence
intervals, hypothesis tests, or the maximum-likelihood machinery of the previous section — then
considerably more must be assumed, starting with the distributional assumption on the errors used above.
Point estimation and inference are not the same activity, and only the second one asks the model to be
believed.

## Sources

- Both derivations (OLS for $\beta_0, \beta_1$; the MLE argument and $\hat\sigma^2$ bias correction; the
  closing note on assumptions) are from the Lecture 6 notes of UC Berkeley Stat 153 (spring 2026),
  "Linear Regression Continued," reading Chapter 2 of Shumway and Stoffer.
- Primary source: `06_linear_regression_notes.md`, the lossless markdown conversion.
- Cross-checked against `Lec06_Notes.md`, a model's reconstruction of the original PDF (`Lec06_Notes.pdf`,
  Liberty Hamilton, Friday 6 February 2026); the two agree on every equation, so nothing here rests on an
  unverified reconstruction.
- Referred to but not contained in either file: the prior lecture's introduction of the two-parameter
  regression model (described here only as "last time"), the assigned reading itself (Shumway and
  Stoffer, Chapter 2), the simulation used in lecture to show the bias of $\hat\sigma^2_{\text{MLE}}$,
  and the following lecture's extension to multiple linear regression.
- No transcript, problem set, or additional notes were supplied for this lecture.

---

[← 4. Linear Regression for Time Series](04-linear-regression-for-time-series.md) · [Contents](index.md) · [6. Simple and Multiple Linear Regression →](06-simple-and-multiple-linear-regression.md)
