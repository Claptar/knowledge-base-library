---
title: Exogenous features
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework5/homework5.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exogenous features

**Source:** [`homeworks/homework5/homework5.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework5/homework5.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

13. (8 pts)
As mentioned in the intro to this homework, exogenous features can play a huge
role developing useful forecasts. Fortunately, here you already have a fairly
obvious candidate for such an exogenous feature: reported Covid-19 case counts.
Both intuitively and quantitatively (recall the cross-correlation plots that we
computed near the start of the course), we know that this is a leading indicator
of Covid-19 deaths. In order to be able to make up to 4 week ahead forecasts,
we'll use 4-week-lagged Covid-19 cases as exogenous feature, to add to our ARIMA
model. Technically, when you add an exogenous feature in a formula in the call
to `ARIMA()`, this fits a regression model with ARIMA errors.

    Consider a regression model of `log(deaths)` on `log(lag(cases, 4))`, with
ARIMA(2,1,0) errors. The log transform is to stabilize the variance; we could
have done this earlier, in our ARIMA models in the above questions, but it would
have made the forecasts from our pure ARIMA models (without exogenous features)
too volatile. Include an intercept (constant) term in the model. Implement time
series CV for this model, using the code provided below as a scaffold. Compute
the MAE per horizon, and compare this to the MAEs from the models considered
thus far, on one plot. Discuss what you find---you should have taken a big leap
toward the performance of the ensemble! Hint: read the comments below carefully.
In order to make forecasts you will need to construct a new data set to pass to
`forecast()` (as opposed to simply specifying the horizon) because `forecast()`
needs to know where to find the exogenous feature(s) to construct forecasts.

```r
cases_deaths = cases_deaths |> mutate(x = lag(cases, 4))

for (i in 1:length(fc_dates)) {
  fc_date = fc_dates[i]
  # cat(as.character(fc_date), "... ")

  # dat = ... construct data set using data up through the forecast date

  # fit = ... fit the regression model using ARIMA(2,1,0) errors

  # new_dat = new_data(dat, 4) |>
  #   left_join(cases_deaths, by = "date")

  # fc = ... make forecasts up to horizon 4, but now by specifying new_dat

  # fable_fc = bind_rows(fable_fc, as_tibble(fc))
}
```

14. (Bonus)
Compute the coverage of 80\% prediction intervals from the ARIMA model with the
exogenous feature (cases), and plot alongside the coverage curves from models
considered thus far.

15. (Bonus)
For the regression model from Q13 (pick a single regression model that was fit
at a single iteration of time series CV), check that its 1 week ahead point
forecast matches the formulas you know underlie it. As before, you'll have to
extract the coefficients from the fitted model, and then form the 1 week ahead
predictions manually, verifying that you get the same result. Hint: here you
should take the forecast to be the median of the forecast distribution and not
the mean. Because of the data transformation (we're modeling log deaths), the
`fable` package will do something to adjust the mean after back-transforming
which is nonobvious. [This](https://robjhyndman.com/hyndsight/backtransforming/)
page gives more details.

16. (Bonus)
Repurposing the code used to plot the ensemble forecasts given at the start of
the homework, plot forecasts from the 5 `fable` models that you've developed, at
the same set of forecast dates. (You should have 5 separate plots.)

---

[← ETS models](07-ets-models.md) · [Up: contents](index.md)
