---
title: Plotting the fitted values
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plotting the fitted values

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(y)
plt.plot(md.fittedvalues, color = 'red')
```

```
[<matplotlib.lines.Line2D at 0x16b4151d0>]
```

*(1 figure omitted — see the original notebook.)*

The Bayesian posterior for $c$ is:
\begin{equation*}
 |X_c^T X_c|^{-1/2} \left(\frac{1}{RSS(c)} \right)^{(n-p)/2}
\end{equation*}
where $p = 2$ and $|X_c^T X_c|$ denotes the determinant of $X_c^T X_c$.

As before, it is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
def logpost(c):
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])
    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X))
    # sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant

    logval = ((p - n) / 2) * np.log(rss) - 0.5 * log_det

    return logval
```

```python
allcvals = np.arange(1, n)
logpostvals = np.array([logpost(c) for c in allcvals])

plt.plot(allcvals, logpostvals)
plt.xlabel('Changepoint')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()

---

[← Estimates of other parameters](03-estimates-of-other-parameters.md) · [Up: contents](index.md) · [this plot looks similar to the RSS plot →](05-this-plot-looks-similar-to-the-rss-plot.md)
