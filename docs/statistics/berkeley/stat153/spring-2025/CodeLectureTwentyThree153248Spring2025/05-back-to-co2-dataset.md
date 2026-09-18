---
title: Back to co2 dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Back to co2 dataset

Let us now get back to the co2 dataset and fit a suitable SARIMA model.

```python
co2 = pd.read_csv('co2_TSA.csv')
print(co2)
y = co2['x']
```

```
Unnamed: 0       x
0             1  363.05
1             2  364.18
2             3  364.87
3             4  364.47
4             5  364.32
..          ...     ...
127         128  368.69
128         129  368.55
129         130  373.39
130         131  378.49
131         132  381.62

[132 rows x 2 columns]
```

From the sample ACF and PACF, we argued that $MA(1) \times MA(1)_{12}$ is a suitable model for the twice differenced data $\nabla_s \nabla y_t$. We can fit this using the ARIMA function as shown below.

```python
m1_co2 = ARIMA(y, order = (0, 1, 1), seasonal_order = (0, 1, 1, 12)).fit()
print(m1_co2.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                x   No. Observations:                  132
Model:             ARIMA(0, 1, 1)x(0, 1, 1, 12)   Log Likelihood                -139.547
Date:                          Sat, 19 Apr 2025   AIC                            285.095
Time:                                  00:59:24   BIC                            293.432
Sample:                                       0   HQIC                           288.481
                                          - 132
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.5791      0.093     -6.254      0.000      -0.761      -0.398
ma.S.L12      -0.8205      0.117     -7.017      0.000      -1.050      -0.591
sigma2         0.5447      0.073      7.484      0.000       0.402       0.687
===================================================================================
Ljung-Box (L1) (Q):                   0.01   Jarque-Bera (JB):                 2.13
Prob(Q):                              0.94   Prob(JB):                         0.34
Heteroskedasticity (H):               1.04   Skew:                            -0.15
Prob(H) (two-sided):                  0.90   Kurtosis:                         3.58
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Predictions using this fitted ARIMA model are obtained in the usual way via the get_prediction function.

```python
k = 48
n = len(y)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast = m1_co2.get_prediction(start = n, end = n+k-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Retail Alcohol Sales Data

Let us now consider the following data from FRED.

```python
#The following is FRED data on retail sales (in millions of dollars) for beer, wine and liquor stores (https://fred.stlouisfed.org/series/MRTSSM4453USN)
beersales = pd.read_csv('MRTSSM4453USN_March2025.csv')
print(beersales.head())
y = beersales['MRTSSM4453USN']
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.title('Retail Sales: Beer, wine and liquor stores')
plt.show()
```

```
observation_date  MRTSSM4453USN
0       1992-01-01           1509
1       1992-02-01           1541
2       1992-03-01           1597
3       1992-04-01           1675
4       1992-05-01           1822
```

*(1 figure omitted — see the original notebook.)*

In order to fit a stationary model, let us first preprocess by differencing. The seasonal differences are calculated and plotted below.

```python
#Seasonal differencing: y_t - y_{t-12}
ydiff12 = y.diff(periods = 12)
plt.figure(figsize = (12, 7))
plt.plot(ydiff12)
plt.xlabel('Time (months)')
plt.ylabel('value')
plt.title('Seasonal Differences of Alcohol Sales')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Certain increasing/decreasing trends are visible in the above data. We do one more differencing below.

```python
#We now take one more differencing; this time regular differencing
y2d = ydiff12.diff()
plt.figure(figsize = (12, 7))
plt.plot(y2d)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us compute the ACF and PACF.

```python
L = 60
# Plot sample ACF/PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))
plot_acf(y2d.dropna(), lags=L, ax=ax1, title='Sample ACF')
plot_pacf(y2d.dropna(), lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It appears a little hard to determine the orders for an appropriate SARIMA model directly from the above ACF and PACF plot. Below we use a brute force approach where we enumerate a whole bunch of $ARIMA(p, d, q) \times (P, D, Q)_{12}$ models, and then pick the best model via the AIC and BIC criteria.

```python
dt = y
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
                    except Exception as e:
                        print(f"ARIMA({p},{d},{q})x({P},{D},{Q}) failed: {e}")
                        continue

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Find best models
best_aic_idx = results_df['AIC'].idxmin()
best_bic_idx = results_df['BIC'].idxmin()

best_aic_model = results_df.loc[best_aic_idx]
best_bic_model = results_df.loc[best_bic_idx]

# Display results
print("Best model by AIC:")
print(best_aic_model)

print("\nBest model by BIC:")
print(best_bic_model)
```

```
ARIMA(0,0,1)x(2,1,2) failed: LU decomposition error.
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
Best model by AIC:
p         2.000000
d         1.000000
q         1.000000
P         2.000000
D         1.000000
Q         2.000000
AIC    4610.329092
BIC    4641.913372
Name: 151, dtype: float64

Best model by BIC:
p         2.000000
d         1.000000
q         0.000000
P         2.000000
D         1.000000
Q         2.000000
AIC    4610.745280
BIC    4638.381525
Name: 142, dtype: float64
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
```

Of the considered models, the best AIC model is $ARIMA(2, 1, 1) \times (2, 1, 2)_{12}$ and the best BIC model is $ARIMA(2, 1, 0) \times (2, 1, 2)_{12}$. We fit these models below. Observe that there seem to be convergence issues for quite a few models. Fitting these models is not easy and the process involves nonlinear optimization for calculating the MLEs.

```python
m1 = ARIMA(y, order = (2, 1, 1), seasonal_order = (2, 1, 2, 12)).fit()
print(m1.summary())
```

```
SARIMAX Results
=============================================================================================
Dep. Variable:                         MRTSSM4453USN   No. Observations:                  396
Model:             ARIMA(2, 1, 1)x(2, 1, [1, 2], 12)   Log Likelihood               -2297.165
Date:                               Sat, 19 Apr 2025   AIC                           4610.329
Time:                                       01:07:26   BIC                           4641.913
Sample:                                            0   HQIC                          4622.858
                                               - 396
Covariance Type:                                 opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.7865      0.134     -5.852      0.000      -1.050      -0.523
ar.L2         -0.3542      0.077     -4.591      0.000      -0.505      -0.203
ma.L1          0.1276      0.141      0.902      0.367      -0.150       0.405
ar.S.L12       1.0035      0.076     13.146      0.000       0.854       1.153
ar.S.L24      -0.6660      0.053    -12.544      0.000      -0.770      -0.562
ma.S.L12      -1.4078      0.087    -16.169      0.000      -1.578      -1.237
ma.S.L24       0.8210      0.068     12.162      0.000       0.689       0.953
sigma2      9127.9453    449.288     20.316      0.000    8247.357       1e+04
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):               241.51
Prob(Q):                              0.97   Prob(JB):                         0.00
Heteroskedasticity (H):               4.64   Skew:                             0.46
Prob(H) (two-sided):                  0.00   Kurtosis:                         6.78
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
m2 = ARIMA(y, order = (2, 1, 0), seasonal_order = (2, 1, 2, 12)).fit()
print(m2.summary())
```

```
SARIMAX Results
=============================================================================================
Dep. Variable:                         MRTSSM4453USN   No. Observations:                  396
Model:             ARIMA(2, 1, 0)x(2, 1, [1, 2], 12)   Log Likelihood               -2298.373
Date:                               Sat, 19 Apr 2025   AIC                           4610.745
Time:                                       01:07:31   BIC                           4638.382
Sample:                                            0   HQIC                          4621.708
                                               - 396
