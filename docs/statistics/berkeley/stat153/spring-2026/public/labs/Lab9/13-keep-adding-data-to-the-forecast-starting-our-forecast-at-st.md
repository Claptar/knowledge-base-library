---
title: Keep adding data to the forecast, starting our forecast at startforecast
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Keep adding data to the forecast, starting our forecast at startforecast

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for idx, t in enumerate(np.arange(start_forecast,len(y_hrv))):
    y_train = y_hrv[:t]
    y_test = y_hrv[t]
    model = ARIMA(y_train, order=order).fit()
    forecasts = model.forecast(steps=1)
    all_forecast.append(forecasts)
    errors = y_test - forecasts
    results_rolling = {
        'rmse': np.sqrt(np.mean(errors**2)),
        'mae': np.mean(np.abs(errors)),
        'forecasts': forecasts,
        'errors': errors,
    }
    print(f"RMSE={results_rolling['rmse']:.5f}")
```

```python

---

[← Legend (one entry per type)](12-legend-one-entry-per-type.md) · [Up: contents](index.md) · [Plot the data and forecast →](14-plot-the-data-and-forecast.md)
