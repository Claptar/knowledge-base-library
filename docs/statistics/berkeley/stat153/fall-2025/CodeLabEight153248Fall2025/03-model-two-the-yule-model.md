---
title: 'Model Two: The Yule Model'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEight153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabEight153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model Two: The Yule Model

This model is motivated by the following observation (discussed with proof in Lecture 16)
\begin{equation*}
   s_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t)
\end{equation*}
for $t = 1, 2, \dots$ is equivalent to (below $\omega = 2 \pi f$)
\begin{equation*}
   s_t = \alpha_0 + \alpha_1 s_{t-1} - s_{t-2} ~~~~ \text{ with } \alpha_0 = 2 \beta_0 (1 - \cos \omega) \text{ and } \alpha_1 = 2 \cos \omega.
\end{equation*}

This suggests that a different Sinusoid plus noise model is obtained by adding noise in the above equation leading to:
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
Date:                Mon, 27 Oct 2025   Prob (F-statistic):          2.78e-141
Time:                        15:10:08   Log-Likelihood:                -1168.0
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
# Generate k-step ahead forecasts:
k = len(tme_test)
yhat = np.concatenate([y, np.full(k, -9999)]) # extend data by k placeholder values
for i in range(1, k+1):
    ans = yulemod.params[0] - yhat[n+i-3]
    ans += yulemod.params[1] * yhat[n+i-2]
    yhat[n+i-1] = ans
predvalues_yulemod = yhat[n:]
print(predvalues_yulemod)
```

```
[146.06104972  75.38685636   4.49010921 -40.73521796 -43.77125261
  -3.50912861  65.34601702 137.64587487 186.98400606 195.34039803
 159.66300392  92.98245693  19.65282692 -33.5433384  -47.17693735
 -16.26850237  47.89312417 121.87387032 178.65337795 197.49378336
 171.513911   110.20251965  35.9526756  -24.11697905 -48.06690374
 -27.14974761  30.99481172 105.13034589 168.17996275 197.11573524
 181.36930636 126.69182313  53.05341637 -12.65059012 -46.42279325
 -35.92840227  14.99966389  87.76069276 155.77980967 194.21405216
 189.02588952 142.11022034  70.60228927   0.6192958  -42.27852115
 -42.42337723   0.23763408  70.12321812 141.70871333 188.84859105
 194.32571784 156.13965529  88.2372901   15.41894292 -35.71957693
 -46.50069192 -12.98676148  52.58175387 126.25693714 181.13003247
 197.15946465 168.49072395 105.59463801  31.44305903 -26.88126073
 -48.07623808 -24.4007254   35.49815135 109.74322567 171.21759752
 197.46867444 178.90864425 122.31627964  48.36109315 -15.94589238]
```

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
#plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions (Model One)')
plt.plot(tme_test, predvalues_yulemod, color = 'green', label = 'Predictions (Model Two)')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
pred_error_rms_yulemod = np.sqrt(np.mean((predvalues_yulemod - sunspots_test.iloc[:,1]) ** 2))
print(pred_error_rms_sinusoid, pred_error_rms_yulemod)
# basically the same prediction errors (slightly smaller for the Yule model); expect different results for different training-test splits.
```

```
79.83531765284938 79.52702577862316
```

---

[← Model One: Sinusoid Model](02-model-one-sinusoid-model.md) · [Up: contents](index.md) · [Model Three: AR(2) →](04-model-three-ar-2.md)
