---
title: Linear Regression with Time as a Covariate
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureThree153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Linear Regression with Time as a Covariate

**Source:** [`LectureThree153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Suppose $y_1, \dots, y_n$ is a time series. We want to decompose this time series as $$\begin{align*}
  y_i = \beta_0 + \beta_1 x_i + \epsilon_i
\end{align*}$$ where $x_i$ is known. The simplest example is $x_i = i$; this corresponds to regression with time as covariate. The analysis also works when $x_i = y_{i-1}$ as in lagged regression but we shall study this later. There are $n+2$ unknowns here: $\beta_0, \beta_1$ and $\epsilon_1, \dots, \epsilon_n$. The goal is to figure them out from the $n$ known observations $y_1, \dots, y_n$.

We make the following modeling assumptions: $$\begin{align*}
  \beta_0 \sim \text{Unif}(-C, C) ~~ \beta_1 \sim \text{Unif}(-C, C)
  ~~ \epsilon_1, \dots, \epsilon_n \mid \sigma
  \overset{\text{i.i.d}}{\sim} N(0, \sigma^2) ~~ \log \sigma \sim
  \text{Unif}(-C, C).
\end{align*}$$ Our interest is usually in $\beta_0, \beta_1$. So we aim to calculate the conditional density of $(\beta_0, \beta_1)$ given $y_1, \dots,
y_n$. We do this by first calculating the density of $(\beta_0,
\beta_1, \sigma)$ given $y_1, \dots, y_n$, and then integrating out $\sigma$. By Bayes rule, $$\begin{align*}
  &f_{\beta_0,\beta_1,\sigma\mid y_1,\ldots,y_n}
  (\beta_0,\beta_1,\sigma) \\
  &\qquad\propto
  \left\{\prod_{i=1}^n
  \frac{1}{\sqrt{2\pi}\sigma}
  \exp\left[-\frac{(y_i-\beta_0-\beta_1x_i)^2}{2\sigma^2}\right]
  \right\}
  \frac{I\{-C<\beta_0<C\}}{2C}
  \frac{I\{-C<\beta_1<C\}}{2C} \\
  &\qquad\quad\times
  \frac{ I\{-C<\log\sigma<C\}}{2C\sigma} \\
  &\qquad\propto \sigma^{-(n+1)}
  \exp\left\{-\frac{S(\beta_0,\beta_1)}{2\sigma^2}\right\} I\{\sigma >
    0\},
\end{align*}$$ where $$\begin{align*}
  S(\beta_0,\beta_1) =\sum_{i=1}^n(y_i-\beta_0-\beta_1x_i)^2
\end{align*}$$ is the sum of squares, and we have ignored the indicator $I\{-C <
\beta_0 < C\}$, $I\{-C <
\beta_1 < C\}$ and replaced the indicator $I\{e^{-C} < \sigma < e^C\}$ by $I\{\sigma > 0\}$.

As in the previous two sections, integrating out $\sigma$ gives $$\begin{align*}
  f_{\beta_0,\beta_1\mid y_1,\ldots,y_n}
  (\beta_0,\beta_1\mid y_1,\ldots,y_n)
  &\propto
  \left\{\frac{1}{S(\beta_0,\beta_1)}\right\}^{n/2}.
\end{align*}$$ We will discuss in the next lecture that this is a multivariate $t$-distribution with $n-2$ degrees of freedom. It is centered at the least squares estimators of $\beta_0$ and $\beta_1$.

---

[← Question 4: Several Measurements of One Quantity](05-question-4-several-measurements-of-one-quantity.md) · [Up: contents](index.md)
