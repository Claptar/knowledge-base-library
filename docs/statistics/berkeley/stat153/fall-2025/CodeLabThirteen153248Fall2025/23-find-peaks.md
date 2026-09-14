---
title: Find peaks
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks, _ = find_peaks(np.log(power_lasso))
#find troughs
troughs, _ = find_peaks(-np.log(power_lasso))
print(peaks)
print(troughs)
```

```
[ 55 176 284]
[118 229]
```

```python
k = 8 # this is the number of knots
#quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
x = np.arange(1, m+1)
x_scaled = (x - np.mean(x))/(np.std(x))
#knots_init = np.quantile(x_scaled, quantile_levels)

knots_init = (np.array([50, 120, 175, 230, 285, 340, 400, 500]) - np.mean(x))/(np.std(x))

---

[← Run this code a few times to be sure of convergence.](22-run-this-code-a-few-times-to-be-sure-of-convergence.md) · [Up: contents](index.md) · [these knots are chosen to be roughly near the peaks and troughs →](24-these-knots-are-chosen-to-be-roughly-near-the-peaks-and-trou.md)
