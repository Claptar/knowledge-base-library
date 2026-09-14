---
title: ETS models
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ETS models

**Source:** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

11. (8 pts)
Fit two ETS models, using `ETS()` from the `fable` package: Holt's linear trend
and damped linear trend. Each of these models should have additive errors, and
no seasonality. Implement time series CV to evaluate them, just as you did in
Q8; you should be appending the forecast from these ETS models to `fable_fc`.
Then, as in Q9, plot their MAE curves as a function of horizon, and overlay the
curves from all models considered thus far. Discuss what you find.

12. (Bonus)
Compute the coverage of 80\% prediction intervals from each of the ETS models,
per horizon, and plot alongside the coverage curves from all models considered
thus far.

---

[← ARIMA models](06-arima-models.md) · [Up: contents](index.md) · [Exogenous features →](08-exogenous-features.md)
