---
title: Fit OLS
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit OLS

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

beta, SSE, rank, s = np.linalg.lstsq(xtraind_int, ytrain, rcond=None)
```

## Cross validation performance

Let's look at performance on held out data by computing predictions from our fitted `beta` values on our new `xtestd` and compare these predictions to the true held out data `ytest`.

```python

---

[← OLS](14-ols.md) · [Up: contents](index.md) · [Let's look at performance on predicted versus actual data →](16-let-s-look-at-performance-on-predicted-versus-actual-data.md)
