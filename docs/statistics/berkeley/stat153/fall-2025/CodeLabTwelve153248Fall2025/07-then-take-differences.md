---
title: Then take differences
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Then take differences

**Source:** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ylogdiff = np.diff(ylog)
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the sample acf and pacf plots for this data, it is clear that MA(1) is appropriate.

```python
L = 60

---

[← First take logarithms](06-first-take-logarithms.md) · [Up: contents](index.md) · [Plot sample ACF/PACF →](08-plot-sample-acf-pacf.md)
