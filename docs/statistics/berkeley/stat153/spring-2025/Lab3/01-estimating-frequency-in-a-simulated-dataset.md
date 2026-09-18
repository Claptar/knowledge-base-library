---
title: Estimating Frequency in a Simulated Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Estimating Frequency in a Simulated Dataset

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

Consider the following dataset simulated using the model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin( 2 \pi f t) + \epsilon_t,
\end{equation*}
for $t = 1, \dots, n$ with some fixed values of $f, \beta_0, \beta_1, \beta_2$ and $\sigma$. The goal of this problem is to estimate $f$ along with associated uncertainty quantification.

```python
f = 0.2
#f = 1.8
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10

rng = np.random.default_rng()
errorsamples = rng.normal(loc = 0, scale = sig, size = n)
t = np.arange(1, n + 1)

y = b0 * np.ones(n) + b1 * np.cos(2 * np.pi * f * t) + b2 * np.sin(2 * np.pi * f * t) + errorsamples
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('A simulated dataset')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The frequentist solution calculates the MLE. For computing the MLE, we first optimize the following criterion function over $f$ to obtain $\hat{f}$:
\begin{equation*}
   \text{crit}(f) := \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos(2 \pi f t) - \beta_2 \sin(2 \pi f t))^2 = RSS(f),
\end{equation*}
where $RSS(f)$ denotes the Residual Sum of Squares in the linear regression model obtaining by fixing $f$. After finding $\hat{f}$, the MLEs for the other parameters are obtained as in standard linear regression with $f$ fixed at $\hat{f}$.

```python
def crit(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

Here is a plot of $\text{crit}(f)$ as a function of $f$ over a grid of values of $f$.

```python
ngrid = 100000
allfvals = np.linspace(0, 0.5, ngrid)
critvals = np.array([crit(f) for f in allfvals])
```

```python
plt.plot(allfvals, critvals)
plt.xlabel('Frequency')
plt.ylabel('Sum of Squares')
plt.title('Least Squares Criterion Function')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# the MLE of f is now calculated as:
fhat = allfvals[np.argmin(critvals)]

print(fhat)
```

```
0.1998969989699897
```

After obtaining $\hat{f}$, the estimates of $\beta_0, \beta_1, \beta_2, \sigma$ are obtained in the usual way for linear regression fixing $f = \hat{f}$

```python
x = np.arange(1, n + 1)
xcos = np.cos(2 * np.pi * fhat * x)
xsin = np.sin(2 * np.pi * fhat * x)
Xfhat = np.column_stack([np.ones(n), xcos, xsin])

md = sm.OLS(y, Xfhat).fit()

print(md.params) # this gives estimates of beta_0, beta_1, beta_2
print(md.summary())
```

```
[0.98353083 3.62686407 4.11283874]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.144
Model:                            OLS   Adj. R-squared:                  0.139
Method:                 Least Squares   F-statistic:                     33.33
Date:                Fri, 07 Feb 2025   Prob (F-statistic):           4.16e-14
Time:                        17:35:53   Log-Likelihood:                -1466.4
No. Observations:                 400   AIC:                             2939.
Df Residuals:                     397   BIC:                             2951.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.9835      0.475      2.071      0.039       0.050       1.917
x1             3.6269      0.672      5.400      0.000       2.307       4.947
x2             4.1128      0.671      6.126      0.000       2.793       5.433
==============================================================================
Omnibus:                        3.795   Durbin-Watson:                   2.183
Prob(Omnibus):                  0.150   Jarque-Bera (JB):                3.854
Skew:                          -0.235   Prob(JB):                        0.146
Kurtosis:                       2.900   Cond. No.                         1.41
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

The true values of $\beta_0, \beta_1, \beta_2$ lie in the corresponding 95\% C.I given for each coefficient in the model summary above.

```python
# Estimate of sigma:
rss = np.sum(md.resid ** 2)
sigmahat = np.sqrt(rss / (n - 3))

print(sigmahat)
```

```
9.495940890783043
```

Next we look at Bayesian inference which will yield similar results but will additionally provide uncertainty intervals for $f$. We use the following formula for the Bayesian posterior that we derived in class:
\begin{equation*}
   I\{0 \leq f \leq 1/2\} \cdot |X_f^T X_f|^{-1/2} \cdot \left(\frac{1}{S(\hat{\beta}(f), f)} \right)^{(n-p)/2}
\end{equation*}
where $p = 3$ and $|X_f^T X_f|$ denotes the determinant of $X_f^T X_f$.

It is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
def logpost(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) # sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant
    logval = ((p - n) / 2) * np.log(rss) - 0.5 * log_det

    return logval
```

While evaluating the log posterior on a grid, it is important to make sure that we do not include frequencies $f$ for which $X_f^T X_f$ is singular. This will be the case for $f = 0$ and $f = 1/2$. When $f$ is very close to 0 or $0.5$, the term $|X_f^T X_f|^{-1/2}$ will be very large because of near-singularity of $X_f^T X_f$. We will therefore exclude frequencies very close to 0 and 0.5 from the grid while calculating posterior probabilities.

```python
logpostvals = np.array([logpost(f) for f in allfvals])
```

```python
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
allfvals = allfvals[100:(ngrid - 100)]

print(np.min(allfvals), np.max(allfvals))

logpostvals = np.array([logpost(f) for f in allfvals])
```

```
0.0005000050000500005 0.49949999499995
```

```python
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we exponentiate the log posterior to obtain posterior. Here we again need to be mindful of numerical issues. If we directly take the exponent of numbers, we might get 0 or $\infty$. So we first subtract a constant so that the values are somewhat closer to 0 before taking the exponent.

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))
```

```python
plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals_density = postvals_unnormalized / (np.sum(postvals_unnormalized))

postvals_density = postvals_density * (ngrid - 200) / 0.5
```

```python
plt.plot(allfvals, postvals_density)
plt.xlabel('Frequency')
plt.ylabel('Density')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Using the posterior distribution, we can calculate posterior mean etc. and obtain credible intervals for $f$.

```python
#Posterior mean of f:
fpostmean = np.sum(postvals * allfvals)

#Posterior mode of f:
fpostmode = allfvals[np.argmax(postvals)]

print(fpostmean, fpostmode, fhat)
```

```
0.19989514344518863 0.1998969989699897 0.1998969989699897
```

Note that the posterior mode coincides with the MLE. Let us now compute a credible interval for $f$. A 95\% credible interval is an interval for which the posterior probability is about 95\%. The following function takes an input value $m$ and compute the posterior probability assigned to the interval $\hat{f} - m*\delta, \hat{f} + m*\delta$ where $\delta$ is the grid resolution that we used for computing the posterior.

```python
def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind - m):(est_ind + m)])

    return(ans)
```

We now start with a small value of $m$ (say $m = 0$) and keep increasing it until the posterior probability reaches 0.95.

```python
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m + 1

print(m)
```

```
65
```

The credible interval for $f$ can then be computed in the following way.

```python
est_ind = np.argmax(postvals)
f_est = allfvals[est_ind]

# 95% credible interval for f:
ci_f_low = allfvals[est_ind - m]
ci_f_high = allfvals[est_ind + m]
print(np.array([f_est, ci_f_low, ci_f_high]))
```

```
[0.199897 0.199572 0.200222]
```

When I implemented this experiment, I found the interval to be very narrow while containing the true value 0.2.

---

[Up: contents](index.md) · [Frequency Aliasing →](02-frequency-aliasing.md)
