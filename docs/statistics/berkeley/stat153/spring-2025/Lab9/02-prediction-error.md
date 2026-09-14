---
title: Prediction error
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Prediction error

**Source:** [`Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

pred_error_rms_sinusoid = np.sqrt(np.mean((pred_test - sunspots_test.iloc[:, 1]) ** 2))
print(pred_error_rms_sinusoid)
```

```
79.83531765284938
```

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Model Two: The Yule Model

This model is motivated by the following observation (discussed with proof in Lecture 16) that
\begin{equation*}
   s_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t)  ~~~ \text{ for } t = 1, 2, \dots
\end{equation*}
is equivalent to (below $\omega = 2 \pi f$)
\begin{equation*}
   s_t = \alpha_0 + \alpha_1 s_{t-1} - s_{t-2} ~~~~ \text{ with } \alpha_0 = 2 \beta_0 (1 - \cos \omega) \text{ and } \alpha_1 = 2 \cos \omega.
\end{equation*}

This suggests that a different sinusoid plus noise model is obtained by adding noise in the above equation leading to:
\begin{equation*}
   y_t = \alpha_0 + \alpha_1 y_{t-1} - y_{t-2} + \epsilon_t
\end{equation*}
The parameters $\alpha_0$ and $\alpha_1$ can be fit by least squares by minimizing
\begin{equation*}
   \sum_{t=3}^n (y_t - \alpha_0 - \alpha_1 y_{t-1} + y_{t-2})^2 = \sum_{t=3}^n (y_t + y_{t-2} - \alpha_0 - \alpha_1 y_{t-1} )^2
\end{equation*}
Note that the time index goes from $3$ to $n$ above (because we do not have access to $y_{t-1}$ and/or $y_{t-2}$ when $t \leq 2$). This least squares estimator can be computed by creating a new response variable $y_t + y_{t-2}$ and regressing it on $y_{t-1}$ (and the constant term).

```python
p = 2
yreg = y[p:]
x1 = y[1:-1]
x2 = y[:-2]
Xmat = np.column_stack([np.ones(len(yreg)), x1])

print(Xmat.shape)
```

```
(248, 2)
```

```python
y_adjusted = yreg + x2
yulemod = sm.OLS(y_adjusted, Xmat).fit()

print(yulemod.summary())
print(yulemod.params)
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.926
Model:                            OLS   Adj. R-squared:                  0.926
Method:                 Least Squares   F-statistic:                     3090.
Date:                Thu, 20 Mar 2025   Prob (F-statistic):          2.78e-141
Time:                        20:49:50   Log-Likelihood:                -1168.0
No. Observations:                 248   AIC:                             2340.
Df Residuals:                     246   BIC:                             2347.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         27.3114      2.791      9.787      0.000      21.815      32.808
x1             1.6348      0.029     55.592      0.000       1.577       1.693
==============================================================================
Omnibus:                       10.450   Durbin-Watson:                   2.408
Prob(Omnibus):                  0.005   Jarque-Bera (JB):               20.195
Skew:                           0.133   Prob(JB):                     4.12e-05
Kurtosis:                       4.372   Cond. No.                         155.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[27.31136502  1.634765  ]
```

Because $\alpha_1 = 2 \cos \omega = 2 \cos (2 \pi f)$, we can obtain an estimate of $f$ from the least squares estimate of $\alpha_1$ obtained above.

```python
alpha1_hat = yulemod.params[1]
yulefhat = np.arccos(alpha1_hat/2) / (2 * np.pi)

print(1/yulefhat)
```

```
10.234141128185033
```

It is interesting that the period corresponding to this estimate of $f$ is less than 11 by a nontrivial amount.

We now obtain predictions for the test times from the Yule model.

```python

---

[← Sunspots prediction](01-sunspots-prediction.md) · [Up: contents](index.md) · [Generate k-step ahead forecasts →](03-generate-k-step-ahead-forecasts.md)
