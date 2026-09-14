---
title: Find peaks in the estimated spectrum
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks in the estimated spectrum

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks_ridge, _ = find_peaks(tau_opt_ridge)
peak_ridge_freqs = peaks_ridge / n
gaps_ridge = np.diff(peaks_ridge)

print("Peak frequencies:", peak_ridge_freqs)
print("Peak periods:", 1 / peak_ridge_freqs)
print("Gaps between peaks:", gaps_ridge)
```

```
Peak frequencies: [0.02141158 0.111023   0.19666931 0.2109437  0.28390167 0.36320381
 0.38382236 0.45757335]
Peak periods: [46.7037037   9.00714286  5.08467742  4.7406015   3.52234637  2.75327511
  2.6053719   2.18544194]
Gaps between peaks: [113 108  18  92 100  26  93]
```

Now the main peak is for the business cycle which corresponds to a period of close to 4 years. The other peaks are much smaller.

```python

---

[← Plotting the tauj estimates (estimated spectrum)](19-plotting-the-tauj-estimates-estimated-spectrum.md) · [Up: contents](index.md) · [Find peaks in the estimated spectrum →](21-find-peaks-in-the-estimated-spectrum.md)
