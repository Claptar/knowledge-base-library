---
title: Linear Regression Details
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Linear Regression Details

**Source:** [`CodeLabTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We shall look at some standard regression terminology and also how some of the numbers shown in the regression output are actually computed.

Let us use the GDP dataset from FRED (https://fred.stlouisfed.org/series/GDP) which gives quarterly data on the Gross Domestic Product (units are billions of dollars).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
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
Date:                Sun, 14 Sep 2025   Prob (F-statistic):               0.00
Time:                        14:30:14   Log-Likelihood:                -2402.2
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

### Least Squares Estimates

The information on the estimates $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3$ along with associated uncertainties (standard errors) are given in the table near the middle of the output. Specifically, the estimates from the above table are $\hat{\beta}_0 = 292.181$, $\hat{\beta}_1 = -2.5806$, $\hat{\beta}_2 = 0.0759$ and $\hat{\beta}_3 = 0.0007$. These numbers can also be obtained using model.params as follows:

```python
print(md.params)
```

```
const    292.184077
x1        -2.580592
x2         0.075924
x3         0.000665
dtype: float64
```


These estimates are known as the Least Squares Estimates (also the same as Maximum Likelihood Estimates) and they are computed via the formula:
\begin{equation*}
   \hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \end{pmatrix} = (X^T X)^{-1} X^T y.
\end{equation*}
Let us verify that this formula indeed gives the reported estimates.

```python
XTX = np.dot(X.T, X)
XTX_inverse = np.linalg.inv(XTX)
XTX_inverse_XT = np.dot(XTX_inverse, X.T)
betahat = np.dot(XTX_inverse_XT, y)

print(np.column_stack([betahat, md.params]))
```

```
[[ 2.92184077e+02  2.92184077e+02]
 [-2.58059163e+00 -2.58059163e+00]
 [ 7.59236235e-02  7.59236235e-02]
 [ 6.64683542e-04  6.64683542e-04]]
```

In reality, sm.OLS does not use the above formula directly (even though the formula is the correct one), instead it uses some efficient linear algebra methods to solve the linear equations $X^T X \beta = X^T y$.

### Fitted Values

The next quantity to understand are the fitted values. These are given by model.fittedvalues and they are obtained via the simple formula:
\begin{equation*}
   \hat{y} = X \hat{\beta}
\end{equation*}
The entries $\hat{y}_1, \dots, \hat{y}_n$ of the vector $\hat{y}$ are known as the fitted values. Let us check the correctness of this formula.

```python
fvals = np.dot(X, betahat)

print(np.column_stack([fvals[:10], md.fittedvalues[:10]]))
```

```
[[289.68007406 289.68007406]
 [287.33190609 287.33190609]
 [285.14356157 285.14356157]
 [283.1190286  283.1190286 ]
 [281.26229528 281.26229529]
 [279.57734972 279.57734972]
 [278.06818001 278.06818001]
 [276.73877426 276.73877426]
 [275.59312056 275.59312056]
 [274.63520702 274.63520702]]
```

To assess how well the regression model fits the data, we plot the fitted values along with the original data.

```python
plt.plot(y, label = "Data")
plt.plot(md.fittedvalues, label = "Fitted values")
plt.legend()
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Gross Domestic Product (GDP) of the United States")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Residuals

The residuals simply are the differences between the observed data and the fitted values. We use the notation $e$ for the vector of residuals:
\begin{equation*}
  e = y - \hat{y}
\end{equation*}
The $i^{th}$ residual is simply the $i^{th}$ entry of $e$.

```python
residuals = y - fvals
print(np.column_stack([md.resid[:10], residuals[:10]]))
```

```
[[-46.51607406 -46.51607406]
 [-41.36390609 -41.36390609]
 [-35.55856157 -35.55856157]
 [-23.3740286  -23.3740286 ]
 [-15.52029529 -15.52029528]
 [ -7.01034972  -7.01034972]
 [  1.12781999   1.12781999]
 [  3.62722574   3.62722574]
 [ -0.55912056  -0.55912056]
 [ -3.28420702  -3.28420702]]
```

A plot of the residuals against time is an important diagnostic tool which can tell us about the effectiveness of the fitted model.

```python
plt.plot(md.resid)
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Residuals")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From this plot, we see that there are some very large residuals indicating the presence of time points where the model predictions are quite far off from the observed values. This could be because of outliers or some systematic features that the model is missing. Also the residual plot looks quite smooth which indicates that there is some correlation between nearby residuals. This can be better visualized via the **acf plot** (sometimes known as the correlogram) of the residuals.

```python

---

[Up: contents](index.md) · [For comparison →](02-for-comparison.md)
