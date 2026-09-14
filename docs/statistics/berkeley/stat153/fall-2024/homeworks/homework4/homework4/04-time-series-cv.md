---
title: Time series CV
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework4/homework4.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Time series CV

**Source:** [`homeworks/homework4/homework4.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

When we learned time series cross-validation in lecture (weeks 3-4, "Linear
regression and prediction"), we implemented it "manually", by writing a loop in
R to iterate over time, rebuild models, and so on. The `fable` package in R does
it differently. It relies on data being stored in a class that is known as a
`tsibble`, which is like a special data frame for time series. You can then use
a function called `stretch_tsibble()` in order to "prepare it" for time series
cross-validation. Take a look at what it does with this example:

```r
library(tidyverse)
library(fpp3)

dat = tsibble(date = as.Date("2023-10-01") + 0:9,
              value = 1:10 + rnorm(10, sd = 0.25),
              index = date)
dat

dat_stretched = dat |> stretch_tsibble(.init = 3)
dat_stretched
```

What this does is it takes the first 3 entries of the time series and assigns
them `.id = 1`. Then it appends the first 4 entries of the time series and
assigns them `.id = 2`. Then it appends the first 5 entries of the time series
and assigns them `.id = 3`, and so on. Downstream, when we go to fit a forecast
model with fable, it (by default) will fit a separate model to the data in each
level of the `.id` column. And by making forecasts at a (say) horizon `h = 1`,
these are actually precisely the 1-step ahead forecasts that we would generate
in time series CV:

```r
dat_fc = dat_stretched |>
  model(RW = RW(value ~ drift())) |>
  forecast(h = 1)
dat_fc
```

The `.mean` column give us the point forecast. To evaluate these, we could join
the original data `dat` to the point forecasts in `dat_fc`, and then align by
the `date` column, and compute whatever metrics we wanted. However, there is
also a handy function to do all of this for us, called `accuracy()`. This
computes a bunch of common metrics, and here we just pull out the `MAE` column:

```r
accuracy(dat_fc, dat) |> select(.model, MAE)
```

Now for the questions.

12. (3 pts)
A clear advantage to the above workflow is convenience: we have to write less
code. A disadvantage is that it can be inefficient, and in particular, memory
inefficient. To see this, consider using this to do time series CV on a sequence
with $n$ observations and burn-in time $t_0$. We store this as a `tsibble`, call
it `x`, with `n` rows, and then we run `stretch_tsibble(x, .init = t0)`. How
many rows does the output have? Derive the answer mathematically (as an explicit
formula involving $n,t_0$), and then verify it with a couple of code examples.

13. (4 pts)
Show that the MAE result for the random walk forecasts produced above, on the
data in `dat`, matches the MAE from a manual implementation of time series CV
with the same forecaster. (Your manual implementation can build off the code
from the regression lecture, and/or from previous homeworks.)

14. (6 pts)
Consider the `leisure` data set from the HA book, which the code excerpt below
(taken from the ARIMA lecture) prepares for us. Use time series CV, implemented
using `stretch_tsibble()`, `model()`, and `forecast()`, as described above, to
evaluate the MAE of the following four models:

- ARIMA$(2,1,0)$
- ARIMA$(0,1,2)$
- ARIMA$(2,1,0)(1,1,0)_{12}$
- ARIMA$(0,1,2)(0,1,1)_{12}$

The last models are motivated by the exploratory analysis done in lecture. The
first two remove the seasonal component, which should not be very good (since
there is clear seasonality in the data). For each model you should use a burn-in
period of length 50 (i.e., set `.init = 50` in the call to `stretch_tsibble()`).
A key difference in how you implement time series CV to the above examples: you
should consider 1-step, 2-step, all the way through 12-step ahead forecasts. But
do not worry! This can be handled with an appropriate call to `forecast()`. For
each model, calculate the MAE by averaging over all forecast horizons (1 through
12). Report the results and rank the models by their MAE.

```r
leisure = us_employment |>
  filter(Title == "Leisure and Hospitality", year(Month) > 2000) |>
  mutate(Employed = Employed/1000) |>
  select(Month, Employed)
```

15. (Bonus)
Break down the MAE for the forecasts made in Q14 by forecast horizon. That is,
for each $h = 1,\dots,12$, calculate the MAE of the $h$-step ahead forecasts
made by each model. Make a plot with the horizon $h$ on the x-axis and MAE on
the y-axis, and compare in particular the models ARIMA$(2,1,0)(1,1,0)_{12}$ and
ARIMA$(0,1,2)(0,1,1)_{12}$. Do you see anything interesting happening here in
the comparison between their MAE as we vary the horizon $h$?

16. (Bonus^2)
Evaluate the forecasts made by auto-ARIMA in this time series CV pipeline.
Remember, this means that auto-ARIMA will be rerun (yikes!) at each iteration
in time series CV. This may take a very long time to run (which is why this is
a Bonus^2). If it finishes for you, how does its MAE compare?

---

[← Long-range ARIMA](03-long-range-arima.md) · [Up: contents](index.md)
