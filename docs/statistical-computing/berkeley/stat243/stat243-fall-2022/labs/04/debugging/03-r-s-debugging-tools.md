---
title: R's debugging tools
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/04/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# R's debugging tools

**Source:** [`labs/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Below is a list of the debugging tools available in R.  I took screenshots illustrating how some of the tools work in RStudio in the example below.

##  Tools

- Use `traceback` to view the call stack, which can help pinpoint where an error is occurring.
- Use `recover`  to navigate the stack of active function calls at the time of the error and browse within the desired call. If you set `options(error = recover)` then `recover` is invoked whenever an error occurs.  You can revert the options to the default with `options(error = NULL)`.
- `browser()`: pauses current execution, provides an interactive interpreter.
You can now step through a function line-by-line to find errors.
- `debug(someFunc)`: sets a `browser()` statement at the first line of `someFunc`
    - `undebug(someFunc)` removes the `debug()` statement. Or close the `R` session
    - `debugonce(someFunc)` lets you debug only once, no need to run `undebug()`
- `trace()`: allows you to temporarily modify a function without saving the modifications
    - This is especially helpful for debugging functions in code where you don't
      have the source handy (e.g., in the packages you're using).
    - Edits will be removed when session ends, or when you call `untrace()` on the function

## Example of debugging

We will use the `jackKnife.R` code to understand the debugging tools.
```r
library(MASS)

gamma_est <- function(data) {
  # this fits a gamma distribution to a collection of numbers
  m <- mean(data)
  v <- var(data)
  s <- v/m
  a <- m/s
  return(list(a=a,s=s))
}

calc_var <- function(estimates){
  var_of_ests <- apply(estimates, 2, var)
  return(((n-1)^2/n)*var_of_ests)
}

gamma_jackknife <- function(data) {
  ## jackknife the estimation

  n <- length(data)
  jack_estimates <- gamma_est(data[-1])
  for (omitted_point in 2:n) {
    jack_estimates <- rbind(jack_estimates, gamma_est(data[-omitted_point]))
  }

  jack_var <- calc_var(jack_estimates)

  return(sqrt(jack_var))
}

---

[← Learning objectives](02-learning-objectives.md) · [Up: contents](index.md) · [jackknife gamma dist. estimates of cat heart weights →](04-jackknife-gamma-dist-estimates-of-cat-heart-weights.md)
