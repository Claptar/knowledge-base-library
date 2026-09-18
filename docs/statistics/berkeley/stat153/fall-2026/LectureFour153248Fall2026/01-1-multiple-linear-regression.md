---
title: 1 Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Multiple Linear Regression

## Lecture Four
Fall 2026, UC Berkeley

Aditya Guntuboyina

08 September 2026

We shall go over the main ideas behind frequentist and Bayesian inference in multiple linear regression.

In multiple linear regression, we have one response variable $y$ and $m$ covariates $x_1, \dots, x_m$ ($m = 1$ corresponds to simple linear regression). We observe data on $n$ instances or subjects for all these variables: $(y_i, x_{i1}, \dots, x_{im})$ for $i = 1, \dots, n$.

The following vector-matrix notation is very standard:

$$y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \qquad X = \begin{pmatrix} 1 & x_{11} & \dots & x_{1m} \\ 1 & x_{21} & \dots & x_{2m} \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ 1 & x_{n1} & \dots & x_{nm} \end{pmatrix}$$

Note the presence of the column of ones in the $X$-matrix. This notation is used not just to write formulae for linear regression, but also in code. For example, the OLS function in statsmodels uses the syntax `sm.OLS(y, X).fit()` to fit the linear regression model, where $y$ ($n \times 1$ vector) and $X$ ($n \times (m + 1)$ matrix) are defined above.

The multiple linear regression model (with normal errors) is given by:

$$y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im} + \epsilon_i \quad \text{with } \epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{1}$$

In the time series context, the model (1) arises in the following ways:

1. **Regression with functions of time:** Suppose we want to fit a quadratic function of time to the data. We can do this via the model (1) with $x_1$ being the time variable, and $x_2$ being the squared time i.e., $x_{i1} = i$ and $x_{i2} = i^2$. Suppose we want to fit a simple sinusoidal function to the data. We can do this via (1) with $x_{i1} = \cos(2\pi i/12)$ and $x_{i2} = \sin(2\pi i/12)$.

2. **AutoRegression (AR):** If we take $x_{ij} = y_{i-j}$, then we get the AR model:

$$y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_m y_{t-m} + \epsilon_t.$$

The idea here is that we are using the $m$ most recent values of the time series to predict the next observation. AR models are very commonly used and they work quite well for time series.

Let us focus for now on regression using functions of time. We shall study AutoRegression in detail later.

Our goal is to use the observed data (in $y, X$) to obtain estimates along with uncertainty interals for the parameters $\beta_0, \dots, \beta_m$. There are two broad principles for doing this: frequentist and Bayesian.

---

[Up: contents](index.md) · [2 Frequentist Inference for Linear Regression →](02-2-frequentist-inference-for-linear-regression.md)
