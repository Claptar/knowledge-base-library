---
title: Posterior mean of beta with fixed tau and sig
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwelve153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwelve153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Posterior mean of beta with fixed tau and sig

**Source:** [`CodeLectureTwelve153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwelve153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

C = 10**4
#tau = 0.001
tau = .0001
sig = 0.2
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

We showed in class that this posterior mean coincides with the ridge regression estimate from last lecture provided $\lambda = \sigma^2/\tau^2$. This can be verified as follows.

```python
#below penalty_start = 2 means that b0 and b1 are not included in the penalty
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
b_ridge = solve_ridge(X, y, lambda_val = (sig ** 2)/(tau ** 2))
ridge_fitted = np.dot(X, b_ridge)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray', label = 'data')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.plot(muhat, color = 'blue', label = 'Posterior mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We next perform posterior inference for all the parameters $\beta, \sigma, \tau$. We follow the method described in lecture. First we take a grid of values of $\tau$ and $\sigma$ and compute the posterior (on the logarithmic scale) of $\tau$ and $\sigma$.

```python
tau_gr = np.logspace(np.log10(0.0001), np.log10(1), 100)
sig_gr = np.logspace(np.log10(0.1), np.log10(1), 100)
#sig_gr = np.array([0.16])

t, s = np.meshgrid(tau_gr, sig_gr)

g = pd.DataFrame({'tau': t.flatten(), 'sig': s.flatten()})

for i in range(len(g)):
    tau = g.loc[i, 'tau']
    sig = g.loc[i, 'sig']
    Q = np.diag(np.concatenate([[C, C], np.repeat(tau**2, n-2)]))
    Mat = np.linalg.inv(Q) + (X.T @ X)/(sig ** 2)
    Matinv = np.linalg.inv(Mat)
    sgn, logcovdet = np.linalg.slogdet(Matinv)
    sgnQ, logcovdetQ = np.linalg.slogdet(Q)
    g.loc[i, 'logpost'] = (-n-1)*np.log(sig) - np.log(tau) - 0.5 * logcovdetQ + 0.5 * logcovdet - ((np.sum(y ** 2))/(2*(sig ** 2))) + (y.T @ X @ Matinv @ X.T @ y)/(2 * (sig ** 4))
```

Point estimates of $\tau$ and $\sigma$ can be obtained either by maximizers of the posterior or posterior means.

```python
#Posterior maximizers:
max_row = g['logpost'].idxmax()
print(max_row)
tau_opt = g.loc[max_row, 'tau']
sig_opt = g.loc[max_row, 'sig']
print(tau_opt, sig_opt)
```

```
2333
0.0021544346900318843 0.1707352647470691
```

Below, we fix $\tau$ and $\sigma$ to be the posterior maximizers, and then find the posterior mean of $\beta$.

```python

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Posterior mean of beta with tauopt and sigopt →](03-posterior-mean-of-beta-with-tauopt-and-sigopt.md)
