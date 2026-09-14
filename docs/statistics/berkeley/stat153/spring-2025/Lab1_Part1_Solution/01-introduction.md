---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab1_Part1_Solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`Lab1_Part1_Solution.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Fitting trends via linear regression
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## US Population Dataset

The following dataset is downloaded from the Federal Reserve Economic Database FRED (https://fred.stlouisfed.org/series/POPTHM).

```python
uspop = pd.read_csv("POPTHM-Jan2025FRED.csv")
print(uspop.head(10))
print(uspop.tail(10))
print(uspop.shape)
```

```
observation_date  POPTHM
0       1959-01-01  175818
1       1959-02-01  176044
2       1959-03-01  176274
3       1959-04-01  176503
4       1959-05-01  176723
5       1959-06-01  176954
6       1959-07-01  177208
7       1959-08-01  177479
8       1959-09-01  177755
9       1959-10-01  178026
    observation_date  POPTHM
781       2024-02-01  336306
782       2024-03-01  336423
783       2024-04-01  336550
784       2024-05-01  336687
785       2024-06-01  336839
786       2024-07-01  337005
787       2024-08-01  337185
788       2024-09-01  337362
789       2024-10-01  337521
790       2024-11-01  337669
(791, 2)
```

```python
plt.plot(uspop['POPTHM'])
plt.xlabel("Time (in months)")
plt.ylabel("Population (in thousands)")
plt.title("US Population Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Problem 1
Fit a simple linear regression model to the data. Interpret the estimated intercept and slope.

```python
import statsmodels.api as sm

t = np.arange(1, len(uspop['POPTHM']) + 1)
X = sm.add_constant(t)

lin_model = sm.OLS(uspop['POPTHM'], X).fit()
print(lin_model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 2.422e+05
Date:                Thu, 23 Jan 2025   Prob (F-statistic):               0.00
Time:                        23:54:49   Log-Likelihood:                -7394.9
No. Observations:                 791   AIC:                         1.479e+04
Df Residuals:                     789   BIC:                         1.480e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.746e+05    198.060    881.427      0.000    1.74e+05    1.75e+05
x1           213.2353      0.433    492.142      0.000     212.385     214.086
==============================================================================
Omnibus:                      409.683   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               73.601
Skew:                          -0.479   Prob(JB):                     1.04e-16
Kurtosis:                       1.853   Cond. No.                         915.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python

---

[Up: contents](index.md) · [Plot the original dataset along with the fitted values →](02-plot-the-original-dataset-along-with-the-fitted-values.md)
