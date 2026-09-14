---
title: this is quarterly data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this is quarterly data

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

Instead of the raw GNP, we work with their logarithms.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of GNP over time')
plt.xlabel('Time (in quarters)')
plt.ylabel('Log of GNP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We fit AR models to differences of the logs (after multiplying by 100). The data now becomes percent change in GNP.

```python
ylogdiff = 100 * np.diff(ylog)
plt.plot(ylogdiff, color = 'black')
plt.title('Percent change in GNP over time')
plt.xlabel('Time (in quarters)')
plt.ylabel('Percent change in GNP')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us now fit the AR(1) model to this dataset. Let us first fit it using AutoReg.

```python
md_autoreg = AutoReg(ylogdiff, lags = 1).fit()
print(md_autoreg.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                     AutoReg(1)   Log Likelihood                -512.052
Method:               Conditional MLE   S.D. of innovations              1.249
Date:                Sat, 15 Nov 2025   AIC                           1030.104
Time:                        16:52:44   BIC                           1041.333
Sample:                             1   HQIC                          1034.591
                                  313
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.1596      0.110     10.519      0.000       0.943       1.376
y.L1           0.2487      0.055      4.536      0.000       0.141       0.356
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            4.0208           +0.0000j            4.0208            0.0000
-----------------------------------------------------------------------------
```

AutoReg uses the method of conditional MLE, which maximizes the conditional likelihood of $y_2, \dots, y_n$ given $y_1$. This conditional likelihood is given by:
\begin{equation*}
\left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n (y_t -
    \phi_0 - \phi_1 y_{t-1})^2 \right).
\end{equation*}

```python
#the estimates of $\phi_0$ and $\phi_1$ are given by:
print(md_autoreg.params)
#if you want the estimate of sigma^2, do the following:
print(md_autoreg.sigma2)
```

```
[1.15955739 0.24870755]
1.5597196592023646
```

Next we use the ARIMA function to fit AR(1). ARIMA models have a triplet of indices $(p, d, q)$. $p$ stands for the AR order, $d$ stands for the amount of differencing, and $q$ stands for the MA order. To fit AR(1) through the ARIMA function, we need to use $p = 1$, $d = 0$ and $q = 0$.

```python
md_arima = ARIMA(ylogdiff, order = (1,0,0)).fit()
print(md_arima.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  313
Model:                 ARIMA(1, 0, 0)   Log Likelihood                -513.262
Date:                Sat, 15 Nov 2025   AIC                           1032.523
Time:                        16:52:44   BIC                           1043.762
Sample:                             0   HQIC                          1037.014
                                - 313
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.5415      0.114     13.581      0.000       1.319       1.764
ar.L1          0.2480      0.020     12.489      0.000       0.209       0.287
sigma2         1.5551      0.041     37.640      0.000       1.474       1.636
===================================================================================
Ljung-Box (L1) (Q):                   0.81   Jarque-Bera (JB):              6696.97
Prob(Q):                              0.37   Prob(JB):                         0.00
Heteroskedasticity (H):               1.65   Skew:                            -0.05
Prob(H) (two-sided):                  0.01   Kurtosis:                        25.66
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

ARIMA parametrizes the AR(1) model differently from AutoReg. It writes the AR(1) model as:
\begin{align*}
    y_t - \mu = \phi_1 (y_{t-1} - \mu) + \epsilon_t.
\end{align*}
In other words, there is no $\phi_0$ parameter. It is replaced by $\mu - \mu \phi_1$. This means that $\phi_0 = \mu - \mu \phi_1$ or $\mu = \phi_0/(1 - \phi_1)$. So to compare the parameter estimates given by AutoReg and ARIMA, we need to convert the estimates $\phi_0, \phi_1$  from AutoReg to $\mu, \phi_1$.

```python
pars_autoreg = [md_autoreg.params[0]/(1 - md_autoreg.params[1]), md_autoreg.params[1], md_autoreg.sigma2]
pars_arima = md_arima.params
print(np.column_stack([pars_autoreg, pars_arima]))
```

```
[[1.5434168  1.5415492 ]
 [0.24870755 0.24797155]
 [1.55971966 1.55508381]]
```

The parameter estimates are similar but not exactly the same. This is because ARIMA is using a different method of parameter estimation compared to AutoReg. ARIMA works with the full likelihood of $y_1, \dots, y_n$ (not the conditional likelihood of $y_2, \dots, y_n$ given $y_1$). We saw in lecture 17 that the full likelihood for AR(1) is given by:
\begin{equation*}
\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2 \pi}
      \sigma} \exp \left(-\frac{1 - \phi_1^2}{2 \sigma^2} \left(y_1 -
        \frac{\phi_0}{1 - \phi_1} \right)^2 \right) \left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n (y_t -
    \phi_0 - \phi_1 y_{t-1})^2 \right).
\end{equation*}
Instead of parametrizing using $\phi_0, \phi_1$ and $\sigma$, an alternative parametrization is via $\phi_1, \sigma$ and $\mu := \phi_0/(1 - \phi_1)$. With this the likelihood becomes:
\begin{equation*}
\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2 \pi}
      \sigma} \exp \left(-\frac{1 - \phi_1^2}{2 \sigma^2} \left(y_1 - \mu \right)^2 \right) \left(\frac{1}{\sqrt{2 \pi} \sigma}
    \right)^{n-1} \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=2}^n ((y_t - \mu)
     - \phi_1 (y_{t-1} - \mu))^2 \right).
\end{equation*}


The following function computes the log-likelihood given values of the parameters.

```python
def loglik_ar1(dt, pars):
    n = len(dt)
    mu = pars[0]
    phi1 = pars[1]
    sigma2 = pars[2]
    sigma = np.sqrt(sigma2)
    # First term: density of y1 under stationary AR(1)
    ll_start = 0.5 * np.log(1 - phi1**2) - 0.5*np.log(2*np.pi) - np.log(sigma) \
               - (1 - phi1**2) * (dt[0] - mu)**2 / (2*sigma2)
    # Second term: density of y2,...,yn
    residuals = (dt[1:] - mu) - phi1*(dt[:-1] - mu)
    ssr = np.sum(residuals**2)
    ll_rest = -(n-1)*0.5*np.log(2*np.pi) - (n-1)*np.log(sigma) - ssr/(2*sigma2)
    return ll_start + ll_rest
```

We can attempt to maximize this full log-likelihood using an inbuilt optimization function, starting with the parameter estimates given by AutoReg. The code for doing this is given below. This gives almost the same results as the parameter estimates given by ARIMA.

```python
from scipy.optimize import minimize
def neg_loglik_ar1(pars, dt):
    return -loglik_ar1(dt, pars)
init_pars = pars_autoreg
bounds = [(-np.inf, np.inf), (-0.99, 0.99), (1e-6, np.inf)]

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [note that the bound on phi1 ensures stationarity →](03-note-that-the-bound-on-phi1-ensures-stationarity.md)
