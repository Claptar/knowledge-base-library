---
title: Ridge and lasso
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Ridge and lasso

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

3. (8 pts)
Using the cardiovascular mortality regression data, form lagged features from
the particulate matter and temperature variables, using lags 4, 8, ..., 40 from
each. Using the `glmnet` package, fit a ridge regression and lasso regression
(two separate models), each over a grid of tuning parameter values $\lambda$
chosen by the `glmnet()` function, with cardiovascular mortality as the response
and all the lagged features as predictors (you should have 20 in total: 10 from
particulate matter, and 10 from temperature). However, make sure you do this in
a split-sample setup for validation, as follows, for each of ridge and lasso:

- fit the `glmnet` object on the *first half of the time series*;
- make predictions on the *second half of the time series*, for each $\lambda$;
- record the MAE of the predictions on the second half, for each $\lambda$;
- choose and report the value of $\lambda$ with the lowest MAE;
- plot the cardiovascular mortality time series, along with the predictions on
  the second half, and print the MAE and the selected value of $\lambda$ on the
  plot.

    You can build on the code from the regularization lecture (weeks 5-6:
"Regularization and smoothing") for fitting the ridge and lasso models, and the
regression lecture (weeks 3-4: "Regression and prediction") for the split-sample
validation. *Note carefully that the lecture code includes lag 0, and here we do
not, so that we can make ex-ante 4-week ahead forecasts!*

4. (1 pts)
Which lagged features were present in the MAE-optimal lasso model, selected by
split-sample validation, in Q3?

5. (8 pts)
Repeat Q3, except implement time series cross-validation instead of split-sample
validation. You should begin time series cross-validation on the second half of
the time series, treating the first half as a burn-in set. Also, be sure to fit
each ridge or lasso model using a trailing window of 200 time points (not all
past).

    Warning: doing time series cross-validation properly will require us to pay
attention to the following. The `glmnet()` function chooses a sequence of tuning
parameter values $\lambda$ based on the passed feature matrix `x` and response
vector `y` (its first two arguments). However, in time series cross-validation,
this will change at each time point. So if you just call `glmnet()` naively,
then you will not have a consistent $\lambda$ sequence over which to calculate
MAE and perform tuning.

    You can circumvent this issue by defining your own $\lambda$ sequence ahead
of time, and forcing `glmnet()` to use it by passing it through its `lambda`
argument. Indeed, the best thing to do here is just to use the `lambda` sequence
that `glmnet()` itself derived for the ridge and lasso models fit to the first
half of the time series, which you already have from Q3. Do this, and then just
as in Q3, produce a plot of the cardiovascular mortality time series, along with
the predictions from time series CV on the second half, and print the MAE and
the selected value of $\lambda$ on the plot.

    You can build off the code given in the regression lecture for time series
cross-validation (or the code you wrote in Homework 2 to implement time series
cross-validation).

6. (Bonus)
Report which lagged features were most frequently selected by the lasso. Because
the lasso models will be refit at each time point (in the second half of the
data set), you will have to additionally store the lasso solutions along your
time series CV pass. Then, look back at the solutions that correspond to the
MAE-optimal $\lambda$ value, and choose some way of summarizing which of its
components were consistently large in magnitude over time.

---

[← Regression troubles](02-regression-troubles.md) · [Up: contents](index.md) · [HP filter →](04-hp-filter.md)
