---
title: ARIMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# ARIMA Models

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

## Selecting the best ARIMA($p$, $d$, $q$) model by AIC or BIC

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

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Find best models
best_aic_model = results_df.loc[results_df['AIC'].idxmin()]
best_bic_model = results_df.loc[results_df['BIC'].idxmin()]

print("Best model by AIC:")
print(best_aic_model)

print("\nBest model by BIC:")
print(best_bic_model)
```

```
Best model by AIC:
p                  1
d                  1
q                  3
trend              n
AIC     -1860.201397
BIC     -1841.470381
Name: 27, dtype: object

Best model by BIC:
p                  0
d                  2
q                  3
trend              n
AIC     -1856.667535
BIC     -1841.695523
Name: 15, dtype: object
```

The best ARIMA($p, d, q$) model (searched over $p \leq 5$, $d \leq 2$, $q \leq 5$) is ARIMA(1, 1, 3) (by AIC) and ARIMA(0, 2, 3) (by BIC). Note I used the default ARIMA functions with no modification for including intercepts in the models with $d \geq 1$.

```python
arima113 = ARIMA(ylog, order = (1, 1, 3)).fit()
fcast_4 = arima113.get_prediction(start = n, end = n+k-1).predicted_mean

arima023 = ARIMA(ylog, order = (0, 2, 3)).fit()
fcast_5 = arima023.get_prediction(start = n, end = n+k-1).predicted_mean

plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_2, label = 'Forecast (ARIMA(2, 1, 0) on ylog)', color = 'darkgreen')
plt.plot(tme_future, fcast_3, label = 'Forecast (ARIMA(2, 1, 0) with trend = t on ylog)', color = 'black')
plt.plot(tme_future, fcast_4, label = 'Forecast (ARIMA(1, 1, 3) on ylog)', color = 'red')
plt.plot(tme_future, fcast_5, label = 'Forecast (ARIMA(0, 2, 3) on ylog)', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here are the predictions on the original data.

```python
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, np.exp(fcast_3), label = 'Forecast (ARIMA(2, 1, 0) with trend = t on ylog)', color = 'black')
plt.plot(tme_future, np.exp(fcast_4), label = 'Forecast (ARIMA(1, 1, 3) on ylog)', color = 'red')
plt.plot(tme_future, np.exp(fcast_5), label = 'Forecast (ARIMA(0, 2, 3) on ylog)', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can compare the AIC and BIC of the best models above (ARIMA(1, 1, 3) and ARIMA(0, 2, 3)) with ARIMA(2, 1, 0) with trend = t

```python
print(ar2_nodiff_withintercept.aic, ar2_nodiff_withintercept.bic)
print(arima113.aic, arima113.bic)
print(arima023.aic, arima023.bic)
```

```
-1862.0098207563674 -1847.0250079942068
-1860.2013971103497 -1841.470381157649
-1856.6675352600519 -1841.6955225088138
```

This suggests that the AR(2) with intercept is better than these models ARIMA(1, 1, 3) and ARIMA(0, 2, 3) without intercepts.

Note that the predictions look different but this is because we are looking at long range forecasts ($k = 100$ corresponds to 25 future years!) If we look at short range forecasts (such as $k = 12$), then the predictions will be quite close to each other.

```python
plt.plot(tme, y, label = 'Data')
#below we only plot the first 8 predictions
k_short = 12
plt.plot(tme_future[0:k_short], np.exp(fcast_3)[0:k_short], label = 'Forecast (ARIMA(2, 1, 0) with trend = t on ylog)', color = 'black')
plt.plot(tme_future[0:k_short], np.exp(fcast_4)[0:k_short], label = 'Forecast (ARIMA(1, 1, 3) on ylog)', color = 'red')
plt.plot(tme_future[0:k_short], np.exp(fcast_5)[0:k_short], label = 'Forecast (ARIMA(0, 2, 3) on ylog)', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← ARMA($p$, $q$) model fitting, AIC and BIC](03-arma-model-fitting-aic-and-bic.md) · [Up: contents](index.md) · [TTLCONS Dataset →](05-ttlcons-dataset.md)
