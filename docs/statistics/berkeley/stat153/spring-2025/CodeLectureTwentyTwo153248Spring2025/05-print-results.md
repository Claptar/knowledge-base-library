---
title: Print results
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyTwo153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Print results

**Source:** [`CodeLectureTwentyTwo153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(f"Best AR model by AIC: AR({best_ar_aic})")
print(f"Best AR model by BIC: AR({best_ar_bic})")

print(f"Best MA model by AIC: MA({best_ma_aic})")
print(f"Best MA model by BIC: MA({best_ma_bic})")

print(f"Best ARMA model by AIC: ARIMA{best_arma_aic}")
print(f"Best ARMA model by BIC: ARIMA{best_arma_bic}")
```

```
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:978: UserWarning: Non-invertible starting MA parameters found. Using zeros as starting parameters.
  warn('Non-invertible starting MA parameters found.'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
Best AR model by AIC: AR(5)
Best AR model by BIC: AR(5)
Best MA model by AIC: MA(3)
Best MA model by BIC: MA(2)
Best ARMA model by AIC: ARIMA(3, 2)
Best ARMA model by BIC: ARIMA(0, 2)
```

The best MA model for the double-differenced data is MA(2) (using BIC) and MA(3) (using AIC). Overall the best ARMA model for the double-differenced data is ARMA(3, 2) (AIC) and MA(2) (BIC). Below we fit the ARMA(3, 2) model to the double-differenced data (we apply it to the original data as ARIMA(3, 2, 2)).

```python
arma_arima = ARIMA(y, order = (3, 2, 2)).fit()
print(arma_arima.summary())
fcast_arma = arma_arima.get_prediction(start = n, end = n+k-1)
fcast_mean_arma = fcast_arma.predicted_mean #this gives the point predictions
plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(predvalues), label = 'Forecast (AR(3) with intercept on differenced data)', color = 'black')
plt.plot(tme_future, np.exp(fcast_mean_arma), label = 'Forecast (ARMA(3,2) without intercept on differenced data)', color = 'green')
plt.plot(tme_future, np.exp(fcast_mean_ma), label = 'Forecast (MA(1) on twice differenced data)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  386
Model:                 ARIMA(3, 2, 2)   Log Likelihood                1184.277
Date:                Thu, 17 Apr 2025   AIC                          -2356.554
Time:                        00:31:41   BIC                          -2332.850
Sample:                             0   HQIC                         -2347.152
                                - 386
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.0097      0.490     -0.020      0.984      -0.970       0.951
ar.L2          0.0023      0.068      0.034      0.973      -0.130       0.135
ar.L3          0.1197      0.059      2.046      0.041       0.005       0.234
ma.L1         -0.7970      0.500     -1.594      0.111      -1.777       0.183
ma.L2         -0.1166      0.448     -0.260      0.795      -0.994       0.761
sigma2         0.0001   7.49e-06     16.293      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):                38.55
Prob(Q):                              0.99   Prob(JB):                         0.00
Heteroskedasticity (H):               0.54   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.50
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

*(1 figure omitted — see the original notebook.)*

It is interesting that ARIMA(3, 2, 2) and ARIMA(3, 1, 0) give nearly the same predictions.

---

[← Best ARMA model overall](04-best-arma-model-overall.md) · [Up: contents](index.md)
