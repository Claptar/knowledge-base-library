---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
```

## ACF and PACF of ARMA processes

Today we shall first look at the theoretical ACF and PACF functions of ARMA processes. The key observation is this: (a) For MA($q$), the ACF becomes zero for $h > q$. (b) For AR($p$), the PACF becomes zero for $h > p$. (c) For ARMA(p, q) with both $p, q \geq 1$, neither the ACF nor the PACF becomes zero after a finite lag. In this case, determining $p$ and $q$ by looking at the ACF and PACF alone is difficult.

In the code below, we are using the statsmodels functions arma_acf and arma_pacf below to compute the ACF and PACF. Different ARMA  processes are obtained by changing the ma_coeffs and ar_coeffs in the code below.

```python
from statsmodels.tsa.arima_process import ArmaProcess, arma_acf, arma_pacf
```

```python
#MA(1)
#th = 0.8
#ma_coeffs = [1]
#ma_coeffs = [1, 0, 0, 0, th]
ma_coeffs = [1, th]
#ma_coeffs = [1, 0.8, 0.6]
ph = 0.8
#ph = -0.8
ar_coeffs = [1]
ar_coeffs = [1, -ph] #these are the coefficients of the AR polynomial (note the sign changes)
#ar_coeffs = [1, -0.5, 0.25]
#ar_coeffs = [1, 0, 0, 0, -ph]
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 20
corrs = arma_acf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
par_corrs = arma_pacf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.stem(range(L), corrs)
ax1.set(title = 'Theoretical ACF', xlabel = 'Lag h', ylabel = 'Autocorrelation')
ax1.axhline(0, lw = 0.5)
ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ax2.stem(range(L), par_corrs)
ax2.set(title = 'Theoretical PACF', xlabel = 'Lag h', ylabel = 'Partial Autocorrelation')
ax2.axhline(0, lw = 0.5)
ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## ARMA($p$, $q$) models for the GNP dataset

Let us consider the GNP dataset from FRED.

```python
gnp = pd.read_csv("GNP_17Nov2025.csv")
#this is quarterly data
print(gnp.head())

y = gnp['GNP'].to_numpy()
plt.plot(y, color = 'black')
plt.xlabel('Time (in quarters)')
plt.ylabel('GNP in Billions of Dollars')
plt.show()
```

```
observation_date      GNP
0       1947-01-01  244.142
1       1947-04-01  247.063
2       1947-07-01  250.716
3       1947-10-01  260.981
4       1948-01-01  267.133
```

*(1 figure omitted — see the original notebook.)*

Instead of working with raw data, we work with logarithms.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of GNP over time')
plt.xlabel('Time (in quarters)')
plt.ylabel('Log of GNP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It does not make sense to fit stationary ARMA($p$, $q$) models directly to the above dataset. So we take differences.

```python
#We difference the log-data:
ylogdiff = np.diff(ylog)
plt.plot(ylogdiff, color = 'black')
plt.title('Percent change in GNP over time')
plt.xlabel('Time (in quarters)')
plt.ylabel('Percent change in GNP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## ARMA($p$, $q$) model fitting, AIC and BIC

We now fit an ARMA($p$, $q$) model to this differenced dataset. Let us see how to fit an ARMA(1, 1) model.

```python
arma11 = ARIMA(ylogdiff, order = (1, 0, 1)).fit()
print(arma11.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(1, 0, 1)   Log Likelihood                 932.499
Date:                Tue, 18 Nov 2025   AIC                          -1856.999
Time:                        16:22:26   BIC                          -1842.014
Sample:                             0   HQIC                         -1851.010
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0154      0.001     10.429      0.000       0.013       0.018
ar.L1          0.6911      0.139      4.955      0.000       0.418       0.964
ma.L1         -0.4642      0.152     -3.054      0.002      -0.762      -0.166
sigma2         0.0002   3.97e-06     38.092      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.27   Jarque-Bera (JB):              7596.39
Prob(Q):                              0.60   Prob(JB):                         0.00
Heteroskedasticity (H):               1.55   Skew:                            -0.01
Prob(H) (two-sided):                  0.03   Kurtosis:                        27.13
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

The summary above gives maximized log-likelihood (called Log Likelihood) and also AIC and BIC. The maximized log-likelihood is the value of the log-likelihood at the MLEs. The AIC are BIC are given by:

AIC for a model = $(-2) \times$ (maximized log-likelihood) + 2 (number of parameters)

BIC for a model = $(-2) \times $(maximized log-likelihood) + ($\log n$) \times (number of parameters)
where $n$ denotes the sample size.

```python
print(arma11.llf) #maximized log-likelihood
print(arma11.aic, (-2)*arma11.llf + 2*4) #AIC (note the number of parameters here equals 4)
print(arma11.bic, (-2)*arma11.llf + np.log(len(ylogdiff))*4) #BIC
```

```
932.4992964756076
-1856.9985929512152 -1856.9985929512152
-1842.0137801890546 -1842.0137801890546
```

### Selecting the best ARMA($p$, $q$) model by automatic model selection

We will go over all ARMA($p$, $q$) models with $p \leq 5$ and $q \leq 5$ and find the best fitting ARMA($p$, $q$) model using AIC and BIC. In the code below, if parameter estimation does not work for some reason for some $p$ and $q$, then the value NaN is given for AIC and BIC for that model.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.

dt = ylogdiff
pmax = 5
qmax = 5

aicmat = np.full((pmax + 1, qmax + 1), np.nan)
bicmat = np.full((pmax + 1, qmax + 1), np.nan)

for i in range(pmax + 1):
    for j in range(qmax + 1):
        try:
            model = ARIMA(dt, order=(i, 0, j)).fit()
            aicmat[i, j] = model.aic
            bicmat[i, j] = model.bic
        except Exception as e:
            # Some models may not converge; skip them
            print(f"ARIMA({i},0,{j}) failed: {e}")
            continue

aic_df = pd.DataFrame(aicmat, index=[f'AR({i})' for i in range(pmax+1)],
                               columns=[f'MA({j})' for j in range(qmax+1)])
bic_df = pd.DataFrame(bicmat, index=[f'AR({i})' for i in range(pmax+1)],
                               columns=[f'MA({j})' for j in range(qmax+1)])

---

[Up: contents](index.md) · [Best AR model (MA = 0) →](02-best-ar-model-ma-0.md)
