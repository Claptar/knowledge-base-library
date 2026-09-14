---
title: Oracle Predictions
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Oracle Predictions

**Source:** [`Lab14.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n_future = 1000
y_extended = np.concatenate([y_sim, np.empty(n_future, dtype=float)])
for t in range(n, n+n_future):
    y_extended[t] = 0.9 * np.sin(0.5 * np.pi * y_extended[t - truelag])
oracle_preds = y_extended[n:]

n = len(y_sim)
tme = range(1, n+1)
tme_future = range(n+1, n+n_future+1)

plt.figure(figsize = (12, 6))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, oracle_preds, label = 'Forecast (Oracle)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us now fit AR(p) to this data. Even if $p$ is taken to be the correct value, this model will not work well (because the actual function which generated the data is nonlinear).

```python

---

[← LSTM Neural Network Models](01-lstm-neural-network-models.md) · [Up: contents](index.md) · [Let us fit AR(p) →](03-let-us-fit-ar-p.md)
