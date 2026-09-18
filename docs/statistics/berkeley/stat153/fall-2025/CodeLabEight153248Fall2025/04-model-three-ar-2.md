---
title: 'Model Three: AR(2)'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEight153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabEight153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model Three: AR(2)

The AR(2) model is a natural extension of the Yule model:
\begin{equation*}
   y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t
\end{equation*}
The only difference between the Yule model and AR(2) is that $\phi_2 = -1$ in the Yule model while it is treated as an adjustable parameter which can provide better fits to the data in AR(2).

The AR(2) model is fit in the following way.

```python
p = 2
yreg = y[p:] # these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) # this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
```

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)
print(armod.summary())
sighat = np.sqrt(np.mean(armod.resid ** 2))
print(sighat)
```

```
[23.08524521  1.37838349 -0.68406411]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.822
Model:                            OLS   Adj. R-squared:                  0.821
Method:                 Least Squares   F-statistic:                     567.0
Date:                Mon, 27 Oct 2025   Prob (F-statistic):           1.19e-92
Time:                        15:10:09   Log-Likelihood:                -1147.2
No. Observations:                 248   AIC:                             2300.
Df Residuals:                     245   BIC:                             2311.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         23.0852      2.647      8.722      0.000      17.872      28.299
x1             1.3784      0.047     29.399      0.000       1.286       1.471
x2            -0.6841      0.047    -14.506      0.000      -0.777      -0.591
==============================================================================
Omnibus:                       25.182   Durbin-Watson:                   2.117
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               37.915
Skew:                           0.631   Prob(JB):                     5.85e-09
Kurtosis:                       4.441   Cond. No.                         220.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
24.69788658707509
```

Note that the estimated value of $\phi_2$ (which is the value of $\phi_2$ which gives the best fit to the data in the least squares sense) is $-0.6841$ which is quite a bit smaller than the value of $-1$ which is hard-coded in the Yule model.

Let us obtain predictions for the future values using the fitted AR(2) model.

```python
# Generate k-step ahead forecasts:
k = len(tme_test)
yhat = np.concatenate([y, np.full(k, -9999)]) # extend data by k placeholder values
for i in range(1, k+1):
    ans = armod.params[0]
    for j in range(1, p+1):
        ans += armod.params[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues_ar = yhat[n:]
```

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions (Model One)')
plt.plot(tme_test, predvalues_yulemod, color = 'green', label = 'Predictions (Model Two)')
plt.plot(tme_test, predvalues_ar, color = 'yellow', label = 'Predictions (Model Three)')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions look quite different. For AR(2), the predictions die out to a constant value.

```python
pred_error_rms_ar = np.sqrt(np.mean((predvalues_ar - sunspots_test.iloc[:,1]) ** 2))
print(pred_error_rms_sinusoid, pred_error_rms_yulemod, pred_error_rms_ar)
```

```
79.83531765284938 79.52702577862316 70.32365837557232
```

It is interesting that even though the predictions of the AR model die out to a constant value, in terms of prediction accuracy, it performs better than the previous two sinusoidal models. One reason for this is that the cycles of the sunspots data are irregular (and their periodicity changes from cycle to cycle). If we use a single sinusoid for prediction (as in Models One and Two), there is a danger that the predictions go out of phase with the actual data. The AR model, by predicting a constant, becomes more accurate than a sinusoidal model that goes out of phase. Note though that this prediction comparison will change if we change the training and test datasets.

---

[← Model Two: The Yule Model](03-model-two-the-yule-model.md) · [Up: contents](index.md) · Model Four: AR($p$) for a higher $p$ →
