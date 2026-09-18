---
title: Airline passengers dataset
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Airline passengers dataset

The airline passengers dataset is a popular dataset for evaluating prediction accuracy of various models. It contains monthly data on the number of international airline passengers (in thousands) from January 1949 to December 1960.

```python
data = sm.datasets.get_rdataset("AirPassengers").data
print(data.head())
y = data['value'].to_numpy()
plt.plot(y)
plt.xlabel('Time (months)')
plt.ylabel('Number of Passengers')
plt.title('Monthly Airline Passenger Numbers 1949-1960')
plt.show()
```

```
time  value
0  1949.000000    112
1  1949.083333    118
2  1949.166667    132
3  1949.250000    129
4  1949.333333    121
```

*(1 figure omitted — see the original notebook.)*

As usual, we fit models to logarithms.

```python
ylog = np.log(y)
plt.plot(ylog)
plt.xlabel('Time (months)')
plt.ylabel('Log(Number of Passengers)')
plt.title('Log of Monthly Airline Passenger Numbers 1949-1960')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We first take seasonal differences: $\log y_t - \log y_{t-12}$.

```python
#Seasonal differencing: y_t - y_{t-12}
ylogdiff12 = ylog[12:] - ylog[:-12]
plt.plot(ylogdiff12)
plt.xlabel('Year')
plt.ylabel('value')
plt.title('Seasonal Differences of Log Airline Passengers')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are still some increasing/decreasing trends. Let us now take regular differences.

```python
#We now take one more differencing; this time regular differencing
ylog2d = np.diff(ylogdiff12)
plt.plot(ylog2d)
plt.xlabel('Time (months)')
plt.ylabel('value')
plt.title('Differences of Seasonally differenced Log Airline Passengers')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can now look at the ACF and PACF to assess if a multiplicative seasonal ARMA model is appropriate.

```python
L = 60
# Plot sample ACF/PACF
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
p        1.000000
d        0.000000
q        1.000000
P        1.000000
D        1.000000
Q        2.000000
AIC   -485.055743
BIC   -467.758931
Name: 68, dtype: float64

Best model by BIC:
p        0.000000
d        1.000000
q        1.000000
P        0.000000
D        1.000000
Q        1.000000
AIC   -483.392972
BIC   -474.767380
Name: 37, dtype: float64
```

The best model in terms of AIC corresponds to $(1, 0, 1) \times (1, 1, 2)_{12}$, and the best model is terms of BIC is $(0, 1, 1) \times (0, 1, 1)_{12}$ (this is the $MA(1) \times MA(1)_{12}$ model for $\nabla \nabla^{12} y_t$). This latter model is just $m1$.

```python
m3 = ARIMA(ylog, order=(1,0,1), seasonal_order=(1,1,2,12)).fit()
print(m3.summary())
```

```
SARIMAX Results
=============================================================================================
Dep. Variable:                                     y   No. Observations:                  144
Model:             ARIMA(1, 0, 1)x(1, 1, [1, 2], 12)   Log Likelihood                 248.528
Date:                               Thu, 20 Nov 2025   AIC                           -485.056
Time:                                       23:02:42   BIC                           -467.759
Sample:                                            0   HQIC                          -478.027
                                               - 144
