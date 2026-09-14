---
title: Split line
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Split line

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ax.axvline(gas.index[-1], color='orange', linewidth=1.5, linestyle=':', label='Forecast start')

ax.set(xlabel='Date', ylabel='$ per gallon',
       title=f'Gas Price Forecast — {best_name} (next {n_ahead} weeks)')
ax.legend()
plt.tight_layout()
plt.show()

print(f"\nCurrent price: ${last_price:.2f}")
print(f"Forecast in {n_ahead} weeks: ${future_prices[-1]:.2f}")
print(f"95% CI: [${ci_lower[-1]:.2f}, ${ci_upper[-1]:.2f}]")
```

```
Best model: AR(1)

Current price: $3.99
Forecast in 26 weeks: $4.10
95% CI: [$1.53, $10.98]
```

*(1 figure omitted — see the original notebook.)*

```python
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(gas.index[-lookback:], y_gas[-lookback:], 'k-', linewidth=0.8, label='Observed')
ax.axvline(gas.index[-1], color='orange', linewidth=1.5, linestyle=':')

for name, order in models_to_test.items():
    m = ARIMA(log_change, order=order).fit()
    fc = m.get_forecast(steps=n_ahead).predicted_mean
    prices = last_price * np.exp(np.cumsum(fc))
    ax.plot(future_dates, prices, '--', linewidth=1.2, label=name)

ax.set(xlabel='Date', ylabel='$ per gallon', title='Gas Price Forecasts — All Models')
ax.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Summary

The gas price data has strong autoregressive persistence, but the residuals from pure AR models often retain some short-lag structure. Adding a single MA term can help in selecting a model with relatively fewer parameters compared to a larger AR model.

---

[← Forecast](22-forecast.md) · [Up: contents](index.md)
