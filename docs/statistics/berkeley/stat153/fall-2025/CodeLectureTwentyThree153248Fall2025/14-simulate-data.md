---
title: Simulate data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulate data

**Source:** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
dt = arma_process.generate_sample(nsample=400)

---

[← Plot sample ACF/PACF](13-plot-sample-acf-pacf.md) · [Up: contents](index.md) · [Plot simulated series →](15-plot-simulated-series.md)
