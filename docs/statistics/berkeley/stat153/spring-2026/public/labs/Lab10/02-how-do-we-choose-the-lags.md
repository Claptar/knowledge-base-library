---
title: How do we choose the lags?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# How do we choose the lags?

If we want to fit a lagged regression model, we first have to choose what lags we want to consider in our model. Usually, we do this based on prior knowledge about a particular brain area (say, if we know that most responses occur within 500 milliseconds, we probably don't need to search beyond that). However, we can also use the cross-correlation function to look at where our peak lead-lag relationships lie between $x$ and $y$. We'll do that here, using a maximum possible lag between the sound features and the neural recordings of 0.6 seconds, which is reasonable based on prior literature.

```python
from scipy.signal import correlate

stim_type = 'spec'  # Try changing this to 'phn' and see how the results compare

ntimes, nelecs = ytrain.shape
ntimes, nfeats = xtrain[stim_type].shape

max_lag_sec = 0.6 # seconds
max_lag = int(max_lag_sec * fs)

lags = np.arange(-max_lag, max_lag + 1)
ccf = np.zeros((nelecs, nfeats, len(lags)))

for e in range(nelecs):
    for f in range(nfeats):
        full = correlate(ytrain[:, e], xtrain[stim_type][:, f], mode='full') / ntimes
        mid = len(full) // 2
        ccf[e, f] = full[mid - max_lag : mid + max_lag + 1]
```

---

[← Lab 10](01-lab-10.md) · [Up: contents](index.md) · [Plotting lag relationships →](03-plotting-lag-relationships.md)
