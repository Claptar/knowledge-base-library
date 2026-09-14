---
title: but is detached from the computation graph.
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# but is detached from the computation graph.

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (12, 6))
plt.plot(x_raw, y_raw, color = 'blue', label = 'Data')
plt.plot(x_raw, nn_fits_1, color = 'red', label = 'PyTorch Fitted Values')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now we shall scale the covariates $x_t$ and $y_t$, and then run the same algorithm again.

```python
y_scaled = (y_raw - np.mean(y_raw)) / (np.std(y_raw))
x_scaled = (x_raw - np.mean(x_raw)) / (np.std(x_raw))

y_torch = torch.tensor(y_scaled, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

```python

---

[← CodeLabThirteen153248Fall2025 Part 10 —](10-codelabthirteen153248fall2025-part-10.md) · [Up: contents](index.md) · [First fix the number of knots →](12-first-fix-the-number-of-knots.md)
