---
title: context with one test that groups expectations
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# context with one test that groups expectations

**Source:** [`section/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

[← different expected type](08-different-expected-type.md) · [Up: contents](index.md) · [(assuming that your working directory is "code/") →](10-assuming-that-your-working-directory-is-code.md)
