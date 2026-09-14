---
title: Evaluating the baseline model's MAE
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Evaluating the baseline model's MAE

**Source:** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

3. (5 pts)
As one more thing to do before building our own models, we'll develop a simple
baseline model and compute its MAE. Make a copy of the joined data from Q1, and
overwrite the point forecasts with the true value of deaths from `h` weeks ago.
In other words, this baseline simply predicts (at all horizons) that we will see
the same number of new reported Covid-19 deaths as what we observed in the last
week. (Its forecast trajectories are thus flat lines, extrapolating forward from
the latest observation.) After you've done this, compute the MAE of the baseline
forecasts, per horizon, and report the results.

4. (Bonus)
Develop a method to form an 80\% prediction interval around the baseline model's
point forecasts. This should still be an ex-ante prediction in the sense that it
should not be using data after the forecast date. Once you've done this, compute
the coverage of these prediction intervals, per horizon, and report the results.

---

[← Evaluating the ensemble model's MAE](04-evaluating-the-ensemble-model-s-mae.md) · [Up: contents](index.md) · [ARIMA models →](06-arima-models.md)
