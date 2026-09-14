---
title: Lab4 Part 11 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab4 Part 11 —

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

b0_est = md.params[0]
b1_est = md.params[1]

b0_true = mu1
b1_true = mu2 - mu1
print(np.column_stack((np.array([b0_est, b1_est]), np.array([b0_true, b1_true]))))

rss_chat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_chat / n)
sigma_unbiased = np.sqrt((rss_chat)/(n - 2))
print(np.array([sigma_mle, sigma_unbiased, sig]))
#sig is the true value of sigma which generated the data
```

```
[0.01969268 0.40873694]
[[0.01969268 0.        ]
 [0.40873694 0.4       ]]
[1.00274789 1.00284818 1.        ]
```

Bayesian uncertainty quantification also works exactly as before.  The Bayesian posterior for $c$ is:
\begin{equation*}
 |X_c^T X_c|^{-1/2} \cdot \left(\frac{1}{RSS(c)} \right)^{(n-p)/2}
\end{equation*}
where $p = 2$ and $|X_c^T X_c|$ denotes the determinant of $X_c^T X_c$.

As before, it is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python

---

[← Estimates of other parameters](10-estimates-of-other-parameters.md) · [Up: contents](index.md) · [Plot the fitted values →](12-plot-the-fitted-values.md)
