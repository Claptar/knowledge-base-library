---
title: Inflation (Consumer Price Index)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFive153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Inflation (Consumer Price Index)

**Source:** [`CodeLectureFive153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

cpi = pd.read_csv('CPIAUCSL_01September2025.csv')
cpi['observation_date'] = pd.to_datetime(cpi['observation_date'])
cpi.set_index('observation_date', inplace = True)
print(cpi)
```

```
CPIAUCSL
observation_date
1947-01-01          21.480
1947-02-01          21.620
1947-03-01          22.000
1947-04-01          22.000
1947-05-01          21.950
...                    ...
2025-03-01         319.615
2025-04-01         320.321
2025-05-01         320.580
2025-06-01         321.500
2025-07-01         322.132

[943 rows x 1 columns]
```

```python
plt.plot(cpi.index, cpi['CPIAUCSL'], label='CPI')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.title('Consumer Price Index (CPI)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We fit a simple linear regression model to this dataset with $y$ being the logarithm of CPI and $x$ being time:
\begin{equation*}
  y_i = \log(\text{CPI}_i) = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation*}
where $x_i = i$. We saw that we can interpret $100 \times \beta_1$ as the **percent change** in CPI from one month to the next. If we want the percent change for one year (as opposed to one month), we can look at $12 \times 100 \times \beta_1$. This number can be taken to represent an estimate of the historical inflation rate.

```python
#Below we plot the log CPI as a function of time:
plt.plot(cpi.index, np.log(cpi['CPIAUCSL']), label='Logarithm of CPI')
plt.xlabel('Year')
plt.ylabel('Log(CPI)')
plt.title('Logarithm of Consumer Price Index (CPI)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The linear regression model is fitted to the data as follows.

```python
y = np.log(np.array(cpi['CPIAUCSL']))
n = cpi.shape[0]
X = np.column_stack((np.ones(n), np.arange(n)))
linreg = sm.OLS(y, X).fit()
print(linreg.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.966
Model:                            OLS   Adj. R-squared:                  0.966
Method:                 Least Squares   F-statistic:                 2.695e+04
Date:                Thu, 11 Sep 2025   Prob (F-statistic):               0.00
Time:                        16:28:35   Log-Likelihood:                 385.22
No. Observations:                 943   AIC:                            -766.4
Df Residuals:                     941   BIC:                            -756.7
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.9890      0.010    285.290      0.000       2.968       3.010
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

The parameter estimates, their standard errors, as well as confidence intervals can be obtained from the regression output as follows.

```python
print(linreg.params) #these are the betahats (least squares estimates)
print(linreg.bse) #these are the standard errors of the betahats
print(linreg.conf_int(alpha=0.05)) #these are the 95%
```

```
[2.98903025 0.0031618 ]
[1.04771516e-02 1.92591769e-05]
[[2.96846896 3.00959154]
 [0.003124   0.00319959]]
```

We can obtain these manually using the formulae that we derived and check if we are getting exactly the same answers.

```python
#For betahat:
betahat = np.linalg.inv(X.T @ X) @ X.T @ y
print(betahat)
#For standard errors:
residuals = y - X @ betahat
sigma2hat = (residuals.T @ residuals) / (n - X.shape[1])
var_betahat = sigma2hat * np.linalg.inv(X.T @ X)
se_betahat = np.sqrt(np.diag(var_betahat))
print(se_betahat)
#For confidence intervals:
from scipy.stats import t
alpha = 0.05
t_critical = t.ppf(1 - alpha/2, df=n - X.shape[1]) #this computes t_{df, 1-alpha/2}
conf_int_lower = betahat - t_critical * se_betahat
conf_int_upper = betahat + t_critical * se_betahat
conf_int = np.column_stack((conf_int_lower, conf_int_upper))
print(conf_int)
```

```
[2.98903025 0.0031618 ]
[1.04771516e-02 1.92591769e-05]
[[2.96846896 3.00959154]
 [0.003124   0.00319959]]
```

---

[Up: contents](index.md) · [Nonlinear Regression →](02-nonlinear-regression.md)
