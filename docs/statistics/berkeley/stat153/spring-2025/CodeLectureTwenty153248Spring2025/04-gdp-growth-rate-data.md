---
title: GDP Growth Rate Data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwenty153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# GDP Growth Rate Data

**Source:** [`CodeLectureTwenty153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Our second dataset is the GDP growth rate data. This can be calculated from the raw GDP data by first taking the logarithms, and then differencing the logarithms. Because, this is a common preprocessing, one can directly obtain the growth rate data from FRED (https://fred.stlouisfed.org/series/A191RP1Q027SBEA).

```python
gdp_percentchange = pd.read_csv('A191RP1Q027SBEA_08April2025.csv')
print(gdp_percentchange.head())
y = gdp_percentchange['A191RP1Q027SBEA']
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Time (quarters)')
plt.ylabel('Percent Change from Preceding Quarter')
plt.title('GDP percent change')
plt.show()
```

```
observation_date  A191RP1Q027SBEA
0       1947-04-01              4.7
1       1947-07-01              6.0
2       1947-10-01             17.3
3       1948-01-01              9.6
4       1948-04-01             10.7
```

*(1 figure omitted — see the original notebook.)*

Let us compute the sample acf of this dataset.

```python
h_max = 50
fig, ax = plt.subplots(figsize=(12, 6))
plot_acf(y, lags = h_max, ax = ax)
ax.set_title("Sample ACF of GDP percent change")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are two spikes sticking out at lags 1 and 2. This indicates that MA(2) is a reasonable model. We fit MA(2) using the following function. Note that the order is now $(0, 0, 2)$ (as opposed to $(0, 0, 1)$ for MA(1)).

```python
mamod = ARIMA(y, order = (0, 0, 2)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:        A191RP1Q027SBEA   No. Observations:                  311
Model:                 ARIMA(0, 0, 2)   Log Likelihood                -947.207
Date:                Wed, 09 Apr 2025   AIC                           1902.414
Time:                        16:01:59   BIC                           1917.373
Sample:                             0   HQIC                          1908.394
                                - 311
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          6.5008      0.484     13.422      0.000       5.552       7.450
ma.L1          0.1927      0.032      6.107      0.000       0.131       0.255
ma.L2          0.2267      0.056      4.036      0.000       0.117       0.337
sigma2        25.8695      0.798     32.417      0.000      24.305      27.434
===================================================================================
Ljung-Box (L1) (Q):                   0.19   Jarque-Bera (JB):              5455.68
Prob(Q):                              0.66   Prob(JB):                         0.00
Heteroskedasticity (H):               1.45   Skew:                             1.24
Prob(H) (two-sided):                  0.06   Kurtosis:                        23.37
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

---

[← Varve Dataset](03-varve-dataset.md) · [Up: contents](index.md)
