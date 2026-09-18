---
title: Model ONE
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFourteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFourteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model ONE

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cvxpy as cp
import yfinance as yf
```

## Three High-Dimensional Models for Time Series

We shall discuss three simple high-dimensional models for time series. The first model was already studied in the previous week. The third model is the same as the spectrum model from last lecture (even though the presentation today will be slightly different). The second model has not been discussed before in this class but it is quite simple.

This is the model
\begin{equation*}
   y_t \overset{\text{ind}}{\sim} N(\mu_t, \sigma^2)
\end{equation*}
where $\mu_t$ (which can be interpreted as the trend function) is smooth in $t$. $\mu_t$ can be estimated from the data using one of the following two regularized estimators obtained by minimizing
\begin{equation*}
   \sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} \left((\mu_t - \mu_{t-1}) - (\mu_{t-1} - \mu_t) \right)^2
\end{equation*}
or
\begin{equation*}
   \sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} \left|(\mu_t - \mu_{t-1}) - (\mu_{t-1} - \mu_t) \right|
\end{equation*}
As we saw previously, these are the same as the estimators obtained by employing the ridge and LASSO penalties to the high-dimensional linear regression model:
\begin{equation*}
   \mu_t = \beta_0 + \beta_1 (t-1) + \beta_2 (t-2)_+ + \dots + \beta_{n-1} (t - (n-1))_+
\end{equation*}

```python
def smoothfun(x):
    ans = np.sin(15*x) + np.exp(-(x ** 2)/2) + 0.5*((x - 0.5) ** 2) + 2*np.log(x + 0.1)
    return ans

n = 2000
xx = np.linspace(0, 1, n)
mu_true = np.array([smoothfun(x) for x in xx])
sig = 1
rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sig, size = n)
y = mu_true + errorsamples
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we compute the estimator $\hat{\mu}_t$ directly without going to the regression representation (with the $X$ matrix that we previously used). We use the optimization functions from cvxpy directly on the optimization in terms of $\mu_t$.

```python
def mu_est_ridge(y, lambda_val):
    n = len(y)
    mu = cp.Variable(n)
    neg_likelihood_term = cp.sum((y - mu)**2)
    smoothness_penalty = cp.sum(cp.square(mu[2:] - 2 * mu[1:-1] + mu[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return mu.value

def mu_est_lasso(y, lambda_val):
    n = len(y)
    mu = cp.Variable(n)
    neg_likelihood_term = cp.sum((y - mu)**2)
    smoothness_penalty = cp.sum(cp.abs(mu[2:] - 2 * mu[1:-1] + mu[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return mu.value

mu_opt_ridge = mu_est_ridge(y, 200000)
mu_opt_lasso = mu_est_lasso(y, 200)
plt.figure(figsize = (12, 6))
plt.plot(y, label = 'Data', color = 'lightgray')
plt.plot(mu_opt_ridge, label = 'ridge')
plt.plot(mu_true, color = 'red', label = 'true')
plt.plot(mu_opt_lasso, color = 'black', label = 'lasso')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Model TWO →](02-model-two.md)
