---
title: Best ARMA model overall
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyTwo153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Best ARMA model overall

**Source:** [`CodeLectureTwentyTwo153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

best_arma_aic = np.unravel_index(np.nanargmin(aicmat), aicmat.shape)
best_arma_bic = np.unravel_index(np.nanargmin(bicmat), bicmat.shape)

---

[← Best MA model (AR = 0)](03-best-ma-model-ar-0.md) · [Up: contents](index.md) · [Print results →](05-print-results.md)
