---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Linear Regression Details
---

We shall look at some standard regression terminology and also how some of the numbers shown in the regression output are actually computed.

Let us use the GDP dataset from FRED (https://fred.stlouisfed.org/series/GDP) which gives quarterly data on the Gross Domestic Product (units are billions of dollars).

```python
import pandas as pd
gdp = pd.read_csv('GDP-Jan2025FRED.csv')
print(gdp.head(10))
```

```
observation_date      GDP
0       1947-01-01  243.164
1       1947-04-01  245.968
2       1947-07-01  249.585
3       1947-10-01  259.745
4       1948-01-01  265.742
5       1948-04-01  272.567
6       1948-07-01  279.196
7       1948-10-01  280.366
8       1949-01-01  275.034
9       1949-04-01  271.351
```

```python
import matplotlib.pyplot as plt
plt.plot(gdp['GDP'])
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Gross Domestic Product (GDP) of the United States")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us fit a cubic trend model to this dataset given by:
\begin{equation*}
  y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \beta_3 t^3 + \epsilon_t
\end{equation*}
for $t = 1, \dots, n$ where $n$ is the total number of observations in the dataset. In vector-matrix notation, this model can be equivalently be represented as:
\begin{equation*}
   y = X \beta + \epsilon
\end{equation*}
where
\begin{equation*}
   y = \begin{pmatrix} y_1\\ y_2 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} ~~~
   X = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 2^2 & 2^3 \\ 1 & 3 & 3^2 & 3^3 \\ \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot \\ 1 & n & n^2 & n^3 \end{pmatrix} ~~~ \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \end{pmatrix} ~ ~ ~ \epsilon = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \cdot \\ \cdot \\ \cdot \\ \epsilon_n \end{pmatrix}
\end{equation*}
Observe $y$ is $n \times 1$, $X$ is $n \times 4$, $\beta$ is $4 \times 1$ and $\epsilon$ is $n \times 1$. The entries $\epsilon_1, \dots, \epsilon_n$ of the vector $\epsilon$ are known as errors and we assume that $\epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. There are 5 parameters in this model $\beta_0, \beta_1, \beta_2, \beta_3, \sigma$ which we need to estimate from the data.

To implement regression, we simply need to create $y$ and $X$ and give them as input to the sm.OLS function.

The following code creates $y$ and $X$.

```python
y = gdp['GDP']
n = len(y)
x = np.arange(1, n + 1)
x2 = x ** 2
x3 = x ** 3
import numpy as np
X = np.column_stack([np.ones(n),x, x2, x3])
print(X[:5])
```

```
[[  1.   1.   1.   1.]
 [  1.   2.   4.   8.]
 [  1.   3.   9.  27.]
 [  1.   4.  16.  64.]
 [  1.   5.  25. 125.]]
```

Now we simply use sm.OLS with $y$ and $X$:

```python
md = sm.OLS(y, X).fit()
print(md.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                    GDP   R-squared:                       0.995
Model:                            OLS   Adj. R-squared:                  0.995
Method:                 Least Squares   F-statistic:                 2.000e+04
Date:                Wed, 29 Jan 2025   Prob (F-statistic):               0.00
Time:                        11:49:03   Log-Likelihood:                -2402.2
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

[Up: contents](index.md) · [Least Squares Estimates →](02-least-squares-estimates.md)
