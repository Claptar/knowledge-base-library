---
title: the MLE of f is now calculated as
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# the MLE of f is now calculated as

**Source:** [`Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← More on fitting sinusoidal models](01-more-on-fitting-sinusoidal-models.md) · [Up: contents](index.md) · [Estimate of sigma →](03-estimate-of-sigma.md)
