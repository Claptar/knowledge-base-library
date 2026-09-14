---
title: Drawing posterior samples
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Drawing posterior samples

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

N = 2000
cpostsamples = rng.choice(allcvals, N, replace = True, p = postvals)

post_samples = np.zeros(shape = (N, 5))
post_samples[:, 0] = cpostsamples
for i in range(N):
    f = cpostsamples[i]
    x = np.arange(1, n + 1)
    xc = ((x > c).astype(float)) * (x - c)
    X = np.column_stack([np.ones(n), x, xc])
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
[[3.02000000e+02 1.78679868e+05 1.89836033e+02 3.42169717e+01
  2.22133894e+03]
 [2.85000000e+02 1.78325271e+05 1.91295418e+02 3.24809108e+01
  2.25595672e+03]
 [2.83000000e+02 1.78395919e+05 1.90801617e+02 3.30139821e+01
  2.25832125e+03]
 ...
 [2.90000000e+02 1.78563273e+05 1.90179251e+02 3.33837727e+01
  2.15566567e+03]
 [2.90000000e+02 1.78292844e+05 1.91629020e+02 3.21929322e+01
  2.29143430e+03]
 [3.04000000e+02 1.78581825e+05 1.90525611e+02 3.27431913e+01
  2.21071767e+03]]
```

```python

---

[← this plot looks similar to the RSS plot](21-this-plot-looks-similar-to-the-rss-plot.md) · [Up: contents](index.md) · [Let us plot the posterior samples for c on the original plot →](23-let-us-plot-the-posterior-samples-for-c-on-the-original-plot.md)
