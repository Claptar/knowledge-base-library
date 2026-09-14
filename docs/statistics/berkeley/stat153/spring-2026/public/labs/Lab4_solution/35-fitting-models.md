---
title: Fitting models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fitting models

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now we can fit some models to see how the number of taps per bin varies as a function of the time bin and other covariates. Note the adjusted R-squared and other metrics. Are these good models? Why or why not?

```python
model=smf.ols('taps_bin ~ time_bin', data=df_bins).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:               taps_bin   R-squared:                       0.062
Model:                            OLS   Adj. R-squared:                  0.061
Method:                 Least Squares   F-statistic:                     39.96
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           5.06e-10
Time:                        15:23:19   Log-Likelihood:                -2264.1
No. Observations:                 603   AIC:                             4532.
Df Residuals:                     601   BIC:                             4541.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     60.4624      0.746     81.047      0.000      58.997      61.927
time_bin      -1.5608      0.247     -6.321      0.000      -2.046      -1.076
==============================================================================
Omnibus:                       38.053   Durbin-Watson:                   0.665
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               51.912
Skew:                           0.520   Prob(JB):                     5.34e-12
Kurtosis:                       3.991   Cond. No.                         5.76
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
model = smf.ols('taps_bin ~ time_bin*C(finger) + C(dominant_hand)', data=df_bins).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:               taps_bin   R-squared:                       0.282
Model:                            OLS   Adj. R-squared:                  0.278
Method:                 Least Squares   F-statistic:                     58.82
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           7.05e-42
Time:                        15:23:19   Log-Likelihood:                -2183.5
No. Observations:                 603   AIC:                             4377.
Df Residuals:                     598   BIC:                             4399.
Df Model:                           4
Covariance Type:            nonrobust
===============================================================================================
                                  coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------------
Intercept                      58.5275      0.990     59.112      0.000      56.583      60.472
C(finger)[T.pinky]             -6.3238      1.317     -4.800      0.000      -8.911      -3.736
C(dominant_hand)[T.True]        8.2628      0.749     11.027      0.000       6.791       9.734
time_bin                       -1.7458      0.291     -5.991      0.000      -2.318      -1.173
time_bin:C(finger)[T.pinky]     0.4467      0.435      1.026      0.305      -0.409       1.302
==============================================================================
Omnibus:                       65.282   Durbin-Watson:                   0.739
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              144.550
Skew:                           0.608   Prob(JB):                     4.09e-32
Kurtosis:                       5.067   Cond. No.                         14.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

---

[← Examples of how taps change as a function of time bin](34-examples-of-how-taps-change-as-a-function-of-time-bin.md) · [Up: contents](index.md) · [Try the regressions again but using a different binning ... what do you notice? →](36-try-the-regressions-again-but-using-a-different-binning-what.md)
