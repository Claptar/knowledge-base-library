---
title: 'Model 5: $gt = \beta0 + \beta1 t + \beta2 (t - c)+ + \epsilont$.'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model 5: $gt = \beta0 + \beta1 t + \beta2 (t - c)+ + \epsilont$.

Here we modify model 4 by adding one more covariate in regression $(t - c)_+$ leading to the model:
\begin{align*}
   g_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t.
\end{align*}
The term $(t - c)_+$ simply equals $\max(t - c, 0)$. This means that $(t - c)_+$ equals $t - c$ if $t \geq c$ and $(t - c)_+$ equals 0 when $t \leq c$. Another way of writing $(t - c)_+$ is $\text{ReLU}(t - c)$. Here $\text{ReLU}(x) = x_+ = x I\{x \geq 0\}$ (where $I\{x \geq 0\}$ equals 1 if $x \geq 0$ and 0 if $x \leq 0$). ReLU is a terminology heavily used in modern machine learning and it stands for Rectified Linear Unit.

This regression fits a continuous function consisting of two straight lines to the data. Before the time point given by $c$, the fitted slope is $\beta_1$. After $c$, the fitted slope is $\beta_1+\beta_2$. The two line segments join continuously at $c$.

If $c$ is a known time point, then this is an example of multiple linear regression with covariates $1$, $t$, and $(t-c)_+$. When $c$ is also unknown, we can treat this is as a nonlinear regression problem. We shall look at estimation of $c$ in detail later. The method we shall use is:

1. try each candidate month $c$;
2. fit the corresponding linear regression;
3. record its residual sum of squares (RSS);
4. choose the candidate with the smallest RSS.

We shall look at the above procedure in detail later. Here is the code for implementing this method to obtain an estimate of $c$.

```python
# Monthly log growth rates
g = ylog.diff().dropna()

t = np.arange(1, len(g) + 1)

# RSS for a given change point c
def rss(c):
    X = np.column_stack([
        np.ones(len(g)),
        t,
        np.maximum(t - c, 0)
    ])

    model = sm.OLS(g, X).fit()
    return np.sum(model.resid ** 2)


# Try all possible change points
c_candidates = np.arange(12, len(g) - 11)

rss_values = [rss(c) for c in c_candidates]

# Best change point
c_hat = c_candidates[np.argmin(rss_values)]

print("Estimated change point:", c_hat)
print("Estimated change date:", g.index[c_hat - 1])
```

```
Estimated change point: 75
Estimated change date: 1965-04-01 00:00:00
```

The estimated $c$ is 75 (which corresponds to the month of April 1965). Fixing this value of $c$, we can estimate $\beta_j, j = 0, 1, 2$ as before using linear regression.

```python
from scipy.optimize import minimize_scalar

g = np.diff(ylog)
t = np.arange(1, len(g) + 1)

X = np.column_stack([np.ones(len(g)), t, np.maximum(t - c_hat, 0)])
md5 = sm.OLS(g, X).fit()

print("Estimated c:", c_hat)
print(md5.summary())
```

```
Estimated c: 75
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.543
Model:                            OLS   Adj. R-squared:                  0.542
Method:                 Least Squares   F-statistic:                     480.4
Date:                Wed, 02 Sep 2026   Prob (F-statistic):          3.92e-138
Time:                        14:56:25   Log-Likelihood:                 5812.1
No. Observations:                 810   AIC:                        -1.162e+04
Df Residuals:                     807   BIC:                        -1.160e+04
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0016   3.81e-05     42.218      0.000       0.002       0.002
x1         -8.097e-06   5.64e-07    -14.348      0.000    -9.2e-06   -6.99e-06
x2          7.491e-06   5.77e-07     12.973      0.000    6.36e-06    8.62e-06
==============================================================================
Omnibus:                       20.728   Durbin-Watson:                   0.163
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               42.343
Skew:                           0.074   Prob(JB):                     6.39e-10
Kurtosis:                       4.110   Cond. No.                     3.61e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.61e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Future predictions can be obtained as follows.

```python
n = len(ylog)

t_future = np.arange(n, n + 168)
X_future = np.column_stack([
    np.ones(168),
    t_future,
    np.maximum(t_future - c_hat, 0)
])

g_pred_md5 = md5.predict(X_future)

# predicted populations y_{n+1},...,y_{n+168}
y_future_md5 = y.iloc[-1] * np.exp(np.cumsum(g_pred_md5))

print("Predicted population at n + 168:", y_future_md5[-1])
```

```
Predicted population at n + 168: 373123.6153089739
```

The prediction is similar (but slightly higher) to that given by Model 4.

```python
plt.plot(np.arange(n), y, label="Observed")
plt.plot(np.arange(n, n + 168), y_future_md5, label="Predicted (model 5)", color = 'red')
plt.plot(np.arange(n, n + 168), y_future_md4, label="Predicted (model 4)", color = 'green')


plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is a plot of the growth rates along with the fitted values for Models 4 and 5.

```python
plt.plot(t, g, label="Observed growth rate")
plt.plot(t, md5.fittedvalues, label="Fitted values for model 5", color = 'red')
plt.plot(t, md4.fittedvalues, label="Fitted values for model 4", color = 'green')

plt.xlabel("Time")
plt.ylabel("Monthly log growth rate")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the fitted slope for Model 5 after the breakpoint is slightly higher than the overall slope obtained from Model 4. This is the reason why Model 5 is giving a slightly larger prediction for future values compared to Model 4.

Below is the plot of residuals for Model 5.

```python
g_residuals = g - md5.fittedvalues
plt.plot(t, g_residuals, label="Residuals")
plt.xlabel("Time")
plt.ylabel("Monthly log growth rate")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Model 4: Modeling growth rate](05-model-4-modeling-growth-rate.md) · [Up: contents](index.md) · [Model 6: Two change of slope points →](07-model-6-two-change-of-slope-points.md)
