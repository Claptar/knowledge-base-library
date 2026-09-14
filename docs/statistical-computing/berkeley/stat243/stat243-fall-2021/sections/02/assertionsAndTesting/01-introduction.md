---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
library(assertthat)
library(testthat)
```

## References and useful links

* [Testing section](http://r-pkgs.had.co.nz/tests.html) of the R packages tutorial by Hadley Wickham
* [GitHub](https://github.com/hadley/assertthat) for assertthat package by Hadley Wickham
* [Assertions and testing tutorial](https://swcarpentry.github.io/python-novice-inflammation/10-defensive/index.html) in Python

## Learning Objectives
  - Understand the benefits of assertions and testings as well as the differences between the two.
  - Introduction to the R package `assertthat`.
  - Introduction to the R package `testthat`.
  - Practice writing assertions and tests on your own.

## Purpose of Assertions and Testing
We all want our code   to be correct the first time we write it. The unfortunate reality is that we all make mistakes when coding, either because of "silly mistakes" (indexing errors,   incorrect syntax,  using a wrong variable name, etc.) or because of a fundamental misunderstanding of the problem we are trying to solve. While print statements and writing test cases can help reduce coding errors, it is desirable to have a formal, structured way to test our code to ensure that it is functioning how we want it to. It is here that the `assertthat` and `testthat` packages in R prove useful.


## Assertion vs. Testing

Assertions check the internal state of a function.  For example, consider a function ```add(x, y)``` which returns ```x + y```.  The function assumes ```x```  is numeric, and an assertion would confirm that this is in the case and return as error if not.  On the other hand, tests check that a function produces the expected output for various inputs.  For example, ensuring that ```add(1, 2)``` returns the number 3.  Tests may include checks that assertions are working properly.

Tests and assertions are similar in that,

- Both are part of ensuring programs run correctly and aspects of defensive programming.
- Both should check small pieces of the code while providing useful error messages, so they tell you exactly where the issue arises.

A couple of important differences between assertions and tests are below:

| Assertions                                                               | Testing                                        |
|--------------------------------------------------------------------------|------------------------------------------------|
| Depends only on the object and method parameters.                        | Can depend on global variables.                |
| Document function properties that are not public.                        | Can only check externally visible properties.  |
| Work with live data, so check cover infinitely many cases.               | Test a small number of cases.                  |
| Excecuted in function calls, so amount of computation should be limited. |                                                |

## Assertions and `assertthat`
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

### Some Useful Assertions

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

### Three main functions: `assert_that`, `see_if`, and `validate_that`

These are the three primary functions from the package:

  - `assert_that()` signals an error
  - `see_if()` returns a logical value, with the error message as an attribute.
  - `validate_that()` returns TRUE on success, otherwise returns the error as a string.

Here is an example of the differences.  When the assertion is `TRUE` they all return `TRUE` and continue with the excecution of the function.
```r

---

[Up: contents](index.md) · [example functions to see differences in assertthat functions →](02-example-functions-to-see-differences-in-assertthat-functions.md)
