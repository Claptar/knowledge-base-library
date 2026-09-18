---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.optimize import minimize
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess, arma_acf, arma_pacf
from statsmodels.tsa.arima.model import ARIMA
```

## Parameter Estimation in MA(1)

Estimating the parameters of ARMA (as well as ARIMA, SARIMA models) is much harder
than parameter estimation in AR models which was handled by standard regression (ordinary
least squares). We will not study this topic in any detail (and simply rely on the ARIMA function for fitting
these models to data). But today, we will discuss estimation for MA(1) to gain some insight into how estimation works in these models.

Recall that the MA(1) model is given by
\begin{equation*}
  y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. For parameter estimation, we need to write down the likelihood.

### Likelihood

The
joint density of $y_1, \dots, y_n$ is multivariate normal with mean
vector $m := (\mu, \dots, \mu)^T$ and
covariance matrix $\Sigma$ where $\Sigma$ equals the $n \times n$
matrix whose
$(i, j)^{th}$ entry is given by $\sigma^2 (1 + \theta^2)$ when $i = j$, equals $\sigma^2 \theta$ when $|i - j| = 1$ and equals 0 for all other $(i, j)$. The likelihood is therefore
\begin{align*}
  \left(\frac{1}{\sqrt{2 \pi}} \right)^n \left(\det \Sigma
  \right)^{-1/2} \exp \left( - \frac{1}{2} (y - m)' \Sigma^{-1} (y -
  m)\right)
\end{align*}
where $y$ is the $n \times 1$ vector with components $y_1, \dots,
y_n$. This is a function of the unknown parameters $\mu, \theta,
\sigma$ which can be estimated by maximizing the logarithm of the
likelihood. The presence of $\Sigma^{-1}$ makes this computationally
expensive. Some (exact or approximate) formula should be used for
$\Sigma^{-1}$ so that one does not need to invert an $n \times n$
matrix every time the log-likelihood is to be computed.

### Conditional Likelihood

Instead of the full likelihood, the form of the conditional likelihood when conditioned on $\epsilon_0 = 0$ is simpler. This is similar to the story for the AR(1) model where the form of the likelihood when conditioned on $y_1$ is much simpler than the full likelihood. The difference here is that instead of conditioning on $y_1$ being the observed value, we are conditioning on $\epsilon_0 = 0$.

Below we write the conditional likelihood:
\begin{equation*}
   f_{y_1, \dots, y_n \mid \epsilon_0 = 0}(y_1, \dots, y_n).
\end{equation*}
This likelihood can be broken down as
\begin{equation*}
  f_{y_1 \mid \epsilon_0 = 0}(y_1) f_{y_2 \mid y_1, \epsilon_0 = 0}(y_2) f_{y_3 \mid y_1, y_2, \epsilon_0 = 0}(y_3) \dots f_{y_n \mid y_1, \dots, y_{n-1}, \epsilon_0 = 0}(y_n)
\end{equation*}
Each of the terms above can be written explicitly. Let $\hat{\epsilon}_1 = y_1 - \mu$ and, for $t = 2, \dots, n$,
\begin{equation*}
    \hat{\epsilon}_t = y_t- \mu - \theta \hat{\epsilon}_{t-1}
\end{equation*}
Then
\begin{equation*}
   f_{y_1 \mid \epsilon_0 = 0}(y_1) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right)
\end{equation*}
and
\begin{align*}
  f_{y_t \mid y_1, \dots, y_{t-1}, \epsilon = 0}(y_t) &= f_{y_t \mid \epsilon_1 = \hat{\epsilon}_1, \epsilon_2 = \hat{\epsilon}_2, \dots, \epsilon_{t-1} = \hat{\epsilon}_{t-1}, \epsilon_0 = 0}(y_t) \\
  &= f_{\epsilon_t}(y_t - \mu - \theta \hat{\epsilon}_{t-1}) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right).
\end{align*}
Thus the conditional likelihood given $\epsilon_0 = 0$ is given by
\begin{align*}
   \text{likelihood} &= \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{(y_1 - \mu)^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^2} (y_t - \mu - \theta \hat{\epsilon}_{t-1})^2 \right) \right] \\ & = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_1^2}{2 \sigma^2} \right) \left[\prod_{t=2}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\hat{\epsilon}_t^2}{2 \sigma^2}  \right) \right] \\
   &= \left(\frac{1}{\sigma \sqrt{2 \pi}} \right)^n \exp \left(-\frac{1}{2 \sigma^2} \sum_{t=1}^n \hat{\epsilon}_t^2 \right).
\end{align*}
The key term in the above likelihood is $\sum_{t=1}^n \hat{\epsilon}_t^2$ which depends on the data $\{y_t\}$ and also on the parameters $\mu$ and $\theta$. So let us denote
\begin{align*}
   S(\mu, \theta) := \sum_{t=1}^n \hat{\epsilon}_t^2
\end{align*}
so that the likelihood and log-likelihood become
\begin{align*}
   \text{likelihood} = \left(\frac{1}{\sigma \sqrt{2 \pi}} \right)^n \exp \left(-\frac{S(\mu, \theta)}{2 \sigma^2} \right)
\end{align*}
and
\begin{align*}
   \text{log-likelihood} = -\frac{n}{2} \log (\sigma^2) - \frac{S(\mu, \theta)}{2 \sigma^2}.
\end{align*}
Thus the MLEs of $\mu, \theta$ are obtained by minimizing $S(\mu, \theta)$, and the MLE of $\sigma$ is
\begin{align*}
   \hat{\sigma} = \sqrt{\frac{S(\hat{\mu}, \hat{\theta})}{n}}
\end{align*}

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

We will use the function 'minimize' from scipy.optimize to minimize S_func. First let us simulate some data from the MA(1) model with theta = -0.7 to evaluate the performance of our estimation strategy.

```python
arma_process = ArmaProcess([1], [1, -0.7])
dt = arma_process.generate_sample(nsample=400)
dt = dt + 5 # adding a mean of 5
```

The output from the ARIMA function is given below.

```python
md = ARIMA(dt, order=(0, 0, 1)).fit()
print(md.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  400
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -559.755
Date:                Sat, 22 Nov 2025   AIC                           1125.511
Time:                        19:48:49   BIC                           1137.485
Sample:                             0   HQIC                          1130.253
                                - 400
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          5.0092      0.017    296.502      0.000       4.976       5.042
ma.L1         -0.6566      0.037    -17.828      0.000      -0.729      -0.584
sigma2         0.9603      0.066     14.579      0.000       0.831       1.089
===================================================================================
Ljung-Box (L1) (Q):                   0.53   Jarque-Bera (JB):                 0.33
Prob(Q):                              0.47   Prob(JB):                         0.85
Heteroskedasticity (H):               0.90   Skew:                             0.02
Prob(H) (two-sided):                  0.54   Kurtosis:                         3.14
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Let us now minimize $S(\mu, \theta)$ and compare the resulting estimates of $\mu$ and $\theta$ with those reported by the ARIMA function.

```python
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
      fun: 384.13856984891936
        x: [ 5.009e+00 -6.582e-01]
      nit: 10
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 1.476e-04 -1.728e-06]
            [-1.728e-06  6.930e-04]]
     nfev: 51
     njev: 17
Estimated mu: 5.009073896055675
Estimated theta: -0.6582279929829957
```

```python
print(result.x)
print(md.params)
```

```
[ 5.0090739  -0.65822799]
[ 5.00917415 -0.65657733  0.96028995]
```

The estimates of $\mu$ and $\theta$ obtained by minimizing $S(\mu, \theta)$ are clearly very close to those reported by the ARIMA function. The estimate of $\sigma$ is given by $\sqrt{S(\hat{\mu}, \hat{\theta})/n}$.

```python
sigma_hat = np.sqrt(S_func(result.x, dt) / len(dt))
print("Estimated sigma:", sigma_hat)
print("ARIMA reported sigma:", np.sqrt(md.params[2]))
```

```
Estimated sigma: 0.9799726652424028
ARIMA reported sigma: 0.9799438524963823
```

---

[Up: contents](index.md) · [Standard Errors corresponding to the parameter estimates →](02-standard-errors-corresponding-to-the-parameter-estimates.md)