Covariance Type:                                 opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.7378      0.041    -17.980      0.000      -0.818      -0.657
ar.L2         -0.3549      0.036     -9.849      0.000      -0.425      -0.284
ar.S.L12       1.2685      0.073     17.396      0.000       1.126       1.411
ar.S.L24      -0.4537      0.067     -6.800      0.000      -0.584      -0.323
ma.S.L12      -1.7809      0.092    -19.434      0.000      -1.961      -1.601
ma.S.L24       0.9368      0.089     10.530      0.000       0.762       1.111
sigma2      8939.0960    561.492     15.920      0.000    7838.592       1e+04
===================================================================================
Ljung-Box (L1) (Q):                   0.37   Jarque-Bera (JB):               231.29
Prob(Q):                              0.54   Prob(JB):                         0.00
Heteroskedasticity (H):               4.64   Skew:                             0.46
Prob(H) (two-sided):                  0.00   Kurtosis:                         6.69
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  warnings.warn("Maximum Likelihood optimization failed to "
```

Below we obtain predictions using both the models.

```python
k = 120
n = len(y)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast1 = m1.get_prediction(start = n, end = n+k-1).predicted_mean
fcast2 = m2.get_prediction(start = n, end = n+k-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, fcast1, label = 'Forecast (M1)', color = 'red')
plt.plot(tme_future, fcast2, label = 'Forecast (M2)', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions by both models seems reasonable. At the initial few future time points, the predictions are also quite close to each other.

---

[← Multiplicative Seasonal ARMA models](04-multiplicative-seasonal-arma-models.md) · [Up: contents](index.md) · [MA(1) Parameter Estimation →](06-ma-1-parameter-estimation.md)
