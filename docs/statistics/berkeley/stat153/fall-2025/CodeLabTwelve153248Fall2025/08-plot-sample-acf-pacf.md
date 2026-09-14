---
title: Plot sample ACF/PACF
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot sample ACF/PACF

**Source:** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))
plot_acf(ylogdiff, lags=L, ax=ax1, title='Sample ACF')
plot_pacf(ylogdiff, lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The MA(1) model can be fit to this data as follows.

```python
mamod = ARIMA(ylogdiff, order=(0, 0, 1)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Sat, 22 Nov 2025   AIC                            887.356
Time:                        19:48:49   BIC                            900.707
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

We now use our functions to check if they result in similar numbers for the estimates and standard errors.

```python
def S_func(params, y): # this is the function S(\mu, \theta)
    mu, theta = params
    n = len(y)
    eps = np.zeros(n)
    eps[0] = y[0] - mu
    for t in range(1, n):
        eps[t] = y[t] - mu - theta * eps[t-1]
    S_val = np.sum(eps**2)
    return S_val
```

```python
dt = ylogdiff

---

[← Then take differences](07-then-take-differences.md) · [Up: contents](index.md) · [Initial guess: [muinit, thetainit] →](09-initial-guess-muinit-thetainit.md)
