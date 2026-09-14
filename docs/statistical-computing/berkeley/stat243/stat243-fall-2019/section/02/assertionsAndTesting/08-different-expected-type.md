---
title: different expected type
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# different expected type

**Source:** [`section/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

expect_type(standardize(x), 'character')
```


### Testing with "missing values"

Let's include a vector with missing values

```r
y <- c(1, 2, NA)
z1 <- (y - mean(y, na.rm = FALSE)) / sd(y, na.rm = FALSE)
z2 <- (y - mean(y, na.rm = TRUE)) / sd(y, na.rm = TRUE)

expect_equal(standardize(y), z1)
expect_length(standardize(y), length(y))
expect_equal(standardize(y, na.rm = TRUE), z2)
expect_length(standardize(y, na.rm = TRUE), length(y))
expect_type(standardize(y), 'double')
```


### Testing with "logical" input

Let's now test `standardize()` with a logical vector:

```r
w <- c(TRUE, FALSE, TRUE)
z <- (w - mean(w)) / sd(w)

expect_equal(standardize(w), z)
expect_length(standardize(w), length(w))
expect_type(standardize(w), 'double')
```


## Function `test_that()`

Now that you've seen how the expectation functions work, the next thing to
talk about is the function `test_that()` which you'll use to group a set
of expectations

Looking at the previous test examples with the "normal" input vector, all the
expectations can be wrapped inside a call to `test_that()`. The first argument
of `test_that()` is a string indicating what is being tested, followed by an R expression with the expectations.

```r
test_that("standardize works with normal input", {
  x <- c(1, 2, 3)
  z <- (x - mean(x)) / sd(x)

  expect_equal(standardize(x), z)
  expect_length(standardize(x), length(x))
  expect_type(standardize(x), 'double')
})
```

Likewise, all the expectations with the vector containing missing values can be
wrapped inside another call to `test_that()` like this:

```r
test_that("standardize works with missing values", {
  y <- c(1, 2, NA)
  z1 <- (y - mean(y, na.rm = FALSE)) / sd(y, na.rm = FALSE)
  z2 <- (y - mean(y, na.rm = TRUE)) / sd(y, na.rm = TRUE)

  expect_equal(standardize(y), z1)
  expect_length(standardize(y), length(y))
  expect_equal(standardize(y, na.rm = TRUE), z2)
  expect_length(standardize(y, na.rm = TRUE), length(y))
  expect_type(standardize(y), 'double')
})
```

And last, but not least, the expectations with the logical vector can be
grouped in a `test_that()` call:

```r
test_that("standardize handles logical vector", {
  w <- c(TRUE, FALSE, TRUE)
  z <- (w - mean(w)) / sd(w)

  expect_equal(standardize(w), z)
  expect_length(standardize(w), length(w))
  expect_type(standardize(w), 'double')
})
```


## Testing Structure

As we mentioned in the introduction, there is a hierarchical structure for the
tests that is made of _expectations_ that are grouped in _tests_, which are
in turn considered to be part of some _context_. In other words:

> A __context__ involves __tests__ formed by groups of __expectations__

The formal way to implement the tests is to include them in a separate `R`
script file, e.g. `tests.R`.

Suppose you are working on a project with some file structure like the one
below. Automated tests are stored in a `test/` directory, containing the auto-run script and your test functions:

```
  project/
    R/
    data/
    man/
    src/
    tests/
      testthat/
        test-myFunc1.R
        test-myFunc2.R
      testthat.R
    DESCRIPTION
    NEWS
    NAMESPACE
    ...
```

The content of `testthat.R` may look like this:

```r
library(testthat)
test_check("project")
```

While the content of `test-myFunc1.R` will look similar to:

```r

---

[← different expected length](07-different-expected-length.md) · [Up: contents](index.md) · [context with one test that groups expectations →](09-context-with-one-test-that-groups-expectations.md)
