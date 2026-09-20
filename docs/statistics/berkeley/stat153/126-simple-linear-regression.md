---
title: "126. Simple Linear Regression"
course: "Berkeley Stat 153 Fall 2024"
chapter: 126
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 126. Simple Linear Regression

## What this covers

This chapter opens Stat 153's unit on regression: the simple linear regression model with one
covariate, how its parameters are fit by least squares and by maximum likelihood, and how both a
frequentist and a Bayesian machinery turn those fits into confidence statements. It assumes only
that you can work with joint densities, the normal distribution, and — for the inference sections —
the chi-squared and $t$ distributions; nothing about time series itself is assumed yet, since this
is the general-purpose toolkit that the course's later treatment of autoregression will reuse. Two
calculus derivations that the lecture leaves as exercises are collected at the end so you can do
them yourself.

## From a single series to a regression problem

Regression relates a response variable $y$ to a covariate $x$, and needs data on both. A time
series, though, is just one variable observed over time: $y_1, \dots, y_n$, with no covariate in
sight. To bring regression to bear on it, a covariate has to be manufactured, and there are two
standard ways of doing it.

1. **Time as covariate.** Take the time index itself as $x$: $x_i = i$. For instance, in a monthly
   series of the US population from January 1959 to December 2024, $y_i$ is the population figure
   for the $i$-th month and $x_i = i$.
2. **Lagged $y$ as covariate.** Take $x_i = y_{i-1}$ — the covariate is the series' own previous
   value. This is called lagged regression, or more commonly **autoregression**.

This chapter develops the machinery using time as the covariate; autoregression is treated later,
once the machinery below is in hand. One assumption worth flagging now: everything that follows
treats the covariate values $x_1, \dots, x_n$ as fixed, known numbers rather than random variables.
That is exactly true when $x_i = i$, but not strictly true when $x_i = y_{i-1}$, since then the
covariate is itself part of the random data. The course returns later to why the same machinery
still applies, approximately, in the autoregressive case.

## The model

The simple linear regression model assumes
$$
y = \beta_0 + \beta_1 x + \epsilon,
$$
where $\epsilon$ is an error term absorbing whatever $y$ does that isn't captured by the straight
line $\beta_0 + \beta_1 x$. The classic example that gives the method its name: $y$ the height of an
adult man, $x$ the height of his father. Read the parameters directly off the equation: $\beta_0$
is the value of $y$ when $x = 0$, and $\beta_1$ is the change in $y$ per unit change in $x$.

Given data $(x_1, y_1), \dots, (x_n, y_n)$, write the equation once per observation:
$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i.
$$
Treating $x_1, \dots, x_n$ as fixed, and assuming the errors are independent and identically
distributed as $\epsilon_i \sim N(0, \sigma^2)$, the model is equivalently
$$
y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_i, \sigma^2).
$$
There are three unknown parameters: $\beta_0$, $\beta_1$, $\sigma^2$. Fitting the model means
producing estimates $\hat\beta_0, \hat\beta_1$ (and quantifying how uncertain they are) from the
data; prediction at a new covariate value $x_{\text{new}}$ is then $\hat\beta_0 + \hat\beta_1
x_{\text{new}}$.

## Fitting by least squares

The estimates that packages such as Python's `statsmodels` report are the ones minimizing the sum
of squared errors,
$$
S(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2,
$$
over all choices of $\beta_0, \beta_1$. Minimizing $S$ gives
$$
\hat\beta_1 = \frac{\sum_{i=1}^n (y_i - \bar y)(x_i - \bar x)}{\sum_{i=1}^n (x_i - \bar x)^2},
\qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x,
$$
where $\bar x = \frac1n \sum_i x_i$ and $\bar y = \frac1n \sum_i y_i$ are the sample means.
(Deriving these two formulas from $S$ is the first exercise below.)

## The likelihood, and why least squares is also maximum likelihood

Add the distributional assumption $\epsilon_1, \dots, \epsilon_n \overset{\text{iid}}{\sim} N(0,
\sigma^2)$, and the least-squares estimates turn out to coincide with the maximum likelihood
estimates. To see why, write down the likelihood — the joint density of the data, viewed as a
function of the parameters:
$$
\begin{aligned}
f_{y_1,\dots,y_n \mid \beta_0,\beta_1,\sigma}(y_1,\dots,y_n)
&= \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{(y_i-\beta_0-\beta_1x_i)^2}{2\sigma^2}\right)\\
&= (2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i-\beta_0-\beta_1x_i)^2\right)\\
&= (2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{S(\beta_0,\beta_1)}{2\sigma^2}\right).
\end{aligned}
$$
For a fixed $\sigma$, this expression is a strictly decreasing function of $S(\beta_0, \beta_1)$ —
the bigger the sum of squares, the smaller the exponential. So whatever $\sigma$ is, the $\beta_0,
\beta_1$ that maximize the likelihood are exactly the ones that minimize $S$: the same $\hat\beta_0,
\hat\beta_1$ as before. That is the entire content of "least squares is maximum likelihood under
Gaussian errors" — it falls out of the exponent, not from anything special about squares.

