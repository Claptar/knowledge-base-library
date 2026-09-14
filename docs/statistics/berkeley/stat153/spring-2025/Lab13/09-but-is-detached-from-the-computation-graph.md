---
title: but is detached from the computation graph.
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# but is detached from the computation graph.

**Source:** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (12, 6))
plt.plot(x_raw, y_raw, color = 'blue', label = 'Data')
plt.plot(x_raw, nn_fits, color = 'red', label = 'PyTorch Fitted Values')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now we shall scale the covariates $x_t$ and $y_t$, and then run the same algorithm again.

```python
y_scaled = (y_raw - np.mean(y_raw)) / (np.std(y_raw))
x_scaled = (x_raw - np.mean(x_raw)) / (np.std(x_raw))

y_torch = torch.tensor(y_scaled, dtype=torch.float32)
x_torch = torch.tensor(x_scaled, dtype=torch.float32)
```

```python

---

[← Lab13 Part 08 —](08-lab13-part-08.md) · [Up: contents](index.md) · [First fix the number of knots →](10-first-fix-the-number-of-knots.md)
