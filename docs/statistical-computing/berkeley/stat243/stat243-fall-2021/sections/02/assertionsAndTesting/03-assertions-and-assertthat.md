---
title: Assertions and assertthat
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Assertions and assertthat

An assertion is a statement in a function or progam that must be true for it to continue.  There are three types of assertions:

  1. Pre-conditions: statements that must be true at the beginning of the function for it to work.  Mostly, this involves checking that inputs to the function are in the expected form.
  2. Invariants: statements that must be true at intermediate points in the function.  For example, checking that the output from a computation is positive before using the `sqrt()` function.
  3. Post-conditions: statements that must be true at the end of a function.  For example, if you write a function that must return a vector of length `n` with all positive numbers you would ensure that is the case after all the computation has been performed.

`assertthat` is a R package that provides functionality for adding assertions to functions, while producing useful error messages.  Calls to `assert_that` are similar to `stopifnot` function from base R.  Consider the examples below:

```r
x <- 1:10
stopifnot(is.character(x))
assert_that(is.character(x))
assert_that(length(x) == 5)
assert_that(is.numeric(x))
```

In addition to giving useful error messages adding assertions to your function allows you to document exactly what your function expects.  This is particularly useful if you come back to the function after a while and need to recall exactly what it does.

`assertthat` can be installed either from CRAN or GitHub (CRAN is the stable version, GitHub usually has the current dev version):

```r
install.packages('assertthat')
devtools::install_github("hadley/assertthat")
```

## Some Useful Assertions

As well as all the functions provided by R, assertthat provides a few more that are useful:

  - `is.flag(x)`: is x TRUE or FALSE? (a boolean flag)
  - `is.string(x)`: is x a length 1 character vector?
  - `has_name(x, nm)`, `x %has_name% nm`: does x have component nm?
  - `has_attr(x, attr)`, `x %has_attr% attr`: does x have attribute attr?
  - `is.count(x)`: is x a single positive integer?
  - `are_equal(x, y)`: are x and y equal?
  - `not_empty(x)`: are all dimensions of x greater than 0?
  - `noNA(x)`: is x free from missing values?
  - `is.dir(path)`: is path a directory?
  - `is.writeable(path)`/`is.readable(path)`: is path writeable/readable?
  - `has_extension(path, extension)`: does file have given extension?

## Three main functions: `assert_that`, `see_if`, and `validate_that`

These are the three primary functions from the package:

  - `assert_that()` signals an error
  - `see_if()` returns a logical value, with the error message as an attribute.
  - `validate_that()` returns TRUE on success, otherwise returns the error as a string.

Here is an example of the differences.  When the assertion is `TRUE` they all return `TRUE` and continue with the excecution of the function.
```r
# example functions to see differences in assertthat functions
returnStringAssert <- function(x){
  assert_that(is.string(x))

  return(x)
}
returnStringSeeIf <- function(x){
  see_if(is.string(x))

  return(x)
}
returnStringValidate <- function(x){
  validate_that(is.string(x))

  return(x)
}

returnStringAssert("a")
returnStringSeeIf("a")
returnStringValidate("a")
```

When the assertion is `FALSE` the functions have different output and function.  `assert_that` will return an error and halt excecution of the function.  `see_if` and `validate_that` will not stop the excecution.
```r
returnStringAssert(c("a", "b"))
returnStringSeeIf(c("a", "b"))
returnStringValidate(c("a", "b"))
```
However, when called outside of function they will give the error messages as described above.

`assert_that` returns an error
```r
assert_that(is.string(c("a", "b")))
```

`see_if` returns `FALSE` with an error message attribute
```r
see_if(is.string(c("a", "b")))
```

`validate_that` returns the error message as a string
```r
validate_that(is.string(c("a", "b")))
```

## Writing Your Own Assertions

You can also write you own assertions with custom error messages.  There are two ways to do this. The first is using the `on_failure()` function. Below is an example of how this works:

```r
is_odd <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  x %% 2 == 1
}
assert_that(is_odd(2))

on_failure(is_odd) <- function(call, env) {
  paste0(deparse(call$x), " is even")
}
assert_that(is_odd(2))
```

Also note theat the assertions from our original `is_odd()` function flow through the function call from `on_failure()`, so we still get the appropriate error messages when we pass a non-numeric or vector value to `is_odd()`.

Another, option is to add a new assertion that checks whether the number is odd and add a custome message directly to the assertion:
```r
is_odd2 <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  assert_that(x %% 2 == 1, msg = paste(x, "is even"))
  x %% 2 == 1
}
assert_that(is_odd2(2))
```

---

[← Assertion vs. Testing](02-assertion-vs-testing.md) · [Up: contents](index.md) · [Testing →](04-testing.md)
