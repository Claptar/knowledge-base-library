---
title: CodeLectureTwo153248Fall2026 Part 31 —
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLectureTwo153248Fall2026 Part 31 —

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

r = 168

t_future = np.arange(n_g + 1, n_g + r + 1)

X7_future = np.column_stack([
    np.ones(r),
    t_future,
    np.maximum(t_future - c1_hat, 0),
    np.maximum(t_future - c2_hat, 0)
])

---

[← Predict the next 168 months](30-predict-the-next-168-months.md) · [Up: contents](index.md) · [Predicted future growth rates →](32-predicted-future-growth-rates.md)
