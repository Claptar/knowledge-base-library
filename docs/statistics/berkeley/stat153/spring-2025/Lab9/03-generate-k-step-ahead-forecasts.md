---
title: Generate k-step ahead forecasts
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generate k-step ahead forecasts

**Source:** [`Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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
#basically the same prediction errors (slightly smaller for the Yule model); expect different results for different training-test splits.
```

```
79.83531765284938 79.52702577862316
```

### Model Three: AR(2)

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
Date:                Thu, 20 Mar 2025   Prob (F-statistic):           1.19e-92
Time:                        20:45:50   Log-Likelihood:                -1147.2
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
24.697886587075086
```

Note that the estimated value of $\phi_2$ (which is the value of $\phi_2$ which gives the best fit to the data in the least squares sense) is $-0.6841$ which is quite a bit smaller than the value of $-1$ which is hard-coded in the Yule model.

Let us obtain predictions for the future values using the fitted AR(2) model.

```python

---

[← Prediction error](02-prediction-error.md) · [Up: contents](index.md) · [Generate k-step ahead forecasts →](04-generate-k-step-ahead-forecasts.md)
