---
title: Detect R-peaks
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Detect R-peaks

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

from scipy.signal import find_peaks

peaks, _ = find_peaks(ecg, distance=int(0.5*128), height=0.5)
rr_intervals = np.diff(peaks) / 128.0 * 1000  # in ms
hrv_data = rr_intervals
data_source = "PhysioNet MIT-BIH Normal Sinus Rhythm DB (record 16265)"

print(f"Data source: {data_source}")
print(f"Number of RR intervals: {len(hrv_data)}")
print(f"Mean RR: {np.mean(hrv_data):.1f} ms ({60000/np.mean(hrv_data):.0f} bpm)")
print(f"SDNN: {np.std(hrv_data):.1f} ms")

fig, axes = plt.subplots(2, 1, figsize=(14, 6))

axes[0].plot(hrv_data, linewidth=0.6)
axes[0].set(xlabel='Beat number', ylabel='RR interval (ms)',
            title='RR Interval Time Series (Heart Rate Variability)')

---

[← is the first upward deflection in the ECG time series.)](07-is-the-first-upward-deflection-in-the-ecg-time-series.md) · [Up: contents](index.md) · [Also show a zoomed window →](09-also-show-a-zoomed-window.md)
