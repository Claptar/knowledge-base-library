---
title: RSS for a given change point c
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# RSS for a given change point c

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def rss(c):
    X = np.column_stack([
        np.ones(len(g)),
        t,
        np.maximum(t - c, 0)
    ])

    model = sm.OLS(g, X).fit()
    return np.sum(model.resid ** 2)

---

[← Monthly log growth rates](17-monthly-log-growth-rates.md) · [Up: contents](index.md) · [Try all possible change points →](19-try-all-possible-change-points.md)
