---
title: Ljung-Box p-values
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Ljung-Box p-values

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

These diagnostics allow us to look at properties of our residuals, but there is one more statistic that is helpful to look at when choosing - the Ljung-Box-Pierce Q statistic.

Looking at the residual ACF plot lag-by-lag (above called "correlogram") can miss a problem where every individual $\hat{\rho}_e(h)$ is just barely under the significance threshold but collectively they're too large. The Q statistic tests them jointly:

$$Q=n(n+2) \sum_{h=1}^{H} \frac{\hat{\rho}_e^2(h)}{n-h}$$

where $n$ is the number of residuals (time points estimated), $h$ is the lag index, and $H$ is the upper cutoff for lags we'll pool over.

```python
acorr_ljungbox(fit.resid, lags=20, model_df=p+q)
```

```
lb_stat  lb_pvalue
1    7.495381        NaN
2    7.574612   0.005920
3   10.540130   0.005143
4   12.713483   0.005299
5   13.069365   0.010942
6   13.299219   0.020730
7   14.303890   0.026420
8   14.305191   0.046012
9   14.370858   0.072597
10  17.126214   0.046776
11  17.474491   0.064502
12  23.259072   0.016245
13  26.387158   0.009458
14  26.928462   0.012725
15  27.067788   0.018867
16  27.075839   0.028124
17  27.210777   0.039199
18  27.935704   0.045695
19  32.351218   0.019972
20  32.846184   0.025041
```

```python
p=1
d=1
q=1
fit = ARIMA(y_train, order=(p, d, q), trend=trend).fit()

fig = plt.figure(figsize=(10,6))
fit.plot_diagnostics(fig=fig);
plt.tight_layout()

acorr_ljungbox(fit.resid, lags=20, model_df=p+q)
```

```
lb_stat  lb_pvalue
1    0.043490        NaN
2    1.348624        NaN
3    1.356608   0.244126
4    1.356782   0.507433
5    1.536546   0.673862
6    3.270533   0.513615
7    3.822495   0.575245
8    4.048409   0.670125
9    4.072609   0.771377
10   6.180928   0.626973
11   6.185163   0.721253
12  10.481868   0.399281
13  13.098675   0.286925
14  13.782588   0.314807
15  14.405222   0.345938
16  14.501819   0.413033
17  14.804895   0.465560
18  15.254424   0.506089
19  18.802026   0.340013
20  19.513412   0.360869
```

*(1 figure omitted — see the original notebook.)*

```python
fit.summary()
```

```
<class 'statsmodels.iolib.summary.Summary'>
"""
                               SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  296
Model:                 ARIMA(3, 2, 1)   Log Likelihood                 901.109
Date:                Tue, 07 Apr 2026   AIC                          -1792.218
Time:                        09:48:18   BIC                          -1773.800
Sample:                             0   HQIC                         -1784.842
                                - 296
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.1414      0.053      2.688      0.007       0.038       0.244
ar.L2          0.1514      0.073      2.080      0.038       0.009       0.294
ar.L3         -0.0988      0.082     -1.210      0.226      -0.259       0.061
ma.L1         -0.9895      0.021    -47.609      0.000      -1.030      -0.949
sigma2         0.0001   4.27e-06     29.140      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.17   Jarque-Bera (JB):              5608.00
Prob(Q):                              0.68   Prob(JB):                         0.00
Heteroskedasticity (H):               1.54   Skew:                             0.01
Prob(H) (two-sided):                  0.03   Kurtosis:                        24.40
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
"""
```

---

[← Forecast](27-forecast.md) · [Up: contents](index.md)
