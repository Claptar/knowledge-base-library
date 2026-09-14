---
title: Residual diagnostics for AR(2)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Residual diagnostics for AR(2)

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

resid_ar2 = ar2_model.resid

fig, axes = plt.subplots(1, 3, figsize=(16, 4))

axes[0].plot(resid_ar2, linewidth=0.5)
axes[0].set(title='AR(2) Residuals', xlabel='Time')

plot_acf(resid_ar2, lags=30, ax=axes[1], title='ACF of Residuals')
plot_pacf(resid_ar2, lags=30, ax=axes[2], title='PACF of Residuals', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Results

AR(2) does a good job on sunspots. Two coefficients with complex roots produce damped oscillations that match the ~11-year solar cycle. The residuals are nearly white noise (though we haven't entirely removed the periodicity).

AR models are powerful when the current value depends on recent past values through a recursive/autoregressive relationship. As seen in this example, the ACF will decay gradually, while the PACF cuts off.

Not every time series has this clean structure, so let's look at a slightly more complex example.

## The AR model and Gas Prices

Gas prices are extremely topical right now. Between early and mid-March 2026, the national average for regular gasoline jumped significantly. Gas price data has relatively strong persistence, but also responds to **shocks** (conflict, policy changes) that create short-lived perturbations.

We'll use [data from FRED](https://fred.stlouisfed.org/series/GASREGW) (Federal Reserve Economic Data).

```python

---

[← Check the characteristic roots](06-check-the-characteristic-roots.md) · [Up: contents](index.md) · [US Regular All Formulations Gas Price →](08-us-regular-all-formulations-gas-price.md)
