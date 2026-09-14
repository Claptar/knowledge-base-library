---
title: Split the data using the last 3 years as the test set (data are in weeks)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Split the data using the last 3 years as the test set (data are in weeks)

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

t = 3    #*52

y_train = log_change[:-t]
y_test = log_change[-t:]

print(f"Train: {len(y_train)} obs, Test: {len(y_test)} obs")

models_to_test = {
    'AR(1)':     (1, 0, 0),
    'AR(2)':     (2, 0, 0),
    'AR(3)':     (3, 0, 0),
    'AR(4)':     (4, 0, 0),
    'ARMA(1,1)': (1, 0, 1),
    'ARMA(2,1)': (2, 0, 1),
    'ARMA(3,1)': (3, 0, 1),
}

results = {}
for name, order in models_to_test.items():
    model = ARIMA(y_train, order=order).fit()
    forecasts = model.forecast(steps=len(y_test))
    errors = y_test - forecasts
    results[name] = {
        'rmse': np.sqrt(np.mean(errors**2)),
        'mae': np.mean(np.abs(errors)),
        'forecasts': forecasts,
        'errors': errors,
    }
    print(f"{name:<12} RMSE={results[name]['rmse']:.5f}")
```

```
Train: 1849 obs, Test: 3 obs
AR(1)        RMSE=0.02041
AR(2)        RMSE=0.02074
AR(3)        RMSE=0.02322
AR(4)        RMSE=0.02445
ARMA(1,1)    RMSE=0.02099
ARMA(2,1)    RMSE=0.02565
ARMA(3,1)    RMSE=0.02379
```

## Discussion

Let's look at the RMSE results. Discuss:

1. Does adding more AR lags keep helping?
2. How does ARMA(1,1) compare to the pure AR models?
3. **Conceptually**: why might gas prices have *both* AR and MA structure?

---

[← Now try ARMA(1,1) — one AR + one MA coefficient](12-now-try-arma-1-1-one-ar-one-ma-coefficient.md) · [Up: contents](index.md) · [Let's look at forecasting results →](14-let-s-look-at-forecasting-results.md)
