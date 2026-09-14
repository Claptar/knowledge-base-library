---
title: Calculate covariance matrix for training data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Calculate covariance matrix for training data

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

dtype = np.single
covmat = np.array(np.dot(xtraind.astype(dtype).T, xtraind.astype(dtype)))
```

```python

---

[← Create the delayed matrices](10-create-the-delayed-matrices.md) · [Up: contents](index.md) · [Show covariance matrix →](12-show-covariance-matrix.md)
