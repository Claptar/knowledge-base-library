---
title: GDP Growth Rate Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# GDP Growth Rate Data

Our second dataset is the GDP growth rate data. This can be calculated from the raw GDP data by first taking the logarithms, and then differencing the logarithms. Because, this is a common preprocessing, one can directly obtain the growth rate data from FRED (https://fred.stlouisfed.org/series/A191RP1Q027SBEA).

```python
gdp = pd.read_csv("GDP_12Nov2025.csv")
print(gdp.head())
y = gdp['GDP'].to_numpy()
plt.plot(y, color = 'black')
plt.xlabel('Quarter')
plt.show()
```

```
observation_date      GDP
0       1947-01-01  243.164
1       1947-04-01  245.968
2       1947-07-01  249.585
3       1947-10-01  259.745
4       1948-01-01  265.742
```

*(1 figure omitted — see the original notebook.)*

We cannot fit MA models directly to this dataset. So we do the usual preprocessing by first taking logarithms and then differences.

```python
ylog = np.log(y)
ylogdiff = np.diff(ylog)*100
plt.plot(ylogdiff, color = 'black')
plt.xlabel('Quarter')
plt.title('Differenced Logarithm of GDP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us compute the sample acf of this dataset.

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(ylogdiff, lags = h_max, ax = ax)
ax.set_title("Sample ACF of GDP percent change")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are two spikes sticking out at lags 1 and 2. This indicates that MA(2) is a reasonable model. We fit MA(2) by using the ARIMA function as follows.

```python
mamod = ARIMA(ylogdiff, order = (0, 0, 2)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(0, 0, 2)   Log Likelihood                -503.717
Date:                Sat, 15 Nov 2025   AIC                           1015.435
Time:                        22:14:36   BIC                           1030.419
Sample:                             0   HQIC                          1021.423
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.5418      0.118     13.081      0.000       1.311       1.773
ma.L1          0.1893      0.026      7.250      0.000       0.138       0.240
ma.L2          0.2232      0.060      3.749      0.000       0.107       0.340
sigma2         1.4628      0.039     37.788      0.000       1.387       1.539
===================================================================================
Ljung-Box (L1) (Q):                   0.18   Jarque-Bera (JB):              6483.73
Prob(Q):                              0.67   Prob(JB):                         0.00
Heteroskedasticity (H):               1.59   Skew:                            -0.03
Prob(H) (two-sided):                  0.02   Kurtosis:                        25.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Fitting MA models is more complicated compared to fitting AR models. This can lead to some numerical issues. For example, in the above code if you fit the MA(2) model to ylogdiff = np.diff(np.log(y)), you might get a warning saying the optimization for computing the MLE is not converging. The warning seems to go away if you work with np.diff(np.log(y))*100 (now you are multiplying by 100).

---

[← MA(2) model](05-ma-2-model.md) · [Up: contents](index.md) · [AR Models →](07-ar-models.md)
