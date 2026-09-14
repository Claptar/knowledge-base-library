---
title: Forecast
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Forecast

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure()
context = 40 # Quarters to look back in the past (zooming in)
plt.plot(dates_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(dates_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (2, 0, 0): ('AR(2)', 'C0'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C3'),
    (1, 2, 1): ('ARIMA(1,2,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(dates_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(dates_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(dates_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

## Changes in linear trends

Here our data includes the COVID-19 pandemic years in the training set, where there were strong changes to the linear trend in GDP that can't be captured by first order differencing. What if we restrict our time points to pre-COVID?

```python

---

[← RMSE vs. complexity](09-rmse-vs-complexity.md) · [Up: contents](index.md) · [---- 2. Train/test split ---- →](11------2-train-test-split.md)
