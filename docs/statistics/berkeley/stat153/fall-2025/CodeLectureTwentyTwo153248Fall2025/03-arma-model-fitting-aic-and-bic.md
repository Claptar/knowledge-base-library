---
title: ARMA($p$, $q$) model fitting, AIC and BIC
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# ARMA($p$, $q$) model fitting, AIC and BIC

We now fit an ARMA($p$, $q$) model to this differenced dataset. Let us see how to fit an ARMA(1, 1) model.

```python
arma11 = ARIMA(ylogdiff, order = (1, 0, 1)).fit()
print(arma11.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(1, 0, 1)   Log Likelihood                 932.499
Date:                Tue, 18 Nov 2025   AIC                          -1856.999
Time:                        16:22:26   BIC                          -1842.014
Sample:                             0   HQIC                         -1851.010
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0154      0.001     10.429      0.000       0.013       0.018
ar.L1          0.6911      0.139      4.955      0.000       0.418       0.964
ma.L1         -0.4642      0.152     -3.054      0.002      -0.762      -0.166
sigma2         0.0002   3.97e-06     38.092      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.27   Jarque-Bera (JB):              7596.39
Prob(Q):                              0.60   Prob(JB):                         0.00
Heteroskedasticity (H):               1.55   Skew:                            -0.01
Prob(H) (two-sided):                  0.03   Kurtosis:                        27.13
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

The summary above gives maximized log-likelihood (called Log Likelihood) and also AIC and BIC. The maximized log-likelihood is the value of the log-likelihood at the MLEs. The AIC are BIC are given by:

AIC for a model = $(-2) \times$ (maximized log-likelihood) + 2 (number of parameters)

BIC for a model = $(-2) \times $(maximized log-likelihood) + ($\log n$) \times (number of parameters)
where $n$ denotes the sample size.

```python
print(arma11.llf) #maximized log-likelihood
print(arma11.aic, (-2)*arma11.llf + 2*4) #AIC (note the number of parameters here equals 4)
print(arma11.bic, (-2)*arma11.llf + np.log(len(ylogdiff))*4) #BIC
```

```
932.4992964756076
-1856.9985929512152 -1856.9985929512152
-1842.0137801890546 -1842.0137801890546
```

## Selecting the best ARMA($p$, $q$) model by automatic model selection

We will go over all ARMA($p$, $q$) models with $p \leq 5$ and $q \leq 5$ and find the best fitting ARMA($p$, $q$) model using AIC and BIC. In the code below, if parameter estimation does not work for some reason for some $p$ and $q$, then the value NaN is given for AIC and BIC for that model.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.

dt = ylogdiff
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

---

← ARMA($p$, $q$) models for the GNP dataset · [Up: contents](index.md) · [ARIMA Models →](04-arima-models.md)
