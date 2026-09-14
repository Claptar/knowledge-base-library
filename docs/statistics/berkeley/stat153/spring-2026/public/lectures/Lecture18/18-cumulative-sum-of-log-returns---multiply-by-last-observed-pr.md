---
title: Cumulative sum of log returns -> multiply by last observed price
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Cumulative sum of log returns -> multiply by last observed price

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

future_prices = last_price * np.exp(np.cumsum(forecast_mean))
ci_lower = last_price * np.exp(np.cumsum(forecast_ci[:, 0]))
ci_upper = last_price * np.exp(np.cumsum(forecast_ci[:, 1]))

---

[← Convert log returns back to prices](17-convert-log-returns-back-to-prices.md) · [Up: contents](index.md) · [Build future date index →](19-build-future-date-index.md)
