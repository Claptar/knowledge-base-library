---
title: 3a. Raw periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# 3a. Raw periodogram

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

f_raw, Pxx_raw = periodogram(y_dance, fs=sr)
axes[0].plot(f_raw, Pxx_raw, color='#e94560', linewidth=0.4, alpha=0.8)
axes[0].set_title('periodogram(y, fs=sr)')
axes[0].set_ylabel('Power')
axes[0].set_xlim(0, 4000)

---

[← scipy.signal.welch — average periodograms over overlapping segments](15-scipy-signal-welch-average-periodograms-over-overlapping-seg.md) · [Up: contents](index.md) · [3b. Welch with different segment lengths →](17-3b-welch-with-different-segment-lengths.md)
