---
title: Fitting a Quadratic Trend
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabOne153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fitting a Quadratic Trend

**Source:** [`CodeLabOne153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabOne153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Suppose we now use the model:
\begin{align*}
  y_i = \beta_0 + \beta_1 i + \beta_2 i^2 + \text{error}
\end{align*}
In this case, the $X$ matrix becomes:
\begin{align*}
   y = \begin{pmatrix} y_1 \\ y_2 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} ~~ X = \begin{pmatrix}1 & x_1 & x_1^2\\ 1 & x_2 & x_2^2 \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ 1 & x_n & x_n^2 \end{pmatrix}.
\end{align*}
where, as before, $x_i = i^2$. With this specification of $X$, the statsmodels code works in the same way as before.

```python
y = uspop['POPTHM']
n = len(y)
x = np.arange(1, n + 1)
X = np.column_stack([np.ones(n),x, x ** 2]) #this is the X matrix above

md2 = sm.OLS(y, X).fit()
print(md2.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 1.569e+05
Date:                Fri, 28 Aug 2026   Prob (F-statistic):               0.00
Time:                        21:36:26   Log-Likelihood:                -7506.9
No. Observations:                 811   AIC:                         1.502e+04
Df Residuals:                     808   BIC:                         1.503e+04
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.766e+05    268.068    658.741      0.000    1.76e+05    1.77e+05
x1           198.4418      1.525    130.151      0.000     195.449     201.435
x2             0.0182      0.002     10.007      0.000       0.015       0.022
==============================================================================
Omnibus:                      204.614   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               55.095
Skew:                          -0.387   Prob(JB):                     1.09e-12
Kurtosis:                       1.984   Cond. No.                     8.86e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.86e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Below we plot the observed data with the fitted quadratic (this is obtained using the "fittedvalues" attribute below).

```python
plt.figure(figsize=(10, 7))
plt.plot(uspop['POPTHM'], label = "population")
plt.plot(md.fittedvalues, color='green', label = 'Linear Fit')
plt.plot(md2.fittedvalues, color='red', label = 'Quadratic Fit')
plt.xlabel("Time (monthly)")
plt.ylabel("Population (thousands)")
plt.title("Population of the United States with Linear and Quadratic Fit")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There is not much difference between the linear and quadratic fits. Note that fitted value of $\beta_2$ above is positive (0.0182). This means that the quadratic is trending upward (convex) which means that it will give an even larger prediction for July 2040 compared to the linear regression model.

```python
#predicting the population in July 2040 using the statsmodels results
n = len(y)
i = n+168
predicted_population_july_2040_quadratic = md2.predict([1, i, i**2])
print(predicted_population_july_2040_quadratic)
```

```
[388300.29946012]
```

The predicted population (July 2040) by the quadratic model is 388.3 million which is more than the prediction given by the linear trend model.

---

[← US Population Dataset](02-us-population-dataset.md) · [Up: contents](index.md) · [Modeling Logarithms →](04-modeling-logarithms.md)
