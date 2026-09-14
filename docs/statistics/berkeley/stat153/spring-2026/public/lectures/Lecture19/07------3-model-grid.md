---
title: '---- 3. Model grid ----'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- 3. Model grid ----

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

specs = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0), # p, d, q - AR models
    (1, 0, 1), (2, 0, 1), (3, 0, 1), # ARMA models
    (1, 1, 0), (2, 1, 0), (3, 1, 0), # ARI (differencing, no MA)
    (1, 1, 1), (2, 1, 1), (3, 1, 1), # ARIMA d=1
    (1, 2, 1), (2, 2, 1), (3, 2, 1), # ARIMA d=2
]

---

[← ---- 2. Train/test split ----](06------2-train-test-split.md) · [Up: contents](index.md) · [---- 4. Fit, forecast, score ---- →](08------4-fit-forecast-score.md)
