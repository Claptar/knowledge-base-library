---
title: the MLE of f is now
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# the MLE of f is now

**Source:** [`Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fhat = allfvals[np.argmin(critvals)]

print(fhat)
```

```
1.7996179961799619
```

Note that the MLE is very close to 1.8. The Bayesian analysis will also give a posterior that is tightly concentrated around 1.8.

```python
def logpost(f):
    xcos = np.cos(2 * np.pi * f * t)
    xsin = np.sin(2 * np.pi * f * t)
    X = np.column_stack([np.ones(n), xcos, xsin])

    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) # sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant
    logval = ((p - n) / 2) * np.log(rss) - 0.5 * log_det

    return logval
```

```python
allfvals = allfvals[100:ngrid] # we are removing some values near 0 to prevent singularity of X_f^T X_f
print(np.min(allfvals), np.max(allfvals))

logpostvals = np.array([logpost(f) for f in allfvals])

plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

```
0.01000010000100001 10.0
```

*(1 figure omitted — see the original notebook.)*

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))

plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← 95% credible interval for f](04-95-credible-interval-for-f.md) · [Up: contents](index.md) · [Posterior mean of f →](06-posterior-mean-of-f.md)
