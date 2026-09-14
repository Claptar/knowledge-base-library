---
title: AR(1) with $|\phi1| > 1$
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyOne153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# AR(1) with $|\phi1| > 1$

**Source:** [`CodeLectureTwentyOne153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Consider the model:
\begin{equation*}
   y_t = \mu - \sum_{j=1}^{\infty} \frac{\epsilon_{t+j}}{\phi_1^j}
\end{equation*}
for some $\phi_1$ with absolute value strictly larger than 1. This is the non-causal AR model.

Let us attempt to simulate data from this model. It is most natural to simulate this for decreasing $t = n, n-1, \dots, 1$ (there might be numerical issues with trying to simulate this in the usual way for $t = 1, 2, \dots$ with increasing $t$).

```python
phi1 = 2
sig = 3
mu = 10
n = 2000
nf = 50 #number of future epsilons that we generate

rng = np.random.default_rng(seed = 43)
eps = rng.normal(loc = 0, scale = sig, size = n + nf)
yn = mu
for i in range(1, nf):
    yn = yn - eps[n+i-1]/(phi1 ** i)
print(yn)
y = np.full(n, -999, dtype = float)
y[-1] = yn
for t in range(n-1, 0, -1):
    y[t-1] = (y[t]/phi1) - (mu*(1-phi1)/phi1) - eps[t]/phi1
print(y)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

```
10.263896524224691
[10.0395212  12.11357735 12.47056656 ...  7.74365861  9.23878741
 10.26389652]
```

*(1 figure omitted — see the original notebook.)*

```python
ar = ARIMA(y, order = (1, 0, 0)).fit()
print(ar.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                 2000
Model:                 ARIMA(1, 0, 0)   Log Likelihood               -3638.593
Date:                Fri, 11 Apr 2025   AIC                           7283.187
Time:                        13:07:18   BIC                           7299.990
Sample:                             0   HQIC                          7289.356
                               - 2000
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         10.0199      0.062    162.683      0.000       9.899      10.141
ar.L1          0.4581      0.020     23.121      0.000       0.419       0.497
sigma2         2.2268      0.070     31.870      0.000       2.090       2.364
===================================================================================
Ljung-Box (L1) (Q):                   0.10   Jarque-Bera (JB):                 0.23
Prob(Q):                              0.75   Prob(JB):                         0.89
Heteroskedasticity (H):               0.99   Skew:                             0.02
Prob(H) (two-sided):                  0.92   Kurtosis:                         3.03
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Note that the estimate of $\phi_1$ in the above regression is $0.4581$ which is quite far from the actual $\phi_1 = 2$ used to generate the data. Also note that the estimate of $\sigma^2$ is 2.2268 while the actual $\sigma^2 = 9$.

---

[← Sample PACF](01-sample-pacf.md) · [Up: contents](index.md)
