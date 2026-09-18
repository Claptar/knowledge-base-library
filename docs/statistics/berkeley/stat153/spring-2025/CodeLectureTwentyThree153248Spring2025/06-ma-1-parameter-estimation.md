---
title: MA(1) Parameter Estimation
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# MA(1) Parameter Estimation

Estimating the parameters of ARMA (as well as ARIMA, SARIMA models) is much harder
than parameter estimation in AR models which was handled by standard regression (ordinary
least squares). We will not study this topic (and simply rely on the ARIMA function for fitting
these models to data). But we will perform estimation for MA(1) as shown below.

To compute estimates of $\mu$ and $\theta$, we can minimize the sum of squares quantity $S(\mu, \theta)$ given by
\begin{align*}
  S(\mu, \theta) &= \left(y_1 - \frac{\mu}{1 + \theta} \right)^2 +
  \left(y_2 - \frac{\mu}{1 + \theta} - \theta y_1 \right)^2 +
  \left(y_3 - \frac{\mu}{1 + \theta} - \theta y_2 + \theta^2 y_1
  \right)^2 + \dots + \\ &\left(y_n - \frac{\mu}{1 + \theta} - \theta
    y_{n-1} + \theta^2 y_{n-2} - \dots + (-1)^{n-1} \theta^{n-1} y_1
                           \right)^2.
\end{align*}
The function S_func below computes this function $S(\mu, \theta)$.

```python
from scipy.optimize import minimize #this is the function that we shall use to minimize S(\mu, \theta)$

def compute_s(y, theta):
    n = len(y)
    s = np.zeros(n)
    s[0] = y[0]
    for t in range(1, n):
        s[t] = y[t] - theta * s[t-1]
    return s

def S_func(params, y): #this is the function S(\mu, \theta)
    mu, theta = params
    if 1 + theta == 0:
        return np.inf
    s = compute_s(y, theta)
    target = mu / (1 + theta)
    return np.sum((s - target)**2)
```

Let us simulate a dataset from the MA(1) model with $\mu = 0$ and $\theta = -0.7$ to evaluate the performance of our estimation strategy.

```python
arma_process = ArmaProcess([1], [1, -0.7])
dt = arma_process.generate_sample(nsample=400)
```

The output from using the ARIMA function is given below.

```python
ma_mod = ARIMA(dt, order = (0, 0, 1)).fit()
print(ma_mod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  400
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -540.927
Date:                Sat, 19 Apr 2025   AIC                           1087.853
Time:                        01:12:36   BIC                           1099.828
Sample:                             0   HQIC                          1092.595
                                - 400
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0027      0.012     -0.226      0.821      -0.026       0.021
ma.L1         -0.7464      0.035    -21.193      0.000      -0.815      -0.677
sigma2         0.8735      0.069     12.702      0.000       0.739       1.008
===================================================================================
Ljung-Box (L1) (Q):                   0.51   Jarque-Bera (JB):                 1.66
Prob(Q):                              0.47   Prob(JB):                         0.44
Heteroskedasticity (H):               0.94   Skew:                            -0.02
Prob(H) (two-sided):                  0.73   Kurtosis:                         2.69
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Now we obtain $\hat{\mu}$ and $\hat{\theta}$ by minimizing $S(\mu, \theta)$ and we can compare our estimates with those reported by the above ARIMA function. We shall use the inbuilt optimization function \texttt{minimize}. It requires initial values which we take to be $\theta = 0$ and $\mu$ to be the mean of the data.

```python
# Initial guess: [mu_init, theta_init]
mu_init = np.mean(dt)
theta_init = 0
init_params = [mu_init, theta_init]

# Perform the optimization
result = minimize(S_func, init_params, args=(dt,))
print(result)
mu_hat, theta_hat = result.x
alphaest = result.x

