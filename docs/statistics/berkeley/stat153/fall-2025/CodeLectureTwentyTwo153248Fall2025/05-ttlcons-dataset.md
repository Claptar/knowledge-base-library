---
title: TTLCONS Dataset
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# TTLCONS Dataset

```python
ttlcons = pd.read_csv('TTLCONS_13Nov2025.csv')
print(ttlcons.tail())
y = ttlcons['TTLCONS'].to_numpy()
print(len(y))
plt.plot(y)
plt.title('Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

```
observation_date  TTLCONS
386       2025-03-01  2150847
387       2025-04-01  2153440
388       2025-05-01  2149124
389       2025-06-01  2140546
390       2025-07-01  2139110
391
```

*(1 figure omitted — see the original notebook.)*

We fit models to the logarithm of the data.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can obtain candidate models by differencing the data, and looking at acf and pacf.

```python
ylogdiff = np.diff(ylog)
plt.plot(ylogdiff, color = 'black')
plt.title('Percent change in Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

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

From the above ACF and PACF plots, probably the best model for ylogdiff is AR(3).

Let us go over all possible $p$ and $q$ and find the best model for ylogdiff.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.

dt = ylogdiff #arma fitting can be unstable. Change dt = ylogdiff to dt = 100*ylogdiff and check if results change
pmax = 5
qmax = 5

aicmat = np.full((pmax + 1, qmax + 1), np.nan)
bicmat = np.full((pmax + 1, qmax + 1), np.nan)

for i in range(pmax + 1):
    for j in range(qmax + 1):
        try:
            model = ARIMA(dt, order=(i, 0, j)).fit()
            aicmat[i, j] = model.aic
            bicmat[i, j] = model.bic
        except Exception as e:
            # Some models may not converge; skip them
            print(f"ARIMA({i},0,{j}) failed: {e}")
            continue

aic_df = pd.DataFrame(aicmat, index=[f'AR({i})' for i in range(pmax+1)],
                               columns=[f'MA({j})' for j in range(qmax+1)])
bic_df = pd.DataFrame(bicmat, index=[f'AR({i})' for i in range(pmax+1)],
                               columns=[f'MA({j})' for j in range(qmax+1)])

# Best AR model (MA = 0)
best_ar_aic = np.nanargmin(aicmat[:, 0])
best_ar_bic = np.nanargmin(bicmat[:, 0])

# Best MA model (AR = 0)
best_ma_aic = np.nanargmin(aicmat[0, :])
best_ma_bic = np.nanargmin(bicmat[0, :])

# Best ARMA model overall
best_arma_aic = np.unravel_index(np.nanargmin(aicmat), aicmat.shape)
best_arma_bic = np.unravel_index(np.nanargmin(bicmat), bicmat.shape)

# Print results
print(f"Best AR model by AIC: AR({best_ar_aic})")
print(f"Best AR model by BIC: AR({best_ar_bic})")

print(f"Best MA model by AIC: MA({best_ma_aic})")
print(f"Best MA model by BIC: MA({best_ma_bic})")

print(f"Best ARMA model by AIC: ARMA{best_arma_aic}")
print(f"Best ARMA model by BIC: ARMA{best_arma_bic}")
```

```
Best AR model by AIC: AR(5)
Best AR model by BIC: AR(3)
Best MA model by AIC: MA(5)
Best MA model by BIC: MA(3)
Best ARMA model by AIC: ARMA(1, 1)
Best ARMA model by BIC: ARMA(1, 1)
```

Best AR model: AR(3) (using BIC) and AR(5) (using AIC)

Best MA model: MA(3) (using BIC) and MA(5) (using AIC)

Best overall ARMA model: ARMA(1, 1)

Instead of fitting the best model to ylogdiff, we can find best models for ylog (in this case, we shall use ARIMA(p, d, q) and vary p, d, q).

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
            #trend = None

            try:
                model = ARIMA(dt, order=(p, d, q)).fit()

                results.append({
                    'p': p, 'd': d, 'q': q,
                    'AIC': model.aic,
                    'BIC': model.bic
                })
            except Exception as e:
                print(f"ARIMA({p},{d},{q}) failed: {e}")
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
p         1.000000
d         1.000000
q         1.000000
AIC   -2405.521236
BIC   -2393.622796
Name: 25, dtype: float64

Best model by BIC:
p         1.000000
d         1.000000
q         1.000000
AIC   -2405.521236
BIC   -2393.622796
Name: 25, dtype: float64
```

Best model is ARIMA(1, 1, 1). Let us use it for prediction.

```python
n = len(ylog)
k = 100
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
```

```python
#ARIMA(1, 1, 1) model for ylog:
arima111 = ARIMA(ylog, order = (1, 1, 1)).fit()
print(arima111.summary())
fcast_arima111 = arima111.get_prediction(start = n, end = n+k-1).predicted_mean
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  391
Model:                 ARIMA(1, 1, 1)   Log Likelihood                1205.761
Date:                Tue, 18 Nov 2025   AIC                          -2405.521
Time:                        20:58:32   BIC                          -2393.623
Sample:                             0   HQIC                         -2400.805
                                - 391
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.9682      0.018     54.374      0.000       0.933       1.003
ma.L1         -0.8394      0.040    -21.130      0.000      -0.917      -0.762
sigma2         0.0001   6.69e-06     17.962      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.92   Jarque-Bera (JB):                49.59
Prob(Q):                              0.34   Prob(JB):                         0.00
Heteroskedasticity (H):               0.54   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.69
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_arima111, label = 'Forecast (ARIMA(1, 1, 1) on ylog)', color = 'darkgreen')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

If we include the intercept term in ARIMA(1, 1, 1), then the predictions will be different.

```python
arima111_t = ARIMA(ylog, order = (1, 1, 1), trend = 't').fit() #trend = 't' includes the intercept term
fcast_arima111_t = arima111_t.get_prediction(start = n, end = n+k-1).predicted_mean
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_arima111, label = 'Forecast (ARIMA(1, 1, 1) on ylog)', color = 'darkgreen')
plt.plot(tme_future, fcast_arima111_t, label = 'Forecast (ARIMA(1, 1, 1) on ylog with intercept)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Which of these predictions would we prefer? We can compare the AIC and BIC of the model with and without the intercept.

```python
print(arima111.aic, arima111.bic)
print(arima111_t.aic, arima111_t.bic)
```

```
-2405.524371156208 -2393.625930938837
-2406.8821088764494 -2391.0175219199546
```

It is interesting that in terms of the AIC, the model with intercept is better, while in terms of BIC, the model without intercept is better. The predictions for the model with no intercept look more natural.

---

[← ARIMA Models](04-arima-models.md) · [Up: contents](index.md) · [Other Models for TTLCONS →](06-other-models-for-ttlcons.md)
