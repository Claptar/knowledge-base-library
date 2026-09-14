---
title: Convert predicted growth rates to population
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Convert predicted growth rates to population

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

logy_future = ylog.iloc[-1] + np.cumsum(g_future)
y_future = np.exp(logy_future)

---

[← Predicted future growth rates](32-predicted-future-growth-rates.md) · [Up: contents](index.md) · [CodeLectureTwo153248Fall2026 Part 34 — →](34-codelecturetwo153248fall2026-part-34.md)
