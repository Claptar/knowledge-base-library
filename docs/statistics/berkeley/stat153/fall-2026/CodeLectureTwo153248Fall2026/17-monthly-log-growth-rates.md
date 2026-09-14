---
title: Monthly log growth rates
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Monthly log growth rates

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

g = ylog.diff().dropna()

t = np.arange(1, len(g) + 1)

---

[← Plot observed data, fitted values, and future predictions](16-plot-observed-data-fitted-values-and-future-predictions.md) · [Up: contents](index.md) · [RSS for a given change point c →](18-rss-for-a-given-change-point-c.md)
