---
title: t-statistic and confidence intervals for the coefficients
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# t-statistic and confidence intervals for the coefficients

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The $t$-statistic for each coefficient is simply the estimate divided by the standard error. The confidence interval for $\beta_j$ is given by:
\begin{equation*}
   \left[\hat{\beta}_j - t_{\alpha/2, n-4} \text{ standard error of } \hat{\beta}_j, \hat{\beta}_j + t_{\alpha/2, n-4} \text{ standard error of } \hat{\beta}_j  \right]
\end{equation*}
where $t_{\alpha/2, n-4}$ is the point beyond the $t$-distribution with $n-4$ degrees of freedom gives probability mass $\alpha/2$. The above formula is the result of:
\begin{equation*}
   \frac{\beta_j - \hat{\beta}_j}{\text{ standard error of } \hat{\beta}_j} \mid \text{ data } \sim t-\text{distribution with} ~n-4 \text{ d.f}
\end{equation*}
The above statement can also be interpreted in a frequentist sense (then the conditional on data will be removed and the randomness will be over the data with fixed $\beta_j$).

```python
from scipy.stats import t
alpha = 0.05
qt = t.ppf(1 - (alpha/2), n-4) #area to the right equaling alpha/2 is the same as area to the left equaling 1-alpha/2
print(qt)
cilower = md.params - md.bse*qt
ciupper = md.params + md.bse*qt
print(np.column_stack([cilower, ciupper]))
print(md.summary())
```

```
1.9677212881552213
[[ 4.32711446e+01  5.41097010e+02]
 [-9.47864205e+00  4.31745880e+00]
 [ 2.45922503e-02  1.27254997e-01]
 [ 5.56525463e-04  7.72841622e-04]]
                            OLS Regression Results
==============================================================================
Dep. Variable:                    GDP   R-squared:                       0.995
Model:                            OLS   Adj. R-squared:                  0.995
Method:                 Least Squares   F-statistic:                 2.000e+04
Date:                Wed, 29 Jan 2025   Prob (F-statistic):               0.00
Time:                        14:30:48   Log-Likelihood:                -2402.2
No. Observations:                 311   AIC:                             4812.
Df Residuals:                     307   BIC:                             4827.
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        292.1841    126.498      2.310      0.022      43.271     541.097
x1            -2.5806      3.506     -0.736      0.462      -9.479       4.317
x2             0.0759      0.026      2.910      0.004       0.025       0.127
x3             0.0007    5.5e-05     12.093      0.000       0.001       0.001
==============================================================================
Omnibus:                       74.600   Durbin-Watson:                   0.095
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              746.989
Skew:                           0.635   Prob(JB):                    6.21e-163
Kurtosis:                      10.485   Cond. No.                     4.63e+07
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.63e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
```

---

[← Standard Errors of the coefficient estimates](08-standard-errors-of-the-coefficient-estimates.md) · [Up: contents](index.md) · [Visualizing Uncertainty →](10-visualizing-uncertainty.md)
