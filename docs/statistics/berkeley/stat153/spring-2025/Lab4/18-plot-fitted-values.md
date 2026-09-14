---
title: Plot fitted values
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot fitted values

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

X_linmod = np.column_stack([np.ones(n), x])
linmod = sm.OLS(y, X_linmod).fit()

plt.figure(figsize = (15, 6))

---

[← sig is the true value of sigma which generated the data](17-sig-is-the-true-value-of-sigma-which-generated-the-data.md) · [Up: contents](index.md) · [Plot this broken regression fitted values along with linear model fitted values →](19-plot-this-broken-regression-fitted-values-along-with-linear.md)
