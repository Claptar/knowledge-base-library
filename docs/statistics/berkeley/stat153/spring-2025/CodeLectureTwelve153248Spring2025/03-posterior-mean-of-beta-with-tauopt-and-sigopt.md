---
title: Posterior mean of beta with tauopt and sigopt
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwelve153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwelve153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Posterior mean of beta with tauopt and sigopt

**Source:** [`CodeLectureTwelve153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwelve153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

C = 10**4
tau = tau_opt
sig = sig_opt
Q = np.diag(np.concatenate([[C, C], np.repeat(tau**2, n-2)]))

XTX = np.dot(X.T, X)
TempMat = np.linalg.inv(np.linalg.inv(Q) + (XTX/(sig ** 2)))
XTy = np.dot(X.T, y)

betahat = np.dot(TempMat, XTy/(sig ** 2))
muhat = np.dot(X, betahat)

plt.figure(figsize = (10, 6))
plt.plot(y)
plt.plot(muhat)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we conver the log-posterior values to posterior values.

```python
g['post'] = np.exp(g['logpost'] - np.max(g['logpost']))
g['post'] = g['post']/np.sum(g['post'])
```

```python
print(g.head(10))
```

```
tau  sig    logpost          post
0  0.000100  0.1  -4.745616  4.468373e-91
1  0.000110  0.1   6.770660  4.483372e-86
2  0.000120  0.1  17.552952  2.159208e-81
3  0.000132  0.1  27.530407  4.649950e-77
4  0.000145  0.1  36.672379  4.342662e-73
5  0.000159  0.1  44.983468  1.766918e-69
6  0.000175  0.1  52.496662  3.237092e-66
7  0.000192  0.1  59.265711  2.817835e-63
8  0.000210  0.1  65.357670  1.246292e-60
9  0.000231  0.1  70.846229  3.014883e-58
```

We can now compute posterior means of $\tau$ and $\sigma$.

```python
tau_pm = np.sum(g['tau'] * g['post'])
sig_pm = np.sum(g['sig'] * g['post'])
print(tau_pm, sig_pm)
```

```
0.0024208108011471072 0.1732583012438226
```

Posterior means are quite close to the posterior maximizers obtained previously.

Below we compute posterior samples of all the parameters $\beta, \tau, \sigma$.

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
    Q = np.diag(np.concatenate([[C, C], np.repeat(tau**2, n-2)]))
    XTX = np.dot(X.T, X)
    TempMat = np.linalg.inv(np.linalg.inv(Q) + (XTX/(sig ** 2)))
    XTy = np.dot(X.T, y)
    betahat = np.dot(TempMat, XTy/(sig ** 2))
    muhat = np.dot(X, betahat)
    betahats[:,i] = betahat
    muhats[:,i] = muhat
```

From these samples, we can obtain approximations of the posterior means of $\beta$ and the fitted values $X \beta$.

```python
beta_est = np.mean(betahats, axis = 1)
mu_est = np.mean(muhats, axis = 1) #these are the fitted values
```

Below we plot the fitted values corresponding to the samples of $\beta$.

```python
plt.figure(figsize = (10, 6))
plt.plot(y, label = 'Data')
for i in range(N):
    plt.plot(muhats[:,i], color = 'red')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is interesting that the uncertainty band is narrow at some time points and wider in others.

Below are histograms of the samples of $\tau$ and $\sigma$.

```python
plt.figure(figsize=(10, 6))
plt.hist(tau_samples, bins=30)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize=(10, 6))
plt.hist(sig_samples, bins=30)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is quite interesting that the posterior samples of $\tau$ correspond to values that are neither too large (wiggly function fits) and neither too small (almost-linear function fits).

---

[← Posterior mean of beta with fixed tau and sig](02-posterior-mean-of-beta-with-fixed-tau-and-sig.md) · [Up: contents](index.md)
