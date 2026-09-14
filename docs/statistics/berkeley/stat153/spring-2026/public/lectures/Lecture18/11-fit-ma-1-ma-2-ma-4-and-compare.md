---
title: Fit MA(1), MA(2), MA(4) and compare
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit MA(1), MA(2), MA(4) and compare

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

orders = [1, 2, 4]
fig, axes = plt.subplots(len(orders), 2, figsize=(14, 3*len(orders)))

for i, q in enumerate(orders):
    model = ARIMA(log_change, order=(0, 0, q)).fit()
    resid = model.resid

    axes[i, 0].plot(resid, linewidth=0.5, alpha=0.8)
    axes[i, 0].set(title=f'MA({q}) Residuals')

    plot_acf(resid, lags=25, ax=axes[i, 1], title=f'ACF of MA({q}) Residuals')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## ARMA model

Now we'll try a combination of the AR and the MA models - a two parameter model.

```python

---

[← Fit AR(1), AR(2), AR(4) and compare](10-fit-ar-1-ar-2-ar-4-and-compare.md) · [Up: contents](index.md) · [Now try ARMA(1,1) — one AR + one MA coefficient →](12-now-try-arma-1-1-one-ar-one-ma-coefficient.md)
