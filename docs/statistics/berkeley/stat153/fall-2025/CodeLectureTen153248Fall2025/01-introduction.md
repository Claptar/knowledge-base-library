---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Change of slope models and Regularization
---

In the last lecture, we started discussing nonlinear regression models. As a motivating example, we considered the following dataset (from FRED) on Annual Estimates of the Resident Population of California (units are thousands of persons) from 1900 to 2024.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
capop = pd.read_csv('CAPOP_11Sept2025.csv')
print(capop.head(10))
print(capop.tail(10))
tme = np.arange(1900, 2025)
plt.plot(tme, capop['CAPOP'], label='California Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.title('California Annual Resident Population (in thousands)')
plt.show()
```

```
observation_date   CAPOP
0       1900-01-01  1490.0
1       1901-01-01  1550.0
2       1902-01-01  1623.0
3       1903-01-01  1702.0
4       1904-01-01  1792.0
5       1905-01-01  1893.0
6       1906-01-01  1976.0
7       1907-01-01  2054.0
8       1908-01-01  2161.0
9       1909-01-01  2282.0
    observation_date      CAPOP
115       2015-01-01  38904.296
116       2016-01-01  39149.186
117       2017-01-01  39337.785
118       2018-01-01  39437.463
119       2019-01-01  39437.610
120       2020-01-01  39521.958
121       2021-01-01  39142.565
122       2022-01-01  39142.414
123       2023-01-01  39198.693
124       2024-01-01  39431.263
```

*(1 figure omitted — see the original notebook.)*

We work with the logarithms of the population data as this will lead to models with better interpretability.

```python
y = np.log(capop['CAPOP'])
n = len(y)
plt.plot(tme, y)
plt.xlabel('Year')
plt.ylabel('Log(Population in thousands)')
plt.title('Logarithm of California Annual Resident Population (in thousands)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The first model we fit is linear regression:
\begin{equation*}
   y_t = \beta_0 + \beta_1 t + \epsilon_t
\end{equation*}
with $\epsilon_t$ being i.i.d $N(0, \sigma^2)$. $\beta_1$ here can be interpreted in terms of the overall growth rate.

```python
x = np.arange(1, n+1)
X = np.column_stack((np.ones(n), x))
linreg = sm.OLS(y, X).fit()
print(linreg.summary())
plt.plot(tme, y, label='Log(Population in thousands)')
plt.plot(tme, linreg.fittedvalues, color='red', label='Fitted least squares line')
plt.xlabel('Year')
plt.ylabel('Log(Population in thousands)')
plt.title('Log Data with fitted least squares line')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  CAPOP   R-squared:                       0.950
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     2343.
Date:                Wed, 01 Oct 2025   Prob (F-statistic):           6.13e-82
Time:                        00:03:03   Log-Likelihood:                 10.482
No. Observations:                 125   AIC:                            -16.96
Df Residuals:                     123   BIC:                            -11.31
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          7.7301      0.040    191.493      0.000       7.650       7.810
x1             0.0269      0.001     48.406      0.000       0.026       0.028
==============================================================================
Omnibus:                       11.512   Durbin-Watson:                   0.006
Prob(Omnibus):                  0.003   Jarque-Bera (JB):                8.521
Skew:                          -0.522   Prob(JB):                       0.0141
Kurtosis:                       2.262   Cond. No.                         146.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

*(1 figure omitted — see the original notebook.)*

The fitted slope coefficient here is 0.0269. The interpretation is that the population increases by 2.69\% each year.

---

[Up: contents](index.md) · [Broken-stick Regression or Change of Slope Model →](02-broken-stick-regression-or-change-of-slope-model.md)
