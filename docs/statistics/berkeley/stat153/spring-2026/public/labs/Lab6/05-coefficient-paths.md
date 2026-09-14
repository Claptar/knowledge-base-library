---
title: Coefficient paths
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Coefficient paths

**Source:** [`public/labs/Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Another point we briefly touched on is that you can look at the beta estimates as a function of your regularization parameter. Here we can refit our coefficients in a loop, then plot the coefficients vs. the alpha values to observe how greater values of alpha more strongly shrink the coefficients.

```python
coef_matrix = np.zeros((len(alphas), X[:, 1:].shape[1]))

for i, a in enumerate(alphas):
    coef_matrix[i] = Ridge(alpha=a, fit_intercept=True).fit(X[:, 1:], y).coef_
```

```python
plt.semilogx(alphas,coef_matrix);
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
```

---

[← Lab6 Part 04 —](04-lab6-part-04.md) · [Up: contents](index.md) · [How ridge regularization affects predictions →](06-how-ridge-regularization-affects-predictions.md)
