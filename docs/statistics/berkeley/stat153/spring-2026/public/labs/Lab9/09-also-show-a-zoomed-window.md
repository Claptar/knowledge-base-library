---
title: Also show a zoomed window
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Also show a zoomed window

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

window = slice(700, 900)
axes[1].plot(np.arange(700, 900), hrv_data[window], 'o-', markersize=3, linewidth=0.8)
axes[1].set(xlabel='Beat number', ylabel='RR interval (ms)',
            title='Zoomed: beats 700-900')

plt.tight_layout()
plt.show()
```

### Predict (discussion)

Let's think about the structure of this time series. Discuss with a partner:

1. **Look at the zoomed plot.** Do you see features that look like slow drifts (AR) *and* sudden jumps (MA)?
2. **Predict the ACF shape.** Will it look like sunspots (oscillatory decay)? Gas prices (monotone decay)? Something else?
3. **Predict the PACF.** Will it cut off cleanly?

```python

---

[← Detect R-peaks](08-detect-r-peaks.md) · [Up: contents](index.md) · [Demean for stationarity →](10-demean-for-stationarity.md)
