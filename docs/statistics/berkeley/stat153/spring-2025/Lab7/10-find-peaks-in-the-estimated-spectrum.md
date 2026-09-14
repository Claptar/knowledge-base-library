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
Peak frequencies: [0.02515723 0.08097484 0.10691824 0.1658805  0.24921384 0.28459119
 0.33254717 0.4158805  0.46069182]
Peak periods: [39.75       12.34951456  9.35294118  6.02843602  4.0126183   3.51381215
  3.0070922   2.40453686  2.17064846]
Gaps between peaks: [ 71  33  75 106  45  61 106  57]
```

```python

---

[← Plotting the tauj estimates (estimated spectrum)](09-plotting-the-tauj-estimates-estimated-spectrum.md) · [Up: contents](index.md) · [Find peaks in the estimated spectrum →](11-find-peaks-in-the-estimated-spectrum.md)
