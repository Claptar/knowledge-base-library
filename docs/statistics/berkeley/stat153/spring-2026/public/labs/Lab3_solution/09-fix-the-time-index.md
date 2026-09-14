---
title: Fix the time index
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fix the time index

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

chicken_data['Time'] = pd.to_datetime(chicken_data['Time'])
chicken_data.set_index('Time', inplace=True)
print(chicken_data)
```

```
Value
Time
2001-08-01   65.58
2001-09-01   66.48
2001-10-01   65.70
2001-11-01   64.33
2001-12-01   63.23
...            ...
2016-03-01  111.56
2016-04-01  111.55
2016-05-01  111.98
2016-06-01  111.84
2016-07-01  111.46

[180 rows x 1 columns]
```

```python
plt.figure(figsize=(8,6))
plt.plot(chicken_data.index, chicken_data['Value'], label='Value')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Value', fontsize=18)
plt.title('Chicken prices (U.S. cents/pound)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);
```

*(1 figure omitted — see the original notebook.)*

## Chicken price regression

We will fit a linear regression model to the chicken price data using time as the covariate. Here, the model is:

$$y_i = \beta_0 + \beta_1 x_i + \epsilon_i$$

where $y_i$ is the price of chicken at time index $i$, and $x_i = i$. We can interpret the coefficient $\beta_1$ as the numerical change in price of chicken from one month to the next (since each time step is in one month). From just looking at the graph, we know that the linear fit is likely not the best model for these data, since there are also underlying (potentially seasonal) fluctuations in the data. Still, we may be interested in the overall trend in price increases for this commodity.

We can then use statsmodels to fit the OLS solution for the line of best fit to the data.

```python
yvec = np.array(chicken_data['Value'])
n = len(yvec) # number of time points
xvec = np.arange(1, n+1)
X = sm.add_constant(xvec)
linreg2 = sm.OLS(yvec, X).fit()
print(linreg2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.917
Model:                            OLS   Adj. R-squared:                  0.917
Method:                 Least Squares   F-statistic:                     1974.
Date:                Thu, 05 Feb 2026   Prob (F-statistic):           2.83e-98
Time:                        11:23:23   Log-Likelihood:                -532.83
No. Observations:                 180   AIC:                             1070.
Df Residuals:                     178   BIC:                             1076.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         58.5832      0.703     83.331      0.000      57.196      59.971
x1             0.2993      0.007     44.434      0.000       0.286       0.313
==============================================================================
Omnibus:                        9.576   Durbin-Watson:                   0.046
Prob(Omnibus):                  0.008   Jarque-Bera (JB):                4.204
Skew:                           0.018   Prob(JB):                        0.122
Kurtosis:                       2.252   Cond. No.                         210.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
linreg2 = sm.OLS(yvec, X).fit()
print(linreg2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.917
Model:                            OLS   Adj. R-squared:                  0.917
Method:                 Least Squares   F-statistic:                     1974.
Date:                Thu, 05 Feb 2026   Prob (F-statistic):           2.83e-98
Time:                        11:23:23   Log-Likelihood:                -532.83
No. Observations:                 180   AIC:                             1070.
Df Residuals:                     178   BIC:                             1076.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         58.5832      0.703     83.331      0.000      57.196      59.971
x1             0.2993      0.007     44.434      0.000       0.286       0.313
==============================================================================
Omnibus:                        9.576   Durbin-Watson:                   0.046
Prob(Omnibus):                  0.008   Jarque-Bera (JB):                4.204
Skew:                           0.018   Prob(JB):                        0.122
Kurtosis:                       2.252   Cond. No.                         210.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

Now we have an estimate of $\beta_0$ (`const`) and an estimate of $\beta_1$ (`x1`). What this means is that the price of chicken is going up by approximately 0.30 cents per pound per month, and had started at a base price of 58.5 cents per pound.

We can also calculate the confidence intervals to understand the uncertainty associated with the estimate.

```python
ci_linreg2 = linreg2.conf_int(alpha=0.05)
print(ci_linreg2)
print(f'95% confidence interval for price fluctuation: [{ci_linreg2[1,0]:.2f}, {ci_linreg2[1,1]:.2f}]')
```

```
[[57.19590866 59.97056185]
 [ 0.28604822  0.31263657]]
95% confidence interval for price fluctuation: [0.29, 0.31]
```

Now let's plot the regression line on the original data.

```python
plt.figure(figsize=(8,6))
plt.plot(chicken_data.index, chicken_data['Value'], label='Value')
plt.plot(chicken_data.index, linreg2.fittedvalues, label='y=B0+B1x')
plt.axhline(chicken_data['Value'].mean(), color='r', label='mean price')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Value', fontsize=18)
plt.title('Chicken prices (U.S. cents/pound)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);
plt.legend()
```

```
<matplotlib.legend.Legend at 0x16cce5d50>
```

*(1 figure omitted — see the original notebook.)*

What are some problems with this? Do our residuals show any strong or unmodeled dependence on time?

```python
residuals = linreg2.resid

plt.figure()
plt.plot(chicken_data.index,residuals)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('Date')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals, lags=80, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

What if we took a moving average of the chicken data to smooth out some of the fluctuations? Here we will smooth over a 3 year + 1 month window (we are choosing an odd length window so it is centered around our observations).

```python
def moving_average(w, n):
    '''
    Create an acausal moving average of the time series `w` using an `n`-point moving average
    '''
    v = np.zeros((len(w),)) * np.nan
    half_win = n // 2
    for t in np.arange(half_win, len(w) - half_win):
        v[t] = np.mean(w[t-half_win : t+half_win+1])
    return v

smoothing_win = 3*12+1 # 3 years * 12 months/year + 1 to make it an odd #
chicken_smoothed = moving_average(chicken_data['Value'], n=smoothing_win)
plt.plot(chicken_data.index,chicken_data['Value'], label='original')
plt.plot(chicken_data.index,chicken_smoothed, label='smoothed')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
```

```
<matplotlib.legend.Legend at 0x17d673220>
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← To show the confidence intervals on the data, we can use the getprediction method](08-to-show-the-confidence-intervals-on-the-data-we-can-use-the.md) · [Up: contents](index.md) · [Now let's fit a regression to this →](10-now-let-s-fit-a-regression-to-this.md)
