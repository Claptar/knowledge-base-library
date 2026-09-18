---
title: Trend filter
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) — berkeley-stat153 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Trend filter

9. (Bonus)
Implement 5-fold cross-validation in order to tune $\lambda$ in trend filtering
applied to the Boston marathon men's data set. Recall the description of how to
set folds in a special "structured" way, for tuning smoothers, given near the
end of the lecture notes (weeks 5-6: "Regularization and smoothing"). The code
below shows how to run trend filtering and derive estimates at the held-out
points for one fold. You can build off this code for your solution. You will
need to install the `glmgen` package from GitHub, which you can do using the
code that has been commented out.

```
Important note: just like `glmnet()`, the `trendfilter()`  function (in the
```
`glmnet` package) computes its own `lambda` sequence. So you will need to define
an initial `lambda` sequence to pass to each subsequent call to `trendfilter()`,
so that you can have a consistent grid of tuning parameter values over which to
perform cross-validation. We do this below by using the `lambda` sequence that
`trendfilter()` itself derived when the trend filtering model is fit on the full
data set.

```
After implementing cross-validation, compute and report the $\lambda$ value
```
with the smallest cross-validated MAE. Then, lastly, plot the solution at this
value of $\lambda$ when the model is fit to the full data set (this is already
available in the `tf` object below.)

```r
# devtools::install_github("glmgen/glmgen", subdir = "R_pkg/glmgen")
library(glmgen)
library(fpp3)

boston = boston_marathon |>
  filter(Year >= 1924) |>
  filter(Event == "Men's open division") |>
  mutate(Minutes = as.numeric(Time)/60) |>
  select(Year, Minutes)

# Fit trend filtering on the entire data in order to grab the lambda sequence
tf = trendfilter(x = boston$Year, y = boston$Minutes, k = 1)
lambda = tf$lambda

n = nrow(boston)       # Number of points
k = 5                  # Number of folds
inds = rep_len(1:k, n) # Folds indices

# Fit trend filtering on all points but those in first fold. We are forcing it
# to use the lambda sequence that we saved above
tf_subset = trendfilter(x = boston$Year[inds != 1],
                        y = boston$Minutes[inds != 1],
                        k = 1, lambda = lambda)

# Compute the predictions on the points in the first fold. Plot the predictions
# (as a sanity check) at a particular value of lambda in the middle of the grid
yhat = predict(tf_subset, x.new = boston$Year[inds == 1])
plot(boston$Year, boston$Minutes, col = 8)
points(boston$Year[inds == 1], yhat[, 25], col = 2, pch = 19, type = "o")
```

## Spectral analysis

10. (3 pts)
Let $\omega_j$, $j = 1,\dots,p$ be fixed and arbitrary frequencies and let
$U_{j1}, U_{j2}$, $j = 1,\dots,p$ be uncorrelated random variables with mean
zero, where $U_{j1}, U_{j2}$ have variance $\sigma^2_j$. Define

$$
x_t = \sum_{j=1}^p \Big( U_{j1} \cos(2\pi\omega_j t) + U_{j2} \sin(2\pi\omega_j t) \Big)
$$

for $t = 1,2,3,\dots$. Prove that this process is stationary, and show that its
auto-covariance function is of the form given in lecture (weeks 7-8, "Spectral
analysis and filtering").

11. (2 pts)
Construct a small empirical example to verify the auto-covariance formula you
derived in Q10. That is, generate a process with at least $p=2$ components.
compute its auto-correlation function with `acf()`, and compare to the analytic
formula you derived.

---

[← Ridge and lasso](02-ridge-and-lasso.md) · [Up: contents](index.md)
