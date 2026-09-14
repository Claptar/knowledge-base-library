---
title: context with one test that groups expectations
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S02/testingAssertion.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# context with one test that groups expectations

**Source:** [`lab/S02/testingAssertion.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

context("Tests for Standardize")


test_that("standardize works with normal input", {
  x <- c(1, 2, 3)
  z <- (x - mean(x)) / sd(x)

  expect_equal(standardize(x), z)
  expect_length(standardize(x), length(x))
  expect_type(standardize(x), 'double')
})


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


test_that("standardize handles logical vector", {
  w <- c(TRUE, FALSE, TRUE)
  z <- (w - mean(w)) / sd(w)

  expect_equal(standardize(w), z)
  expect_length(standardize(w), length(w))
  expect_type(standardize(w), 'double')
})
```


### Runing the tests

If your working directory is the `code/` directory, then you could run the
tests in `tests.R` from the R console using the function `test_file()`

```r

---

[← load the source code of the functions to be tested](09-load-the-source-code-of-the-functions-to-be-tested.md) · [Up: contents](index.md) · [(assuming that your working directory is "code/") →](11-assuming-that-your-working-directory-is-code.md)
