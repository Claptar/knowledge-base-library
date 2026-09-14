---
title: Let's look at forecasting results
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's look at forecasting results

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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
    ax.set(ylabel='Log return', title=f'{name}  |  RMSE={res["rmse"]:.5f}')
    ax.legend(loc='upper left')

axes[-1].set(xlabel='Time index')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Split the data using the last 3 years as the test set (data are in weeks)](13-split-the-data-using-the-last-3-years-as-the-test-set-data-a.md) · [Up: contents](index.md) · [Pick the best model by RMSE →](15-pick-the-best-model-by-rmse.md)