print("Estimated mu:", mu_hat)
print("Estimated theta:", theta_hat)
```

```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 349.95037593379897
        x: [-3.971e-03 -7.474e-01]
      nit: 12
      jac: [ 3.815e-06  0.000e+00]
 hess_inv: [[ 7.978e-05 -1.413e-06]
            [-1.413e-06  6.066e-04]]
     nfev: 60
     njev: 20
Estimated mu: -0.00397079554935901
Estimated theta: -0.747415904826925
```

The estimates are quite close to those obtained by ARIMA.

To obtain the standard errors for uncertainty quantification, we shall use the formula given at the end of the notes for Lecture 23. This formula involves calculating the Hessian matrix of $S(\mu, \theta)$ at the point estimates $\hat{\mu}$ and $\hat{\theta}$. We shall use the python library numdifftools for numerically evaluating the Hessian of $S(\mu, \theta)$.

```python
import numdifftools as nd #this library has functions to calculate first and second derivatives

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
```

```
Estimated mu: -0.00397079554935901
Estimated theta: -0.747415904826925
Estimated sigma: 0.9424430612455296
Covariance matrix:
 [[ 1.41671210e-04 -2.63105421e-06]
 [-2.63105421e-06  1.07831062e-03]]
Standard errors: [0.01190257 0.03283764]
```

The obtained standard errors are also close to those obtained from ARIMA.

## One more example

Here is one more example where we can check that our estimates and their standard errors for parameters in MA(1) are close to those obtained from the ARIMA function.

```python
beersales = pd.read_csv('MRTSSM4453USN_March2025.csv')
y = beersales['MRTSSM4453USN']
ydiff12 = y.diff(periods = 12)
y2d = ydiff12.diff()
dt = y2d.dropna().to_numpy()
```

Below we fit MA(1) via the ARIMA function.

```python
ma_mod = ARIMA(dt, order = (0, 0, 1)).fit()
print(ma_mod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  383
Model:                 ARIMA(0, 0, 1)   Log Likelihood               -2358.779
Date:                Sat, 19 Apr 2025   AIC                           4723.558
Time:                        01:20:09   BIC                           4735.402
Sample:                             0   HQIC                          4728.256
                                - 383
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1714      2.575      0.067      0.947      -4.876       5.219
ma.L1         -0.5697      0.028    -20.263      0.000      -0.625      -0.515
sigma2      1.308e+04    652.547     20.037      0.000    1.18e+04    1.44e+04
===================================================================================
Ljung-Box (L1) (Q):                   6.31   Jarque-Bera (JB):               125.42
Prob(Q):                              0.01   Prob(JB):                         0.00
Heteroskedasticity (H):               5.26   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         5.77
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Next we fit MA(1) using our method.

```python
# Initial guess: [mu_init, theta_init]
mu_init = np.mean(dt)
theta_init = 0
init_params = [mu_init, theta_init]

# Perform the optimization
result = minimize(S_func, init_params, args=(dt,))
print(result)
mu_hat, theta_hat = result.x
alphaest = result.x

print("Estimated mu:", mu_hat)
print("Estimated theta:", theta_hat)
```

```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 5011626.773814039
        x: [ 3.935e-02 -5.698e-01]
      nit: 14
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 6.139e-06 -3.174e-07]
            [-3.174e-07  7.938e-08]]
     nfev: 72
     njev: 24
Estimated mu: 0.03934764631035018
Estimated theta: -0.569755702273577
```

The estimated $\theta$ is quite close to that given by ARIMA. The estimate of $\mu$ seems slightly off from that given by ARIMA. Standard errors are computed below.

```python
import numdifftools as nd #this library has functions to calculate first and second derivatives

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
```

```
Estimated mu: 0.03934764631035018
Estimated theta: -0.569755702273577
Estimated sigma: 112.78237853564474
Covariance matrix:
 [[ 6.07038956e+00 -5.25557790e-04]
 [-5.25557790e-04  1.18250503e-03]]
Standard errors: [2.46381606 0.03438757]
```

These standard errors seem close to those given by ARIMA.

---

[← Back to co2 dataset](05-back-to-co2-dataset.md) · [Up: contents](index.md)
