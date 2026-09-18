---
title: Fitting MA models using the ARIMA function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fitting MA models using the ARIMA function

Fitting MA models to data is more complicated compared to AR models. We use an inbuilt function in statsmodels called ARIMA for this. ARIMA models (which we will define later) are determined by three orders $(p, d, q)$. $p$ denotes the AR order, $q$ denotes the MA order, and $d$ denotes differencing. To fit the MA(1) model, we take $p = 0, d = 0$ and $q = 1$.

```python
from statsmodels.tsa.arima.model import ARIMA
mamod = ARIMA(ylogdiff, order = (0, 0, 1)).fit()
print(mamod.summary())
print(mamod.params)
mu_hat = mamod.params[0]
theta_hat = mamod.params[1]
sigma_hat = np.sqrt(mamod.params[2])
print(f"mu_hat = {mu_hat: .4f}, theta_hat = {theta_hat: .4f}, sigma_hat = {sigma_hat: .4f}")
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Sat, 15 Nov 2025   AIC                            887.356
Time:                        22:14:29   BIC                            900.707
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
[-0.00125667 -0.77099236  0.23528045]
mu_hat = -0.0013, theta_hat = -0.7710, sigma_hat =  0.4851
```

This ARIMA function can be applied on the log varve data also, instead of first differencing and then applying it on the differenced log data. If we are not using differencing data, we have to use d = 1 in the ARIMA function (i.e., $(p, d, q)
$  = $(0, 1, 1)$).

```python
mamod_ylog = ARIMA(ylog, order = (0, 1, 1)).fit()
print(mamod_ylog.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      x   No. Observations:                  634
Model:                 ARIMA(0, 1, 1)   Log Likelihood                -440.718
Date:                Sat, 15 Nov 2025   AIC                            885.435
Time:                        22:14:30   BIC                            894.336
Sample:                             0   HQIC                           888.892
                                - 634
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.7705      0.023    -32.948      0.000      -0.816      -0.725
sigma2         0.2353      0.012     19.124      0.000       0.211       0.259
===================================================================================
Ljung-Box (L1) (Q):                   9.10   Jarque-Bera (JB):                 7.59
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Note now that there is no constant. This ARIMA function, by default, fits $y_t = \epsilon_t + \theta \epsilon_{t-1}$ (with no $\mu$ i.e., with $\mu = 0$) if the differencing order is strictly positive.

---

[← Varve Dataset](03-varve-dataset.md) · [Up: contents](index.md) · [MA(2) model →](05-ma-2-model.md)
