---
title: Find peaks
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFifteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureFifteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks, _ = find_peaks(np.log(power_ridge))
print("Peaks:", peaks)
print(freq[peaks])
print(1/freq[peaks])
```

```
Peaks: [ 27 140 248 266 358 458 484 577]
[0.0222046  0.11181602 0.19746233 0.21173672 0.28469469 0.36399683
 0.38461538 0.45836638]
[45.03571429  8.94326241  5.06425703  4.72284644  3.51253482  2.74727669
  2.6         2.1816609 ]
```

Economists use this as evidence for existence of a business cycle with period around 45 months (which is close to 4 years). See Section 6.4 for the Hamilton book on time series for more on this example.

---

[← Find peaks](03-find-peaks.md) · [Up: contents](index.md)
