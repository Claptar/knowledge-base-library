---
title: 'Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n = len(ylog)
x = np.arange(1, n + 1)
X = np.column_stack([np.ones(n),x, x ** 2])
md3 = sm.OLS(ylog, X).fit()
print(md3.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.998
Model:                            OLS   Adj. R-squared:                  0.998
Method:                 Least Squares   F-statistic:                 2.202e+05
Date:                Tue, 01 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:25:10   Log-Likelihood:                 2729.6
No. Observations:                 811   AIC:                            -5453.
Df Residuals:                     808   BIC:                            -5439.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         12.0885      0.001   1.37e+04      0.000      12.087      12.090
x1             0.0010   5.03e-06    206.261      0.000       0.001       0.001
x2         -2.532e-07      6e-09    -42.213      0.000   -2.65e-07   -2.41e-07
==============================================================================
Omnibus:                      481.365   Durbin-Watson:                   0.001
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               69.444
Skew:                          -0.414   Prob(JB):                     8.32e-16
Kurtosis:                       1.830   Cond. No.                     8.86e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.86e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Indeed the estimate of $\beta_2$ is negative.

```python
#Plotting the fitted values from the model
plt.figure(figsize=(6, 4))
plt.plot(ylog, label = "log population")
plt.plot(md3.fittedvalues, label = "fitted values")
plt.xlabel("Time (monthly)")
plt.ylabel("Log Population (thousands)")
plt.title("Log Population of the United States with fitted values (quadratic model)")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting residuals:
plt.figure(figsize=(6, 4))
plt.plot(md3.resid, label="Residuals")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the Log Population Model (quadratic)")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that the scale of the residuals is now  smaller than the residuals for model 2.

```python
#Plotting both model 2 and model 3 residuals in one plot:
plt.figure(figsize=(6, 4))
plt.plot(mdlog.resid, label="Residuals of log model")
plt.plot(md3.resid, label="Residuals of quadratic model")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the Log Population Models")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Prediction of log-population (and population) for time t = n + 168 (July 2040) using Model 3:
n = len(y)
i = n+168
predicted_population_july_2040_quadratic = md3.get_prediction([1, i, i**2])
print("Mean prediction of log-population for July 2040 (quadratic model):", predicted_population_july_2040_quadratic.predicted_mean)
print("Mean prediction of population for July 2040 (quadratic model):", np.exp(predicted_population_july_2040_quadratic.predicted_mean))
```

```
Mean prediction of log-population for July 2040 (quadratic model): [12.86138429]
Mean prediction of population for July 2040 (quadratic model): [385148.51545984]
```

This prediction is still on the higher side but not as bad as the predictions for model two.

```python

---

[← Prediction 168 months ahead](09-prediction-168-months-ahead.md) · [Up: contents](index.md) · [Predict the next 168 monthly observations →](11-predict-the-next-168-monthly-observations.md)
