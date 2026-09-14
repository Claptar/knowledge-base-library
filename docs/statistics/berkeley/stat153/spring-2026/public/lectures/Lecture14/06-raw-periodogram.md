---
title: Raw periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Raw periodogram

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

freqs_raw, power_raw = periodogram(wn, fs=1)
axes[0].plot(freqs_raw, power_raw, color='steelblue', lw=0.3, alpha=0.7)
axes[0].axhline(2 * sigma2, color='r', lw=2)
axes[0].set_title(f'Raw periodogram\n(1 segment of {n})', fontsize=10)
axes[0].set_ylabel('Power')
axes[0].set_xlabel('Frequency')
axes[0].set_ylim([0, 12])

---

[← (c) Daniell-smoothed periodogram from single realization](05-c-daniell-smoothed-periodogram-from-single-realization.md) · [Up: contents](index.md) · [Welch with decreasing segment sizes →](07-welch-with-decreasing-segment-sizes.md)
