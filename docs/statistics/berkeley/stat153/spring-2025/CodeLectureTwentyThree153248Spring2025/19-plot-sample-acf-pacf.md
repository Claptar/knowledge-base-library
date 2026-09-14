---
title: Plot sample ACF/PACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot sample ACF/PACF

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

### Retail Alcohol Sales Data

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

---

[← Plot simulated series](18-plot-simulated-series.md) · [Up: contents](index.md) · [Plot sample ACF/PACF →](20-plot-sample-acf-pacf.md)
