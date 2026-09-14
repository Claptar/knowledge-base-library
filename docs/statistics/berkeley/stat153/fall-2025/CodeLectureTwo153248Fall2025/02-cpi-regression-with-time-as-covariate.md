---
title: CPI Regression with Time as Covariate
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CPI Regression with Time as Covariate

**Source:** [`CodeLectureTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We will fit a linear regression model to the CPI data, with time as the covariate. The simplest model is:
\begin{equation*}
  y_i = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation*}
where $y_i$ denotes the CPI for time index $i$, and $x_i = i$. The interpretation of $\beta_1$ is that it represents the numerical change in CPI for one month to the next. This is not a good model for CPI, because the relationship between CPI and data does not appear to be linear. Also CPI increases are usually reported in percentages (e.g., inflation is now at 2.8% etc.), and not in raw numerical increase. A better linear regression model here would use $y_i$ as the **logarithm** of CPI for time index $i$:
\begin{equation*}
  y_i = \log(\text{CPI}_i) = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation*}
where $x_i = i$ as before. Now the interpretation of $\beta_1$ is that it represents the numerical change in $\log \text{CPI}_i$ for one month to the next. Note that
\begin{equation*}
   \log \text{CPI}_i - \log \text{CPI}_{i-1} = \log \frac{\text{CPI}_i}{\text{CPI}_{i-1}} \approx \frac{\text{CPI}_i}{\text{CPI}_{i-1}}  - 1 = \frac{\text{CPI}_i - \text{CPI}_{i-1}}{\text{CPI}_{i-1}}
\end{equation*}
In other words, $100 \times \beta_1$ represents the **percent change** in CPI from one month to the next. If we want the percent change for one year (as opposed to one month), we can look at $12 \times 100 \times \beta_1$. This number can be taken to represent an estimate of the historical inflation rate.

```python
plt.figure(figsize=(6,4))
plt.plot(cpi.index, np.log(cpi['CPIAUCSL']), label='Logarithm of CPI')
plt.xlabel('Year')
plt.ylabel('Log(CPI)')
plt.title('Logarithm of Consumer Price Index (CPI)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The process of using the observed data to obtain estimates of the unknown parameters (in this case $\beta_0$ and $\beta_1$) is known as ** Model Fitting **. For the linear regression model, model fitting will be done using the OLS function from the statsmodels library.

```python
import statsmodels.api as sm
```

We need to input the observed response values $y_1, \dots, y_n$ as well as the covariate values $x_1, \dots, x_n$ (remember that we are using $x_i = i$).

```python
yvec = np.log(np.array(cpi['CPIAUCSL']))
n = cpi.shape[0]
xvec = np.arange(1, n+1)
linreg = sm.OLS(yvec, xvec).fit()
print(linreg.summary())
```

```
OLS Regression Results
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.892
Model:                            OLS   Adj. R-squared (uncentered):              0.892
Method:                 Least Squares   F-statistic:                              7771.
Date:                Tue, 02 Sep 2025   Prob (F-statistic):                        0.00
Time:                        16:08:51   Log-Likelihood:                         -1720.7
No. Observations:                 943   AIC:                                      3443.
Df Residuals:                     942   BIC:                                      3448.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.0079   8.97e-05     88.151      0.000       0.008       0.008
==============================================================================
Omnibus:                      148.417   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               37.391
Skew:                          -0.138   Prob(JB):                     7.60e-09
Kurtosis:                       2.064   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

In the context of the linear regression model, the parameters $\beta_0$ and $\beta_1$ are also known as the coefficients. The table in the output above reports only one coefficient value. Actually the function sm.OLS(yvec, xvec).fit() is not fitting our intended model $y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ but it is fitting instead $y_i = \beta_1 x_i + \epsilon_i$ (i.e., it is not using $\beta_0$). To enable $\beta_0$, we need to do the following:

```python
X = sm.add_constant(xvec)
linreg2 = sm.OLS(yvec, X).fit()
print(linreg2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.966
Model:                            OLS   Adj. R-squared:                  0.966
Method:                 Least Squares   F-statistic:                 2.695e+04
Date:                Tue, 02 Sep 2025   Prob (F-statistic):               0.00
Time:                        16:10:36   Log-Likelihood:                 385.22
No. Observations:                 943   AIC:                            -766.4
Df Residuals:                     941   BIC:                            -756.7
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.9859      0.010    284.536      0.000       2.965       3.006
x1             0.0032   1.93e-05    164.171      0.000       0.003       0.003
==============================================================================
Omnibus:                     8570.174   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               72.093
Skew:                          -0.026   Prob(JB):                     2.21e-16
Kurtosis:                       1.646   Cond. No.                     1.09e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.09e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

From this table, we see that the estimate of $\beta_0$ is 2.9859 and the estimate of $\beta_1$ is 0.0032. As per our interpretation, the month-to-month inflation rate is $100 \times \beta_1$ which is $0.32 \%$. If we want the annual inflation rate, we would have to multiply this by 12 which gives:

```python
historical_inflation_rate = 12 * 100 * linreg2.params[1]
print(f'Historical annual inflation rate: {historical_inflation_rate:.3f}%')
```

```
Historical annual inflation rate: 3.794%
```

The regression output also gives an indication of the uncertainty associated with this inflation estimate:

```python
conf_intervals_linreg2 = linreg2.conf_int(alpha=0.05)
print(conf_intervals_linreg2)
print(f'95% confidence interval for historical annual inflation rate (Linear Regression model): [{12*100*conf_intervals_linreg2[1,0]:.3f}%, {   12*100*conf_intervals_linreg2[1,1]:.3f}%]')
```

```
[[2.96527443 3.00646247]
 [0.003124   0.00319959]]
95% confidence interval for historical annual inflation rate (Linear Regression model): [3.749%, 3.840%]
```

```python
plt.figure(figsize=(6,4))
plt.plot(cpi.index, cpi['CPIAUCSL'], label='CPI')
plt.xlabel('Year')
plt.plot(cpi.index, np.exp(linreg2.fittedvalues))
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From this plot, it is clear that this regression model may not do a good job in predicting the values of CPI for the next few months.

```python
plt.figure(figsize=(6,4))
plt.plot(cpi.index, np.log(cpi['CPIAUCSL']), label='Logarithm of CPI')
plt.xlabel('Year')
plt.plot(cpi.index, linreg2.fittedvalues)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Lagged Regression for CPI →](03-lagged-regression-for-cpi.md)
