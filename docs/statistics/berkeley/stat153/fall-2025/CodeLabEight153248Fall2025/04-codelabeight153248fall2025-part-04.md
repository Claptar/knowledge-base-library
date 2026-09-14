---
title: CodeLabEight153248Fall2025 Part 04 —
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEight153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLabEight153248Fall2025 Part 04 —

**Source:** [`CodeLabEight153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
79.83531765284938 79.52702577862316
```

### Model Three: AR(2)

The AR(2) model is a natural extension of the Yule model:
\begin{equation*}
   y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t
\end{equation*}
The only difference between the Yule model and AR(2) is that $\phi_2 = -1$ in the Yule model while it is treated as an adjustable parameter which can provide better fits to the data in AR(2).

The AR(2) model is fit in the following way.

```python
p = 2
yreg = y[p:] # these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) # this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
```

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)
print(armod.summary())
sighat = np.sqrt(np.mean(armod.resid ** 2))
print(sighat)
```

```
[23.08524521  1.37838349 -0.68406411]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.822
Model:                            OLS   Adj. R-squared:                  0.821
Method:                 Least Squares   F-statistic:                     567.0
Date:                Mon, 27 Oct 2025   Prob (F-statistic):           1.19e-92
Time:                        15:10:09   Log-Likelihood:                -1147.2
No. Observations:                 248   AIC:                             2300.
Df Residuals:                     245   BIC:                             2311.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         23.0852      2.647      8.722      0.000      17.872      28.299
x1             1.3784      0.047     29.399      0.000       1.286       1.471
x2            -0.6841      0.047    -14.506      0.000      -0.777      -0.591
==============================================================================
Omnibus:                       25.182   Durbin-Watson:                   2.117
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               37.915
Skew:                           0.631   Prob(JB):                     5.85e-09
Kurtosis:                       4.441   Cond. No.                         220.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
24.69788658707509
```

Note that the estimated value of $\phi_2$ (which is the value of $\phi_2$ which gives the best fit to the data in the least squares sense) is $-0.6841$ which is quite a bit smaller than the value of $-1$ which is hard-coded in the Yule model.

Let us obtain predictions for the future values using the fitted AR(2) model.

```python

---

[← Generate k-step ahead forecasts](03-generate-k-step-ahead-forecasts.md) · [Up: contents](index.md) · [Generate k-step ahead forecasts →](05-generate-k-step-ahead-forecasts.md)
