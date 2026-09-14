---
title: Plot this broken regression fitted values along with linear model fitted values
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot this broken regression fitted values along with linear model fitted values

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(y, color = 'None')
plt.plot(md.fittedvalues, color = 'red')
plt.plot(linmod.fittedvalues, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Plot fitted values](18-plot-fitted-values.md) · [Up: contents](index.md) · [Bayesian log posterior →](20-bayesian-log-posterior.md)
