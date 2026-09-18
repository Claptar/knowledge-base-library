---
title: 'Model 1: $yt = \beta0 + \beta1 t + \epsilont$'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model 1: $yt = \beta0 + \beta1 t + \epsilont$

Parameter interpretation: $\beta_0$: population at time 0 (note that the data starts from January 1959 so time 0 refers to December 1958) and $\beta_1$: change in population for each additional month.

We fit this model to the data using the following code.

```python
#Model 1: y_t = beta_0 + beta_1 t + \epsilon_t
#y_t is the population at time t
y = uspop['POPTHM']
n = len(y)
x = np.arange(1, n + 1)
X = np.column_stack([np.ones(n),x])

md1 = sm.OLS(y, X).fit()
print(md1.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 2.794e+05
Date:                Tue, 01 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:06:34   Log-Likelihood:                -7554.3
No. Observations:                 811   AIC:                         1.511e+04
Df Residuals:                     809   BIC:                         1.512e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.746e+05    189.054    923.472      0.000    1.74e+05    1.75e+05
x1           213.2157      0.403    528.562      0.000     212.424     214.008
==============================================================================
Omnibus:                      562.602   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               69.512
Skew:                          -0.398   Prob(JB):                     8.05e-16
Kurtosis:                       1.807   Cond. No.                         938.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

The output above consists of many different things. We shall see how some of these numbers are calculated in the next couple of lectures. The main output is the estimates of $\beta_0$ and $\beta_1$ (these are given by the 'coef' column above).

```python
print(md1.params)
```

```
const    174585.548486
x1          213.215735
dtype: float64
```

After fitting a model, it is a good idea to look at the plot of the data along with the 'fitted values' and also the 'residuals'. Fitted values are defined by:
\begin{align*}
   \hat{\beta}_0 + \hat{\beta}_1 t
\end{align*}
for $t = 1, \dots, n$.

Residuals are defined by:
\begin{align*}
   y_t - \hat{\beta}_0 - \hat{\beta}_1 t.
\end{align*}
Residuals represent the part of the data that is not explained by the model equation.

```python
#Plotting data along with residuals
plt.figure(figsize=(6, 4))
plt.plot(y, label = "population")
plt.plot(md1.fittedvalues, label = "fitted values")
plt.xlabel("Time (monthly)")
plt.ylabel("Population (thousands)")
plt.title("Population of the United States with fitted values")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values plot suggests that the line is explaining the data well. Note though that the $y$-axis goes from 175K to 350K which covers a wide range, so even small changes in this plot can indicate big numerical departures.

```python
#Plotting residuals:
plt.figure(figsize=(6, 4))
plt.plot(md1.resid, label = "residuals")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the OLS Model")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

All the recent residuals are negative which means that the fitted line takes higher values compared to the actual observations. From here, we can perhaps guess that future predictions will also be on the larger side.

There is a lot of structure in the residuals which indicates that more modeling on the residuals is necessary.

Here is how this fitted model can be used to predict the population in July 2040.

```python
#Prediction for time t = n + 168 (July 2040):
n = len(y)
i = n+168
prediction = md1.get_prediction([1, i])
print("Mean prediction for July 2040:", prediction.predicted_mean)
```

```
Mean prediction for July 2040: [383323.7529835]
```

We are getting a prediction of 383.323 million which is quite a bit higher than the Census Bureau as well as the UN predictions. Below we plot the predictions along with the original dataset.

```python
# Predict the next 168 monthly observations
r = 168
x_future = np.arange(n + 1, n + r + 1)
X_future = np.column_stack([
    np.ones(r),
    x_future
])
y_future = md1.predict(X_future)
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Observed data")
plt.plot(x_future, y_future, label="Predictions", color = 'red')
plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Observed U.S. Population and Model 1 Predictions")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Notice the small jump between where the data end, and the predictions.

```python
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Observed data")
plt.plot(x, md1.fittedvalues, label="Fitted values")
plt.plot(x_future, y_future, label="Future predictions", color = 'red')
plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Model 1: Linear Trend")
plt.legend()

plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Model Two: $\log yt = \beta0 + \beta1 t + \epsilont$ →](03-model-two.md)
