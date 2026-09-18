---
title: Chicken price regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Chicken price regression

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

[← Another (messier) example](02-another-messier-example.md) · [Up: contents](index.md)
