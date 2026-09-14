---
title: load it
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S02/testingAssertion.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# load it

**Source:** [`lab/S02/testingAssertion.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

library(testthat)
```


### List of common expectation functions

| Function                  | Description                             |
|---------------------------|-----------------------------------------|
| `expect_true(x)`          | expects that `x` is `TRUE`              |
| `expect_false(x)`         | expects that `x` is `FALSE`             |
| `expect_null(x)`          | expects that `x` is `NULL`              |
| `expect_type(x)`          | expects that `x` is of type `y`         |
| `expect_is(x, y)`         | expects that `x` is of class `y`        |
| `expect_length(x, y)`     | expects that `x` is of length `y`       |
| `expect_equal(x, y)`      | expects that `x` is equal to `y`        |
| `expect_equivalent(x, y)` | expects that `x` is equivalent to `y`   |
| `expect_identical(x, y)`  | expects that `x` is identical to `y`    |
| `expect_lt(x, y)`         | expects that `x` is less than `y`       |
| `expect_gt(x, y)`         | expects that `x` is greater than `y`    |
| `expect_lte(x, y)`        | expects that `x` is less than or equal to `y` |
| `expect_gte(x, y)`        | expects that `x` is greater than or equal `y` |
| `expect_named(x)`         | expects that `x` has names `y`          |
| `expect_matches(x, y)`    | expects that `x` matches `y` (regex)    |
| `expect_message(x, y)`    | expects that `x` gives message `y`      |
| `expect_warning(x, y)`    | expects that `x` gives warning `y`      |
| `expect_error(x, y)`      | expects that `x` throws error `y`       |


-----


## Motivation

To understand how `"testthat"` works, let's start with the `standardize()`
function.

```r
#' @title Standardize
#' @description Computes z-scores (scores in standard units)
#' @param x numeric vector
#' @param na.rm whether to remove missing values
#' @return vector of standard scores
#' @examples
#'  a <- runif(5)
#'  z <- standardize(a)
#'  mean(z)
#'  sd(z)
standardize <- function(x, na.rm = FALSE) {
  z <- (x - mean(x, na.rm = na.rm)) / sd(x, na.rm = na.rm)
  return(z)
}
```

When writing a function, we typically test it like this:

```r
a <- c(2, 4, 7, 8, 9)
z <- standardize(a)
z
```

We can check the mean and standard deviation of `z` to make sure `standardize()`
works correctly:

```r

---

[← remember to install "testthat"](02-remember-to-install-testthat.md) · [Up: contents](index.md) · [zero mean →](04-zero-mean.md)
