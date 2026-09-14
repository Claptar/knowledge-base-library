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
Best AR model by AIC: AR(2)
Best AR model by BIC: AR(2)
Best MA model by AIC: MA(3)
Best MA model by BIC: MA(2)
Best ARMA model by AIC: ARMA(2, 0)
Best ARMA model by BIC: ARMA(2, 0)
```

It seems that no errors were thrown for any of the ARMA models. There are a lot of warnings though. Go back and remove the warnings suppression code.

The best overall model here is AR(2).

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ylogdiff, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

AR(2) seems like a good model overall.

```python
ar2 = ARIMA(ylogdiff, order = (2, 0, 0)).fit()
print(ar2.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(2, 0, 0)   Log Likelihood                 935.005
Date:                Tue, 18 Nov 2025   AIC                          -1862.010
Time:                        16:27:21   BIC                          -1847.025
Sample:                             0   HQIC                         -1856.022
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0154      0.001     10.725      0.000       0.013       0.018
ar.L1          0.1971      0.025      7.856      0.000       0.148       0.246
ar.L2          0.2077      0.066      3.140      0.002       0.078       0.337
sigma2         0.0001   3.86e-06     38.565      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):              7833.57
Prob(Q):                              0.97   Prob(JB):                         0.00
Heteroskedasticity (H):               1.61   Skew:                            -0.09
Prob(H) (two-sided):                  0.02   Kurtosis:                        27.51
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Below we obtain predictions for this AR(2) model. These would be predictions for $\log(y_t) - \log(y_{t-1})$. We can convert them to predictions for $\log(y_t)$ as in the code below.

```python
n = len(y)
k = 100
fcast_diff_1 = ar2.get_prediction(start = n-1, end = n+k-2).predicted_mean #these are the forecasts for the differenced data
last_observed_ylog = ylog[-1]
fcast_1 = np.zeros(k)
fcast_1[0] = last_observed_ylog + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

```python
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (AR(2) on ylogdiff)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## ARIMA Models

Instead of fitting AR(2) to the differences of the logs, we can fit ARIMA with $p = 2, d = 1, q = 0$ on logarithms.

```python
ar2_nodiff = ARIMA(ylog, order = (2, 1, 0)).fit()
print(ar2_nodiff.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  314
Model:                 ARIMA(2, 1, 0)   Log Likelihood                 909.630
Date:                Tue, 18 Nov 2025   AIC                          -1813.260
Time:                        16:38:29   BIC                          -1802.022
Sample:                             0   HQIC                         -1808.769
                                - 314
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.4048      0.024     16.847      0.000       0.358       0.452
ar.L2          0.4130      0.045      9.193      0.000       0.325       0.501
sigma2         0.0002   5.51e-06     31.677      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   3.52   Jarque-Bera (JB):             13524.06
Prob(Q):                              0.06   Prob(JB):                         0.00
Heteroskedasticity (H):               1.71   Skew:                             1.58
Prob(H) (two-sided):                  0.01   Kurtosis:                        35.05
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
fcast_2 = ar2_nodiff.get_prediction(start = n, end = n+k-1).predicted_mean

plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (AR(2) on ylogdiff)', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Forecast (ARIMA(2, 1, 0) on ylog)', color = 'darkgreen')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The reason the predictions are different is because the ARIMA model does not fit a constant term when $d > 1$. To get the constant term with $d = 1$, one needs to use the trend = 't' option.

```python
ar2_nodiff_withintercept = ARIMA(ylog, order = (2, 1, 0), trend = 't').fit() #note the trend = 't'
print(ar2_nodiff_withintercept.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  314
Model:                 ARIMA(2, 1, 0)   Log Likelihood                 935.005
Date:                Tue, 18 Nov 2025   AIC                          -1862.010
Time:                        16:42:17   BIC                          -1847.025
Sample:                             0   HQIC                         -1856.022
                                - 314
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.0154      0.001     10.725      0.000       0.013       0.018
ar.L1          0.1971      0.025      7.856      0.000       0.148       0.246
ar.L2          0.2077      0.066      3.140      0.002       0.078       0.337
sigma2         0.0001   3.86e-06     38.565      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):              7833.57
Prob(Q):                              0.97   Prob(JB):                         0.00
Heteroskedasticity (H):               1.61   Skew:                            -0.09
Prob(H) (two-sided):                  0.02   Kurtosis:                        27.51
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
print(ar2.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(2, 0, 0)   Log Likelihood                 935.005
Date:                Tue, 18 Nov 2025   AIC                          -1862.010
Time:                        16:41:07   BIC                          -1847.025
Sample:                             0   HQIC                         -1856.022
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0154      0.001     10.725      0.000       0.013       0.018
ar.L1          0.1971      0.025      7.856      0.000       0.148       0.246
ar.L2          0.2077      0.066      3.140      0.002       0.078       0.337
sigma2         0.0001   3.86e-06     38.565      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):              7833.57
Prob(Q):                              0.97   Prob(JB):                         0.00
Heteroskedasticity (H):               1.61   Skew:                            -0.09
Prob(H) (two-sided):                  0.02   Kurtosis:                        27.51
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Note that the summaries for AR(2) fitted to ylogdiff and ARIMA((2, 1, 0), trend = 'n') fitted to ylog are almost fully identical (one difference is in the number of observations; it is one smaller for AR(2)).

```python
fcast_3 = ar2_nodiff_withintercept.get_prediction(start = n, end = n+k-1).predicted_mean

plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (AR(2) on ylogdiff)', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Forecast (ARIMA(2, 1, 0) on ylog)', color = 'darkgreen')
plt.plot(tme_future, fcast_3, label = 'Forecast (ARIMA(2, 1, 0) with trend = t on ylog)', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions on ARIMA(2, 1, 0) with trend = t coincide with the predictions for $\log y_t$ obtained via AR(2) on $\log (y_t/y_{t-1})$.

### Selecting the best ARIMA($p$, $d$, $q$) model by AIC or BIC

Below we go over all possible values of $p \leq 5$, $d \leq 2$ and $q \leq 5$ and calculate the AIC, BIC values of each ARIMA model. We use the default ARIMA (no modification for inclusion of intercepts when $d \geq 1$).

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.

dt = ylog
pmax, dmax, qmax = 5, 2, 5

results = []

for p in range(pmax + 1):
    for d in range(dmax + 1):
        for q in range(qmax + 1):

            # Use linear trend only when d = 1
            #trend = 't' if d == 1 else None
            #trend = 'n'if d >= 1 else 'c'

            try:
                model = ARIMA(dt, order=(p, d, q)).fit()

                results.append({
                    'p': p, 'd': d, 'q': q,
                    'trend': trend,
                    'AIC': model.aic,
                    'BIC': model.bic
                })
            except Exception as e:
                print(f"ARIMA({p},{d},{q}, trend={trend}) failed: {e}")
                continue

---

[← Best ARMA model overall](04-best-arma-model-overall.md) · [Up: contents](index.md) · [Convert to DataFrame →](06-convert-to-dataframe.md)
