---
title: Plot sample ACF/PACF
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot sample ACF/PACF

**Source:** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))
plot_acf(ylog2d, lags=L, ax=ax1, title='Sample ACF')
plot_pacf(ylog2d, lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Two simple models for this dataset are: $MA(0, 1) \times MA(0, 1)_{12}$ or $AR(1, 0) \times AR(1, 0)_{12}$. For the original ylog, these models would be $ARIMA(0, 1, 1) \times (0, 1, 1)_{12}$ and $ARIMA(1, 1, 0) \times (1, 1, 0)_{12}$. Below we fit these models.

```python
#Fit these models:
m1 = ARIMA(ylog, order = (0, 1, 1), seasonal_order = (0, 1, 1, 12)).fit()
print(m1.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                y   No. Observations:                  144
Model:             ARIMA(0, 1, 1)x(0, 1, 1, 12)   Log Likelihood                 244.696
Date:                          Thu, 20 Nov 2025   AIC                           -483.393
Time:                                  23:00:26   BIC                           -474.767
Sample:                                       0   HQIC                          -479.888
                                          - 144
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.4018      0.073     -5.503      0.000      -0.545      -0.259
ma.S.L12      -0.5570      0.096     -5.785      0.000      -0.746      -0.368
sigma2         0.0013      0.000      9.121      0.000       0.001       0.002
===================================================================================
Ljung-Box (L1) (Q):                   0.04   Jarque-Bera (JB):                 1.90
Prob(Q):                              0.84   Prob(JB):                         0.39
Heteroskedasticity (H):               0.58   Skew:                             0.02
Prob(H) (two-sided):                  0.08   Kurtosis:                         3.59
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
m2 = ARIMA(ylog, order = (1, 1, 0), seasonal_order = (1, 1, 0, 12)).fit()
print(m2.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                y   No. Observations:                  144
Model:             ARIMA(1, 1, 0)x(1, 1, 0, 12)   Log Likelihood                 240.406
Date:                          Thu, 20 Nov 2025   AIC                           -474.813
Time:                                  23:00:27   BIC                           -466.187
Sample:                                       0   HQIC                          -471.308
                                          - 144
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.3747      0.071     -5.273      0.000      -0.514      -0.235
ar.S.L12      -0.4636      0.071     -6.510      0.000      -0.603      -0.324
sigma2         0.0015      0.000      8.333      0.000       0.001       0.002
===================================================================================
Ljung-Box (L1) (Q):                   0.11   Jarque-Bera (JB):                 0.54
Prob(Q):                              0.74   Prob(JB):                         0.76
Heteroskedasticity (H):               0.53   Skew:                             0.12
Prob(H) (two-sided):                  0.04   Kurtosis:                         3.20
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Here are the predictions by these two models.

```python
k = 72
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast_1 = m1.get_prediction(start = n, end = n+k-1).predicted_mean
fcast_2 = m2.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (m1)', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Forecast (m2)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions are quite similar to each other.

Below we loop over a set of values of $p, d, q$ and $P, D, Q$ to find the best models (in terms of AIC and BIC).

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.


dt = ylog
pmax, dmax, qmax = 2, 1, 2
Pmax, D, Qmax = 2, 1, 2
seasonal_period = 12

results = []

for p in range(pmax + 1):
    for d in range(dmax + 1):
        for q in range(qmax + 1):
            for P in range(Pmax + 1):
                for Q in range(Qmax + 1):
                    try:
                        model = ARIMA(dt,
                                      order=(p, d, q),
                                      seasonal_order=(P, D, Q, seasonal_period)).fit()
                        results.append({
                            'p': p, 'd': d, 'q': q,
                            'P': P, 'D': D, 'Q': Q,
                            'AIC': model.aic,
                            'BIC': model.bic
                        })
                    # Progress message
                        print(f"Successfully fit ARIMA({p},{d},{q})x({P},{D},{Q})")
                    except Exception as e:
                        print(f"ARIMA({p},{d},{q})x({P},{D},{Q}) failed: {e}")
                        continue

---

[← Plot sample ACF/PACF](16-plot-sample-acf-pacf.md) · [Up: contents](index.md) · [Convert results to DataFrame →](18-convert-results-to-dataframe.md)
