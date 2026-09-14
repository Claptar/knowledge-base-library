---
title: Test specific alpha parameters
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Test specific alpha parameters

**Source:** [`public/labs/Lab6_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now let's look at how the range of regularization parameters affects our predictions. What is the scale of the alpha values that work here compared to ridge regression?

```python
for alpha in [0.1, 1, 5]:
    model = Lasso(alpha=alpha).fit(X, y)
    y_hat_lasso = model.predict(X)
    plt.plot(t, y_hat_lasso, label=f'λ={alpha}')

plt.legend()
```

```
<matplotlib.legend.Legend at 0x32fed37c0>
```

*(1 figure omitted — see the original notebook.)*

---

[← Compare to the Lasso model](07-compare-to-the-lasso-model.md) · [Up: contents](index.md)
