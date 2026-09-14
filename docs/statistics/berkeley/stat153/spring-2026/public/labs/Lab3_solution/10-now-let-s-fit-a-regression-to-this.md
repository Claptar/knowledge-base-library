---
title: Now let's fit a regression to this
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Now let's fit a regression to this

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

yvec = np.array(chicken_smoothed)
n = len(yvec) # number of time points
xvec = np.arange(1, n+1)
X = sm.add_constant(xvec)
linreg_smooth = sm.OLS(yvec, X).fit()
print(linreg_smooth.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                         nan
Model:                            OLS   Adj. R-squared:                    nan
Method:                 Least Squares   F-statistic:                       nan
Date:                Thu, 05 Feb 2026   Prob (F-statistic):                nan
Time:                        12:20:04   Log-Likelihood:                    nan
No. Observations:                 180   AIC:                               nan
Df Residuals:                     178   BIC:                               nan
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const             nan        nan        nan        nan         nan         nan
x1                nan        nan        nan        nan         nan         nan
==============================================================================
Omnibus:                          nan   Durbin-Watson:                     nan
Prob(Omnibus):                    nan   Jarque-Bera (JB):                  nan
Skew:                             nan   Prob(JB):                          nan
Kurtosis:                         nan   Cond. No.                         210.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We got nans ("Not a Number"/undefined)! Why did this happen? It turns out when we defined our moving average, we only calculated the windowed average once we got enough samples, so the beginning and end of our function is now undefined.

To make this work out, we have to remove the nan values as follows:

```python
yvec = np.array(chicken_smoothed[~np.isnan(chicken_smoothed)]) # Take only the points that are *not* NaN (that's what ~ is shorthand for)
n = len(yvec) # number of time points
xvec = np.arange(1, n+1)
print(len(yvec), len(xvec))
X = sm.add_constant(xvec)
linreg_smooth = sm.OLS(yvec, X).fit()
print(linreg_smooth.summary())
```

```
144 144
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.949
Model:                            OLS   Adj. R-squared:                  0.949
Method:                 Least Squares   F-statistic:                     2635.
Date:                Thu, 05 Feb 2026   Prob (F-statistic):           1.41e-93
Time:                        12:20:05   Log-Likelihood:                -353.12
No. Observations:                 144   AIC:                             710.2
Df Residuals:                     142   BIC:                             716.2
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         63.8031      0.474    134.568      0.000      62.866      64.740
x1             0.2912      0.006     51.336      0.000       0.280       0.302
==============================================================================
Omnibus:                       15.433   Durbin-Watson:                   0.005
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                8.071
Skew:                           0.395   Prob(JB):                       0.0177
Kurtosis:                       2.150   Cond. No.                         168.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
residuals_smooth = linreg_smooth.resid

---

[← Fix the time index](09-fix-the-time-index.md) · [Up: contents](index.md) · [Make sure we get the new time index as well →](11-make-sure-we-get-the-new-time-index-as-well.md)
