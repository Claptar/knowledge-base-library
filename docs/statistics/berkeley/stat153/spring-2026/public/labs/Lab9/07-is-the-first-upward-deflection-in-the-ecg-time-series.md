---
title: is the first upward deflection in the ECG time series.)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# is the first upward deflection in the ECG time series.)

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

timepts = np.linspace(0,600,128*600)
plt.plot(timepts[1:1000], ecg[1:1000])
plt.xlabel('Time (s)')
```

Next we will detect R-peaks in this ECG waveform and find their intervals.

```python

---

[← the heart rate variability by finding peaks in the signal (the R wave - which](06-the-heart-rate-variability-by-finding-peaks-in-the-signal-th.md) · [Up: contents](index.md) · [Detect R-peaks →](08-detect-r-peaks.md)
