---
title: Hold out the last 25 observations for testing
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Hold out the last 25 observations for testing

**Source:** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n_test = 50
X_train, X_test = X_all[:-n_test], X_all[-n_test:]
y_train, y_test = y[:-n_test], y[-n_test:]

---

[← Build design matrix for ALL times (intercept + cos/sin for each f), vectorized](07-build-design-matrix-for-all-times-intercept-cos-sin-for-each.md) · [Up: contents](index.md) · [Fit on train only →](09-fit-on-train-only.md)
