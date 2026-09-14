---
title: Grid search over all pairs
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Grid search over all pairs

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

best_rss = np.inf

for c1 in c_candidates:
    for c2 in c_candidates:

        if c2 > c1:

            current_rss = rss(c1, c2)

            if current_rss < best_rss:
                best_rss = current_rss
                c1_hat = c1
                c2_hat = c2


print("Estimated change points:")
print(c1_hat, growth_dates[c1_hat - 1])
print(c2_hat, growth_dates[c2_hat - 1])

print("Minimum RSS:", best_rss)
```

```
Estimated change points:
108 1968-01-01 00:00:00
453 1996-10-01 00:00:00
Minimum RSS: 2.0261488639824974e-05
```

The estimated $c_1$ and $c_2$ are 108 (corresponding to January 1968) and 453 (corresponding to October 1996). With these values of $c_1$ and $c_2$, we can simply fit the model using linear regression (OLS) as before.

```python
X7 = np.column_stack([
    np.ones(n_g),
    t,
    np.maximum(t - c1_hat, 0),
    np.maximum(t - c2_hat, 0)
])

md7 = sm.OLS(g, X7).fit()

print(md7.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.667
Model:                            OLS   Adj. R-squared:                  0.666
Method:                 Least Squares   F-statistic:                     537.7
Date:                Wed, 02 Sep 2026   Prob (F-statistic):          7.93e-192
Time:                        15:09:46   Log-Likelihood:                 5939.7
No. Observations:                 810   AIC:                        -1.187e+04
Df Residuals:                     806   BIC:                        -1.185e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0016   2.76e-05     57.221      0.000       0.002       0.002
x1         -7.123e-06   3.16e-07    -22.565      0.000   -7.74e-06    -6.5e-06
x2          7.537e-06   3.52e-07     21.388      0.000    6.84e-06    8.23e-06
x3         -2.025e-06   1.12e-07    -18.016      0.000   -2.25e-06    -1.8e-06
==============================================================================
Omnibus:                       68.866   Durbin-Watson:                   0.223
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              192.544
Skew:                           0.423   Prob(JB):                     1.55e-42
Kurtosis:                       5.234   Cond. No.                     3.03e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.03e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Predictions are obtained as follows.

```python

---

[← Possible change points](25-possible-change-points.md) · [Up: contents](index.md) · [Fitted growth rates →](27-fitted-growth-rates.md)
