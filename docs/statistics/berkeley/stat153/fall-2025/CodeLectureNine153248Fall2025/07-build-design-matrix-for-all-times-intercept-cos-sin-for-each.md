---
title: Build design matrix for ALL times (intercept + cos/sin for each f), vectorized
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Build design matrix for ALL times (intercept + cos/sin for each f), vectorized

**Source:** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

cos_cols = np.cos(2*np.pi*np.outer(x, f))   # shape (n, k)
sin_cols = np.sin(2*np.pi*np.outer(x, f))   # shape (n, k)
X_all = np.column_stack([np.ones(n), cos_cols, sin_cols])

---

[← time index 1..n](06-time-index-1-n.md) · [Up: contents](index.md) · [Hold out the last 25 observations for testing →](08-hold-out-the-last-25-observations-for-testing.md)
