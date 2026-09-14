---
title: Plot simulated series
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot simulated series

**Source:** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(10, 4))
plt.plot(dt, 'o-', markersize=4)
plt.title("Simulated Data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

---

[← Simulate data](14-simulate-data.md) · [Up: contents](index.md) · [Plot sample ACF/PACF →](16-plot-sample-acf-pacf.md)
