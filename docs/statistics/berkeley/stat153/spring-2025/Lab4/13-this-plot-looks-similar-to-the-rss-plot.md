---
title: this plot looks similar to the RSS plot
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this plot looks similar to the RSS plot

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

*(1 figure omitted — see the original notebook.)*

Let us exponentiate the log-posterior values to get the posterior.

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))

plt.plot(allcvals, postvals)
plt.xlabel('Changepoint')
plt.ylabel('Probability')
plt.title('Posterior distribution of change points')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We draw posterior samples exactly as before.

```python
N = 1000
cpostsamples = rng.choice(allcvals, N, replace = True, p = postvals)

post_samples = np.zeros(shape = (N, 4))
post_samples[:, 0] = cpostsamples
for i in range(N):
    c = cpostsamples[i]
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])
    p = X.shape[1]

    md_c = sm.OLS(y, X).fit()

    chirv = rng.chisquare(df = n - p)
    sig_sample = np.sqrt(np.sum(md_c.resid ** 2) / chirv) # posterior sample from sigma
    post_samples[i, (p + 1)] = sig_sample

    covmat = (sig_sample ** 2) * np.linalg.inv(np.dot(X.T, X))
    beta_sample = rng.multivariate_normal(mean = md_c.params, cov = covmat, size = 1)
    post_samples[i, 1:(p + 1)] = beta_sample

print(post_samples)
```

```
[[5.01400000e+03 1.61186008e-02 4.15836357e-01 9.94694854e-01]
 [5.07500000e+03 2.21172885e-02 4.02259427e-01 9.96874208e-01]
 [4.93100000e+03 6.69816740e-03 4.29948362e-01 9.91129525e-01]
 ...
 [5.03000000e+03 1.52941625e-02 4.27556266e-01 1.00020949e+00]
 [5.01400000e+03 2.52471690e-02 3.94416060e-01 9.92312337e-01]
 [4.99600000e+03 1.99135692e-02 3.90096091e-01 1.00377472e+00]]
```

These posterior samples can be used to visualize the uncertainty in the fitted functions.

```python
x = np.arange(1, n + 1)
plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    c = cpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    ftdval = b0 + b1 * (x > c).astype(float)

    plt.plot(ftdval, color = 'red')
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Plot the fitted values](12-plot-the-fitted-values.md) · [Up: contents](index.md) · [Summary of the posterior samples →](14-summary-of-the-posterior-samples.md)
