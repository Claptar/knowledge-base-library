---
title: 'Model Two: $\log yt = \beta0 + \beta1 t + \epsilont$'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model Two: $\log yt = \beta0 + \beta1 t + \epsilont$

Now we fit the line to the logarithms $\log y_t = \beta_0 + \beta_1 t + \epsilon_t$. Here is the interpretation of the parameters: $\beta_0$: log-population at time 0, and $\beta_1$: change in log-population from one month to the next. This change is given by:
\begin{align*}
   \log y_t - \log y_{t-1} = \log \frac{y_t}{y_{t-1}} \approx \frac{y_t - y_{t-1}}{y_{t-1}}.
\end{align*}
So therefore $100 \times \beta_1$ is the percent change in population from one month to the next. In other words, $100 \times \beta_1$ is the monthly population growth rate (expressed as a percentage). We can also say that $100 \times \beta_1 \times 12$ is the annual population growth rate (expressed as a percentage).

```python
#Model 2: $\log y_t = \beta_0 + \beta_1 t + \epsilon_t$.
ylog = np.log(y)
mdlog = sm.OLS(ylog, X).fit()
print(mdlog.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.994
Model:                            OLS   Adj. R-squared:                  0.994
Method:                 Least Squares   F-statistic:                 1.370e+05
Date:                Tue, 01 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:17:25   Log-Likelihood:                 2257.3
No. Observations:                 811   AIC:                            -4511.
Df Residuals:                     809   BIC:                            -4501.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         12.1164      0.001   1.15e+04      0.000      12.114      12.118
x1             0.0008   2.25e-06    370.158      0.000       0.001       0.001
==============================================================================
Omnibus:                      112.155   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              157.688
Skew:                          -1.028   Prob(JB):                     5.73e-35
Kurtosis:                       3.664   Cond. No.                         938.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

The estimate of $\beta_1$ is $0.0008$. This means that for each additional month, $\log y_t$ increases by 0.0008. This implies that the growth rate of the population is 0.08% each month, or $12 * 0.08 = 0.96%$ annually. So, according to this model, the estimate of the annual growth rate of the US population is 0.96%.

```python
#Plotting fitted values and residuals:
plt.figure(figsize=(6, 4))
plt.plot(ylog, label = "log population")
plt.plot(mdlog.fittedvalues, label = "fitted values")
plt.xlabel("Time (monthly)")
plt.ylabel("Log Population (thousands)")
plt.title("Log Population of the United States with fitted values")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values are reasonably close to the actual data, but in recent years, there is a slowdown in the growth. So predictions will probably be higher than what they should be.

```python
#Plotting residuals:
plt.figure(figsize=(6, 4))
plt.plot(mdlog.resid, label="Residuals")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the Log Population Model")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Residuals are negative in the recent past (as in the case of Model 1). Also there is a lot of structure in the residuals.

```python
#Prediction for time t = n + 168 (July 2040):
n = len(ylog)
i = n+168
prediction_log = mdlog.get_prediction([1, i])
print("Mean prediction of log-population for July 2040 (log model):", prediction_log.predicted_mean)
print("Mean prediction of population for July 2040 (log model):", np.exp(prediction_log.predicted_mean))
```

```
Mean prediction of log-population for July 2040 (log model): [12.93062718]
Mean prediction of population for July 2040 (log model): [412762.30604638]
```

This is not a good prediction because the growth rate has significantly slowed down in recent years (while this model assumes constant growth rate throughout).

```python
# Predict the next 168 monthly observations
r = 168

# Future time points: n+1, ..., n+168
x_future = np.arange(n + 1, n + r + 1)

# Design matrix for future observations
X_future = np.column_stack([
    np.ones(r),
    x_future
])

# Fitted and predicted values on the log scale
ylog_fitted = mdlog.predict(X)
ylog_future = mdlog.predict(X_future)

# Convert back to population scale
y_fitted = np.exp(ylog_fitted)
y_future = np.exp(ylog_future)

# Plot observed data, fitted values, and future predictions
plt.figure(figsize=(6, 4))

plt.plot(x, y, label="Observed data")
plt.plot(x, y_fitted, label="Fitted values")
plt.plot(x_future, y_future, label="Future predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Model 2: Log-Linear Trend")
plt.legend()

plt.show()

# Prediction 168 months ahead
print("Prediction 168 months ahead:", y_future[-1])
```

```
Prediction 168 months ahead: 412762.30604638177
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize=(6, 4))

plt.plot(x, y, label="Observed data")
plt.plot(x_future, y_future, label="Predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Observed U.S. Population and Model 2 Predictions")
plt.legend()

plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Model 1: $yt = \beta0 + \beta1 t + \epsilont$](02-model-1.md) · [Up: contents](index.md) · [Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$ →](04-model-3.md)
