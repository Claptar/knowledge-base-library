---
title: Now try ARMA(1,1) — one AR + one MA coefficient
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Now try ARMA(1,1) — one AR + one MA coefficient

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

arma11 = ARIMA(log_change, order=(1, 0, 1)).fit()
resid_arma = arma11.resid

fig, axes = plt.subplots(1, 2, figsize=(14, 4))
axes[0].plot(resid_arma, linewidth=0.5, alpha=0.8)
axes[0].set(title=f'ARMA(1,1) Residuals')

plot_acf(resid_arma, lags=25, ax=axes[1], title='ACF of ARMA(1,1) Residuals')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Using the models for forecasting

To look at performance of the models, we could use techniques like AIC/BIC, or we can go back to using them more general method of cross-validation. Here we will use a very simple train/test split, though you can also try methods like rolling cross-validation (where your training set grows for each fold, or using a fixed-width sliding window).

```python

---

[← Fit MA(1), MA(2), MA(4) and compare](11-fit-ma-1-ma-2-ma-4-and-compare.md) · [Up: contents](index.md) · [Split the data using the last 3 years as the test set (data are in weeks) →](13-split-the-data-using-the-last-3-years-as-the-test-set-data-a.md)
