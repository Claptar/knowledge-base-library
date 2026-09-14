---
title: Best change point
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Best change point

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

c_hat = c_candidates[np.argmin(rss_values)]

print("Estimated change point:", c_hat)
print("Estimated change date:", g.index[c_hat - 1])
```

```
Estimated change point: 75
Estimated change date: 1965-04-01 00:00:00
```

The estimated $c$ is 75 (which corresponds to the month of April 1965). Fixing this value of $c$, we can estimate $\beta_j, j = 0, 1, 2$ as before using linear regression.

```python
from scipy.optimize import minimize_scalar

g = np.diff(ylog)
t = np.arange(1, len(g) + 1)

X = np.column_stack([np.ones(len(g)), t, np.maximum(t - c_hat, 0)])
md5 = sm.OLS(g, X).fit()

print("Estimated c:", c_hat)
print(md5.summary())
```

```
Estimated c: 75
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.543
Model:                            OLS   Adj. R-squared:                  0.542
Method:                 Least Squares   F-statistic:                     480.4
Date:                Wed, 02 Sep 2026   Prob (F-statistic):          3.92e-138
Time:                        14:56:25   Log-Likelihood:                 5812.1
No. Observations:                 810   AIC:                        -1.162e+04
Df Residuals:                     807   BIC:                        -1.160e+04
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0016   3.81e-05     42.218      0.000       0.002       0.002
x1         -8.097e-06   5.64e-07    -14.348      0.000    -9.2e-06   -6.99e-06
x2          7.491e-06   5.77e-07     12.973      0.000    6.36e-06    8.62e-06
==============================================================================
Omnibus:                       20.728   Durbin-Watson:                   0.163
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               42.343
Skew:                           0.074   Prob(JB):                     6.39e-10
Kurtosis:                       4.110   Cond. No.                     3.61e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.61e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Future predictions can be obtained as follows.

```python
n = len(ylog)

t_future = np.arange(n, n + 168)
X_future = np.column_stack([
    np.ones(168),
    t_future,
    np.maximum(t_future - c_hat, 0)
])

g_pred_md5 = md5.predict(X_future)

---

[← Try all possible change points](19-try-all-possible-change-points.md) · [Up: contents](index.md) · [predicted populations y{n+1},...,y →](21-predicted-populations-y-n-1-y.md)
