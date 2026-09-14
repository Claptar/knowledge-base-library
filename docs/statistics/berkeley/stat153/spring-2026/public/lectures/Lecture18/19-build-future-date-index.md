---
title: Build future date index
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Build future date index

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

last_date = gas.index[-1]
future_dates = pd.date_range(last_date, periods=n_ahead + 1, freq='W')[1:]

---

[← Cumulative sum of log returns -> multiply by last observed price](18-cumulative-sum-of-log-returns---multiply-by-last-observed-pr.md) · [Up: contents](index.md) · [Plot →](20-plot.md)
