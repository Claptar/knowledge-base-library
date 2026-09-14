---
title: '---- 2. Train/test split ----'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- 2. Train/test split ----

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

h = 20 # 5 years of data

y_train = y_gdp[:-h] # take up to the last five years
y_test = y_gdp[-h:]  # predict last five years
dates_train = gdp.index[:-h]
dates_test = gdp.index[-h:]

---

[← Fitting the model](05-fitting-the-model.md) · [Up: contents](index.md) · [---- 3. Model grid ---- →](07------3-model-grid.md)
