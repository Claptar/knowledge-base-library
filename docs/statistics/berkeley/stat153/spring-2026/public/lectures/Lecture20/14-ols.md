---
title: OLS
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# OLS

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's first look at fitting the model using OLS. Here we'll use numpy least squares for simplicity, though you can use any OLS solver.

```python
print(xtraind_int.shape)
print(ytrain.shape)
```

```
(161034, 3201)
(161034, 3)
```

```python

---

[← add an intercept term](13-add-an-intercept-term.md) · [Up: contents](index.md) · [Fit OLS →](15-fit-ols.md)
