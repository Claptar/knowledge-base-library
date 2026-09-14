---
title: Plotting the tauj estimates (estimated spectrum)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plotting the tauj estimates (estimated spectrum)

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

tau_opt_lasso = np.exp(alpha_opt_lasso)

plt.figure(figsize = (12, 6))
plt.plot(freq, tau_opt_lasso)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← This illustrates how the spectrum estimate can be viewed as a smoothing of the periodogram](18-this-illustrates-how-the-spectrum-estimate-can-be-viewed-as.md) · [Up: contents](index.md) · [Find peaks in the estimated spectrum →](20-find-peaks-in-the-estimated-spectrum.md)
