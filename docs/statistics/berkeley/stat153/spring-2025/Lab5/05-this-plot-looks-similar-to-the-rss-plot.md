---
title: this plot looks similar to the RSS plot
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this plot looks similar to the RSS plot

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

The following code generates posterior samples.

```python
N = 2000
cpostsamples = rng.choice(allcvals, N, replace = True, p = postvals)
post_samples = np.zeros(shape = (N, 4))
post_samples[:,0] = cpostsamples

for i in range(N):
    c = cpostsamples[i]

    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])
    p = X.shape[1]

    md_c = sm.OLS(y, X).fit()

    chirv = rng.chisquare(df = n - p)
    sig_sample = np.sqrt(np.sum(md_c.resid ** 2) / chirv) #posterior sample from sigma
    post_samples[i, (p + 1)] = sig_sample

    covmat = (sig_sample ** 2) * np.linalg.inv(np.dot(X.T, X))
    beta_sample = rng.multivariate_normal(mean = md_c.params, cov = covmat, size = 1)
    post_samples[i, 1:(p + 1)] = beta_sample

print(post_samples)
```

```
[[ 5.05000000e+03 -1.28000430e-02  4.20797852e-01  1.00231554e+00]
 [ 5.02500000e+03  8.04560220e-03  4.26058253e-01  1.01677879e+00]
 [ 5.05300000e+03  7.02856193e-03  4.00933767e-01  1.00499166e+00]
 ...
 [ 5.06700000e+03 -2.11369872e-02  4.34416448e-01  9.87343752e-01]
 [ 5.01700000e+03 -3.12764767e-02  4.09694942e-01  9.93151258e-01]
 [ 5.00600000e+03  3.34638353e-03  4.09055268e-01  1.00213666e+00]]
```

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

[← Plotting the fitted values](04-plotting-the-fitted-values.md) · [Up: contents](index.md) · [Plotting only the change-point samples →](06-plotting-only-the-change-point-samples.md)
