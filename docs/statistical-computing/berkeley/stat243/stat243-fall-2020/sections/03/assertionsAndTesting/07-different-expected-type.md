---
title: different expected type
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/03/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# different expected type

**Source:** [`sections/03/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

expect_type(standardize(x), 'character')
```


### Testing with missing values

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


### Testing with logical input

Let's now test `standardize()` with a logical vector:

```r
w <- c(TRUE, FALSE, TRUE)
z <- (w - mean(w)) / sd(w)

expect_equal(standardize(w), z)
expect_length(standardize(w), length(w))
expect_type(standardize(w), 'double')
```


### Combining multiple expectations into a test with `test_that()`

Now that you've seen how the expectation functions work, the next thing to
talk about is the function `test_that()` which you'll use to group a set
of expectations.

Looking at the previous test examples with the normal input vector, all the
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

Likewise, all the expectations with the vector containing missing values can be wrapped inside another call to `test_that()` like this:

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


### Running tests

The formal way to implement the tests is to include them in a separate `R`
script file, e.g. `tests-function-name.R`.  Then you

If your working directory is the `sections/03/` directory, then you could run the tests in `tests-standardize.R` from the R console using the function `test_file()`

```r

---

[← different expected length](06-different-expected-length.md) · [Up: contents](index.md) · [(assuming that your working directory is "sections/03/") →](08-assuming-that-your-working-directory-is-sections-03.md)
