---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: More on Bayesian Regularization
---

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import cvxpy as cp
```

Let us consider the temperature anomalies dataset that we used in the last couple of lectures.

```python
temp_jan = pd.read_csv('TempAnomalies_January.csv', skiprows=4)
print(temp_jan.head())
y = temp_jan['Anomaly']
plt.plot(y)
plt.xlabel('year')
plt.ylabel('Celsius')
plt.title('Temperature anomalies (from 1901-2000 average) for January')
plt.show()
```

```
Year  Anomaly
0  1850    -0.46
1  1851    -0.17
2  1852    -0.02
3  1853    -0.12
4  1854    -0.28
```

*(1 figure omitted — see the original notebook.)*

We will fit our high-dimensional regression model:
\begin{align*}
  y_t = \beta_0 + \beta_1 (t - 1) + \beta_2 (t - 2)_+ + \dots + \beta_{n-1}(t - (n-1))_+ + \epsilon_t
\end{align*}
to this dataset. This can be written in the usual regression form as $y = X \beta + \epsilon$ with the $X$ matrix calculated as follows.

```python
n = len(y)
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    X = np.column_stack([X, xc])
print(X)
```

```
[[  1.   0.  -0. ...  -0.  -0.  -0.]
 [  1.   1.   0. ...  -0.  -0.  -0.]
 [  1.   2.   1. ...  -0.  -0.  -0.]
 ...
 [  1. 173. 172. ...   1.   0.  -0.]
 [  1. 174. 173. ...   2.   1.   0.]
 [  1. 175. 174. ...   3.   2.   1.]]
```

### Quick Recap: Ridge Regularization (Lecture 11)

The estimator is given by the minimizer of:
\begin{align*}
   \|y - X \beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2
\end{align*}
where $\lambda$ is the tuning parameter. Small $\lambda$ leads to fitted values close to the data (overfitting) and large $\lambda$ leads to fitted values coming from a straight line (underfitting). We used the following code for computing the ridge estimator for fixed $\lambda$ (note that, instead of using this code, we can also use the formula derived in Lecture 12: $(X^T X + \lambda J)^{-1} X^T y$ to compute the ridge estimator).

```python
def solve_ridge(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

```python
b_ridge = solve_ridge(X, y, lambda_val = 1e4) #also try 1e-4, 1e8 etc.
plt.plot(y)
ridge_fitted = np.dot(X, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To choose $\lambda$, we use cross-validation (CV). Here is the code for CV.

```python
def ridge_cv(X, y, lambda_candidates):
    n = len(y)
    k = 5
    fold_size = n // k
    folds = []

    for i in range(k):
        start = i * fold_size
        end = (i + 1) * fold_size if i < k - 1 else n  # last fold includes remainder
        test_indices = np.arange(start, end)
        train_indices = np.concatenate([np.arange(0, start), np.arange(end, n)])
        folds.append((train_indices, test_indices))

    cv_errors = {lamb: 0 for lamb in lambda_candidates}

    for train_index, test_index in folds:
        X_train = X[train_index]
        X_test = X[test_index]
        y_train = y[train_index]
        y_test = y[test_index]

        for lamb in lambda_candidates:
            beta = solve_ridge(X_train, y_train, lambda_val=lamb)
            y_pred = np.dot(X_test, beta)
            squared_errors = (y_test - y_pred) ** 2
            cv_errors[lamb] += np.sum(squared_errors)

    for lamb in lambda_candidates:
        cv_errors[lamb] /= n

    best_lambda = min(cv_errors, key=cv_errors.get)
    return best_lambda, cv_errors
```

```python
lambda_candidates = np.array([1e-2, 1e-1, 1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8])

best_lambda, cv_errors = ridge_cv(X, y, lambda_candidates)
print(best_lambda)
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
1000.0
Lambda = 0.01, CV Error = 20.473188
Lambda = 0.10, CV Error = 11.850955
Lambda = 1.00, CV Error = 2.261767
Lambda = 10.00, CV Error = 0.513626
Lambda = 100.00, CV Error = 0.126082
Lambda = 1000.00, CV Error = 0.044625
Lambda = 10000.00, CV Error = 0.048169
Lambda = 100000.00, CV Error = 0.073446
Lambda = 1000000.00, CV Error = 0.105209
Lambda = 10000000.00, CV Error = 0.155146
Lambda = 100000000.00, CV Error = 0.167589
```

Below we calculate the ridge estimator for $\lambda$ chosen to be the best $\lambda$ given by CV:

```python
b_ridge = solve_ridge(X, y, lambda_val = best_lambda)
plt.plot(y)
ridge_fitted = np.dot(X, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Bayesian regularization (from Lecture 12)

In the last lecture, we worked with the following prior (as a Bayesian method for regularization):
\begin{align*}
   \beta_0, \beta_1 \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C) ~~~ \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d}}{\sim} N(0, \tau^2),
