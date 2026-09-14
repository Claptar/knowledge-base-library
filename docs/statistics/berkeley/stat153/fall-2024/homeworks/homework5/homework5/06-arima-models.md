---
title: ARIMA models
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ARIMA models

**Source:** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

5. (2 pts)
Now we'll start building our own models, starting with ARIMA. Because the data
is highly nonstationary (recall the plot above which showed death counts along
with the ensemble forecasts), we'll consider differencing. Plot the first and
second differences of the death data, and comment on what you find.

6. (5 pts)
Fit two models: ARIMA(1,1,0) and ARIMA(2,1,0), using `ARIMA()` from the `fable`
package. Each model should be fit only using the data up through June 6, 2020.
(This is also therefore the forecast date.) These models should be fit *with*
the inclusion of a constant but *without* any seasonality terms (specify the
formula carefully to ensure this). After fitting these models, use these to make
1-4 week ahead forecasts and plot them (along with the true death counts through
June 6, 2020) with `autoplot()`. Hint: before calling `fable::model()` you'll
have to convert `cases_deaths `to a `tsibble` object, with `index = date`.

7. (4 pts)
For the two models from Q6, check that their 1 week ahead point forecasts match
the formulas you know underlie them. To do so, extract the coefficients from the
fitted models, form the 1 week ahead predictions manually, and demonstrate that
these match the given forecasts.

8. (6 pts)
Implement time series cross-validation (CV) for these ARIMA models, ARIMA(1,1,0)
and ARIMA(2,1,0), each with constants (and no seasonality). The simplest way to
do this will be write a loop (to refresh yourself, look back at the lecture code
from weeks 3-4, "Linear regression and prediction", or from the homeworks after
that). As you saw in the last homework, the `fable` package provides its own way
to run time series CV, but it will use up too much memory (and be too cumbersome
for the computations that involve exogenous features, later).

    The code below provides a scaffold that you should build on, where we run
time series CV over June 6, 2020 to February 4, 2023. Make sure to explicitly
define the horizon `h` in forecasts stored in the `fc` object, which will be
useful for subsequent computations.The end result of this question will be a
`tibble`, called `fable_fc`, which contains all of the 1-4 week ahead forecasts
made in time series CV by your two ARIMA models. We will continue to append
forecasts to this `tibble` in subsequent questions, as we build more models
using `fable`.

```r
t0 = as.Date("2020-06-06")
t1 = as.Date("2023-02-04")
fc_dates = cases_deaths |> filter(between(date, t0, t1)) |> pull(date)
fable_fc = tibble()

for (i in 1:length(fc_dates)) {
  fc_date = fc_dates[i]
  # cat(as.character(fc_date), "... ")

  # dat = ... construct data set using data up through the forecast date

  # fit = ... fit the ARIMA(1,1,0) and ARIMA(2,1,0) models

  # fc  = ... make forecasts, up to horizon 4; important: it will help to
  #           create a column in fc that indicates the forecast horizon!

  # fable_fc = bind_rows(fable_fc, as_tibble(fc))
}
```

9. (4 pts)
Compute the MAE of the time series CV forecasts made by each ARIMA model, per
horizon. (In order to do this, you'll need to join `fable_fc` to the death data
from `cases_deaths`.) Compare this to the previously-computed MAEs of the
ensemble and baseline models by displaying their MAE curves, as a function of
horizon, all on the same plot. According to MAE, your ARIMA models should be
better than the baseline, but notably worse than the ensemble.

10. (Bonus)
Do the same as in Q9, but substituting MAE with coverage of the 80\% prediction
intervals.

---

[← Evaluating the baseline model's MAE](05-evaluating-the-baseline-model-s-mae.md) · [Up: contents](index.md) · [ETS models →](07-ets-models.md)
