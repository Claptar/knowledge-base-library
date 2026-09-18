---
title: Stat 248 - Homework 1 - YOUR NAME HERE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat 248 - Homework 1 - YOUR NAME HERE

## Student ID: {-}

## Collaborated with: {-}

Due Feb 10 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

*Instructions:* Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

## Q1. Autocovariance, autocorrelation, and stationarity {-}

Let $w_t$ be i.i.d. with $\mathbb{E}[w_t]=0$ and $\operatorname{Var}(w_t)=\sigma^2<\infty$.

(a) Show that $\gamma_w(h) = \operatorname{Cov}(w_t, w_{t+h})=0$ for all $h\neq 0$, and $\gamma_w(0)=\sigma^2$. (2 points)

(b) Show that the autocorrelation function $\rho_w(h)=0$ for all $h \neq 0$. (2 points)

(c) Explain why $w_t$ is weakly stationary. Is it also *strictly stationary*? If so, why? (2 points)

## Q2. Data simulation {-}

(a) Write two separate python functions to simulate two time series of length $T=500$: (1) Gaussian white noise, (2) an autoregressive process defined by $x_t = 0.5 x_{t-1} + w_t$ where $w_t$ is Gaussian white noise with $\sigma_w=1$. (2 points)

(b) Compute and plot the sample autocorrelation function for up to lag 40 for each time series. Be sure to label your x and y axes appropriately. (2 points)

(c) For each time series, estimate $\gamma(1)$ using the formula

$$\hat{\gamma}(1) = \frac{1}{T}\displaystyle\sum_{t=1}^{T-1}(x_t-\bar{x})(x_{t+1}-\bar{x})$$

and report the value for each case (2 points).

(d) Apply the moving average filter $v_t=\frac{1}{4}(x_t+x_{t-1}+x_{t-2}+x_{t-3})$ to the data generated from the autoregressive process you generated previously. How does the moving average affect the signal? (2 points)

## Q3. Correlation and independence {-}

Give an example of two random variables that are uncorrelated but not independent. Prove that they are uncorrelated but not independent. (2 points)

## Q4. Random walk with drift {-}

Write some python code to simulate 100 random walks each of length 500, with nonzero drift, and plot them on the same plot using transparent coloring (you should be able to use your labs to help). Calculate the sample mean $\hat{\mu}_t$ at each time $t$ across the repetitions, and plot as a dark line on the same plot. Then, calculate the sample standard deviation $\sigma_t$ at each $t$, and plot the mean plus or minus one standard deviation as dark dotted lines on the same plot. Describe what you see related to the mean and variance over time. (5 points)

## Q5. Stationarity {-}

Compute the mean, variance, auto-covariance, and auto-correlation functions for the process $$x_t = w_t w_{t-2}$$ where each $w_t \sim N(0,\sigma^2)$ independently. Is $x_t$ stationary? (5 points)

## Q6. Theoretical and sample ACF {-}

(a) Simulate a series of $n=500$ Gaussian white noise observations and compute the sample ACF, $\hat{\rho}(h)$, to lag 20. Compare the sample ACF you obtain to the actual ACF, $\rho(h)$. (2 points)

(b) Repeat part (a) using only $n =50$. How does changing $n$ aﬀect the results? (2 points)

## Q7. Random walk and a trend stationary process {-}

(a) Write a python function to generate six series that are random walk with drift, of length $n =100$ with $\delta=0.1$ and $\sigma_w =1$. Call the data $x_t$ for $t =1,\dots,100$. Fit the regression $x_t = \beta t + w_t$ using least squares. Plot the data, the true mean function (i.e., $\hat{μ}(t) = 0.1 t$) and the fitted line, $\hat{x}(t) = \beta t$, on the same graph.  (3 points)

(b) Write a python function to generate six series of length $n =100$ that are linear trend plus noise, for example $y_t =0.1 t + w_t$, where $t$ and $w_t$ are as in part (a). Fit the regression $y_t = \beta t +w_t$ using least squares. Plot the data, the true mean function (i.e., $\hat{μ}(t) = 0.1 t$) and the fitted line, $\hat{y}(t) = \beta t$, on the same graph.  (3 points)

(c) Comment on what differences you notice between these. (2 points)

## Q8. Linear trends and stationarity {-}

Consider a process consisting of a linear trend with an additive noise term consisting of independent random variables $w_t$ with zero means and variances $\sigma^2_w$, that is, $x_t = \beta_0 +\beta_1 t + w_t$, where $\beta_0, \beta_1$ are fixed constants.

(a) Prove $x_t$ is nonstationary. (1 point)

(b) Prove that the first diﬀerence series $\nabla x_t = x_t− x_{t−1}$ is stationary by finding its mean and autocovariance function. (2 points)

(c) Repeat part (b) if $w_t$ is replaced by a general stationary process, say $y_t$, with mean function $\mu_y$ and autocovariance function $\gamma_y(h)$. (2 points)

## Q9. Auto- and cross-correlation for brain data {-}

(a) Following the code used in Lab 2, calculate and plot the autocorrelation functions for the fMRI data from the `astsa` package for `cort1`, `cort2`, `thal1`, and `thal2` separately (2 points). Label all axes and put meaningful titles on each of your plots.

(b) Then, calculate and plot the cross-correlations between the pairs of these measurements (e.g. `cort1` vs. `cort2`, `cort1` vs `thal1`, `cort1` vs. `thal2`, etc. (2 points). Label all axes and put meaningful titles on each of your plots.

(c) Comment on whether you see any patterns between them. Do the patterns look similar across different brain areas? (4 points)

## Q10. Linear regression with dependent errors  {-}

Consider the linear regression model $y_t = \beta_0 + \beta_1 x_t + \epsilon_t$ for $t=1, \dots, T$ where $x_t$ is a known, fixed regressor and $\epsilon_t$ represents noise.

Assume the noise $\epsilon_t$ is weakly stationary, with $\mathbb{E}(\epsilon_t)=0$, $\operatorname{cov}(\epsilon_t, \epsilon_{t+h}) = \gamma(h)$ and $\displaystyle\sum_{h=-\infty}^\infty \left|\gamma(h)\right| < \infty$

(a) Derive the ordinary least squares (OLS) estimator $\hat{\beta_1}$ and show that it is unbiased even when the noise is temporally correlated. (4 points)

(b) Explain why assuming independent noise (and ignoring temporal correlations in the noise) can yield incorrect standard errors. (4 points)

---

[Up: contents](../../index.md)
