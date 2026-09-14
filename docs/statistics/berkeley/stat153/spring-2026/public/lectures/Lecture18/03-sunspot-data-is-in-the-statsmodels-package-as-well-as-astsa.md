---
title: Sunspot data is in the statsmodels package (as well as astsa, but here we don't
  need it!)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspot data is in the statsmodels package (as well as astsa, but here we don't need it!)

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

import statsmodels.api as sm
sunspots = sm.datasets.sunspots.load_pandas().data
sunspots.columns = ['year', 'sunspots']
sunspots = sunspots.set_index('year')

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(sunspots.index, sunspots['sunspots'], linewidth=0.8)
ax.set(xlabel='Year', ylabel='Sunspot number', title='Yearly Sunspot Numbers (1700–2008)')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Predict (pair discussion, 2 min)

Before we look at the ACF and PACF:

1. **What kind of autocorrelation structure do you expect?** Slowly decaying? Oscillating? Sharp cutoff?
2. **If you had to guess: AR, MA, or ARMA?** Why?
3. **How many parameters do you think you'd need?**

Write down your predictions before running the next cell.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(sunspots['sunspots'].dropna(), lags=40, ax=axes[0], title='ACF — Sunspots')
plot_pacf(sunspots['sunspots'].dropna(), lags=40, ax=axes[1], title='PACF — Sunspots', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← statsmodels imports](02-statsmodels-imports.md) · [Up: contents](index.md) · [What do we see? →](04-what-do-we-see.md)
