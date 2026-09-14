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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(dt, lags=L, ax=ax1, title='Sample ACF')
plot_pacf(dt, lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

In all the examples, it is much harder (due to noise) to guess the models from the sample ACF and PACFs (from data generated according to the model) compared to the  theoretical ACF and PACF of the model.

## Back to co2 dataset

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

```python
ydiff12 = y.diff(periods = 12)
y2d = ydiff12.diff()
```

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(y2d.dropna(), lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
axes[0].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plot_pacf(y2d.dropna(), lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
axes[1].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the sample ACF and PACF, it can be argued that $MA(1) \times MA(1)_{12}$ is a suitable model for the twice differenced data $\nabla_s \nabla y_t$. To see this, let us first focus only on the seasonal lags 12, 24, 36 etc., for the ACF function at these lags, there is only one spike (at lag 12) which suggests $MA(1)_{12}$. Next let us look at the regular (i.e., non-seasonal) initial lags 1,2,3,4 etc. Here also in the ACF, there is a single spike suggesting regular $MA(1)$. The overall model is therefore $MA(1) \times MA(1)_{12}$.

We can fit this using the ARIMA function as shown below.

```python
m1_co2 = ARIMA(y, order = (0, 1, 1), seasonal_order = (0, 1, 1, 12)).fit()
print(m1_co2.summary())
```

```
SARIMAX Results
========================================================================================
Dep. Variable:                                x   No. Observations:                  132
Model:             ARIMA(0, 1, 1)x(0, 1, 1, 12)   Log Likelihood                -139.547
Date:                          Thu, 20 Nov 2025   AIC                            285.095
Time:                                  23:00:16   BIC                            293.432
Sample:                                       0   HQIC                           288.481
                                          - 132
Covariance Type:                            opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.5791      0.093     -6.254      0.000      -0.761      -0.398
ma.S.L12      -0.8205      0.117     -7.017      0.000      -1.050      -0.591
sigma2         0.5448      0.073      7.484      0.000       0.402       0.687
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

## Airline passengers dataset

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

---

[← Plot simulated series](15-plot-simulated-series.md) · [Up: contents](index.md) · [Plot sample ACF/PACF →](17-plot-sample-acf-pacf.md)
