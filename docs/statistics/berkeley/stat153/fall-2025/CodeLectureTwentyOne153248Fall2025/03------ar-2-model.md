---
title: '---- AR(2) model ----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- AR(2) model ----

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ar = np.array([1, -0.21, -0.2010])   # AR polynomial
ma = np.array([1])                   # no MA terms
sigma2 = 1.207**2

acov_ar2 = arma_acovf(ar=ar, ma=ma, sigma2=sigma2, nobs=20)

---

[← Plot the simulated series](02-plot-the-simulated-series.md) · [Up: contents](index.md) · [---- MA(2) model ---- →](04------ma-2-model.md)
