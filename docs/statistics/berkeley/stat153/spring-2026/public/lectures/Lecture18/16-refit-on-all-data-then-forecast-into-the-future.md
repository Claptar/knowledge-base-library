---
title: Refit on ALL data, then forecast into the future
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Refit on ALL data, then forecast into the future

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

full_model = ARIMA(log_change, order=best_order).fit()

n_ahead = 26  # 26 weeks ~ 6 months
forecast_result = full_model.get_forecast(steps=n_ahead)
forecast_mean = forecast_result.predicted_mean
forecast_ci = forecast_result.conf_int(alpha=0.05)  # 95% CI

---

[← Pick the best model by RMSE](15-pick-the-best-model-by-rmse.md) · [Up: contents](index.md) · [Convert log returns back to prices →](17-convert-log-returns-back-to-prices.md)
