---
title: 2 Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Multiple Linear Regression

In multiple linear regression, we have one response variable $y$ and $m$ covariates $x_1, \dots, x_m$ ($m = 1$ corresponds to simple linear regression). We observe data on $n$ instances or subjects for all these variables: $(y_i, x_{i1}, \dots, x_{im})$ for $i = 1, \dots, n$. The multiple linear regression model (with normal errors) is given by:
$$
y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im} + \epsilon_i \quad \text{with } \epsilon_i \stackrel{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{4}
$$
In the time series context, the model (4) arises in the following ways:

1. **Regression with functions of time:** Suppose we want to fit a quadratic function of time to the data. We can do this via the model (4) with $x_1$ being the time variable, and $x_2$ being the squared time i.e., $x_{i1} = i$ and $x_{i2} = i^2$. Suppose we want to fit a simple sinusoidal function to the data. We can do this via (4) with $x_{i1} = \cos(2\pi i/12)$ and $x_{i2} = \sin(2\pi i/12)$.

2. **AutoRegression (AR):** If we take $x_{ij} = y_{i-j}$, then we get the AR model:
$$
y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_m y_{t-m} + \epsilon_t.
$$
The idea here is that we are using the $m$ most recent values of the time series to predict the next observation. AR models are very commonly used and they work quite well for time series.

In Bayesian inference for (4), we work with the prior
$$
\beta_0, \beta_1, \dots, \beta_m, \log \sigma \stackrel{\text{i.i.d}}{\sim} \text{unif}(-C, C)
$$
for a very large positive $C$. The joint posterior density of $\beta_0, \dots, \beta_m, \sigma$ is then given by
$$
f_{\beta_0, \beta_1, \dots, \beta_m, \sigma|\text{data}}(\beta_0, \beta_1, \dots, \beta_m, \sigma) \propto \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \dots, \beta_m)}{2\sigma^2} \right) I\{-C < \beta_0, \beta_1, \dots, \beta_m, \log \sigma < C\}.
$$
where we use the notation
$$
S(\beta_0, \beta_1, \dots, \beta_m) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2
$$
for the sum of squares.

The posterior over only the coefficient parameters $\beta_0, \beta_1$ can be obtained by integrating (or marginalizing) the parameter $\sigma$.
$$
\begin{aligned}
&f_{\beta_0, \beta_1, \dots, \beta_m|\text{data}}(\beta_0, \beta_1, \dots, \beta_m) \\
&= \int f_{\beta_0, \beta_1, \dots, \beta_m, \sigma|\text{data}}(\beta_0, \beta_1, \dots, \beta_m, \sigma) d\sigma \\
&\propto I\{-C < \beta_0, \beta_1, \dots, \beta_m < C\} \int_{e^{-C}}^{e^C} \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \dots, \beta_m)}{2\sigma^2} \right) d\sigma \\
&\approx I\{-C < \beta_0, \beta_1, \dots, \beta_m < C\} \int_0^{\infty} \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \dots, \beta_m)}{2\sigma^2} \right) d\sigma \\
&= I\{-C < \beta_0, \beta_1, \dots, \beta_m < C\} \left( \frac{1}{S(\beta_0, \dots, \beta_m)} \right)^{n/2} \int_0^{\infty} s^{-n-1} \exp \left( -\frac{1}{2s^2} \right) ds \\
&\propto I\{-C < \beta_0, \beta_1, \dots, \beta_m < C\} \left( \frac{1}{S(\beta_0, \dots, \beta_m)} \right)^{n/2} \\
&\approx \left( \frac{1}{S(\beta_0, \dots, \beta_m)} \right)^{n/2} \propto \left( \frac{S(\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_m)}{S(\beta_0, \beta_1, \dots, \beta_m)} \right)^{n/2}
\end{aligned}
$$
where $\hat{\beta}_0, \dots, \hat{\beta}_m$ denote the least squares estimators of $\beta_0, \dots, \beta_m$ (i.e., $(\hat{\beta}_0, \dots, \hat{\beta}_m)$ minimizes $S(\beta_0, \dots, \beta_m)$ over all values of $\beta_0, \dots, \beta_m$).

Our posterior density for $\beta_0, \dots, \beta_m$ is thus:
$$
f_{\beta_0, \beta_1, \dots, \beta_m|\text{data}}(\beta_0, \beta_1, \dots, \beta_m) \propto \left( \frac{S(\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_m)}{S(\beta_0, \beta_1, \dots, \beta_m)} \right)^{n/2}. \tag{5}
$$
Now we will explain why this is a multivariate $t$-density.

## 3 Why is (5) a $t$-density?

If you go to the wikipedia page (https://en.wikipedia.org/wiki/Multivariate_t-distribution) for Multivariate $t$-distribution, it gives the following formula for the density:
$$
\begin{aligned}
f(x) &:= \frac{\Gamma((\nu + p)/2)}{\Gamma(\nu/2) \nu^{p/2} \pi^{p/2} \sqrt{\det \Sigma}} \left[ 1 + \frac{1}{\nu} (x - \mu)^T \Sigma^{-1} (x - \mu) \right]^{-(\nu+p)/2} \\
&\propto \left[ 1 + \frac{1}{\nu} (x - \mu)^T \Sigma^{-1} (x - \mu) \right]^{-(\nu+p)/2}.
\end{aligned} \tag{6}
$$
Their notation for this distribution is $t_p(\mu, \Sigma, \nu)$ where:

1. $p$ denotes dimension of the vector $x$ (this is a $p$-variate joint density)
2. $\mu$ is a $p \times 1$ vector called the location
3. $\Sigma$ is a $p \times p$ matrix called the scale matrix
4. $\nu > 0$ denotes the degrees of freedom.

It turns out that (5) is a special case of (6) for some $p, \mu, \Sigma, \nu$. To see this, we need to first rewrite (5) using matrix notation which we do in the next section.

---

[← 1 Bayesian Inference for Simple Linear Regression](01-1-bayesian-inference-for-simple-linear-regression.md) · [Up: contents](index.md) · [4 Matrix Notation for Multiple Linear Regression →](03-4-matrix-notation-for-multiple-linear-regression.md)
