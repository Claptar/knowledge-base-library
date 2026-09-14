---
title: Truncate to pre-COVID
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Truncate to pre-COVID

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

mask = gdp.index <= '2019-12-31'
y_pre = y_gdp[mask]
dates_pre = gdp.index[mask]

h = 20
y_train = y_pre[:-h]
y_test = y_pre[-h:]
dates_train = dates_pre[:-h]
dates_test = dates_pre[-h:]

---

[← ---- 2. Train/test split ----](11------2-train-test-split.md) · [Up: contents](index.md) · [---- 3. Model grid ---- →](13------3-model-grid.md)
