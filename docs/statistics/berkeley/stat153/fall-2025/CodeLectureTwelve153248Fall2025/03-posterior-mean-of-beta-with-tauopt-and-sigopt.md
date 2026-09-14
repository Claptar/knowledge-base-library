---
title: Posterior mean of beta with tauopt and sigopt
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Posterior mean of beta with tauopt and sigopt

**Source:** [`CodeLectureTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

Below we convert the log-posterior values to posterior values (this is the posterior over $\tau$ and $\sigma$).

```python
g['post'] = np.exp(g['logpost'] - np.max(g['logpost']))
g['post'] = g['post']/np.sum(g['post'])
```

```python
print(g.head(10))
```

```
tau  sig    logpost          post
0  0.000100  0.1   4.464728  4.468381e-91
1  0.000110  0.1  15.981004  4.483378e-86
2  0.000120  0.1  26.763295  2.159210e-81
3  0.000132  0.1  36.740750  4.649953e-77
4  0.000145  0.1  45.882721  4.342665e-73
5  0.000159  0.1  54.193811  1.766918e-69
6  0.000175  0.1  61.707004  3.237092e-66
7  0.000192  0.1  68.476053  2.817835e-63
8  0.000210  0.1  74.568012  1.246292e-60
9  0.000231  0.1  80.056570  3.014882e-58
```

We can now compute posterior means of $\tau$ and $\sigma$.

```python
tau_pm = np.sum(g['tau'] * g['post'])
sig_pm = np.sum(g['sig'] * g['post'])
print(tau_pm, tau_opt)
print(sig_pm, sig_opt)
```

```
0.0024208109728322967 0.0021544346900318843
0.17325830094841208 0.1707352647470691
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
    #generate betahat from the normal distribution with mean:
    norm_mean = np.dot(TempMat, XTy/(sig ** 2))
    #and covariance matrix:
    norm_cov = TempMat
    betahat = np.random.multivariate_normal(norm_mean, norm_cov)
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

Below are histograms of the samples of $\tau$ and $\sigma$.

```python
plt.figure(figsize=(10, 6))
plt.hist(tau_samples, bins=30)
plt.title('Histogram of tau samples')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is quite interesting that the posterior samples of $\tau$ correspond to values that are neither too large (wiggly function fits) and neither too small (almost-linear function fits).

```python
plt.figure(figsize=(10, 6))
plt.hist(sig_samples, bins=30)
plt.title('Histogram of sigma samples')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Posterior mean of beta with fixed tau and sig](02-posterior-mean-of-beta-with-fixed-tau-and-sig.md) · [Up: contents](index.md)
