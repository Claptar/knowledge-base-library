---
title: Below we fit these models to the original data without any differencing or
  logging.
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Below we fit these models to the original data without any differencing or logging.

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

md_autoreg_y = AutoReg(y, lags = 1).fit()
print(md_autoreg_y.params[1])

---

[← CodeLabEleven153248Fall2025 Part 04 —](04-codelabeleven153248fall2025-part-04.md) · [Up: contents](index.md) · [AutoReg's estimate of phi1 is slightly more than 1 →](06-autoreg-s-estimate-of-phi1-is-slightly-more-than-1.md)
