---
title: Let us plot the posterior samples for c on the original plot
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let us plot the posterior samples for c on the original plot

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(y)

for i in range(N):
    plt.axvline(x = cpostsamples[i], color = 'gray')

plt.plot(y, color = 'blue')
plt.axvline(x = c_hat, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Drawing posterior samples](22-drawing-posterior-samples.md) · [Up: contents](index.md) · [Plot the fitted values for the different posterior draws →](24-plot-the-fitted-values-for-the-different-posterior-draws.md)
