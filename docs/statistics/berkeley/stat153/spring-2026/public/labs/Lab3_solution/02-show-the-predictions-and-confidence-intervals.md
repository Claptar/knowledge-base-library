---
title: Show the predictions and confidence intervals
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Show the predictions and confidence intervals

If we want to show the predicted data and confidence intervals for the fitted values, we can use `get_prediction`. We will then produce `pred_summary`, which contains:
* `mean` - fitted values
* `mean_ci_lower`, `mean_ci_upper` - confidence intervals for the mean
* `obs_ci_lower`, `obs_ci_upper` - prediction interval for new observations

```python
# To show the confidence intervals on the data, we can use the `get_prediction` method
#
pred = linreg_simple2.get_prediction(T)
pred_ci = pred.conf_int(alpha=0.05)
pred_summary = pred.summary_frame(alpha=0.05)

plt.plot(t,y)
plt.plot(t, pred_summary['mean'])
plt.fill_between(t, pred_summary['mean_ci_lower'], pred_summary['mean_ci_upper'], alpha=0.3, label="95% CI (mean)")
#plt.fill_between(t, pred_summary['obs_ci_lower'], pred_summary['obs_ci_upper'], alpha=0.3, label="95% CI (mean)")

plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
```

```
Text(0, 0.5, 'y')
```

*(1 figure omitted — see the original notebook.)*

For time series, one thing we want to check is that our residuals (the difference between the predicted data and our actual value) are weakly stationary, which allows us to assume that our error $\epsilon_t$ is weakly stationary.

We can do that by plotting the residuals over time as well as the autocorrelation function of the residuals. How does this look?

```python
residuals = linreg_simple2.resid

plt.figure()
plt.plot(t,residuals)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('t')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals, lags=40, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

## The chicken example

Now let's load some data from `astsa`, for example, the price of chicken over time, from 2001 to 2016. As pointed out in your book, commodities (such as raw materials, basic resources, agricultural, or mining products) show specific fluctuations in their prices over time. For this example, we'll fit a regression model for chicken prices as our response $y$ and time as our predictor $x$.

```python
chicken_data = astsa.load_chicken()
# Fix the time index
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
# Now let's fit a regression to this:

yvec = np.array(chicken_smoothed)
n = len(yvec) # number of time points
xvec = np.arange(1, n+1)
X = sm.add_constant(xvec)
linreg_smooth = sm.OLS(yvec, X).fit()
print(linreg_smooth.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                         nan
Model:                            OLS   Adj. R-squared:                    nan
Method:                 Least Squares   F-statistic:                       nan
Date:                Thu, 05 Feb 2026   Prob (F-statistic):                nan
Time:                        12:20:04   Log-Likelihood:                    nan
No. Observations:                 180   AIC:                               nan
Df Residuals:                     178   BIC:                               nan
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const             nan        nan        nan        nan         nan         nan
x1                nan        nan        nan        nan         nan         nan
==============================================================================
Omnibus:                          nan   Durbin-Watson:                     nan
Prob(Omnibus):                    nan   Jarque-Bera (JB):                  nan
Skew:                             nan   Prob(JB):                          nan
Kurtosis:                         nan   Cond. No.                         210.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We got nans ("Not a Number"/undefined)! Why did this happen? It turns out when we defined our moving average, we only calculated the windowed average once we got enough samples, so the beginning and end of our function is now undefined.

To make this work out, we have to remove the nan values as follows:

```python
yvec = np.array(chicken_smoothed[~np.isnan(chicken_smoothed)]) # Take only the points that are *not* NaN (that's what ~ is shorthand for)
n = len(yvec) # number of time points
xvec = np.arange(1, n+1)
print(len(yvec), len(xvec))
X = sm.add_constant(xvec)
linreg_smooth = sm.OLS(yvec, X).fit()
print(linreg_smooth.summary())
```

```
144 144
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.949
Model:                            OLS   Adj. R-squared:                  0.949
Method:                 Least Squares   F-statistic:                     2635.
Date:                Thu, 05 Feb 2026   Prob (F-statistic):           1.41e-93
Time:                        12:20:05   Log-Likelihood:                -353.12
No. Observations:                 144   AIC:                             710.2
Df Residuals:                     142   BIC:                             716.2
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         63.8031      0.474    134.568      0.000      62.866      64.740
x1             0.2912      0.006     51.336      0.000       0.280       0.302
==============================================================================
Omnibus:                       15.433   Durbin-Watson:                   0.005
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                8.071
Skew:                           0.395   Prob(JB):                       0.0177
Kurtosis:                       2.150   Cond. No.                         168.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
residuals_smooth = linreg_smooth.resid

# Make sure we get the new time index as well
half_win = smoothing_win // 2
new_t = [chicken_data.index[a] for a in np.arange(half_win, len(chicken_data.index) - half_win)]

plt.figure()
plt.plot(new_t,residuals_smooth)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('Date')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals_smooth, lags=100, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show();
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

As it turns out, there are still pretty strong autocorrelations in these data, even when we apply the moving average, so probably we will want to do some differencing or other transformations first.

---

[← Lab 3 Solutions - Stat 153/248](01-lab-3-solutions---stat-153-248.md) · [Up: contents](index.md) · [Lecture 6 review →](03-lecture-6-review.md)
