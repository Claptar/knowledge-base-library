---
title: keep only nondecreasing triples to kill permutations
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# keep only nondecreasing triples to kill permutations

**Source:** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

mask = (X <= Y)
xf, yf = X[mask], Y[mask]
def _rss3(x, y):
    return rss([float(x), float(y)])
rss_vec = np.vectorize(_rss3)
rss_vals = rss_vec(xf, yf)
g = pd.DataFrame({'x': xf, 'y': yf, 'rss': rss_vals})
```

```python
min_row = g.loc[g['rss'].idxmin()]
print(min_row)
f_opt_2 = np.array([min_row['x'], min_row['y']])
print(f_opt_2)
print(1/f_opt_2)
```

```
x           0.090691
y           0.099850
rss    702139.356644
Name: 421955, dtype: float64
[0.09069069 0.09984985]
[11.02649007 10.01503759]
```

Below we plot the fitted function with the two best frequencies obtained as above.

```python
n = len(y)
f = f_opt_2 #f_opt was obtained from the grid minimization
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
if np.isscalar(f):
    f = [f]
for j in range(len(f)):
    f1 = f[j]
    xcos = np.cos(2 * np.pi * f1 * x)
    xsin = np.sin(2 * np.pi * f1 * x)
    X = np.column_stack([X, xcos, xsin])

md_2 = sm.OLS(y, X).fit()
print(md_2.summary())
best_rss_2 = np.sum(md_2.resid ** 2)
print(best_rss_2)


plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
#plt.plot(md_1.fittedvalues, color = 'black')
#plt.plot(md2.fittedvalues, color = 'black', marker = '', linestyle = '')
plt.plot(md_2.fittedvalues, color = 'red')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.436
Model:                            OLS   Adj. R-squared:                  0.429
Method:                 Least Squares   F-statistic:                     61.75
Date:                Thu, 25 Sep 2025   Prob (F-statistic):           1.26e-38
Time:                        16:28:55   Log-Likelihood:                -1708.8
No. Observations:                 325   AIC:                             3428.
Df Residuals:                     320   BIC:                             3447.
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         79.0015      2.599     30.398      0.000      73.888      84.115
x1           -43.8394      3.676    -11.925      0.000     -51.072     -36.607
x2           -18.6771      3.674     -5.084      0.000     -25.905     -11.450
x3            30.9542      3.678      8.417      0.000      23.719      38.189
x4            -9.3010      3.672     -2.533      0.012     -16.526      -2.076
==============================================================================
Omnibus:                       32.983   Durbin-Watson:                   0.383
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               45.724
Skew:                           0.699   Prob(JB):                     1.18e-10
Kurtosis:                       4.192   Cond. No.                         1.42
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
702139.3566439697
```

*(1 figure omitted — see the original notebook.)*

Next we try to find the three best frequencies, again using a grid minimization strategy.

```python
f1_gr = np.linspace(0, 0.15, 200)
f2_gr = np.linspace(0, 0.15, 200)
f3_gr = np.linspace(0, 0.15, 200)

---

[← mesh on the 3 axes; 'ij' preserves axis ordering](02-mesh-on-the-3-axes-ij-preserves-axis-ordering.md) · [Up: contents](index.md) · [mesh on the 3 axes; 'ij' preserves axis ordering →](04-mesh-on-the-3-axes-ij-preserves-axis-ordering.md)
