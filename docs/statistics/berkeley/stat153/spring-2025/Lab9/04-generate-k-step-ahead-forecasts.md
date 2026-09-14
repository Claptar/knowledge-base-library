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

### Model Four: AR($p$) for a higher $p$

We can see how the predictions change if we use $AR(p)$ for a higher $p$. The AR(p) for $p \geq 2$ should give better fits to the data. Unless there is overfitting, this should lead to better predictions as well.

```python
p = 12
yreg = y[p:] # these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) # this will be the design matrix (X) in the autoregression

for j in range(1, p+1):
    col = y[p-j: n-j].reshape(-1, 1)
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
[13.12906966  1.21947938 -0.50695376 -0.10670251  0.16956741 -0.15634832
  0.05883931 -0.05974739  0.10456934  0.09940318 -0.06642164  0.14368696
 -0.06191045]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.850
Model:                            OLS   Adj. R-squared:                  0.842
Method:                 Least Squares   F-statistic:                     106.0
Date:                Thu, 20 Mar 2025   Prob (F-statistic):           2.00e-85
Time:                        20:45:50   Log-Likelihood:                -1082.3
No. Observations:                 238   AIC:                             2191.
Df Residuals:                     225   BIC:                             2236.
Df Model:                          12
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         13.1291      4.789      2.742      0.007       3.693      22.565
x1             1.2195      0.067     18.239      0.000       1.088       1.351
x2            -0.5070      0.106     -4.795      0.000      -0.715      -0.299
x3            -0.1067      0.112     -0.957      0.340      -0.327       0.113
x4             0.1696      0.112      1.517      0.131      -0.051       0.390
x5            -0.1563      0.113     -1.389      0.166      -0.378       0.065
x6             0.0588      0.112      0.525      0.600      -0.162       0.280
x7            -0.0597      0.111     -0.540      0.590      -0.278       0.158
x8             0.1046      0.110      0.951      0.343      -0.112       0.321
x9             0.0994      0.109      0.908      0.365      -0.116       0.315
x10           -0.0664      0.109     -0.608      0.544      -0.282       0.149
x11            0.1437      0.105      1.372      0.171      -0.063       0.350
x12           -0.0619      0.067     -0.922      0.358      -0.194       0.070
==============================================================================
Omnibus:                       30.370   Durbin-Watson:                   1.990
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               51.328
Skew:                           0.713   Prob(JB):                     7.15e-12
Kurtosis:                       4.773   Cond. No.                         859.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
22.837160267072164
```

```python

---

[← Generate k-step ahead forecasts](03-generate-k-step-ahead-forecasts.md) · [Up: contents](index.md) · [Generate k-step ahead forecasts →](05-generate-k-step-ahead-forecasts.md)
