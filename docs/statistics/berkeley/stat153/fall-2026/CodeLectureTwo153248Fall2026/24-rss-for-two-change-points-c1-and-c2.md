---
title: RSS for two change points c1 and c2
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# RSS for two change points c1 and c2

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def rss(c1, c2):

    X = np.column_stack([
        np.ones(n_g),
        t,
        np.maximum(t - c1, 0),
        np.maximum(t - c2, 0)
    ])

    beta_hat = np.linalg.lstsq(X, g, rcond=None)[0]
    residuals = g - X @ beta_hat

    return np.sum(residuals ** 2)

---

[← Dates corresponding to the growth rates](23-dates-corresponding-to-the-growth-rates.md) · [Up: contents](index.md) · [Possible change points →](25-possible-change-points.md)
