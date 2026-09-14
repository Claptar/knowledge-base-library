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
plt.plot(times_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(times_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (0, 0, 1): ('MA(2)', 'C0'),
    (0, 1, 1): ('ARIMA(0,1,1)', 'C3'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(times_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(times_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(times_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

```python
p=0
d=1
q=1
fit = ARIMA(y_train, order=(p, d, q), trend=trend).fit()

fig = plt.figure(figsize=(10,6))
fit.plot_diagnostics(fig=fig);
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

---

[← RMSE vs. complexity](26-rmse-vs-complexity.md) · [Up: contents](index.md) · [Ljung-Box p-values →](28-ljung-box-p-values.md)
