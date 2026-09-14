---
title: Estimation of $\beta0$ and $\beta1$
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureTwo153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureTwo153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Estimation of $\beta0$ and $\beta1$

**Source:** [`LectureTwo153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureTwo153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

## Least Squares Estimates {#least-squares-estimates}

The estimates of $\beta_0$ and $\beta_1$ reported by standard libraries (such as `statsmodels`) are obtained using the method of least squares. This involves minimizing the sum of squares criterion: $$\begin{equation}
\label{ss}
  S(\beta_0, \beta_1) = \sum_{i=1}^n \left(y_i - \beta_0 - \beta_1 x_i
  \right)^2
\end{equation}$$ over all values of $\beta_0$ and $\beta_1$. It is left as an exercise to verify that: $$\begin{equation*}
  \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}  ~~ \text{ and } ~~
  \hat{\beta}_1 = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i -
    \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2},
\end{equation*}$$ where $$\begin{equation*}
  \bar{y} = \frac{y_1 + \dots + y_n}{n} ~~ \text{ and } ~~   \bar{x} =
  \frac{x_1 + \dots + x_n}{n}.
\end{equation*}$$

## MLE under Normality of Errors {#mle-under-normality-of-errors}

Suppose we assume that the error terms $\epsilon_1, \dots, \epsilon_n$ in <a href="#linmod" data-reference-type="eqref" data-reference="linmod">[linmod]</a> are i.i.d normal with mean zero and some variance $\sigma^2$: $$\begin{equation}
\label{errgauss}
 \epsilon_1, \dots, \epsilon_n \overset{\text{i.i.d}}{\sim} N(0,
 \sigma^2).
\end{equation}$$ Then the least squares estimates of $\beta_0$ and $\beta_1$ coincide with the Maximum Likelihood Estimates (MLEs).

Another way of writing the model <a href="#linmod" data-reference-type="eqref" data-reference="linmod">[linmod]</a> and <a href="#errgauss" data-reference-type="eqref" data-reference="errgauss">[errgauss]</a> is: $$\begin{equation*}
  y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_i,
  \sigma^2).
\end{equation*}$$ To obtain the MLEs of the parameters ($\beta_0, \beta_1$ as well as $\sigma$), we need to write the likelihood function and then maximize it. The likelihood function is the joint density of the data for fixed values of the parameters $\beta_0, \beta_1, \sigma$: $$\begin{align}
  f_{y_1, \dots, y_n \mid \beta_0, \beta_1, \sigma}(y_1, \dots, y_n) &=
  \prod_{i=1}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_i -
                                                                       \beta_0
                                                                       -
                                                                       \beta_1
                                                                       x_i)^2}{2
                                                                       \sigma^2}
                                                                       \right)
  \nonumber \\
  &= (2 \pi)^{-n/2} \sigma^{-n} \exp \left(-\frac{1}{2 \sigma^2}
    \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \right) \nonumber \\
  &= (2 \pi)^{-n/2} \sigma^{-n} \exp \left(-\frac{S(\beta_0,
    \beta_1)}{2 \sigma^2} \right) \label{like}
\end{align}$$ where $S(\beta_0, \beta_1)$ is the sum of squares <a href="#ss" data-reference-type="eqref" data-reference="ss">[ss]</a>. $$\begin{equation*}
  S(\beta_0, \beta_1) :=
    \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.
\end{equation*}$$ To write this likelihood, we are assuming that $x_1, \dots, x_n$ are fixed. This assumption is fine if $x_i = i$ (regression with time as covariate) but not strictly true when $x_i = y_{i-1}$ (auto-regression). We shall see how it is still approximately true in the case of AutoRegression later.

Maximization of the likelihood is a three variable optimization problem (the variables being $\beta_0, \beta_1, \sigma$). The optimal values of $\beta_0$ and $\beta_1$ in this problem coincide with the least squares estimate. We shall see why in the next lecture.

---

[← Simple Linear Regression](01-simple-linear-regression.md) · [Up: contents](index.md)
