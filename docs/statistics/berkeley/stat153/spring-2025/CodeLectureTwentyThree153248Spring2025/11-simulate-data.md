---
title: Simulate data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulate data

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
dt = arma_process.generate_sample(nsample=400)

---

[← Plot sample ACF/PACF](10-plot-sample-acf-pacf.md) · [Up: contents](index.md) · [Plot simulated series →](12-plot-simulated-series.md)
