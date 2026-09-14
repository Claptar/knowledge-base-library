---
title: Three High-Dimensional Models for Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFourteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Three High-Dimensional Models for Time Series

**Source:** [`CodeLectureFourteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We shall discuss three simple high-dimensional models for time series. The first model was already studied in the previous week. The third model is the same as the spectrum model from last lecture (even though the presentation today will be slightly different). The second model has not been discussed before in this class but it is quite simple.

## Model ONE

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

## Model TWO

This is the model
\begin{equation*}
   y_t \overset{\text{independent}}{\sim} N(0, \tau_t^2)
\end{equation*}
Negative log-likelihood parametrized by $\alpha_t = \log \tau_t$ is given by
\begin{equation*}
  \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2 \alpha_t} \right)
\end{equation*}
We add regularization and minimize:
\begin{equation*}
  \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2 \alpha_t} \right) + \lambda \sum_{t=2}^{n-1} \left((\alpha_{t+1} - \alpha_{t})- (\alpha_{t} - \alpha_{t-1})\right)^2
\end{equation*}
or
\begin{equation*}
  \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2 \alpha_t} \right) + \lambda \sum_{t=2}^{n-1} \left|(\alpha_{t+1} - \alpha_{t})- (\alpha_{t} - \alpha_{t-1})\right|
\end{equation*}

```python
def alpha_est_ridge(y, lambda_val):
    n = len(y)
    alpha = cp.Variable(n)
    neg_likelihood_term = cp.sum(cp.multiply(((y ** 2)/2), cp.exp(-2 * alpha)) + alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value

def alpha_est_lasso(y, lambda_val):
    n = len(y)
    alpha = cp.Variable(n)
    neg_likelihood_term = cp.sum(cp.multiply(((y ** 2)/2), cp.exp(-2 * alpha)) + alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value
```

Below we describe two simulation settings for this model.

### Simulation 1 for Model 2

```python
#Simulate data from this variance model:
n = 400
tvals = np.arange(1, n+1)
th = -0.8
tau_t = np.sqrt((1 + (th ** 2) + 2*th*np.cos(2 * np.pi * (tvals)/n))) #this is a smooth function of t
y = rng.normal(loc = 0, scale = tau_t)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
alpha_true = np.log(tau_t)
alpha_opt_ridge = alpha_est_ridge(y, 2000000)
alpha_opt_lasso = alpha_est_lasso(y, 200)
plt.figure(figsize = (12, 6))
plt.plot(alpha_opt_ridge, label = 'ridge')
plt.plot(alpha_true, color = 'red', label = 'true')
plt.plot(alpha_opt_lasso, color = 'black', label = 'lasso')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The sufficient statistic in this model is $y_1^2, \dots, y_n^2$. Because $y_t^2 \sim \tau_t^2 \chi^2_1$, the mean of $y_t^2$ equals $\tau_t^2$ and its variance is $2 \tau^4$. Below we plot $y_t^2$ as well as $\tau_t^2$.

```python
#Plotting y^2 against tau^2
plt.figure(figsize = (12, 6))
plt.plot(y ** 2, label = 'Data', color = 'lightgray')
plt.plot(tau_t ** 2, color = 'blue', label = 'Truth')
plt.plot(np.exp(2*alpha_opt_ridge), color = 'red', label = 'Ridge')
plt.plot(np.exp(2*alpha_opt_lasso), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Observe from the above plot that both the level (mean) of $y_t^2$ as well as its variance changes with $\tau_t^2$. This is because the mean of $y_t^2$ equals $\tau_t^2$, and its variance equals $2 \tau_t^4$.

Because $y_t^2 \sim \tau_t^2 \chi^2_1$, we can write
\begin{equation*}
   \log(y_t^2) = \log(\tau_t^2) + \log (\chi^2_1)
\end{equation*}
The mean of $\log \chi^2_1$ is negative (internet says it is about -1.27). This means that if we plot $\log y_t^2$ and $\log \tau_t^2$ in one figure, most of the values for $\log y_t^2$ will appear to be below $\log \tau_t^2$.

```python
#Plotting log y^2 against log tau^2
plt.figure(figsize = (12, 6))
plt.plot(np.log(y ** 2), color = 'lightgray', label = 'Data')
plt.plot(np.log(tau_t ** 2), color = 'blue', label = 'Truth')
plt.plot(np.log(np.exp(2*alpha_opt_ridge)), color = 'red', label = 'Ridge')
plt.plot(np.log(np.exp(2*alpha_opt_lasso)), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Simulation 2 for Model 2

Here is the second simulation setting for this model.

```python
def smoothfun(x):
    ans = np.sin(15*x) + np.exp(-(x ** 2)/2) + 0.5*((x - 0.5) ** 2) + 2*np.log(x + 0.1)
    return ans

n = 2000
xx = np.linspace(0, 1, n)
alpha_true = np.array([smoothfun(x) for x in xx])
plt.figure(figsize = (12, 6))
plt.plot(alpha_true)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
tau_t = np.exp(alpha_true)
y = rng.normal(loc = 0, scale = tau_t)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
alpha_opt_ridge = alpha_est_ridge(y, 40000)
alpha_opt_lasso = alpha_est_lasso(y, 200)
plt.figure(figsize = (12, 6))
plt.plot(alpha_opt_ridge, label = 'ridge')
plt.plot(alpha_true, color = 'red', label = 'true')
plt.plot(alpha_opt_lasso, color = 'black', label = 'lasso')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting y^2 against tau^2
plt.figure(figsize = (12, 6))
plt.plot(y ** 2, label = 'Data', color = 'lightgray')
plt.plot(tau_t ** 2, color = 'blue', label = 'Truth')
plt.plot(np.exp(2*alpha_opt_ridge), color = 'red', label = 'Ridge')
plt.plot(np.exp(2*alpha_opt_lasso), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting log y^2 against log tau^2
plt.figure(figsize = (12, 6))
plt.plot(np.log(y ** 2), color = 'lightgray', label = 'Data')
plt.plot(np.log(tau_t ** 2), color = 'blue', label = 'Truth')
plt.plot(np.log(np.exp(2*alpha_opt_ridge)), color = 'red', label = 'Ridge')
plt.plot(np.log(np.exp(2*alpha_opt_lasso)), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### A real dataset from finance for which Model 2 is applicable

Next, we examine a real dataset where this variance model (Model 2) may be applicable. The dataset consists of stock price data for the S&P 500 mutual fund, downloaded from Yahoo Finance using the yfinance library.

```python

---

[Up: contents](index.md) · [Download S&P 500 data →](02-download-s-p-500-data.md)
