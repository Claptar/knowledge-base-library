---
title: Varve Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwenty153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Varve Dataset

**Source:** [`CodeLectureTwenty153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This dataset is from the Shumway and Stoffer book. It gives the thickness of the yearly varves collected from one location in Massachusetts for 634 years (beginning 11,834 years ago!). Varves are sedimentary deposits of sand and silt that are deposited by melting glaciers during the spring melting seasons (see Example 2.6 of the Shumway-Stoffer book, 4th edition, for more details).

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.figure(figsize = (12, 6))
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We shall work with the logarithms of the raw data.

```python
#We shall work with the logarithms:
ylog = np.log(yraw)
plt.figure(figsize = (12, 6))
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Fitting a stationary model such as MA($q$) is not appropriate for the logarithmed data. This is because the data does not seem to have constant mean. To deal with this, we difference the data as follows.

```python
ylogdiff = np.diff(ylog)
plt.figure(figsize = (12, 6))
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now we apply the MA($q$) model to this dataset. To figure out the value of $q$, we look at the sample_acf values as follows.

```python
h_max = 50
fig, ax = plt.subplots(figsize=(12, 6))
plot_acf(ylogdiff, lags = h_max, ax = ax)
ax.set_title("Sample ACF of log differenced varve series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the sample ACF shows one negative nonnegligible spike at lag one.  The other spikes seem insignificant. So we fit the MA(1) model to this data.

```python
mamod = ARIMA(ylogdiff, order = (0, 0, 1)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Wed, 09 Apr 2025   AIC                            887.356
Time:                        15:59:47   BIC                            900.707
Sample:                             0   HQIC                           892.541
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0013      0.004     -0.280      0.779      -0.010       0.008
ma.L1         -0.7710      0.023    -33.056      0.000      -0.817      -0.725
sigma2         0.2353      0.012     18.881      0.000       0.211       0.260
===================================================================================
Ljung-Box (L1) (Q):                   9.16   Jarque-Bera (JB):                 7.58
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

It is interesting that the fitted $\theta$ is negative.

---

[← Sample ACF](02-sample-acf.md) · [Up: contents](index.md) · [GDP Growth Rate Data →](04-gdp-growth-rate-data.md)
