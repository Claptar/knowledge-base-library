---
title: Print results
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Print results

**Source:** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(f"Best AR model by AIC: AR({best_ar_aic})")
print(f"Best AR model by BIC: AR({best_ar_bic})")

print(f"Best MA model by AIC: MA({best_ma_aic})")
print(f"Best MA model by BIC: MA({best_ma_bic})")

print(f"Best ARMA model by AIC: ARMA{best_arma_aic}")
print(f"Best ARMA model by BIC: ARMA{best_arma_bic}")
```

```
Best AR model by AIC: AR(5)
Best AR model by BIC: AR(5)
Best MA model by AIC: MA(4)
Best MA model by BIC: MA(1)
Best ARMA model by AIC: ARMA(2, 4)
Best ARMA model by BIC: ARMA(0, 1)
```

According to BIC, the best model is MA(1). This is the same model that is suggested by ACF and PACF.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1)
plot_acf(ylogdiff2, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff2, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This suggests the ARIMA(0, 2, 1) model for ylog.

```python
arima021 = ARIMA(ylog, order = (0, 2, 1)).fit()
print(arima021.summary())
fcast_arima021 = arima021.get_prediction(start = n, end = n+k-1).predicted_mean
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  391
Model:                 ARIMA(0, 2, 1)   Log Likelihood                1199.732
Date:                Tue, 18 Nov 2025   AIC                          -2395.464
Time:                        21:03:58   BIC                          -2387.537
Sample:                             0   HQIC                         -2392.321
                                - 391
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.8732      0.026    -33.741      0.000      -0.924      -0.823
sigma2         0.0001   6.74e-06     18.122      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   1.69   Jarque-Bera (JB):                47.79
Prob(Q):                              0.19   Prob(JB):                         0.00
Heteroskedasticity (H):               0.55   Skew:                            -0.20
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.67
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_arima111, label = 'Forecast (ARIMA(1, 1, 1) on ylog)', color = 'darkgreen')
plt.plot(tme_future, fcast_arima111_t, label = 'Forecast (ARIMA(1, 1, 1) on ylog with intercept)', color = 'red')
plt.plot(tme_future, fcast_arima021, label = 'Forecast (ARIMA(0, 2, 1) on ylog)', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The model ARIMA(0, 2, 1) does not include any intercept term. We can also fit MA(1) to ylogdiff2, and then convert the predictions for the double differenced data to ylog.

```python
#predictions for ylogdiff2:
ma1_diff2 = ARIMA(ylogdiff2, order = (0, 0, 1)).fit()
fcast_diff2 = (ma1_diff2.get_prediction(start = n-2, end = n+k-3).predicted_mean)/100 #the division by 100 is because ylogdiff2 has a multiplication by 100 in its definition
```

The code below converts predictions for diff(diff(ylog)) into predictions for ylog.

```python
tmp1 = ylog[-1] - ylog[-2]
fcast_d1 = np.zeros(k)
fcast_d1[0] = tmp1 + fcast_diff2[0]
for i in range(1, k):
    fcast_d1[i] = fcast_d1[i-1] + fcast_diff2[i]
tmp2 = ylog[-1]
fcast_ma1_diff2 = np.zeros(k)
fcast_ma1_diff2[0] = tmp2 + fcast_d1[0]
for i in range(1, k):
    fcast_ma1_diff2[i] = fcast_ma1_diff2[i-1] + fcast_d1[i]
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_arima111, label = 'Forecast (ARIMA(1, 1, 1) on ylog)', color = 'darkgreen')
plt.plot(tme_future, fcast_arima111_t, label = 'Forecast (ARIMA(1, 1, 1) on ylog with intercept)', color = 'red')
plt.plot(tme_future, fcast_arima021, label = 'Forecast (ARIMA(0, 2, 1) on ylog)', color = 'black')
plt.plot(tme_future, fcast_ma1_diff2, label = 'Forecast (ARIMA(0, 2, 1) on ylog with intercept)', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These predictions (except for the red predictions) seem divergent because the horizon of prediction is very long. If we do short range predictions, they are much closer.

```python
k_short = 20
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future[0:k_short], fcast_arima111[0:k_short], label = 'Forecast (ARIMA(1, 1, 1) on ylog)', color = 'darkgreen')
plt.plot(tme_future[0:k_short], fcast_arima111_t[0:k_short], label = 'Forecast (ARIMA(1, 1, 1) on ylog with intercept)', color = 'red')
plt.plot(tme_future[0:k_short], fcast_arima021[0:k_short], label = 'Forecast (ARIMA(0, 2, 1) on ylog)', color = 'black')
plt.plot(tme_future[0:k_short], fcast_ma1_diff2[0:k_short], label = 'Forecast (ARIMA(0, 2, 1) on ylog with intercept)', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Best ARMA model overall](16-best-arma-model-overall.md) · [Up: contents](index.md)