\end{align*}
We also treat $\tau$ (and $\sigma$) as unknown parameters and used the prior:
\begin{align*}
    \log \tau, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).
\end{align*}
With this prior, the posterior for $\beta, \tau, \sigma$ can be described as follows. The posterior of $\beta$ conditional on $\sigma$ and $\tau$ is given by:
\begin{align*}
   \beta \mid \text{data}, \sigma, \tau \sim N \left(\left(\frac{X^T
                          X}{\sigma^2} + Q^{-1}  \right)^{-1} \frac{X^T y}{\sigma^2},  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}\right).
\end{align*}
where $Q$ is the diagonal matrix with diagonal entries $C, C, \tau^2, \dots, \tau^2$. Further the posterior of $\tau$ and $\sigma$ is given by:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \frac{\sigma^{-n-1} \tau^{-1}}{\sqrt{\det Q}}  \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} +
   Q^{-1} \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
We can simplify this formula slightly in order to avoid specifying $C$ explicitly using
\begin{align*}
   \det Q  = C \times C \times \tau^2 \times \dots \times \tau^2 = C^2 \tau^{2(n-2)} \propto \tau^{2(n-2)}.
\end{align*}
Also
\begin{align*}
   Q^{-1} = \text{diag}(1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2) \approx \text{diag}(0, 0, 1/\tau^2, \dots, 1/\tau^2) = \frac{J}{\tau^2}
\end{align*}
where $J$ is the diagonal matrix with diagonals $0, 0, 1, \dots, 1$.

Let $Q^{-1}_{\text{approx}}$ be the above diagonal matrix with diagonal entries $0, 0, 1/\tau^2, \dots, 1/\tau^2$. We shall use $Q^{-1}_{\text{approx}}$ as our proxy for $Q^{-1}$. Note that $Q^{-1}_{\text{approx}}$ does not involve any specification of $C$. With this, we rewrite the posterior of $\tau, \sigma$ as:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \sigma^{-n-1} \tau^{-n+1}   \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + \frac{J}{\tau^2} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} + \frac{J}{\tau^2}
   \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
Below we compute this posterior on log-scale for each value in a grid chosen for $\tau$ and $\sigma$.

```python
tau_gr = np.logspace(np.log10(0.0001), np.log10(1), 100)
sig_gr = np.logspace(np.log10(0.1), np.log10(1), 100)

t, s = np.meshgrid(tau_gr, sig_gr)

g = pd.DataFrame({'tau': t.flatten(), 'sig': s.flatten()})

for i in range(len(g)):
    tau = g.loc[i, 'tau']
    sig = g.loc[i, 'sig']
    J_by_tausq = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    Mat = J_by_tausq + (X.T @ X)/(sig ** 2)
    Matinv = np.linalg.inv(Mat)
    sgn, logcovdet = np.linalg.slogdet(Matinv)
    g.loc[i, 'logpost'] = (-n-1)*np.log(sig) + (-n+1)*np.log(tau) + 0.5 * logcovdet - ((np.sum(y ** 2))/(2*(sig ** 2))) + (y.T @ X @ Matinv @ X.T @ y)/(2 * (sig ** 4))
```

The posterior samples for all the parameters can be generated as follows.

```python
g['post'] = np.exp(g['logpost'] - np.max(g['logpost']))
g['post'] = g['post']/np.sum(g['post'])
```

```python
N = 1000
samples = g.sample(N, weights = g['post'], replace = True)
tau_samples = np.array(samples.iloc[:,0])
sig_samples = np.array(samples.iloc[:,1])
betahats = np.zeros((n, N))
muhats = np.zeros((n, N))
for i in range(N):
    tau = tau_samples[i]
    sig = sig_samples[i]
    J_by_tausq = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    XTX = np.dot(X.T, X)
    TempMat = np.linalg.inv(J_by_tausq + (XTX/(sig ** 2)))
    XTy = np.dot(X.T, y)
    #generate betahat from the normal distribution with mean:
    norm_mean = np.dot(TempMat, XTy/(sig ** 2))
    #and covariance matrix:
    norm_cov = TempMat
    betahat = np.random.multivariate_normal(norm_mean, norm_cov)
    muhat = np.dot(X, betahat)
    betahats[:,i] = betahat
    muhats[:,i] = muhat
```

```python
beta_est = np.mean(betahats, axis = 1)
mu_est = np.mean(muhats, axis = 1) #these are the fitted values

plt.plot(y, label = 'Data')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting all the posterior fitted values:
plt.plot(y, label = 'Data')
for i in range(N):
    plt.plot(muhats[:,i], color = 'red')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The posterior samples of $\tau$ and $\sigma$ can be visualized by their histograms.

```python

---

[Up: contents](index.md) · [First histogram: tausamples →](02-first-histogram-tausamples.md)
