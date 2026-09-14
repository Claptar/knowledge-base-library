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

peaks_lasso, _ = find_peaks(tau_opt_lasso)
peak_lasso_freqs = peaks_lasso / n
gaps_lasso = np.diff(peaks_lasso)

print("Peak frequencies:", peak_lasso_freqs)
print("Peak periods:", 1 / peak_lasso_freqs)
print("Gaps between peaks:", gaps_lasso)
```

```
Peak frequencies: [0.02379064 0.10705789 0.19666931 0.28310864 0.36082474 0.45440127]
Peak periods: [42.03333333  9.34074074  5.08467742  3.53221289  2.77142857  2.20069808]
Gaps between peaks: [105 113 109  98 118]
```

Please read Section 6.4 of the Hamilton book for more on the interpretation of these spectral estimates.

---

[← Find peaks in the estimated spectrum](20-find-peaks-in-the-estimated-spectrum.md) · [Up: contents](index.md)
