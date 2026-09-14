---
title: Show covariance matrix
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Show covariance matrix

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(5,5))
plt.imshow(covmat[:80,:80], cmap=cm.Reds)
plt.colorbar()
```

```
<matplotlib.colorbar.Colorbar at 0x12db9a350>
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Calculate covariance matrix for training data](11-calculate-covariance-matrix-for-training-data.md) · [Up: contents](index.md) · [add an intercept term →](13-add-an-intercept-term.md)
