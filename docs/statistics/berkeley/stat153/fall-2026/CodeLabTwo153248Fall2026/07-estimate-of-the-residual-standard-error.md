---
title: 'Estimate of $\sigma$: the residual standard error'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimate of $\sigma$: the residual standard error

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The estimate of $\sigma$ is given by:
\begin{equation*}
   \hat{\sigma} = \sqrt{\frac{RSS}{n-4}} = \sqrt{\frac{S(\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3)}{n-4}}
\end{equation*}
This quantity is sometimes called the Residual Standard Error. The value of the Residual Standard Error can be used to assess the size of the residuals (residuals much larger than say twice the Residual Standard Error indicate points where the model fits particularly poorly).

```python
rss = np.sum(md.resid ** 2)
rse = np.sqrt(rss/(n - 4))
print(rse)
```

```
550.9932711741245
```

This intuitively means that residuals with magnitude above 1100 are points where the model fits particularly poorly. From a look at the plot of the residuals against time, there are many residuals which are this large in magnitude.

---

[← Residual Sum of Squares (RSS) and Residual df](06-residual-sum-of-squares-rss-and-residual-df.md) · [Up: contents](index.md) · [Standard Errors of the coefficient estimates →](08-standard-errors-of-the-coefficient-estimates.md)