(This is also why the algebra works out cleanly when $x_1, \dots, x_n$ are treated as fixed: the
likelihood above is a density in $y_1, \dots, y_n$ only, for given $x_i$'s.)

## Estimating $\sigma$: the frequentist route

Maximizing the likelihood over all three parameters at once is a three-variable optimization
problem, but it splits into two easy stages:

1. For fixed $\sigma$, maximize over $\beta_0, \beta_1$ — as above, this is equivalent to
   minimizing $S(\beta_0, \beta_1)$, giving $\hat\beta_0, \hat\beta_1$ regardless of what $\sigma$
   turns out to be.
2. Substitute those values into the likelihood and maximize the resulting one-variable function
   of $\sigma$.

Carrying out step 2 (the second exercise below) gives
$$
\hat\sigma_{\text{MLE}} = \sqrt{\frac{S(\hat\beta_0, \hat\beta_1)}{n}}.
$$

Point estimates alone don't quantify uncertainty; for that we need the sampling distributions of
$\hat\beta_0, \hat\beta_1, \hat\sigma$, and these can be worked out in closed form. For the slope,
$$
\hat\beta_1 = \frac{\sum_i (y_i - \bar y)(x_i - \bar x)}{\sum_i (x_i - \bar x)^2}
= \frac{\sum_i y_i (x_i - \bar x)}{\sum_i (x_i - \bar x)^2}
\sim N\left(\beta_1, \frac{\sigma^2}{\sum_i (x_i - \bar x)^2}\right),
$$
which is normal because it is a linear combination of the independent normal $y_i$'s. Jointly,
$\hat\beta_0$ and $\hat\beta_1$ are bivariate normal:
$$
\begin{pmatrix}\hat\beta_0\\ \hat\beta_1\end{pmatrix} \sim
N\left(\begin{pmatrix}\beta_0\\ \beta_1\end{pmatrix}, \
\frac{\sigma^2}{n\sum_i (x_i-\bar x)^2}
\begin{pmatrix}\sum_i x_i^2 & -\sum_i x_i\\ -\sum_i x_i & n\end{pmatrix}\right).
$$
(These are easier to derive once the model is written in matrix form, which is how the course
handles multiple regression, the following week's topic.)

The variance estimate has a chi-squared distribution:
$$
\frac{n\hat\sigma^2_{\text{MLE}}}{\sigma^2} \sim \chi^2_{n-2}.
$$
Since a $\chi^2_{n-2}$ variable has mean $n-2$, taking expectations gives $\mathbb E\,
\hat\sigma^2_{\text{MLE}} = \sigma^2 \frac{n-2}{n}$ — the MLE for $\sigma^2$ is biased downward,
unlike $\hat\beta_0, \hat\beta_1$, which are unbiased. The bias is easy to remove:
$$
\hat\sigma^2_{\text{unbiased}} = \frac{n}{n-2}\hat\sigma^2_{\text{MLE}}
= \frac{S(\hat\beta_0, \hat\beta_1)}{n-2},
$$
and it is this corrected version, not $\hat\sigma_{\text{MLE}}$, that gets used in practice (note
that only its square is unbiased for $\sigma^2$ — $\hat\sigma_{\text{unbiased}}$ itself is not
unbiased for $\sigma$).

$(\hat\beta_0, \hat\beta_1)$ and $\hat\sigma^2_{\text{unbiased}}$ turn out to be independent.
Combined with the two facts above, that independence gives a confidence interval for $\beta_1$.
Standardizing with the true $\sigma$ gives a standard normal pivot; replacing $\sigma$ by its
estimate turns it into a $t$-distributed pivot:
$$
\frac{\hat\beta_1 - \beta_1}{\sigma}\sqrt{\sum_i (x_i - \bar x)^2} \sim N(0, 1),
\qquad
\frac{\hat\beta_1 - \beta_1}{\hat\sigma}\sqrt{\sum_i (x_i - \bar x)^2} \sim t_{n-2}.
$$
Inverting the second gives the confidence interval
$$
\left[\hat\beta_1 - \frac{\hat\sigma_{\text{unbiased}}}{\sqrt{\sum_i (x_i - \bar x)^2}}\,
t_{n-2,\alpha/2},\ \ \hat\beta_1 + \frac{\hat\sigma_{\text{unbiased}}}{\sqrt{\sum_i (x_i - \bar
x)^2}}\, t_{n-2,\alpha/2}\right],
$$
where $t_{n-2,\alpha/2}$ is the point with $\mathbb P\{t_{n-2} \ge t_{n-2,\alpha/2}\} = \alpha/2$.

## Bayesian inference

The frequentist route treats $\beta_0, \beta_1, \sigma$ as fixed unknowns and studies the sampling
distribution of the estimators. The Bayesian route instead puts a prior distribution on the
parameters and updates it with the data — and, remarkably, ends up at the same point estimates by
a completely different route.

A prior meant to reflect ignorance takes $\beta_0$, $\beta_1$ and $\log\sigma$ to be independent
and uniform over a wide range $(-C, C)$, for some large constant $C$ whose exact value won't matter
once the calculation is done:
$$
\beta_0,\ \beta_1,\ \log\sigma \overset{\text{iid}}{\sim} \text{Unif}(-C, C).
$$
The uniform assumption is put on $\log\sigma$ rather than $\sigma$ itself because $\sigma$ has to
be positive; by the change-of-variables formula, this induces the density
$$
f_\sigma(x) = f_{\log\sigma}(\log x)\cdot \frac1x
= \frac{\mathbb I\{-C < \log x < C\}}{2Cx}
= \frac{\mathbb I\{e^{-C} < x < e^C\}}{2Cx}
$$
on $\sigma$ directly.

The posterior is proportional to likelihood times prior. The likelihood, keeping only the terms
that depend on the parameters, is
$$
f_{y_1,\dots,y_n \mid \beta_0,\beta_1,\sigma}(y_1,\dots,y_n) \propto
\sigma^{-n}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right),
$$
and the prior, written out and simplified, is
$$
f_{\beta_0,\beta_1,\sigma}(\beta_0,\beta_1,\sigma) \propto \frac1\sigma\,
\mathbb I\{-C < \beta_0, \beta_1, \log\sigma < C\}.
$$
Multiplying the two gives the joint posterior over all three parameters:
$$
f_{\beta_0,\beta_1,\sigma \mid \text{data}}(\beta_0,\beta_1,\sigma) \propto
\sigma^{-n-1}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right)
\mathbb I\{-C < \beta_0, \beta_1, \log\sigma < C\}.
$$
This is a posterior over three parameters at once; what's usually wanted is the posterior over
$\beta_0, \beta_1$ alone, obtained by integrating $\sigma$ out. That marginalization — and the
comparison with the frequentist confidence interval above — is where the lecture leaves off.

