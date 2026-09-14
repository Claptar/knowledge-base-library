---
title: each time (for example, when generating white noise)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# each time (for example, when generating white noise)

**Source:** [`public/labs/Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
```

First we'll start with a simple example where we have a linear trend plus noise. We'll take a sample from this function and try to fit a regression line to predict $y$ from $t$.

```python
t = np.arange(1, 101)
sigma = #FILL IN # If sigma=1, standard normal
beta0 = #FILL IN
beta1 = #FILL IN
y = beta0 + beta1*t + sigma*np.random.randn(len(t))

plt.plot(t,y,label='y=2+0.5t+w')
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.legend()
```

```
<matplotlib.legend.Legend at 0x1581b24a0>
```

*(1 figure omitted — see the original notebook.)*

We will fit the simple model

$$y_i = \beta_0 + \beta_1 t + \epsilon_i$$

using Ordinary Least Squares (OLS) in the `statsmodels` library.

We first have to add a constant term to our model to be sure that we actually get an estimate of $\beta_0$

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
Date:                Thu, 05 Feb 2026   Prob (F-statistic):           1.62e-62
Time:                        11:01:59   Log-Likelihood:                -270.29
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

---

[← Set the random seed, this is so you will generate the same answers](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md) · [Up: contents](index.md) · [Now plot the predictions - we can do this a few ways, either using →](04-now-plot-the-predictions---we-can-do-this-a-few-ways-either.md)
