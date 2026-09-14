---
title: Modeling Logarithms
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabOne153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Modeling Logarithms

**Source:** [`CodeLabOne153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Another variant of these models is to use the model for the logarithm of the data, than the original data.

```python
ylog = np.log(uspop['POPTHM'])
n = len(ylog)
x = np.arange(1, n + 1)
X = np.column_stack([np.ones(n),x]) #this is the X matrix

mdlog = sm.OLS(ylog, X).fit()
print(mdlog.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.994
Model:                            OLS   Adj. R-squared:                  0.994
Method:                 Least Squares   F-statistic:                 1.370e+05
Date:                Fri, 28 Aug 2026   Prob (F-statistic):               0.00
Time:                        23:04:02   Log-Likelihood:                 2257.3
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

```python
#Plotting the log of the population and the linear fit
plt.figure(figsize=(10, 7))
plt.plot(ylog, label = "log of population")
plt.plot(mdlog.fittedvalues, color='red', label = 'Linear Fit')
plt.xlabel("Time (monthly)")
plt.ylabel("Log of Population (thousands)")
plt.title("Log of Population of the United States with Linear Fit")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the plot above, the fitted line closely tracks the data, but in recent times, the actual log population is much lower than the fitted line. It is then clear that a prediction based on the line would be quite large.

Below we predict the population in July 2040 using this model. This model will provide a prediction for $\log y_t$ which needs to be exponentiated to get prediction for $y_t$.

```python
#predicting the population in July 2040 using the statsmodels results
n = len(ylog)
i = n+168
predicted_population_july_2040_log = mdlog.predict([1, i])
print(np.exp(predicted_population_july_2040_log)) #we take the exponential of the predicted value to get the predicted population in thousands
```

```
[412762.30604638]
```

The prediction now is 412.7 million which is even larger than the previously obtain prediction for the linear model directly fitted to $y_t$.

How to do improved modeling which gives more realistic future predictions (perhaps closer to the population projections by the Census Bureau)? We shall see some answers later in the course.

---

[← Fitting a Quadratic Trend](03-fitting-a-quadratic-trend.md) · [Up: contents](index.md)
