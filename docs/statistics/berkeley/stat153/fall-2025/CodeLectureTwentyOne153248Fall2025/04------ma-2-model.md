---
title: '---- MA(2) model ----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- MA(2) model ----

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ar2 = np.array([1])
ma2 = np.array([1, 0.1893, 0.2232])
sigma2_ma = 1.4628

acov_ma2 = arma_acovf(ar=ar2, ma=ma2, sigma2=sigma2_ma, nobs=20)

---

[← ---- AR(2) model ----](03------ar-2-model.md) · [Up: contents](index.md) · [---- Plot both ---- →](05------plot-both.md)
