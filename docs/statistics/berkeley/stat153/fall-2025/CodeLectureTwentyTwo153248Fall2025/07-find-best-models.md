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

## TTLCONS Dataset

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

---

[← Convert to DataFrame](06-convert-to-dataframe.md) · [Up: contents](index.md) · [Best AR model (MA = 0) →](08-best-ar-model-ma-0.md)
