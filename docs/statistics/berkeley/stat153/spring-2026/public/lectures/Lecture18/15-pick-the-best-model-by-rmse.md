---
title: Pick the best model by RMSE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Pick the best model by RMSE

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

best_name = min(results, key=lambda n: results[n]['rmse'])
best_order = models_to_test[best_name]
print(f"Best model: {best_name}")

---

[← Let's look at forecasting results](14-let-s-look-at-forecasting-results.md) · [Up: contents](index.md) · [Refit on ALL data, then forecast into the future →](16-refit-on-all-data-then-forecast-into-the-future.md)