## Exercises

1. Minimize $S(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$ over $\beta_0,
   \beta_1$ (for instance by setting both partial derivatives to zero) to verify
   $$
   \hat\beta_1 = \frac{\sum_{i=1}^n (y_i - \bar y)(x_i - \bar x)}{\sum_{i=1}^n (x_i - \bar x)^2},
   \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x.
   $$
2. With $\beta_0, \beta_1$ fixed at their least-squares values $\hat\beta_0, \hat\beta_1$, maximize
   $$
   (2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{S(\hat\beta_0, \hat\beta_1)}{2\sigma^2}\right)
   $$
   over $\sigma$, and show that the maximizer is $\hat\sigma_{\text{MLE}} =
   \sqrt{S(\hat\beta_0, \hat\beta_1)/n}$.

## Sources

Berkeley Stat 153 (time series), Lecture 2 — "Simple Linear Regression" / "Estimation of
$\beta_0$ and $\beta_1$" / "Frequentist Inference" / "Bayesian Inference" — appears across three
course offerings; this chapter merges them, taking the fullest treatment of each part rather than
repeating overlap:

- **Fall 2026** — `01-simple-linear-regression.md`, `02-estimation-of-and.md` (pandoc conversion of
  the lecture's `.tex` source, high fidelity). Source of the "time as covariate vs. lagged-$y$ as
  covariate" framing and the note that the fixed-$x$ assumption is only approximate for
  autoregression.
- **Fall 2025** — `01-1-simple-linear-regression.md`, `02-2-estimation-of-and.md` (same lecture,
  LLM-reconstructed from a PDF with no text layer; used only to confirm the Fall 2026 `.tex`
  version, since its own equations are marked unverified).
- **Spring 2025** — `01-1-simple-linear-regression.md`, `02-2-frequentist-inference.md`,
  `03-3-bayesian-inference.md` (LLM-reconstructed from a PDF). The fullest of the three, and the
  source of the model setup, the likelihood derivation, the frequentist-inference section (MLE for
  $\sigma$, sampling distributions, the confidence interval for $\beta_1$), and the
  Bayesian-inference section (prior, posterior).

Referred to but not contained in any of the supplied lectures, and so not covered here: the
matrix-notation derivation of the joint distribution of $(\hat\beta_0, \hat\beta_1)$ (deferred by
the lecturer to the multiple-regression lecture the following week), the marginal posterior of
$\beta_0, \beta_1$ obtained by integrating out $\sigma$ (deferred to "the next lecture"), and the
treatment of autoregression itself.

---

[← 125. Stationary Solutions of AR(p)](125-stationary-solutions-of-ar-p.md) · [Contents](index.md) · [127. Evaluating Forecasting Hub Performance →](127-evaluating-forecasting-hub-performance.md)
