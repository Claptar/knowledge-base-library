---
title: Evaluating the ensemble model's MAE
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Evaluating the ensemble model's MAE

**Source:** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

1. (4 pts)
Before building any forecasters of our own, we'll evaluate the ensemble model's
mean absolute error (MAE). We won't be able to beat this with our models, but
it'll give us a sense of how gold-standard forecasts perform, for this problem.
First, you need join the death data to the forecast data. Using `left_join()`,
join `covidhub_fc` and `cases_deaths` by date: specifically, the `target_date`
variable in the first data set should be matched to the `date` variable in the
second. As a check, you should see for that the 4 week ahead prediction for the
target date July 4, 2020, the point forecast is 5169.654 and the death count
is 3684. After joining the data sets, compute the MAE of the point forecasts per
horizon, report the results.

2. (2 pts)
Using the same joined data set from Q1, compute the coverage of 80\% prediction
intervals, per horizon, and report the results.

---

[← Covid-19 cases and deaths](03-covid-19-cases-and-deaths.md) · [Up: contents](index.md) · [Evaluating the baseline model's MAE →](05-evaluating-the-baseline-model-s-mae.md)
