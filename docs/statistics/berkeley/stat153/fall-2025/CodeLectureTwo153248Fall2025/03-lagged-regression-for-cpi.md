---
title: Lagged Regression for CPI
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lagged Regression for CPI

**Source:** [`CodeLectureTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Next let us look at lagged regression, where the covariate is chosen to be $x_i = y_{i-1}$ (i.e., the covariate value for time index i equals the response value for the previous time index).

```python
yreg = yvec[1:]
xreg = yvec[:-1]
Xmat = sm.add_constant(xreg)
armod = sm.OLS(yreg, Xmat).fit()
print(armod.summary())
print(armod.params)
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 6.245e+07
Date:                Tue, 02 Sep 2025   Prob (F-statistic):               0.00
Time:                        21:31:13   Log-Likelihood:                 4019.3
No. Observations:                 942   AIC:                            -8035.
Df Residuals:                     940   BIC:                            -8025.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0039      0.001      6.707      0.000       0.003       0.005
x1             0.9998      0.000   7902.303      0.000       1.000       1.000
==============================================================================
Omnibus:                      129.091   Durbin-Watson:                   0.855
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              640.198
Skew:                           0.519   Prob(JB):                    9.61e-140
Kurtosis:                       6.903   Cond. No.                         24.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[0.00387065 0.9997775 ]
```

Note that the estimated value of $\beta$ is 0.9998 which is fairly close to 1. Because of this, this AutoRegression model can be treated as approximately trying to fit a constant to the month-to-month inflation rate, as shown below.

The regression model corresponding to the output above is:
\begin{equation*}
  \log \text{CPI}_t = \beta_0 + \beta_1 \log \text{CPI}_{t-1} + \epsilon_t
\end{equation*}
This fitted coefficients are $\hat{\beta}_0 = 0.0039$ and $\hat{\beta}_1 = 0.9998 \approx 1$. Thus the fitted model is approximately:
\begin{equation*}
   \log \text{CPI}_t \approx 0.0039 + \log \text{CPI}_{t-1} + \epsilon_t,
\end{equation*}
or equivalently
\begin{equation*}
    \log \text{CPI}_t - \log \text{CPI}_{t-1} \approx 0.0039 +  \epsilon_t,
\end{equation*}
which is again the same as
\begin{equation*}
   100 \times \log \frac{\text{CPI}_t}{\text{CPI}_{t-1}} \approx 0.39 + \text{error}
\end{equation*}
So this model is giving a historical inflation rate estimate (month-to-month) of $0.39\%$ which is equivalent to a historic annual inflation rate estimate of $12 \times 0.39$:

```python
historical_inflation_rate_armodel = 12 * 100 * armod.params[0] #armod.params[0] is the estimate of beta_0
print(f'Historical annual inflation rate (AR(1) model): {historical_inflation_rate_armodel:.3f}%')
```

```
Historical annual inflation rate (AR(1) model): 4.645%
```

This estimate of $4.645\%$ is somewhat higher than the estimate $3.794\%$ obtained by the previous regression (where the covariate was time). This increase is the estimate is because of the approximation 0.9998 vs 1. Note that the correct model (without the approximation 0.9998 vs 1) is:
\begin{equation*}
    \log \text{CPI}_t - 0.9998 * \log \text{CPI}_{t-1} = 0.0039 +  \epsilon_t,
\end{equation*}
which is equivalent to
\begin{equation*}
    \log \frac{\text{CPI}_t}{\text{CPI}_{t-1}} = 0.0039 - 0.0002 * \log \text{CPI}_{t-1} +  \epsilon_t,
\end{equation*}
The variable $0.0002 * \log \text{CPI}_{t-1}$ is not exactly negligble; it has a mean of about 0.0008 (see below) which will have an effect of reducing 0.0039 by some amount.

```python
np.mean(0.0002 * yvec[:-1])
```

```
0.0008953722086746689
```

The uncertainty interval associated with the estimate of $\beta_0$ is given by:

```python
# 95% confidence intervals
conf_intervals = armod.conf_int(alpha=0.05)
print(conf_intervals)
```

```
[[0.00273806 0.00500324]
 [0.99952921 1.00002579]]
```

Multiplying the interval above for $\beta_0$ by $12 * 100$, we get an estimate of the historical inflation rate (with again the caveat that this will be slightly inflated because of the approximation $0.9998 \approx 1$)

```python
#So the uncertainty interval for the estimated historical annual inflation rate is:
print(f'95% confidence interval for historical annual inflation rate (AR(1) model): [{12*100*conf_intervals[0,0]:.3f}%, {12*100*conf_intervals[0,1]:.3f}%]')
```

```
95% confidence interval for historical annual inflation rate (AR(1) model): [3.286%, 6.004%]
```

Compare this interval $[3.286, 6.004] \%$ (which is much wider) with the previous one $[3.749, 3.84]\%$.

To check how well this second model (AutoRegression) fits the data, we can plot the values of $100 \times \log \frac{\text{CPI}_t}{\text{CPI}_{t-1}}$ with time:

```python
#Plot the values of 12 * 100 * log(CPI_t / CPI_{t-1}) with time
inflation_rates = 12 * 100 * (yvec[1:] - yvec[:-1])
dates = cpi.index[1:]
plt.figure(figsize=(12,7))
plt.plot(dates, inflation_rates, label='Annual Inflation Rate')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.title('Annual Inflation Rate based on CPI')
plt.axhline(y=historical_inflation_rate_armodel, color='r', linestyle='--', label='Estimated Historical Inflation Rate (AR(1) model)')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The individual inflation rates vary quite widely, so it is natural for the uncertainty interval for the inflation rate to be somewhat wide (unlike the interval that we got from the regression with time model).

Let us plot the mean of the inflation rates. It is below the estimate that we got from the AutoRegression because of the approximation $0.9998 \approx 1$.

```python
#Plot the values of 12 * 100 * log(CPI_t / CPI_{t-1}) with time
inflation_rates = 12 * 100 * (np.exp(yvec[1:]) - np.exp(yvec[:-1]))/np.exp(yvec[:-1])
dates = cpi.index[1:]
plt.figure(figsize=(12,7))
plt.plot(dates, inflation_rates, label='Annual Inflation Rate')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')
plt.title('Annual Inflation Rate based on CPI')
plt.axhline(y=historical_inflation_rate_armodel, color='r', linestyle='--', label='Estimated Historical Inflation Rate (AR(1) model)')
plt.axhline(y=np.mean(inflation_rates), color='b', linestyle='--', label='Mean Historical Inflation Rate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This was just an illustration of how regressions can be used for time series data. We shall study AutoRegressions in much more detail later.

---

[← CPI Regression with Time as Covariate](02-cpi-regression-with-time-as-covariate.md) · [Up: contents](index.md)
