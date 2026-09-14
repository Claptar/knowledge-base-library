---
title: note that the bound on phi1 ensures stationarity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# note that the bound on phi1 ensures stationarity

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

res = minimize(neg_loglik_ar1, init_pars, args=(ylogdiff,), bounds=bounds)
print("MLE estimates from custom optimization:")
print(np.column_stack([pars_autoreg, pars_arima, res.x]))
print(loglik_ar1(ylogdiff, pars_autoreg), loglik_ar1(ylogdiff, pars_arima), loglik_ar1(ylogdiff, res.x))

---

[← this is quarterly data](02-this-is-quarterly-data.md) · [Up: contents](index.md) · [CodeLabEleven153248Fall2025 Part 04 — →](04-codelabeleven153248fall2025-part-04.md)
