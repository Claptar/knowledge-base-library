---
title: each time (for example, when generating white noise)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# each time (for example, when generating white noise)

**Source:** [`public/lectures/Lecture5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
```

First we'll start with a simple example where we have a linear trend plus noise. We'll take a sample from this function and try to fit a regression line to predict $y$ from $t$.

```python
t = np.arange(1, 101)
sigma = 4 # If sigma=1, standard normal
y = 2 + 0.5*t + sigma*np.random.randn(len(t))

plt.plot(t,y,label='y=2+0.5t+w')
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.legend()
```

```
<matplotlib.legend.Legend at 0x168d86560>
```

*(1 figure omitted — see the original notebook.)*

We will fit the simple model

$$y_i = \beta_0 + \beta_1 t + \epsilon_i$$

using Ordinary Least Squares (OLS) in the `statsmodels` library.

```python
linreg_simple = sm.OLS(y, t).fit()
print(linreg_simple.summary())
```

```
OLS Regression Results
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.986
Model:                            OLS   Adj. R-squared (uncentered):              0.986
Method:                 Least Squares   F-statistic:                              6862.
Date:                Tue, 03 Feb 2026   Prob (F-statistic):                    3.01e-93
Time:                        19:51:25   Log-Likelihood:                         -271.87
No. Observations:                 100   AIC:                                      545.7
Df Residuals:                      99   BIC:                                      548.3
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.5250      0.006     82.834      0.000       0.512       0.538
==============================================================================
Omnibus:                        0.411   Durbin-Watson:                   1.979
Prob(Omnibus):                  0.814   Jarque-Bera (JB):                0.259
Skew:                          -0.125   Prob(JB):                        0.879
Kurtosis:                       3.011   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We can see that our regression recovered the coefficient $x1=0.5286$, which is pretty close to our true $\beta_1=0.5$, but it's not quite right because we didn't get the intercept $\beta_0$. When we show the fitted line, we can see that the best fit line should be shifted up.

```python
plt.plot(t,y)
plt.plot(t,linreg_simple.fittedvalues)
plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
```

```
Text(0, 0.5, 'y')
```

*(1 figure omitted — see the original notebook.)*

We can fix this by adding a constant term to our OLS fit, as follows:

```python
T = sm.add_constant(t)
linreg_simple2 = sm.OLS(y, T).fit()
print(linreg_simple2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.942
Model:                            OLS   Adj. R-squared:                  0.942
Method:                 Least Squares   F-statistic:                     1601.
Date:                Tue, 03 Feb 2026   Prob (F-statistic):           1.62e-62
Time:                        19:51:25   Log-Likelihood:                -270.29
No. Observations:                 100   AIC:                             544.6
Df Residuals:                      98   BIC:                             549.8
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.3032      0.735      1.773      0.079      -0.155       2.762
x1             0.5056      0.013     40.010      0.000       0.480       0.531
==============================================================================
Omnibus:                        0.521   Durbin-Watson:                   2.042
Prob(Omnibus):                  0.771   Jarque-Bera (JB):                0.518
Skew:                          -0.167   Prob(JB):                        0.772
Kurtosis:                       2.885   Cond. No.                         117.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

We can also report the confidence intervals on our estimates of $\beta_0$ and $\beta_1$, which can be useful for determining our certainty of these estimates.

```python
ci_linreg_simple2 = linreg_simple2.conf_int(alpha=0.05)
print(ci_linreg_simple2)
print(f'95% confidence interval for B0$: [{ci_linreg_simple2[0,0]:.3f}, {ci_linreg_simple2[0,1]:.3f}]')
print(f'95% confidence interval for B1$: [{ci_linreg_simple2[1,0]:.3f}, {ci_linreg_simple2[1,1]:.3f}]')
```

```
[[-0.15543644  2.76178753]
 [ 0.48049713  0.53064895]]
95% confidence interval for B0$: [-0.155, 2.762]
95% confidence interval for B1$: [0.480, 0.531]
```

```python
plt.plot(t,y)
plt.plot(t,linreg_simple2.fittedvalues)
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

## Another (messier) example

Now let's load some data from `astsa`, for example, the price of chicken over time, from 2001 to 2016. As pointed out in your book, commodities (such as raw materials, basic resources, agricultural, or mining products) show specific fluctuations in their prices over time. For this example, we'll fit a regression model for chicken prices as our response $y$ and time as our predictor $x$.

```python
chicken_data = astsa.load_chicken()
print(chicken_data)
```

```
Time   Value
0    2001-08   65.58
1    2001-09   66.48
2    2001-10   65.70
3    2001-11   64.33
4    2001-12   63.23
..       ...     ...
175  2016-03  111.56
176  2016-04  111.55
177  2016-05  111.98
178  2016-06  111.84
179  2016-07  111.46

[180 rows x 2 columns]
```

```python
plt.plot(chicken_data['Time'], chicken_data['Value'])
```

```
[<matplotlib.lines.Line2D at 0x1690fc790>]
```

*(1 figure omitted — see the original notebook.)*

```python
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
linreg = sm.OLS(yvec, xvec).fit()
print(linreg.summary())
```

```
OLS Regression Results
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.885
Model:                            OLS   Adj. R-squared (uncentered):              0.885
Method:                 Least Squares   F-statistic:                              1381.
Date:                Tue, 03 Feb 2026   Prob (F-statistic):                    4.53e-86
Time:                        19:51:26   Log-Likelihood:                         -864.85
No. Observations:                 180   AIC:                                      1732.
Df Residuals:                     179   BIC:                                      1735.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.7862      0.021     37.157      0.000       0.744       0.828
==============================================================================
Omnibus:                       81.414   Durbin-Watson:                   0.001
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               12.683
Skew:                           0.251   Prob(JB):                      0.00176
Kurtosis:                       1.800   Cond. No.                         1.00
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

Here, notice that in the table only one coefficient, $x1$ is reported. This is because we have not actually fit the model $y_i = \beta_0 + \beta_1 x_i + \epsilon_i$. Instead, we have fit the model without an intercept: $y_i = \beta_1 x_1$. If we do want to include a $\beta_0$ term, we need to add a constant to our model.

```python
X = sm.add_constant(xvec)
print(X)
```

```
[[  1.   1.]
 [  1.   2.]
 [  1.   3.]
 [  1.   4.]
 [  1.   5.]
 [  1.   6.]
 [  1.   7.]
 [  1.   8.]
 [  1.   9.]
 [  1.  10.]
 [  1.  11.]
 [  1.  12.]
 [  1.  13.]
 [  1.  14.]
 [  1.  15.]
 [  1.  16.]
 [  1.  17.]
 [  1.  18.]
 [  1.  19.]
 [  1.  20.]
 [  1.  21.]
 [  1.  22.]
 [  1.  23.]
 [  1.  24.]
 [  1.  25.]
 [  1.  26.]
 [  1.  27.]
 [  1.  28.]
 [  1.  29.]
 [  1.  30.]
 [  1.  31.]
 [  1.  32.]
 [  1.  33.]
 [  1.  34.]
 [  1.  35.]
 [  1.  36.]
 [  1.  37.]
 [  1.  38.]
 [  1.  39.]
 [  1.  40.]
 [  1.  41.]
 [  1.  42.]
 [  1.  43.]
 [  1.  44.]
 [  1.  45.]
 [  1.  46.]
 [  1.  47.]
 [  1.  48.]
 [  1.  49.]
 [  1.  50.]
 [  1.  51.]
 [  1.  52.]
 [  1.  53.]
 [  1.  54.]
 [  1.  55.]
 [  1.  56.]
 [  1.  57.]
 [  1.  58.]
 [  1.  59.]
 [  1.  60.]
 [  1.  61.]
 [  1.  62.]
 [  1.  63.]
 [  1.  64.]
 [  1.  65.]
 [  1.  66.]
 [  1.  67.]
 [  1.  68.]
 [  1.  69.]
 [  1.  70.]
 [  1.  71.]
 [  1.  72.]
 [  1.  73.]
 [  1.  74.]
 [  1.  75.]
 [  1.  76.]
 [  1.  77.]
 [  1.  78.]
 [  1.  79.]
 [  1.  80.]
 [  1.  81.]
 [  1.  82.]
 [  1.  83.]
 [  1.  84.]
 [  1.  85.]
 [  1.  86.]
 [  1.  87.]
 [  1.  88.]
 [  1.  89.]
 [  1.  90.]
 [  1.  91.]
 [  1.  92.]
 [  1.  93.]
 [  1.  94.]
 [  1.  95.]
 [  1.  96.]
 [  1.  97.]
 [  1.  98.]
 [  1.  99.]
 [  1. 100.]
 [  1. 101.]
 [  1. 102.]
 [  1. 103.]
 [  1. 104.]
 [  1. 105.]
 [  1. 106.]
 [  1. 107.]
 [  1. 108.]
 [  1. 109.]
 [  1. 110.]
 [  1. 111.]
 [  1. 112.]
 [  1. 113.]
 [  1. 114.]
 [  1. 115.]
 [  1. 116.]
 [  1. 117.]
 [  1. 118.]
 [  1. 119.]
 [  1. 120.]
 [  1. 121.]
 [  1. 122.]
 [  1. 123.]
 [  1. 124.]
 [  1. 125.]
 [  1. 126.]
 [  1. 127.]
 [  1. 128.]
 [  1. 129.]
 [  1. 130.]
 [  1. 131.]
 [  1. 132.]
 [  1. 133.]
 [  1. 134.]
 [  1. 135.]
 [  1. 136.]
 [  1. 137.]
 [  1. 138.]
 [  1. 139.]
 [  1. 140.]
 [  1. 141.]
 [  1. 142.]
 [  1. 143.]
 [  1. 144.]
 [  1. 145.]
 [  1. 146.]
 [  1. 147.]
 [  1. 148.]
 [  1. 149.]
 [  1. 150.]
 [  1. 151.]
 [  1. 152.]
 [  1. 153.]
 [  1. 154.]
 [  1. 155.]
 [  1. 156.]
 [  1. 157.]
 [  1. 158.]
 [  1. 159.]
 [  1. 160.]
 [  1. 161.]
 [  1. 162.]
 [  1. 163.]
 [  1. 164.]
 [  1. 165.]
 [  1. 166.]
 [  1. 167.]
 [  1. 168.]
 [  1. 169.]
 [  1. 170.]
 [  1. 171.]
 [  1. 172.]
 [  1. 173.]
 [  1. 174.]
 [  1. 175.]
 [  1. 176.]
 [  1. 177.]
 [  1. 178.]
 [  1. 179.]
 [  1. 180.]]
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
Date:                Tue, 03 Feb 2026   Prob (F-statistic):           2.83e-98
Time:                        19:51:28   Log-Likelihood:                -532.83
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

Now we have an estimate of $\beta_0 = 58.5832$ and an estimate of $\beta_1=0.2993$. What this means is that the price of chicken is going up by approximately 0.30 cents per pound per month, and had started at a base price of 58.5 cents per pound.

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
#plt.plot(chicken_data.index, linreg.fittedvalues, label='No B0')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Value', fontsize=18)
plt.title('Chicken prices (U.S. cents/pound)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);
plt.legend()
```

```
<matplotlib.legend.Legend at 0x169618af0>
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
plot_acf(residuals, lags=40, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

---

[← Set the random seed, this is so you will generate the same answers](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md) · [Up: contents](index.md)
