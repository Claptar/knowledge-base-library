---
title: This illustrates how the spectrum estimate can be viewed as a smoothing of
  the periodogram
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# This illustrates how the spectrum estimate can be viewed as a smoothing of the periodogram

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram))
plt.plot(freq, np.log(n / 2) + 2 * alpha_opt_ridge)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Below we plot the log(periodogram) and the fitted spectrum estimator on the same plot](13-below-we-plot-the-log-periodogram-and-the-fitted-spectrum-es.md) · [Up: contents](index.md) · [Plotting the tauj estimates (estimated spectrum) →](15-plotting-the-tauj-estimates-estimated-spectrum.md)
