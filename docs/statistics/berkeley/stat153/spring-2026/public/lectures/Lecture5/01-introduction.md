---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Lecture 5 - Simple linear regression

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.api as sm # This contains the model fitting libraries for linear regression
from statsmodels.graphics.tsaplots import plot_acf # autocorrelation function

#!pip install astsa
import astsa # You should have pip installed this for Lab 1.. if not, uncomment line above

# Set the random seed, this is so you will generate the same answers
# each time (for example, when generating white noise)
np.random.seed(42)
```

First we'll start with a simple example where we have a linear trend plus noise. We'll take a sample from this function and try to fit a regression line to predict $y$ from $t$.

```python
t = np.arange(1, 101)
sigma = 4 # If sigma=1, standard normal
y = 2 + 0.5*t + sigma*np.random.randn(len(t))

plt.plot(t,y,label='y=2+0.5t+w')
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.legend()
```

```
<matplotlib.legend.Legend at 0x168d86560>
```

*(1 figure omitted — see the original notebook.)*

We will fit the simple model

$$y_i = \beta_0 + \beta_1 t + \epsilon_i$$

using Ordinary Least Squares (OLS) in the `statsmodels` library.

```python
linreg_simple = sm.OLS(y, t).fit()
print(linreg_simple.summary())
```

```
OLS Regression Results
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.986
Model:                            OLS   Adj. R-squared (uncentered):              0.986
Method:                 Least Squares   F-statistic:                              6862.
Date:                Tue, 03 Feb 2026   Prob (F-statistic):                    3.01e-93
Time:                        19:51:25   Log-Likelihood:                         -271.87
No. Observations:                 100   AIC:                                      545.7
Df Residuals:                      99   BIC:                                      548.3
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.5250      0.006     82.834      0.000       0.512       0.538
==============================================================================
Omnibus:                        0.411   Durbin-Watson:                   1.979
Prob(Omnibus):                  0.814   Jarque-Bera (JB):                0.259
Skew:                          -0.125   Prob(JB):                        0.879
Kurtosis:                       3.011   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We can see that our regression recovered the coefficient $x1=0.5286$, which is pretty close to our true $\beta_1=0.5$, but it's not quite right because we didn't get the intercept $\beta_0$. When we show the fitted line, we can see that the best fit line should be shifted up.

```python
plt.plot(t,y)
plt.plot(t,linreg_simple.fittedvalues)
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
```

```
Text(0, 0.5, 'y')
```

*(1 figure omitted — see the original notebook.)*

We can fix this by adding a constant term to our OLS fit, as follows:

```python
T = sm.add_constant(t)
linreg_simple2 = sm.OLS(y, T).fit()
print(linreg_simple2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.942
Model:                            OLS   Adj. R-squared:                  0.942
Method:                 Least Squares   F-statistic:                     1601.
Date:                Tue, 03 Feb 2026   Prob (F-statistic):           1.62e-62
Time:                        19:51:25   Log-Likelihood:                -270.29
No. Observations:                 100   AIC:                             544.6
Df Residuals:                      98   BIC:                             549.8
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.3032      0.735      1.773      0.079      -0.155       2.762
x1             0.5056      0.013     40.010      0.000       0.480       0.531
==============================================================================
Omnibus:                        0.521   Durbin-Watson:                   2.042
Prob(Omnibus):                  0.771   Jarque-Bera (JB):                0.518
Skew:                          -0.167   Prob(JB):                        0.772
Kurtosis:                       2.885   Cond. No.                         117.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We can also report the confidence intervals on our estimates of $\beta_0$ and $\beta_1$, which can be useful for determining our certainty of these estimates.

```python
ci_linreg_simple2 = linreg_simple2.conf_int(alpha=0.05)
print(ci_linreg_simple2)
print(f'95% confidence interval for B0$: [{ci_linreg_simple2[0,0]:.3f}, {ci_linreg_simple2[0,1]:.3f}]')
print(f'95% confidence interval for B1$: [{ci_linreg_simple2[1,0]:.3f}, {ci_linreg_simple2[1,1]:.3f}]')
```

```
[[-0.15543644  2.76178753]
 [ 0.48049713  0.53064895]]
95% confidence interval for B0$: [-0.155, 2.762]
95% confidence interval for B1$: [0.480, 0.531]
```

```python
plt.plot(t,y)
plt.plot(t,linreg_simple2.fittedvalues)
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
```

```
Text(0, 0.5, 'y')
```

*(1 figure omitted — see the original notebook.)*

For time series, one thing we want to check is that our residuals (the difference between the predicted data and our actual value) are weakly stationary, which allows us to assume that our error $\epsilon_t$ is weakly stationary.

We can do that by plotting the residuals over time as well as the autocorrelation function of the residuals. How does this look?

```python
residuals = linreg_simple2.resid

plt.figure()
plt.plot(t,residuals)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('t')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals, lags=40, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Another (messier) example →](02-another-messier-example.md)
