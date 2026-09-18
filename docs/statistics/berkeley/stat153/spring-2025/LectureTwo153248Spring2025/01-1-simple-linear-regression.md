---
title: 1 Simple Linear Regression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Simple Linear Regression

## Lecture Two
### Spring 2025, UC Berkeley

### Aditya Guntuboyina

### January 23, 2025

We shall start the first topic of the course: Linear Regression. We shall discuss both frequentist and Bayesian approaches for linear regression. Both approaches end up with identical solutions even though they use very different ideas. We start our discussion with simple linear regression (where there is a single covariate), and then extend to multiple linear regression (where there are multiple covariates).

We observe data $(x_1, y_1), \dots, (x_n, y_n)$. $x_i$ denotes the covariate value and $y_i$ denotes the response value for the $i^{\text{th}}$ observation. In the time series context, in our initial applications, we shall apply linear regression with time as the covariate. For example, in the time series dataset on the population of the United States for each month from January 1959 to December 2024: $n$ denotes the total number of data points, $x_i = i$ and $y_i$ denotes the observed population data for the $i^{\text{th}}$ month (first month is January 1959, second month is February 1959 and so on).

In the linear regression model, it is assumed that $x_1, \dots, x_n$ are fixed deterministic values, and that the response values $y_1, \dots, y_n$ satisfy the model equation:
$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i \quad \text{with } \epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2).
$$
Another way of writing the model is:
$$
y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_i, \sigma^2).
$$
There are three parameters in this model: $\beta_0, \beta_1$ and $\sigma^2$.

We discuss frequentist and Bayesian approaches for estimating the parameters (as well as uncertainty quantification) from the observed data. A key role in both approaches will be played by the likelihood function which is the joint density of the observations given the parameter values. The likelihood function is given by:
$$
\begin{aligned}
f_{y_1, \dots, y_n \mid \beta_0, \beta_1, \sigma}(y_1, \dots, y_n) &= \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2}\right) \\
&= (2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right) \\
&= (2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right)
\end{aligned}
\tag{1}
$$
where
$$
S(\beta_0, \beta_1) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.
$$
Note again that we are assuming that $x_1, \dots, x_n$ are fixed.

---

[Up: contents](index.md) · [2 Frequentist Inference →](02-2-frequentist-inference.md)
