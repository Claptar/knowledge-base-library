---
title: 'Model 6: Two change of slope points'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model 6: Two change of slope points

Next we fit a modification of Model 5 which has two change of slope points:
\begin{align*}
   g_t = \beta_0 + + \beta_1 t + \beta_2 (t - c_1)_+ + \beta_3 (t - c_2)_+ + \epsilon_t.
\end{align*}
This fits a curve with two different slopes. Assuming $c_1 < c_2$, the slopes are $\beta_1$ (before $c_1$), $\beta_1 + \beta_2$ (between $c_1$ and $c_2$) and $\beta_1 + \beta_2 + \beta_3$ after $c_2$. We will treat $c_1, c_2$ as unknown and estimate them from the data. We will go over the estimation strategy later in detail (essentially, we go over all values of $c_1, c_2$ and select the ones which give the smallest sum of squares); the code given below computes the estimates.

```python
# Growth rates
g = np.diff(ylog)
n_g = len(g)

t = np.arange(1, n_g + 1)

# Dates corresponding to the growth rates
growth_dates = y.index[1:]


# RSS for two change points c1 and c2
def rss(c1, c2):

```
X = np.column_stack([
    np.ones(n_g),
    t,
    np.maximum(t - c1, 0),
    np.maximum(t - c2, 0)
])

beta_hat = np.linalg.lstsq(X, g, rcond=None)[0]
residuals = g - X @ beta_hat

return np.sum(residuals ** 2)
```


# Possible change points
c_candidates = np.arange(12, n_g - 11)

# Grid search over all pairs
best_rss = np.inf

for c1 in c_candidates:
    for c2 in c_candidates:

        if c2 > c1:

            current_rss = rss(c1, c2)

            if current_rss < best_rss:
                best_rss = current_rss
                c1_hat = c1
                c2_hat = c2


print("Estimated change points:")
print(c1_hat, growth_dates[c1_hat - 1])
print(c2_hat, growth_dates[c2_hat - 1])

print("Minimum RSS:", best_rss)
```

```
Estimated change points:
108 1968-01-01 00:00:00
453 1996-10-01 00:00:00
Minimum RSS: 2.0261488639824974e-05
```

The estimated $c_1$ and $c_2$ are 108 (corresponding to January 1968) and 453 (corresponding to October 1996). With these values of $c_1$ and $c_2$, we can simply fit the model using linear regression (OLS) as before.

```python
X7 = np.column_stack([
    np.ones(n_g),
    t,
    np.maximum(t - c1_hat, 0),
    np.maximum(t - c2_hat, 0)
])

md7 = sm.OLS(g, X7).fit()

print(md7.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.667
Model:                            OLS   Adj. R-squared:                  0.666
Method:                 Least Squares   F-statistic:                     537.7
Date:                Wed, 02 Sep 2026   Prob (F-statistic):          7.93e-192
Time:                        15:09:46   Log-Likelihood:                 5939.7
No. Observations:                 810   AIC:                        -1.187e+04
Df Residuals:                     806   BIC:                        -1.185e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0016   2.76e-05     57.221      0.000       0.002       0.002
x1         -7.123e-06   3.16e-07    -22.565      0.000   -7.74e-06    -6.5e-06
x2          7.537e-06   3.52e-07     21.388      0.000    6.84e-06    8.23e-06
x3         -2.025e-06   1.12e-07    -18.016      0.000   -2.25e-06    -1.8e-06
==============================================================================
Omnibus:                       68.866   Durbin-Watson:                   0.223
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              192.544
Skew:                           0.423   Prob(JB):                     1.55e-42
Kurtosis:                       5.234   Cond. No.                     3.03e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.03e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Predictions are obtained as follows.

```python
# Fitted growth rates
g_fitted = md7.predict(X7)

# Convert fitted growth rates back to population
logy_fitted = np.r_[ylog.iloc[0], ylog.iloc[0] + np.cumsum(g_fitted)]
y_fitted = np.exp(logy_fitted)


# --------------------------------------------------
# Predict the next 168 months
# --------------------------------------------------

r = 168

t_future = np.arange(n_g + 1, n_g + r + 1)

X7_future = np.column_stack([
    np.ones(r),
    t_future,
    np.maximum(t_future - c1_hat, 0),
    np.maximum(t_future - c2_hat, 0)
])

# Predicted future growth rates
g_future = md7.predict(X7_future)

# Convert predicted growth rates to population
logy_future = ylog.iloc[-1] + np.cumsum(g_future)
y_future = np.exp(logy_future)


# --------------------------------------------------
# Plot population: data, fitted values, predictions
# --------------------------------------------------

x = np.arange(1, len(y) + 1)
x_future = np.arange(len(y) + 1, len(y) + r + 1)

plt.figure(figsize=(12, 5))

plt.plot(x, y, label="Observed data")
plt.plot(x, y_fitted, label="Fitted values")
plt.plot(x_future, y_future, label="Future predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Model 7: Observed Data, Fitted Values, and Predictions")
plt.legend()

plt.show()


# --------------------------------------------------
# Plot residuals
# --------------------------------------------------

residuals = md7.resid

plt.figure(figsize=(12, 4))

plt.plot(t, residuals)
plt.axhline(0, linestyle="--")

plt.xlabel("Time (months)")
plt.ylabel("Residual")
plt.title("Model 7 Residuals")

plt.show()


print("Prediction 168 months ahead:", y_future[-1])
```

```
Prediction 168 months ahead: 356954.5625958116
```

*(2 figures omitted — see the original notebook.)*

The prediction for July 2040 given by this model is 356.954 million, which is quite close to the prediction given by the Census Bureau.

Below is the plot for the growth rates along with the fitted regression curve.

```python
plt.figure(figsize=(12, 5))

plt.plot(t, g, label="Observed growth rates")
plt.plot(t, g_fitted, label="Fitted growth rates")

plt.axvline(c1_hat, linestyle="--", label="Change point 1")
plt.axvline(c2_hat, linestyle="--", label="Change point 2")

plt.xlabel("Time (months)")
plt.ylabel("Monthly log growth rate")
plt.title("Model 7: Piecewise Linear Model for Population Growth")
plt.legend()

plt.show()
```

*(1 figure omitted — see the original notebook.)*

This model fits a smaller slope for the data after time October 1996. This is the reason for its smaller prediction compared to the other models.

Overall message from this notebook is that there are several ways of using linear regression for time series forecasting, and different models yield different predictions. The idea of working with **differenced** data is quite common in time series analysis, and yields good results often. Differencing means working with $x_t - x_{t-1}$ instead of $x_t$. In the above analysis, we worked with growth rates which are the result of differencing applied to $\log y_t$. We shall work with differenced data in many applications in this course.

---

[← Model 5: $gt = \beta0 + \beta1 t + \beta2 (t - c)+ + \epsilont$.](06-model-5.md) · [Up: contents](index.md)