Covariance Type:                                 opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.9925      0.008    121.715      0.000       0.977       1.009
ma.L1         -0.4321      0.082     -5.301      0.000      -0.592      -0.272
ar.S.L12       0.9726      0.084     11.550      0.000       0.808       1.138
ma.S.L12      -1.9115      1.549     -1.234      0.217      -4.948       1.125
ma.S.L24       0.9680      1.545      0.626      0.531      -2.061       3.997
sigma2         0.0010      0.001      0.666      0.506      -0.002       0.004
===================================================================================
Ljung-Box (L1) (Q):                   0.03   Jarque-Bera (JB):                 3.65
Prob(Q):                              0.86   Prob(JB):                         0.16
Heteroskedasticity (H):               0.63   Skew:                            -0.04
Prob(H) (two-sided):                  0.13   Kurtosis:                         3.81
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast_3 = m3.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Forecast (m1)', color = 'black')
plt.plot(tme_future, fcast_2, label = 'Forecast (m2)', color = 'red')
plt.plot(tme_future, fcast_3, label = 'Forecast (m3)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here are the predictions on the original data (without logarithms).

```python
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, np.exp(fcast_1), label = 'Forecast (m1)', color = 'black')
plt.plot(tme_future, np.exp(fcast_2), label = 'Forecast (m2)', color = 'red')
plt.plot(tme_future, np.exp(fcast_3), label = 'Forecast (m3)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions are largely similar especially for future time points that are in the near future.

## Retail Alcohol Sales Data

Let us now consider the following data from FRED.

```python
#The following is FRED data on retail sales (in millions of dollars) for beer, wine and liquor stores (https://fred.stlouisfed.org/series/MRTSSM4453USN)
beersales = pd.read_csv('MRTSSM4453USN_19Nov2025.csv')
print(beersales.head())
y = beersales['MRTSSM4453USN']
plt.plot(y)
plt.xlabel('Month')
plt.ylabel('Millions of Dollars')
plt.title('Retail Sales: Beer, wine and liquor stores')
plt.show()
```

```
observation_date  MRTSSM4453USN
0       1992-01-01           1414
1       1992-02-01           1444
2       1992-03-01           1496
3       1992-04-01           1569
4       1992-05-01           1707
```

*(1 figure omitted — see the original notebook.)*

```python
ylog = np.log(y)
plt.plot(ylog)
plt.xlabel('Month')
plt.ylabel('Logarithms')
plt.title('Retail Sales: Beer, wine and liquor stores')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In order to fit a stationary model, let us first preprocess by differencing. The seasonal differences are calculated and plotted below.

```python
#Seasonal differencing: y_t - y_{t-12}
ylogdiff12 = ylog.diff(periods = 12)
plt.plot(ylogdiff12)
plt.xlabel('Time (months)')
plt.ylabel('value')
plt.title('Seasonal Differences of Log(Alcohol Sales)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Certain increasing/decreasing trends are visible in the above data. We do one more differencing below.

```python
#We now take one more differencing; this time regular differencing
ylog2d = ylogdiff12.diff()
plt.plot(ylog2d)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us compute the ACF and PACF.

```python
L = 60
# Plot sample ACF/PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))
plot_acf(ylog2d.dropna(), lags=L, ax=ax1, title='Sample ACF')
plot_pacf(ylog2d.dropna(), lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It appears  hard to determine the orders for an appropriate SARIMA model directly from the above ACF and PACF plot. Below we use a brute force approach where we enumerate a whole bunch of $ARIMA(p, d, q) \times (P, D, Q)_{12}$ models, and then pick the best model via the AIC and BIC criteria.

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
p         2.000000
d         1.000000
q         0.000000
P         2.000000
D         1.000000
Q         2.000000
AIC   -1757.455493
BIC   -1729.692466
Name: 143, dtype: float64

Best model by BIC:
p         2.000000
d         1.000000
q         0.000000
P         0.000000
D         1.000000
Q         2.000000
AIC   -1751.223411
BIC   -1731.392678
Name: 137, dtype: float64
```

Of the considered models, the best AIC model is $ARIMA(2, 1, 0) \times (2, 1, 2)_{12}$ and the best BIC model is $ARIMA(2, 1, 0) \times (0, 1, 2)_{12}$. We fit these models below. If we do not suppress warnings, we will see a bunch of warnings. Fitting these models is not easy and the process involves nonlinear optimization for calculating the MLEs.

```python
m1 = ARIMA(ylog, order = (2, 1, 0), seasonal_order = (2, 1, 2, 12)).fit()
print(m1.summary())
```

```
SARIMAX Results
=============================================================================================
Dep. Variable:                         MRTSSM4453USN   No. Observations:                  403
Model:             ARIMA(2, 1, 0)x(2, 1, [1, 2], 12)   Log Likelihood                 885.728
Date:                               Thu, 20 Nov 2025   AIC                          -1757.455
Time:                                       23:10:47   BIC                          -1729.692
Sample:                                            0   HQIC                         -1746.450
                                               - 403
Covariance Type:                                 opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.6115      0.053    -11.624      0.000      -0.715      -0.508
ar.L2         -0.2716      0.045     -5.997      0.000      -0.360      -0.183
ar.S.L12       0.6794      0.175      3.873      0.000       0.336       1.023
ar.S.L24      -0.4539      0.072     -6.291      0.000      -0.595      -0.312
ma.S.L12      -1.1981      0.197     -6.088      0.000      -1.584      -0.812
ma.S.L24       0.4384      0.172      2.556      0.011       0.102       0.775
sigma2         0.0006   4.05e-05     15.266      0.000       0.001       0.001
===================================================================================
Ljung-Box (L1) (Q):                   0.95   Jarque-Bera (JB):                22.67
Prob(Q):                              0.33   Prob(JB):                         0.00
Heteroskedasticity (H):               0.98   Skew:                             0.13
Prob(H) (two-sided):                  0.89   Kurtosis:                         4.15
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

```python
m2 = ARIMA(ylog, order = (2, 1, 0), seasonal_order = (0, 1, 2, 12)).fit()
print(m2.summary())
```

```
SARIMAX Results
=============================================================================================
Dep. Variable:                         MRTSSM4453USN   No. Observations:                  403
Model:             ARIMA(2, 1, 0)x(0, 1, [1, 2], 12)   Log Likelihood                 880.612
Date:                               Thu, 20 Nov 2025   AIC                          -1751.223
Time:                                       23:10:50   BIC                          -1731.393
Sample:                                            0   HQIC                         -1743.362
                                               - 403
Covariance Type:                                 opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.7730      0.049    -15.816      0.000      -0.869      -0.677
ar.L2         -0.4199      0.046     -9.146      0.000      -0.510      -0.330
ma.S.L12      -0.6055      0.058    -10.407      0.000      -0.720      -0.491
ma.S.L24      -0.2214      0.062     -3.586      0.000      -0.342      -0.100
sigma2         0.0006   4.13e-05     14.988      0.000       0.001       0.001
===================================================================================
Ljung-Box (L1) (Q):                   0.32   Jarque-Bera (JB):                25.58
Prob(Q):                              0.57   Prob(JB):                         0.00
Heteroskedasticity (H):               1.01   Skew:                             0.27
Prob(H) (two-sided):                  0.96   Kurtosis:                         4.13
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Below we obtain predictions using both the models.

```python
k = 120
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
fcast1 = m1.get_prediction(start = n, end = n+k-1).predicted_mean
fcast2 = m2.get_prediction(start = n, end = n+k-1).predicted_mean
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast1, label = 'Forecast (M1)', color = 'red')
plt.plot(tme_future, fcast2, label = 'Forecast (M2)', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions by both models seem reasonable, and they are also very close to each other. Below we convert these predictions to the original data (not logarithms).

```python
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, np.exp(fcast1), label = 'Forecast (M1)', color = 'red')
plt.plot(tme_future, np.exp(fcast2), label = 'Forecast (M2)', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Back to co2 dataset](04-back-to-co2-dataset.md) · [Up: contents](index.md) · [FRED Industrial Production Dataset →](06-fred-industrial-production-dataset.md)
