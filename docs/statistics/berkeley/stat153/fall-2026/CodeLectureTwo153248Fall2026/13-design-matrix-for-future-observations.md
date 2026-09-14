---
title: Design matrix for future observations
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Design matrix for future observations

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

X_future = np.column_stack([
    np.ones(r),
    x_future,
    x_future ** 2
])

---

[← Future time points: n+1, ..., n+168](12-future-time-points-n-1-n-168.md) · [Up: contents](index.md) · [Fitted and predicted values on the log scale →](14-fitted-and-predicted-values-on-the-log-scale.md)
