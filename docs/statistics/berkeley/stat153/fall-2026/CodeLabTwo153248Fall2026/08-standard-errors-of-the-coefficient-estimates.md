---
title: Standard Errors of the coefficient estimates
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLabTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Standard Errors of the coefficient estimates

**Source:** [`CodeLabTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLabTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The standard errors corresponding to $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3$ are the square roots of the diagonal entries of $\hat{\sigma}^2 (X^T X)^{-1}$. They are given by md.bse as verified below.

```python
sebetahat_squared = (rse ** 2)*(np.diag(XTX_inverse))
sebetahat = np.sqrt(sebetahat_squared)
print(np.array([md.bse, sebetahat]))
```

```
[[1.26498064e+02 3.50560340e+00 2.60867093e-02 5.49661580e-05]
 [1.26498064e+02 3.50560340e+00 2.60867093e-02 5.49661580e-05]]
```

---

[← Estimate of $\sigma$: the residual standard error](07-estimate-of-the-residual-standard-error.md) · [Up: contents](index.md) · [t-statistic and confidence intervals for the coefficients →](09-t-statistic-and-confidence-intervals-for-the-coefficients.md)
