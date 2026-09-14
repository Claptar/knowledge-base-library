---
title: Assertions and assertthat
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Assertions and assertthat

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

An assertion is a statement in a function or program that must be `TRUE` for it to
continue and throws an error if `FALSE`. There are three types of assertions:

  1. _Pre-conditions_: statements that must be true at the beginning of the function for it to work.  Mostly, this involves checking that inputs to the function are in the expected form.
  2. _Invariants_: statements that must be true at intermediate points in the function.  For example, checking that the output from a computation is positive before using the `sqrt()` function.
  3. _Post-conditions_: statements that must be true at the end of a function.  For example, if you write a function that must always return a vector of length `n` with all positive numbers you would ensure that is the case after all the computation has been performed.

`assertthat` is a R package that provides functionality for adding assertions to
functions, while producing useful error messages. Calls to `assert_that` are
similar to `stopifnot` function from base R. Consider the examples below:

```r
x <- 1:10
stopifnot(is.character(x))
assert_that(is.character(x))
assert_that(length(x) == 5)
assert_that(is.numeric(x))
```

In addition to giving useful error messages to the user about their inputs,
adding assertions to your function allows you to document exactly what you as
the developer expect to happen at intermediate points. This is particularly
useful if you come back to the function after a while and need to recall exactly
what it does.

`assertthat` can be installed either from CRAN or GitHub (CRAN is the stable
version, GitHub usually has the current dev version):

- Installation from CRAN:
  ```r
  install.packages('assertthat')
  ```
- Installation from GitHub (requires the [`remotes`](https://remotes.r-lib.org/) package):
  ```r
  remotes::install_github("hadley/assertthat")
  ```

## Three main functions: `assert_that`, `see_if`, and `validate_that`

These are the three primary functions from the package:

  - `assert_that()` signals (i.e., throws) an error. This is primarily what you will use in your functions.
  - `see_if()` returns a logical value, with the error message as an attribute, but no error is thrown.
  - `validate_that()` returns `TRUE` on success and otherwise returns the error as a string.

Here is an example of the differences. When the assertion is `TRUE` they all
return `TRUE` and continue with the execution of the function.

```r

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [these functions will help us see the differences in assertthat's functions →](03-these-functions-will-help-us-see-the-differences-in-assertth.md)
