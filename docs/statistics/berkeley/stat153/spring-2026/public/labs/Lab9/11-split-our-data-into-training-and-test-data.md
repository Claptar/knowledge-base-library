---
title: Split our data into training and test data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Split our data into training and test data

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_train = y_hrv[:-t]
y_test = y_hrv[-t:]

print(f"Train: {len(y_train)} obs, Test: {len(y_test)} obs")

models_to_test = {
    'AR(1)':     (1, 0, 0),
    'AR(2)':     (2, 0, 0),
    'AR(3)':     (3, 0, 0),
    'AR(4)':     (4, 0, 0),
    'MA(1)':     (0, 0, 1),
    'MA(2)':     (0, 0, 2),
    'MA(4)':     (0, 0, 4),
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

## Question:

* What do you notice about these models?
* Which is the best in terms of RMSE?
* Does this depend on your train/test split? Try different values of t and see what you find

```python
fig, axes = plt.subplots(len(results), 1, figsize=(14, 2 * len(results)), sharex=True)

split_point = len(y_train)

for ax, (name, res) in zip(axes, results.items()):
    # Training data
    ax.plot(np.arange(len(y_train)), y_train, 'k-', linewidth=0.4, alpha=0.5, label='Train')
    # Test actual
    ax.plot(np.arange(split_point, split_point + len(y_test)), y_test, 'k-', linewidth=0.8, label='Actual')
    # Forecast
    ax.plot(np.arange(split_point, split_point + len(y_test)), res['forecasts'], 'r--', linewidth=1.2, label=f'{name} forecast')
    # Split line
    ax.axvline(split_point, color='orange', linewidth=1.5, linestyle=':', label='Train/Test split')
    ax.set(ylabel='RR interval', title=f'{name}  |  RMSE={res["rmse"]:.5f}')
    ax.legend(loc='upper left')
    ax.set_xlim(600,1000)

axes[-1].set(xlabel='Time index')
plt.tight_layout()
plt.show()
```

## Model parameter counts

Now let's look at model performance as a function of number of parameters. What do you notice about the comparison between AR, MA, and ARMA models for the same number of parameters for this dataset?

```python
fig, ax = plt.subplots(figsize=(10, 5))

colors = {'AR': '#2196F3', 'MA': '#FF9800', 'ARMA': '#4CAF50'}

for name, res in results.items():
    # Determine model type and parameter count
    order = models_to_test[name]
    p, d, q = order
    nparams = p + q
    mtype = 'ARMA' if (p > 0 and q > 0) else ('AR' if p > 0 else 'MA')

    ax.scatter(nparams, res['rmse'], c=colors[mtype], s=100, zorder=3, edgecolors='white')
    ax.annotate(name, (nparams, res['rmse']), textcoords="offset points", xytext=(6, 6), fontsize=10)

---

[← Demean for stationarity](10-demean-for-stationarity.md) · [Up: contents](index.md) · [Legend (one entry per type) →](12-legend-one-entry-per-type.md)
