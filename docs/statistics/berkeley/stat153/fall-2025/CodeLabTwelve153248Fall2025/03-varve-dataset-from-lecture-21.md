---
title: Varve Dataset from Lecture 21
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Varve Dataset from Lecture 21

Let us see if the numbers from the calculations above match with those reported by ARIMA on the varve dataset (which we used in Lecture 21).

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In Lecture 21, we fit the MA(1) model to the differences of logarithms of this dataset.

```python
# First take logarithms:
ylog = np.log(yraw)
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# Then take differences:
ylogdiff = np.diff(ylog)
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the sample acf and pacf plots for this data, it is clear that MA(1) is appropriate.

```python
L = 60
# Plot sample ACF/PACF
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

# Initial guess: [mu_init, theta_init]
mu_init = np.mean(dt)
theta_init = 0
init_params = [mu_init, theta_init]

# Perform the optimization
result = minimize(S_func, init_params, args=(dt,))
print(result)
mu_hat, theta_hat = result.x

print("Estimated mu:", mu_hat)
print("Estimated theta:", theta_hat)
```

```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 149.0042362521212
        x: [-1.137e-03 -7.728e-01]
      nit: 12
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 4.132e-05  4.927e-06]
            [ 4.927e-06  2.550e-03]]
     nfev: 63
     njev: 21
Estimated mu: -0.0011366484142282629
Estimated theta: -0.7728310145141554
```

```python
print(result.x)
print(mamod.params)
```

```
[-0.00113665 -0.77283101]
[-0.00125667 -0.77099236  0.23528045]
```

```python
sigma_hat = np.sqrt(S_func(result.x, dt) / len(dt))
print("Estimated sigma:", sigma_hat)
print("MA reported sigma:", np.sqrt(mamod.params[2]))
```

```
Estimated sigma: 0.485173925675123
MA reported sigma: 0.4850571581949342
```

The estimates are very close to each other. Below are the standard errors.

```python
alphaest = result.x
n = len(dt)
H = nd.Hessian(lambda alpha: S_func(alpha, dt), step = 1e-6)(alphaest)

sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))

# ---- Output ----
print("Estimated mu:", alphaest[0])
print("Estimated theta:", alphaest[1])
print("Estimated sigma:", sighat)
print("Covariance matrix:\n", covmat)
print("Standard errors:", stderrs)

# The standard errors of mu and theta reported by ARIMA function are:
print("MA standard errors:", md.bse[0:2])
```

```
Estimated mu: -0.0011366484142282629
Estimated theta: -0.7728310145141554
Estimated sigma: 0.48594221424137307
Covariance matrix:
 [[1.94152441e-05 8.29322690e-07]
 [8.29322690e-07 1.17034011e-03]]
Standard errors: [0.00440627 0.03421023]
MA standard errors: [0.01689423 0.03682785]
```

The standard error corresponding to $\mu$ that we computed is a little off from the one reported by the ARIMA function, but the standard errors corresponding to $\theta$ are almost the same.

Note that we did not calculate standard errors for $\sigma$. This can be done by calculating the posterior of $\sigma$ (this can be written in terms of the chi-squared distribution).

The ARIMA function works with the full likelihood unlike the analysis above which works with the conditional likelihood (conditioning on $\epsilon_0 = 0$). So the answers will be slightly different. The full likelihood is more complicated to write down.

---

[← Standard Errors corresponding to the parameter estimates](02-standard-errors-corresponding-to-the-parameter-estimates.md) · [Up: contents](index.md)
