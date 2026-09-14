---
title: Example of Lagged or Auto Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFour153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Example of Lagged or Auto Regression

**Source:** [`CodeLectureFour153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We apply lagged regression to the following dataset. The model is:
\begin{align*}
   y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_m y_{t-m} + \epsilon_t
\end{align*}
for some $m$. The response vector and covariate matrix in this regression are:
\begin{align*}
   y = \begin{pmatrix}y_{m+1} \\ y_{m+2} \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \text{ and } X = \begin{pmatrix} 1 & y_m & y_{m-1} & \cdot & \cdot & \cdot & y_1 \\
    1 & y_{m+1} & y_{m} & \cdot & \cdot & \cdot & y_2 \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
    \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
    1 & y_{n-1} & y_{n-2} & \cdot & \cdot & \cdot & y_{n-m}\end{pmatrix}
\end{align*}
So the number of observations in this regression is $n-m$.

```python
#The following is FRED data on retail sales (in millions of dollars) for beer, wine and liquor stores (https://fred.stlouisfed.org/series/MRTSSM4453USN)
beersales = pd.read_csv('MRTSSM4453USN_October2025.csv')
print(beersales.head())
y = beersales['MRTSSM4453USN'].to_numpy()
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.title('Retail Sales: Beer, wine and liquor stores')
plt.show()
```

```
observation_date  MRTSSM4453USN
0       1992-01-01           1414
1       1992-02-01           1444
2       1992-03-01           1496
3       1992-04-01           1569
4       1992-05-01           1707
```

*(1 figure omitted — see the original notebook.)*

The code below forms $y$: $(n-m) \times 1$ and $X$: $(n-m) \times (m+1)$ as above.

```python
m = 12
n = len(y)
yreg = y[m:] #these are the response values in the autoregression
Xmat = np.ones((n-m, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, m+1):
    col = y[m-j : n-j]
    Xmat = np.column_stack([Xmat, col])
print(Xmat.shape)
print(n)
```

```
(391, 13)
403
```

Below we run regression (using OLS).

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.988
Model:                            OLS   Adj. R-squared:                  0.988
Method:                 Least Squares   F-statistic:                     2597.
Date:                Tue, 08 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:02:35   Log-Likelihood:                -2529.9
No. Observations:                 391   AIC:                             5086.
Df Residuals:                     378   BIC:                             5137.
Df Model:                          12
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          6.7819     21.711      0.312      0.755     -35.907      49.471
x1             0.0439      0.018      2.448      0.015       0.009       0.079
x2             0.0428      0.018      2.379      0.018       0.007       0.078
x3             0.0521      0.018      2.913      0.004       0.017       0.087
x4             0.0336      0.018      1.870      0.062      -0.002       0.069
x5             0.0523      0.018      2.898      0.004       0.017       0.088
x6             0.0002      0.018      0.009      0.993      -0.036       0.036
x7            -0.0128      0.018     -0.697      0.486      -0.049       0.023
x8            -0.0304      0.019     -1.633      0.103      -0.067       0.006
x9            -0.0440      0.019     -2.368      0.018      -0.081      -0.007
x10           -0.0621      0.019     -3.352      0.001      -0.099      -0.026
x11           -0.0163      0.019     -0.875      0.382      -0.053       0.020
x12            0.9739      0.019     52.184      0.000       0.937       1.011
==============================================================================
Omnibus:                      172.369   Durbin-Watson:                   0.812
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1196.724
Skew:                           1.726   Prob(JB):                    1.36e-260
Kurtosis:                      10.845   Cond. No.                     3.36e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.36e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

The code below does prediction for $y_{n+1}, \dots, y_{n+k}$. This needs to be done sequentially: first predict $y_{n+1}$, then use that prediction for $y_{n+2}$ and so on. We shall study AutoRegressions in more detail later in the course.

```python
#Generate k-step ahead forecasts:
k = 100
yhat = np.concatenate([y, np.full(k, -9999)]) #extend data by k placeholder values
for i in range(1, k+1):
    ans = armod.params[0]
    for j in range(1, m+1):
        ans += armod.params[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]
```

```python
#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat,  color='C0')
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues, label='Forecasts', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(' + str(m) + ') Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The value of $m$ is crucial for the performance of this method. If $m < 12$, then the predictions will look clearly off. But values of $m$ larger than 12 seem to give sensible predictions.

---

[← Example of Regression with functions of time: USA Accidents Dataset](02-example-of-regression-with-functions-of-time-usa-accidents-d.md) · [Up: contents](index.md)
