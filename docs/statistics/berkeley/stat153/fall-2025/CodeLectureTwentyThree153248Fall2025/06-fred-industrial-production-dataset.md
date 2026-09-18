---
title: FRED Industrial Production Dataset
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# FRED Industrial Production Dataset

The following dataset is from FRED (see https://fred.stlouisfed.org/series/IPB50001N). It gives monthly data on the Industrial Production (IP) index which measures the total industrial output and is indicative of the health of the economy.

```python
ip = pd.read_csv('IPB50001N _20Nov2025.csv')
print(ip.head())
y = ip['IPB50001N'].to_numpy()
plt.plot(y)
plt.xlabel('Month')
plt.ylabel('Index')
plt.title('Industrial Production: Total Index')
plt.show()
```

```
observation_date  IPB50001N
0       1919-01-01     4.7841
1       1919-02-01     4.5959
2       1919-03-01     4.4884
3       1919-04-01     4.5691
4       1919-05-01     4.7035
```

*(1 figure omitted — see the original notebook.)*

An older version of this dataset was analyzed in the book Shumway and Stoffer (see Example 3.46 in the fourth edition). Their first step is to take first order differences of the data.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.


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
                    # Progress message
                        print(f"Successfully fit ARIMA({p},{d},{q})x({P},{D},{Q})")
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
Successfully fit ARIMA(0,0,0)x(0,1,0)
Successfully fit ARIMA(0,0,0)x(0,1,1)
Successfully fit ARIMA(0,0,0)x(0,1,2)
Successfully fit ARIMA(0,0,0)x(1,1,0)
Successfully fit ARIMA(0,0,0)x(1,1,1)
Successfully fit ARIMA(0,0,0)x(1,1,2)
Successfully fit ARIMA(0,0,0)x(2,1,0)
Successfully fit ARIMA(0,0,0)x(2,1,1)
Successfully fit ARIMA(0,0,0)x(2,1,2)
Successfully fit ARIMA(0,0,1)x(0,1,0)
Successfully fit ARIMA(0,0,1)x(0,1,1)
Successfully fit ARIMA(0,0,1)x(0,1,2)
Successfully fit ARIMA(0,0,1)x(1,1,0)
Successfully fit ARIMA(0,0,1)x(1,1,1)
Successfully fit ARIMA(0,0,1)x(1,1,2)
Successfully fit ARIMA(0,0,1)x(2,1,0)
Successfully fit ARIMA(0,0,1)x(2,1,1)
Successfully fit ARIMA(0,0,1)x(2,1,2)
Successfully fit ARIMA(0,0,2)x(0,1,0)
Successfully fit ARIMA(0,0,2)x(0,1,1)
Successfully fit ARIMA(0,0,2)x(0,1,2)
Successfully fit ARIMA(0,0,2)x(1,1,0)
Successfully fit ARIMA(0,0,2)x(1,1,1)
Successfully fit ARIMA(0,0,2)x(1,1,2)
Successfully fit ARIMA(0,0,2)x(2,1,0)
Successfully fit ARIMA(0,0,2)x(2,1,1)
Successfully fit ARIMA(0,0,2)x(2,1,2)
Successfully fit ARIMA(0,1,0)x(0,1,0)
Successfully fit ARIMA(0,1,0)x(0,1,1)
Successfully fit ARIMA(0,1,0)x(0,1,2)
Successfully fit ARIMA(0,1,0)x(1,1,0)
Successfully fit ARIMA(0,1,0)x(1,1,1)
Successfully fit ARIMA(0,1,0)x(1,1,2)
Successfully fit ARIMA(0,1,0)x(2,1,0)
Successfully fit ARIMA(0,1,0)x(2,1,1)
Successfully fit ARIMA(0,1,0)x(2,1,2)
Successfully fit ARIMA(0,1,1)x(0,1,0)
Successfully fit ARIMA(0,1,1)x(0,1,1)
Successfully fit ARIMA(0,1,1)x(0,1,2)
Successfully fit ARIMA(0,1,1)x(1,1,0)
Successfully fit ARIMA(0,1,1)x(1,1,1)
Successfully fit ARIMA(0,1,1)x(1,1,2)
Successfully fit ARIMA(0,1,1)x(2,1,0)
Successfully fit ARIMA(0,1,1)x(2,1,1)
Successfully fit ARIMA(0,1,1)x(2,1,2)
Successfully fit ARIMA(0,1,2)x(0,1,0)
Successfully fit ARIMA(0,1,2)x(0,1,1)
Successfully fit ARIMA(0,1,2)x(0,1,2)
Successfully fit ARIMA(0,1,2)x(1,1,0)
Successfully fit ARIMA(0,1,2)x(1,1,1)
Successfully fit ARIMA(0,1,2)x(1,1,2)
Successfully fit ARIMA(0,1,2)x(2,1,0)
Successfully fit ARIMA(0,1,2)x(2,1,1)
Successfully fit ARIMA(0,1,2)x(2,1,2)
Successfully fit ARIMA(1,0,0)x(0,1,0)
Successfully fit ARIMA(1,0,0)x(0,1,1)
Successfully fit ARIMA(1,0,0)x(0,1,2)
Successfully fit ARIMA(1,0,0)x(1,1,0)
Successfully fit ARIMA(1,0,0)x(1,1,1)
Successfully fit ARIMA(1,0,0)x(1,1,2)
Successfully fit ARIMA(1,0,0)x(2,1,0)
Successfully fit ARIMA(1,0,0)x(2,1,1)
Successfully fit ARIMA(1,0,0)x(2,1,2)
Successfully fit ARIMA(1,0,1)x(0,1,0)
Successfully fit ARIMA(1,0,1)x(0,1,1)
Successfully fit ARIMA(1,0,1)x(0,1,2)
Successfully fit ARIMA(1,0,1)x(1,1,0)
Successfully fit ARIMA(1,0,1)x(1,1,1)
Successfully fit ARIMA(1,0,1)x(1,1,2)
Successfully fit ARIMA(1,0,1)x(2,1,0)
Successfully fit ARIMA(1,0,1)x(2,1,1)
Successfully fit ARIMA(1,0,1)x(2,1,2)
Successfully fit ARIMA(1,0,2)x(0,1,0)
Successfully fit ARIMA(1,0,2)x(0,1,1)
Successfully fit ARIMA(1,0,2)x(0,1,2)
Successfully fit ARIMA(1,0,2)x(1,1,0)
Successfully fit ARIMA(1,0,2)x(1,1,1)
Successfully fit ARIMA(1,0,2)x(1,1,2)
Successfully fit ARIMA(1,0,2)x(2,1,0)
Successfully fit ARIMA(1,0,2)x(2,1,1)
Successfully fit ARIMA(1,0,2)x(2,1,2)
Successfully fit ARIMA(1,1,0)x(0,1,0)
Successfully fit ARIMA(1,1,0)x(0,1,1)
Successfully fit ARIMA(1,1,0)x(0,1,2)
Successfully fit ARIMA(1,1,0)x(1,1,0)
Successfully fit ARIMA(1,1,0)x(1,1,1)
Successfully fit ARIMA(1,1,0)x(1,1,2)
Successfully fit ARIMA(1,1,0)x(2,1,0)
Successfully fit ARIMA(1,1,0)x(2,1,1)
Successfully fit ARIMA(1,1,0)x(2,1,2)
Successfully fit ARIMA(1,1,1)x(0,1,0)
Successfully fit ARIMA(1,1,1)x(0,1,1)
Successfully fit ARIMA(1,1,1)x(0,1,2)
Successfully fit ARIMA(1,1,1)x(1,1,0)
Successfully fit ARIMA(1,1,1)x(1,1,1)
Successfully fit ARIMA(1,1,1)x(1,1,2)
Successfully fit ARIMA(1,1,1)x(2,1,0)
Successfully fit ARIMA(1,1,1)x(2,1,1)
Successfully fit ARIMA(1,1,1)x(2,1,2)
Successfully fit ARIMA(1,1,2)x(0,1,0)
Successfully fit ARIMA(1,1,2)x(0,1,1)
Successfully fit ARIMA(1,1,2)x(0,1,2)
Successfully fit ARIMA(1,1,2)x(1,1,0)
Successfully fit ARIMA(1,1,2)x(1,1,1)
Successfully fit ARIMA(1,1,2)x(1,1,2)
Successfully fit ARIMA(1,1,2)x(2,1,0)
Successfully fit ARIMA(1,1,2)x(2,1,1)
Successfully fit ARIMA(1,1,2)x(2,1,2)
Successfully fit ARIMA(2,0,0)x(0,1,0)
Successfully fit ARIMA(2,0,0)x(0,1,1)
Successfully fit ARIMA(2,0,0)x(0,1,2)
Successfully fit ARIMA(2,0,0)x(1,1,0)
Successfully fit ARIMA(2,0,0)x(1,1,1)
Successfully fit ARIMA(2,0,0)x(1,1,2)
Successfully fit ARIMA(2,0,0)x(2,1,0)
Successfully fit ARIMA(2,0,0)x(2,1,1)
Successfully fit ARIMA(2,0,0)x(2,1,2)
Successfully fit ARIMA(2,0,1)x(0,1,0)
Successfully fit ARIMA(2,0,1)x(0,1,1)
Successfully fit ARIMA(2,0,1)x(0,1,2)
Successfully fit ARIMA(2,0,1)x(1,1,0)
Successfully fit ARIMA(2,0,1)x(1,1,1)
Successfully fit ARIMA(2,0,1)x(1,1,2)
Successfully fit ARIMA(2,0,1)x(2,1,0)
Successfully fit ARIMA(2,0,1)x(2,1,1)
Successfully fit ARIMA(2,0,1)x(2,1,2)
Successfully fit ARIMA(2,0,2)x(0,1,0)
Successfully fit ARIMA(2,0,2)x(0,1,1)
Successfully fit ARIMA(2,0,2)x(0,1,2)
Successfully fit ARIMA(2,0,2)x(1,1,0)
Successfully fit ARIMA(2,0,2)x(1,1,1)
Successfully fit ARIMA(2,0,2)x(1,1,2)
Successfully fit ARIMA(2,0,2)x(2,1,0)
Successfully fit ARIMA(2,0,2)x(2,1,1)
Successfully fit ARIMA(2,0,2)x(2,1,2)
Successfully fit ARIMA(2,1,0)x(0,1,0)
Successfully fit ARIMA(2,1,0)x(0,1,1)
Successfully fit ARIMA(2,1,0)x(0,1,2)
Successfully fit ARIMA(2,1,0)x(1,1,0)
Successfully fit ARIMA(2,1,0)x(1,1,1)
Successfully fit ARIMA(2,1,0)x(1,1,2)
Successfully fit ARIMA(2,1,0)x(2,1,0)
Successfully fit ARIMA(2,1,0)x(2,1,1)
Successfully fit ARIMA(2,1,0)x(2,1,2)
Successfully fit ARIMA(2,1,1)x(0,1,0)
Successfully fit ARIMA(2,1,1)x(0,1,1)
Successfully fit ARIMA(2,1,1)x(0,1,2)
Successfully fit ARIMA(2,1,1)x(1,1,0)
Successfully fit ARIMA(2,1,1)x(1,1,1)
Successfully fit ARIMA(2,1,1)x(1,1,2)
Successfully fit ARIMA(2,1,1)x(2,1,0)
Successfully fit ARIMA(2,1,1)x(2,1,1)
Successfully fit ARIMA(2,1,1)x(2,1,2)
Successfully fit ARIMA(2,1,2)x(0,1,0)
Successfully fit ARIMA(2,1,2)x(0,1,1)
Successfully fit ARIMA(2,1,2)x(0,1,2)
Successfully fit ARIMA(2,1,2)x(1,1,0)
Successfully fit ARIMA(2,1,2)x(1,1,1)
Successfully fit ARIMA(2,1,2)x(1,1,2)
Successfully fit ARIMA(2,1,2)x(2,1,0)
Successfully fit ARIMA(2,1,2)x(2,1,1)
Successfully fit ARIMA(2,1,2)x(2,1,2)
Best model by AIC:
p         1.000000
d         0.000000
q         2.000000
P         1.000000
D         1.000000
Q         2.000000
AIC    2753.200892
BIC    2789.217265
Name: 77, dtype: float64

Best model by BIC:
p         0.000000
d         1.000000
q         1.000000
P         0.000000
D         1.000000
Q         1.000000
AIC    2764.431184
BIC    2779.864406
Name: 37, dtype: float64
```

Best AIC model is $ARIMA(1, 0, 2) \times (1, 1, 2)_{12}$ and the best BIC model is $ARIMA(0, 1, 1) \times (0, 1, 1)_{12}$.

```python
m1 = ARIMA(y, order=(1,0,2), seasonal_order=(1,1,2,12)).fit()
print(m1.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                y   No. Observations:                 1280
Model:             ARIMA(1, 0, 2)x(1, 1, 2, 12)   Log Likelihood               -1369.600
Date:                          Thu, 20 Nov 2025   AIC                           2753.201
Time:                                  23:17:51   BIC                           2789.217
Sample:                                       0   HQIC                          2766.731
                                         - 1280
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.9890      0.004    236.630      0.000       0.981       0.997
ma.L1          0.1716      0.009     18.454      0.000       0.153       0.190
ma.L2         -0.0667      0.011     -6.278      0.000      -0.088      -0.046
ar.S.L12      -0.9527      0.025    -38.522      0.000      -1.001      -0.904
ma.S.L12       0.2335      0.070      3.317      0.001       0.096       0.371
ma.S.L24      -0.7602      0.053    -14.336      0.000      -0.864      -0.656
sigma2         0.4987      0.025     19.819      0.000       0.449       0.548
===================================================================================
Ljung-Box (L1) (Q):                   0.01   Jarque-Bera (JB):            393127.39
Prob(Q):                              0.91   Prob(JB):                         0.00
Heteroskedasticity (H):              13.65   Skew:                            -4.58
Prob(H) (two-sided):                  0.00   Kurtosis:                        88.77
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
m2 = ARIMA(y, order=(0,1,1), seasonal_order=(0,1,1,12)).fit()
print(m2.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                y   No. Observations:                 1280
Model:             ARIMA(0, 1, 1)x(0, 1, 1, 12)   Log Likelihood               -1379.216
Date:                          Thu, 20 Nov 2025   AIC                           2764.431
Time:                                  23:17:51   BIC                           2779.864
Sample:                                       0   HQIC                          2770.229
                                         - 1280
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1          0.1707      0.008     22.501      0.000       0.156       0.186
ma.S.L12      -0.7640      0.011    -72.132      0.000      -0.785      -0.743
sigma2         0.5122      0.004    128.529      0.000       0.504       0.520
===================================================================================
Ljung-Box (L1) (Q):                   0.15   Jarque-Bera (JB):            426630.01
Prob(Q):                              0.70   Prob(JB):                         0.00
Heteroskedasticity (H):              14.68   Skew:                            -4.59
Prob(H) (two-sided):                  0.00   Kurtosis:                        92.43
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
k = 120
n = len(y)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast_1 = m1.get_prediction(start = n, end = n+k-1).predicted_mean
fcast_2 = m2.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (m1)', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Forecast (m2)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The two predictions above are close for future points that are near but diverge for farther points.

Below we repeat the analysis with logarithms of the original data.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.


dt = np.log(y)
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
Successfully fit ARIMA(0,0,0)x(0,1,0)
Successfully fit ARIMA(0,0,0)x(0,1,1)
Successfully fit ARIMA(0,0,0)x(0,1,2)
Successfully fit ARIMA(0,0,0)x(1,1,0)
Successfully fit ARIMA(0,0,0)x(1,1,1)
Successfully fit ARIMA(0,0,0)x(1,1,2)
Successfully fit ARIMA(0,0,0)x(2,1,0)
Successfully fit ARIMA(0,0,0)x(2,1,1)
Successfully fit ARIMA(0,0,0)x(2,1,2)
Successfully fit ARIMA(0,0,1)x(0,1,0)
Successfully fit ARIMA(0,0,1)x(0,1,1)
Successfully fit ARIMA(0,0,1)x(0,1,2)
Successfully fit ARIMA(0,0,1)x(1,1,0)
Successfully fit ARIMA(0,0,1)x(1,1,1)
Successfully fit ARIMA(0,0,1)x(1,1,2)
Successfully fit ARIMA(0,0,1)x(2,1,0)
Successfully fit ARIMA(0,0,1)x(2,1,1)
Successfully fit ARIMA(0,0,1)x(2,1,2)
Successfully fit ARIMA(0,0,2)x(0,1,0)
Successfully fit ARIMA(0,0,2)x(0,1,1)
Successfully fit ARIMA(0,0,2)x(0,1,2)
Successfully fit ARIMA(0,0,2)x(1,1,0)
Successfully fit ARIMA(0,0,2)x(1,1,1)
Successfully fit ARIMA(0,0,2)x(1,1,2)
Successfully fit ARIMA(0,0,2)x(2,1,0)
Successfully fit ARIMA(0,0,2)x(2,1,1)
Successfully fit ARIMA(0,0,2)x(2,1,2)
Successfully fit ARIMA(0,1,0)x(0,1,0)
Successfully fit ARIMA(0,1,0)x(0,1,1)
Successfully fit ARIMA(0,1,0)x(0,1,2)
Successfully fit ARIMA(0,1,0)x(1,1,0)
Successfully fit ARIMA(0,1,0)x(1,1,1)
Successfully fit ARIMA(0,1,0)x(1,1,2)
Successfully fit ARIMA(0,1,0)x(2,1,0)
Successfully fit ARIMA(0,1,0)x(2,1,1)
Successfully fit ARIMA(0,1,0)x(2,1,2)
Successfully fit ARIMA(0,1,1)x(0,1,0)
Successfully fit ARIMA(0,1,1)x(0,1,1)
Successfully fit ARIMA(0,1,1)x(0,1,2)
Successfully fit ARIMA(0,1,1)x(1,1,0)
Successfully fit ARIMA(0,1,1)x(1,1,1)
Successfully fit ARIMA(0,1,1)x(1,1,2)
Successfully fit ARIMA(0,1,1)x(2,1,0)
Successfully fit ARIMA(0,1,1)x(2,1,1)
Successfully fit ARIMA(0,1,1)x(2,1,2)
Successfully fit ARIMA(0,1,2)x(0,1,0)
Successfully fit ARIMA(0,1,2)x(0,1,1)
Successfully fit ARIMA(0,1,2)x(0,1,2)
Successfully fit ARIMA(0,1,2)x(1,1,0)
Successfully fit ARIMA(0,1,2)x(1,1,1)
Successfully fit ARIMA(0,1,2)x(1,1,2)
Successfully fit ARIMA(0,1,2)x(2,1,0)
Successfully fit ARIMA(0,1,2)x(2,1,1)
Successfully fit ARIMA(0,1,2)x(2,1,2)
Successfully fit ARIMA(1,0,0)x(0,1,0)
Successfully fit ARIMA(1,0,0)x(0,1,1)
Successfully fit ARIMA(1,0,0)x(0,1,2)
Successfully fit ARIMA(1,0,0)x(1,1,0)
Successfully fit ARIMA(1,0,0)x(1,1,1)
Successfully fit ARIMA(1,0,0)x(1,1,2)
Successfully fit ARIMA(1,0,0)x(2,1,0)
Successfully fit ARIMA(1,0,0)x(2,1,1)
Successfully fit ARIMA(1,0,0)x(2,1,2)
Successfully fit ARIMA(1,0,1)x(0,1,0)
Successfully fit ARIMA(1,0,1)x(0,1,1)
Successfully fit ARIMA(1,0,1)x(0,1,2)
Successfully fit ARIMA(1,0,1)x(1,1,0)
Successfully fit ARIMA(1,0,1)x(1,1,1)
Successfully fit ARIMA(1,0,1)x(1,1,2)
Successfully fit ARIMA(1,0,1)x(2,1,0)
Successfully fit ARIMA(1,0,1)x(2,1,1)
Successfully fit ARIMA(1,0,1)x(2,1,2)
Successfully fit ARIMA(1,0,2)x(0,1,0)
Successfully fit ARIMA(1,0,2)x(0,1,1)
Successfully fit ARIMA(1,0,2)x(0,1,2)
Successfully fit ARIMA(1,0,2)x(1,1,0)
Successfully fit ARIMA(1,0,2)x(1,1,1)
Successfully fit ARIMA(1,0,2)x(1,1,2)
Successfully fit ARIMA(1,0,2)x(2,1,0)
Successfully fit ARIMA(1,0,2)x(2,1,1)
Successfully fit ARIMA(1,0,2)x(2,1,2)
Successfully fit ARIMA(1,1,0)x(0,1,0)
Successfully fit ARIMA(1,1,0)x(0,1,1)
Successfully fit ARIMA(1,1,0)x(0,1,2)
Successfully fit ARIMA(1,1,0)x(1,1,0)
Successfully fit ARIMA(1,1,0)x(1,1,1)
Successfully fit ARIMA(1,1,0)x(1,1,2)
Successfully fit ARIMA(1,1,0)x(2,1,0)
Successfully fit ARIMA(1,1,0)x(2,1,1)
Successfully fit ARIMA(1,1,0)x(2,1,2)
Successfully fit ARIMA(1,1,1)x(0,1,0)
Successfully fit ARIMA(1,1,1)x(0,1,1)
Successfully fit ARIMA(1,1,1)x(0,1,2)
Successfully fit ARIMA(1,1,1)x(1,1,0)
Successfully fit ARIMA(1,1,1)x(1,1,1)
Successfully fit ARIMA(1,1,1)x(1,1,2)
Successfully fit ARIMA(1,1,1)x(2,1,0)
Successfully fit ARIMA(1,1,1)x(2,1,1)
Successfully fit ARIMA(1,1,1)x(2,1,2)
Successfully fit ARIMA(1,1,2)x(0,1,0)
Successfully fit ARIMA(1,1,2)x(0,1,1)
Successfully fit ARIMA(1,1,2)x(0,1,2)
Successfully fit ARIMA(1,1,2)x(1,1,0)
Successfully fit ARIMA(1,1,2)x(1,1,1)
Successfully fit ARIMA(1,1,2)x(1,1,2)
Successfully fit ARIMA(1,1,2)x(2,1,0)
Successfully fit ARIMA(1,1,2)x(2,1,1)
Successfully fit ARIMA(1,1,2)x(2,1,2)
Successfully fit ARIMA(2,0,0)x(0,1,0)
Successfully fit ARIMA(2,0,0)x(0,1,1)
Successfully fit ARIMA(2,0,0)x(0,1,2)
Successfully fit ARIMA(2,0,0)x(1,1,0)
Successfully fit ARIMA(2,0,0)x(1,1,1)
Successfully fit ARIMA(2,0,0)x(1,1,2)
Successfully fit ARIMA(2,0,0)x(2,1,0)
Successfully fit ARIMA(2,0,0)x(2,1,1)
Successfully fit ARIMA(2,0,0)x(2,1,2)
Successfully fit ARIMA(2,0,1)x(0,1,0)
Successfully fit ARIMA(2,0,1)x(0,1,1)
Successfully fit ARIMA(2,0,1)x(0,1,2)
Successfully fit ARIMA(2,0,1)x(1,1,0)
Successfully fit ARIMA(2,0,1)x(1,1,1)
Successfully fit ARIMA(2,0,1)x(1,1,2)
Successfully fit ARIMA(2,0,1)x(2,1,0)
Successfully fit ARIMA(2,0,1)x(2,1,1)
Successfully fit ARIMA(2,0,1)x(2,1,2)
Successfully fit ARIMA(2,0,2)x(0,1,0)
Successfully fit ARIMA(2,0,2)x(0,1,1)
Successfully fit ARIMA(2,0,2)x(0,1,2)
Successfully fit ARIMA(2,0,2)x(1,1,0)
Successfully fit ARIMA(2,0,2)x(1,1,1)
Successfully fit ARIMA(2,0,2)x(1,1,2)
Successfully fit ARIMA(2,0,2)x(2,1,0)
Successfully fit ARIMA(2,0,2)x(2,1,1)
Successfully fit ARIMA(2,0,2)x(2,1,2)
Successfully fit ARIMA(2,1,0)x(0,1,0)
Successfully fit ARIMA(2,1,0)x(0,1,1)
Successfully fit ARIMA(2,1,0)x(0,1,2)
Successfully fit ARIMA(2,1,0)x(1,1,0)
Successfully fit ARIMA(2,1,0)x(1,1,1)
Successfully fit ARIMA(2,1,0)x(1,1,2)
Successfully fit ARIMA(2,1,0)x(2,1,0)
Successfully fit ARIMA(2,1,0)x(2,1,1)
Successfully fit ARIMA(2,1,0)x(2,1,2)
Successfully fit ARIMA(2,1,1)x(0,1,0)
Successfully fit ARIMA(2,1,1)x(0,1,1)
Successfully fit ARIMA(2,1,1)x(0,1,2)
Successfully fit ARIMA(2,1,1)x(1,1,0)
Successfully fit ARIMA(2,1,1)x(1,1,1)
Successfully fit ARIMA(2,1,1)x(1,1,2)
Successfully fit ARIMA(2,1,1)x(2,1,0)
Successfully fit ARIMA(2,1,1)x(2,1,1)
Successfully fit ARIMA(2,1,1)x(2,1,2)
Successfully fit ARIMA(2,1,2)x(0,1,0)
Successfully fit ARIMA(2,1,2)x(0,1,1)
Successfully fit ARIMA(2,1,2)x(0,1,2)
Successfully fit ARIMA(2,1,2)x(1,1,0)
Successfully fit ARIMA(2,1,2)x(1,1,1)
Successfully fit ARIMA(2,1,2)x(1,1,2)
Successfully fit ARIMA(2,1,2)x(2,1,0)
Successfully fit ARIMA(2,1,2)x(2,1,1)
Successfully fit ARIMA(2,1,2)x(2,1,2)
Best model by AIC:
p         1.000000
d         0.000000
q         2.000000
P         0.000000
D         1.000000
Q         2.000000
AIC   -6202.315594
BIC   -6171.444417
Name: 74, dtype: float64

Best model by BIC:
p         2.000000
d         0.000000
q         0.000000
P         0.000000
D         1.000000
Q         1.000000
AIC   -6201.938289
BIC   -6181.357504
Name: 109, dtype: float64
```

Best AIC model is $ARIMA(1, 0, 2) \times (0, 1, 2)_{12}$ and best BIC model is $ARIMA(2, 0, 0) \times (0, 1, 1)_{12}$.

```python
m1log = ARIMA(np.log(y), order=(1,0,2), seasonal_order=(0,1,2,12)).fit()
print(m1log.summary())
m2log = ARIMA(np.log(y), order=(2,0,0), seasonal_order=(0,1,1,12)).fit()
print(m2log.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                y   No. Observations:                 1280
Model:             ARIMA(1, 0, 2)x(0, 1, 2, 12)   Log Likelihood                3107.158
Date:                          Thu, 20 Nov 2025   AIC                          -6202.316
Time:                                  23:29:16   BIC                          -6171.444
Sample:                                       0   HQIC                         -6190.718
                                         - 1280
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.9801      0.005    191.027      0.000       0.970       0.990
ma.L1          0.4454      0.013     33.248      0.000       0.419       0.472
ma.L2          0.1740      0.015     11.847      0.000       0.145       0.203
ma.S.L12      -0.7692      0.021    -37.154      0.000      -0.810      -0.729
ma.S.L24       0.0120      0.019      0.637      0.524      -0.025       0.049
sigma2         0.0004   8.33e-06     51.284      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.05   Jarque-Bera (JB):              2730.69
Prob(Q):                              0.82   Prob(JB):                         0.00
Heteroskedasticity (H):               0.17   Skew:                             0.16
Prob(H) (two-sided):                  0.00   Kurtosis:                        10.18
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
                                     SARIMAX Results
==========================================================================================
Dep. Variable:                                  y   No. Observations:                 1280
Model:             ARIMA(2, 0, 0)x(0, 1, [1], 12)   Log Likelihood                3104.969
Date:                            Thu, 20 Nov 2025   AIC                          -6201.938
Time:                                    23:29:19   BIC                          -6181.358
Sample:                                         0   HQIC                         -6194.207
                                           - 1280
Covariance Type:                              opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          1.4101      0.012    118.083      0.000       1.387       1.434
ar.L2         -0.4237      0.012    -35.977      0.000      -0.447      -0.401
ma.S.L12      -0.7541      0.015    -51.822      0.000      -0.783      -0.726
sigma2         0.0004   8.45e-06     51.135      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.12   Jarque-Bera (JB):              2849.55
Prob(Q):                              0.73   Prob(JB):                         0.00
Heteroskedasticity (H):               0.16   Skew:                             0.12
Prob(H) (two-sided):                  0.00   Kurtosis:                        10.34
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
k = 120
n = len(y)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast_1 = m1log.get_prediction(start = n, end = n+k-1).predicted_mean
fcast_2 = m2log.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, np.log(y), label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (m1)', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Forecast (m2)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
k = 120
n = len(y)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast_1 = m1log.get_prediction(start = n, end = n+k-1).predicted_mean
fcast_2 = m2log.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, np.exp(fcast_1), label = 'Forecast (m1)', color = 'red')
plt.plot(tme_future, np.exp(fcast_2), label = 'Forecast (m2)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The discrepancy between the predictions given by the best AIC and best BIC model differ significantly when the models are fitted first to the logarithms, than when the models are fitted for the original data.

---

[← Airline passengers dataset](05-airline-passengers-dataset.md) · [Up: contents](index.md)
