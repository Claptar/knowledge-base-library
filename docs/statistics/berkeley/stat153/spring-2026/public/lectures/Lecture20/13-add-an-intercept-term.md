---
title: add an intercept term
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# add an intercept term

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

xtraind_int = np.hstack((np.ones((xtraind.shape[0],1)), xtraind))
xtestd_int = np.hstack((np.ones((xtestd.shape[0],1)), xtestd))
```

---

[← Show covariance matrix](12-show-covariance-matrix.md) · [Up: contents](index.md) · [OLS →](14-ols.md)
