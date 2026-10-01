---
title: "84. Evaluating Covid-19 Death Forecasts"
course: "Berkeley Stat 153"
chapter: 84
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 84. Evaluating Covid-19 Death Forecasts

## What this covers

This chapter works through Homework 5 of Stat 153 (time series), a single applied exercise in
forecasting U.S. Covid-19 deaths at the national level. Rather than introducing new theory, it asks
you to put two frameworks from "the last few lectures" — ARIMA and ETS — to work on real
pandemic data, and to judge them the way a working forecaster would: against a proper accuracy
metric, against a naive baseline, and against the gold-standard ensemble forecasts that fed CDC
communications during the pandemic. It assumes you already have ARIMA and ETS models, the idea of a
rolling time-series cross-validation, and the earlier lecture's cross-correlation analysis of
Covid-19 cases against deaths (used to justify treating cases as a leading indicator) — those are
used here, not re-derived, and the numbered items below are the course's own homework problems, not
solved.

## The forecasting task and the data

Two files anchor the homework. `cases_deaths.csv` holds weekly reported U.S. Covid-19 case and
death counts from February 29, 2020 to March 4, 2023. `covidhub_fc.csv` holds 1–4 week ahead
forecasts of weekly deaths, from June 13, 2020 to March 4, 2023, produced by the **CovidHub
ensemble model** — an ensemble of every qualifying submission to the U.S. Covid-19 Forecast Hub,
and the basis of official CDC communications during the pandemic (see
[Ray et al. (2022)](https://www.sciencedirect.com/science/article/pii/S0169207022000966)).

Each forecast row carries a horizon `h` (in weeks), a `target_date` (the end of the week whose
death count is being predicted), a point forecast `forecast_0.5` — the predicted median — and
predicted quantiles such as `forecast_0.1` and `forecast_0.9`, whose difference gives the width of
an 80% prediction interval. The forecast date itself is recovered as `target_date - h * 7` days.

Two features of the setup are worth holding onto before building anything. First, this is a
**retrospective** exercise: you have the finalized death counts throughout, whereas real
(prospective) forecasters only ever saw preliminary counts subject to later revision, sometimes
severe ones — see [McDonald et al. (2021)](https://www.pnas.org/doi/10.1073/pnas.2111453118) on
what that did to forecast accuracy. The homework is therefore easier than the real problem it
mimics. Second, an operational forecaster would normally lean on **exogenous** information beyond
the series' own history — here that only enters at the very end, through lagged case counts.

## Evaluating a forecast: MAE and coverage

Two numbers do all the evaluation work in this homework, computed **per horizon** so that accuracy
at 1 week ahead is never averaged together with accuracy at 4 weeks ahead:

- **Mean absolute error (MAE)**, comparing the point forecast (`forecast_0.5`, or its analogue for
  a home-built model) against the actual death count, once the two are joined by date.
- **Coverage** of the 80% prediction interval — the fraction of times the actual value fell between
  `forecast_0.1` and `forecast_0.9` — which should sit close to 80% if the interval is honestly
  calibrated.

The ensemble's own MAE and coverage (Exercises 1–2) set the benchmark: no model built later in the
homework is expected to beat it, but it shows what "good" looks like for this problem.

## A naive baseline

Before reaching for ARIMA or ETS, the homework asks for the simplest forecaster imaginable: at
every horizon, predict that next week's deaths will equal deaths from `h` weeks ago — i.e.,
whatever was last observed, carried forward flat (Exercise 3). Any real model has to beat this to
be worth using; the homework returns to this baseline's MAE curve every time a new model is added,
as the floor a model must clear.

## ARIMA models: differencing, fitting, and rolling-origin cross-validation

The death series is visibly nonstationary, so the first step is differencing: Exercise 5 asks for a
look at the first and second differences before fitting anything. Two models are then fit with
`fable::ARIMA()` — ARIMA(1,1,0) and ARIMA(2,1,0), each with a constant term and no seasonality
(they differ only in the autoregressive order, one lag against two, both applied after the same
single differencing established in Exercise 5). Fit once, on data only through June 6, 2020, they
produce 1–4 week-ahead forecasts to plot against the true trajectory (Exercise 6); Exercise 7 then
asks you to reconstruct the 1-week-ahead forecast by hand from the fitted coefficients, as a check
that you understand what the fitted model is actually doing, not just how to call `forecast()`.

A single fit, though, only tells you about one moment in the pandemic. Exercise 8 asks for a full
**rolling-origin time-series cross-validation**: refit the model at every forecast date from June
6, 2020 to February 4, 2023, each time using only the data available up to that date, and record
the 1–4 week-ahead forecasts made from it. The homework is explicit that this should be a
hand-written loop rather than `fable`'s built-in CV utility, because the built-in version is too
memory-hungry once exogenous features are added later. Every forecast produced this way is tagged
with its horizon `h` and accumulated into one running table (`fable_fc`), which later exercises
keep appending to as more models are built.

<figure>
<svg viewBox="0 0 360 190" role="img" aria-label="Rolling-origin cross-validation: at each forecast date, fit on all data so far and forecast four weeks ahead, then roll the origin forward.">
  <line x1="20" y1="150" x2="345" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <rect x="20" y="60" width="160" height="90" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <text x="100" y="50" text-anchor="middle" font-size="12" fill="currentColor">data used to fit</text>
  <line x1="180" y1="45" x2="180" y2="150" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="180" y="168" text-anchor="middle" font-size="12" fill="currentColor">forecast date t</text>
  <circle cx="210" cy="150" r="3" fill="currentColor"/>
  <circle cx="240" cy="150" r="3" fill="currentColor"/>
  <circle cx="270" cy="150" r="3" fill="currentColor"/>
  <circle cx="300" cy="150" r="3" fill="currentColor"/>
  <text x="210" y="130" text-anchor="middle" font-size="11" fill="currentColor">h=1</text>
  <text x="240" y="112" text-anchor="middle" font-size="11" fill="currentColor">h=2</text>
  <text x="270" y="95" text-anchor="middle" font-size="11" fill="currentColor">h=3</text>
  <text x="300" y="78" text-anchor="middle" font-size="11" fill="currentColor">h=4</text>
  <line x1="210" y1="147" x2="210" y2="135" stroke="currentColor" stroke-width="1"/>
  <line x1="240" y1="147" x2="240" y2="117" stroke="currentColor" stroke-width="1"/>
  <line x1="270" y1="147" x2="270" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="300" y1="147" x2="300" y2="83" stroke="currentColor" stroke-width="1"/>
  <path d="M 305 175 L 335 175" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="320" y="188" text-anchor="middle" font-size="11" fill="currentColor">t rolls forward</text>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
</svg>
<figcaption>One iteration of the cross-validation loop: fit on everything up to the forecast date t,
forecast horizons h = 1..4 beyond it, then move t forward to the next forecast date and repeat.</figcaption>
</figure>

Exercise 9 turns the accumulated CV forecasts into MAE curves — one per horizon, for each ARIMA
model — and overlays them on the ensemble's and the baseline's MAE curves from earlier. The
expected ordering is a sandwich: ARIMA should sit between the baseline (worse) and the ensemble
(better). Exercise 10 (bonus) repeats the comparison using coverage instead of MAE.

## ETS models

The same rolling-CV machinery is reused for a second model family: Exercise 11 fits two ETS models
via `fable::ETS()` — Holt's linear trend and the damped linear trend, both with additive errors and
no seasonality — and adds their CV forecasts to the same running `fable_fc` table, then overlays
their MAE curves against every model considered so far. Exercise 12 (bonus) does the same
comparison for 80% interval coverage.

## Adding an exogenous feature: cases as a leading indicator

The last stretch of the homework brings in the piece the earlier sections deliberately withheld: an
**exogenous** signal. Reported case counts are a leading indicator of deaths — the homework recalls
the cross-correlation analysis from earlier in the course as the evidence for this — so Exercise 13
regresses `log(deaths)` on `log(lag(cases, 4))` (a 4-week lag, matching the longest forecast
horizon) with ARIMA(2,1,0) errors and an intercept. Fitting an exogenous feature inside `ARIMA()`
is exactly a regression model with ARIMA errors on the residuals, and the log transform is there to
stabilize variance — applying it to the pure ARIMA models earlier would have made their forecasts
too volatile, which is why it only appears now. The same rolling-CV loop is run again, with one
extra wrinkle: because the model now needs the exogenous feature's future values to forecast,
`forecast()` must be handed a constructed `new_data` object (built via `new_data()` and a join back
to the case counts) rather than just a horizon. The resulting MAE curve, compared against every
model built so far, is expected to close much of the remaining gap to the ensemble.

Exercise 14 (bonus) repeats the coverage comparison for this model. Exercise 15 (bonus) asks for
the same by-hand check as Exercise 7, but on a single fitted regression model from one CV
iteration — with a twist: because the response is `log(deaths)`, the point forecast that `fable`
reports after back-transforming is the **median**, not the mean, of the forecast distribution
(`fable` applies a mean-adjustment after back-transformation that is easy to miss; see
[Hyndman's discussion](https://robjhyndman.com/hyndsight/backtransforming/)). Exercise 16 (bonus)
closes the homework by reusing the ensemble-forecast plotting code from the introduction to show
all five fitted `fable` models — ARIMA(1,1,0), ARIMA(2,1,0), Holt's ETS, damped-trend ETS, and the
regression with exogenous cases — forecasting at the same set of forecast dates.

## Exercises

Point values are the course's own; "(Bonus)" items can recover points lost elsewhere but cannot
raise the total past full credit.

**Evaluating the ensemble model's MAE**

1. (4 pts) Join `covidhub_fc` and `cases_deaths` with `left_join()`, matching `target_date` in the
   forecast data to `date` in the death data. Check your join: the 4-week-ahead prediction targeting
   July 4, 2020 should have point forecast 5169.654 against an actual death count of 3684. Using the
   joined data, compute the MAE of the ensemble's point forecasts, per horizon, and report it.
2. (2 pts) Using the same joined data, compute the coverage of the ensemble's 80% prediction
   intervals, per horizon, and report it.

**Evaluating the baseline model's MAE**

3. (5 pts) Make a copy of the joined data from Exercise 1 and overwrite the point forecasts with
   the true death count from `h` weeks before the forecast date — i.e., a flat-line extrapolation of
   the most recent observation. Compute the MAE of this baseline, per horizon, and report it.
4. (Bonus) Devise an ex-ante method (using no data after the forecast date) for an 80% prediction
   interval around the baseline's point forecasts, and compute its coverage, per horizon.

**ARIMA models**

5. (2 pts) Plot the first and second differences of the death data and comment on what you see.
6. (5 pts) Fit ARIMA(1,1,0) and ARIMA(2,1,0) with `fable::ARIMA()`, each with a constant and no
   seasonality, using data only through June 6, 2020 (also the forecast date). Convert
   `cases_deaths` to a `tsibble` with `index = date` first. Make 1–4 week-ahead forecasts from each
   and plot them, together with the true death counts through June 6, 2020, using `autoplot()`.
7. (4 pts) For both models from Exercise 6, extract the fitted coefficients and reconstruct the
   1-week-ahead point forecast by hand, and show it matches the forecast each model actually
   produced.
8. (6 pts) Implement rolling-origin time-series cross-validation for ARIMA(1,1,0) and ARIMA(2,1,0)
   (each with a constant, no seasonality) as a loop, over forecast dates from June 6, 2020 to
   February 4, 2023: at each forecast date, fit on the data available up to it, forecast horizons 1
   through 4, tag each forecast with its horizon `h`, and accumulate the results into a tibble
   `fable_fc`. (Write your own loop rather than using `fable`'s built-in CV utility — it is too
   memory-intensive here and will be more so once exogenous features are added.)
9. (4 pts) Join `fable_fc` to the death data and compute the MAE of the CV forecasts from each
   ARIMA model, per horizon. Plot these MAE curves as a function of horizon alongside the
   previously-computed ensemble and baseline MAE curves, on one plot.
10. (Bonus) Repeat Exercise 9 using coverage of the 80% prediction intervals instead of MAE.

**ETS models**

11. (8 pts) Fit two ETS models with `fable::ETS()` — Holt's linear trend and the damped linear
    trend — each with additive errors and no seasonality. Implement rolling-origin CV for them as
    in Exercise 8, appending their forecasts to `fable_fc`. Plot their MAE curves as in Exercise 9,
    overlaid with all models considered so far, and discuss what you find.
12. (Bonus) Compute the coverage of 80% prediction intervals for each ETS model, per horizon, and
    plot alongside the coverage curves from every model considered so far.

**Exogenous features**

13. (8 pts) Add a 4-week-lagged case count as an exogenous feature: regress `log(deaths)` on
    `log(lag(cases, 4))` with ARIMA(2,1,0) errors and an intercept. Implement rolling-origin CV for
    this model (you will need to construct a `new_data` object carrying the exogenous feature's
    future values before calling `forecast()`). Compute the MAE per horizon and compare it against
    every model considered so far, on one plot. Discuss what you find.
14. (Bonus) Compute the coverage of 80% prediction intervals for the exogenous-feature model, per
    horizon, and plot alongside the coverage curves from every model considered so far.
15. (Bonus) Pick a single fit of the regression model from Exercise 13, from a single CV iteration.
    Extract its coefficients and reconstruct its 1-week-ahead point forecast by hand, verifying it
    matches. (Take the point forecast to be the median, not the mean, of the forecast distribution —
    the log transform means `fable`'s back-transformed mean carries a nonobvious adjustment.)
16. (Bonus) Reusing the code that plotted the ensemble's forecasts at the start of the homework,
    plot the forecasts from all five `fable` models built above — ARIMA(1,1,0), ARIMA(2,1,0),
    Holt's ETS, the damped-trend ETS, and the exogenous-feature regression — at the same set of
    forecast dates. (Five separate plots.)

## Sources

- All exposition and exercises are from Berkeley Stat 153, Fall 2024, Homework 5
  (`homeworks/homework5/homework5.Rmd`, CC BY 4.0), converted to markdown:
  [Notes about this homework](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd)
  for the framing, the note on data revisions, and the note on exogenous signals;
  [Covid-19 cases and deaths](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd)
  for the data description and Exercises 1–4;
  [ARIMA models](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd)
  for Exercises 5–12; and
  [Exogenous features](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd)
  for Exercises 13–16.
- No slides or lecture transcript were supplied for this chapter. The homework repeatedly points to
  material it does not itself contain: "the last few lectures" on ARIMA and ETS (used throughout but
  not defined here), "the cross-correlation plots that we computed near the start of the course"
  (invoked in Exercise 13 to justify cases as a leading indicator), and "the lecture code from weeks
  3–4, 'Linear regression and prediction'" referenced as a model for writing the cross-validation
  loop in Exercise 8. Also referred to but not supplied: McDonald et al. (2021), on the effect of
  data revisions on Covid-19 forecasting; Ray et al. (2022), describing the CovidHub ensemble model;
  and Rob Hyndman's note on back-transforming forecasts after a log transform, cited in Exercise 15.
- The data files themselves (`cases_deaths.csv`, `covidhub_fc.csv`) and the course's R/`fable` code
  scaffolds are referenced but not reproduced beyond what appears in the homework text above.

---

[← 83. Long-Range ARIMA and Cross-Validation](83-long-range-arima-and-cross-validation.md) · [Contents](index.md) · [85. Course Overview: Time Series Analysis →](85-course-overview-time-series-analysis.md)
