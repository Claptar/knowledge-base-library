---
title: Estimates of other parameters
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimates of other parameters

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x = np.arange(1, n + 1)
c = c_hat
xc = (x > c).astype(float)

X = np.column_stack([np.ones(n), xc])
md = sm.OLS(y, X).fit()

print(md.params) # this gives estimates of beta_0, beta_1 (compare them to the true values which generated the data)

b0_est = md.params[0]
b1_est = md.params[1]

b0_true = mu1
b1_true = mu2 - mu1

print(np.column_stack((np.array([b0_est, b1_est]), np.array([b0_true, b1_true]))))

rss_chat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_chat / n)
sigma_unbiased = np.sqrt(rss_chat / (n - 2))

print(np.array([sigma_mle, sigma_unbiased, sig])) #sig is the true value of sigma which generated the data
```

```
[-0.01930042  0.42189817]
[[-0.01930042  0.        ]
 [ 0.42189817  0.4       ]]
[1.00596521 1.00606582 1.        ]
```

```python

---

[← Here is a simulated dataset having a change point](02-here-is-a-simulated-dataset-having-a-change-point.md) · [Up: contents](index.md) · [Plotting the fitted values →](04-plotting-the-fitted-values.md)
