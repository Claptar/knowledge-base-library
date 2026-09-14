---
title: Find best models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find best models

**Source:** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Other Models for TTLCONS

Below we consider the double differenced dataset.

```python
ylogdiff2 = np.diff(np.diff(ylog))
plt.plot(ylogdiff2)
plt.title("Double Differenced Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us attempt to find best ARMA($p$, $q$) models for this data.

```python
dt = 100*ylogdiff2 #notice the multiplication by 100 (without it the code does not seem to work well)
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

---

[← Convert to DataFrame](12-convert-to-dataframe.md) · [Up: contents](index.md) · [Best AR model (MA = 0) →](14-best-ar-model-ma-0.md)
