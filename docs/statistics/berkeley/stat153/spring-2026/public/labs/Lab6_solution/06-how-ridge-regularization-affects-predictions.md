---
title: How ridge regularization affects predictions
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# How ridge regularization affects predictions

**Source:** [`public/labs/Lab6_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We have observed how changing our regularization parameter affects the parameters, but what about the predictions themselves? Here we will plot the estimates from ridge on top of the original data. What do you notice?

Also try some other values of alpha (or go back and change your X parameters to add fewer or more frequencies in the grid search).

```python
for alpha in [0.1, 100, 1000]:
    model = Ridge(alpha=alpha).fit(X, y)
    y_hat_ridge = model.predict(X)
    plt.plot(t, y_hat_ridge, label=f'λ={alpha}')

plt.legend()
```

```
<matplotlib.legend.Legend at 0x332065150>
```

*(1 figure omitted — see the original notebook.)*

---

[← Coefficient paths](05-coefficient-paths.md) · [Up: contents](index.md) · [Compare to the Lasso model →](07-compare-to-the-lasso-model.md)
