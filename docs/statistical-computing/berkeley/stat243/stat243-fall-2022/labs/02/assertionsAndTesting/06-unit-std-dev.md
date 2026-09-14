---
title: unit std-dev
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# unit std-dev

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

sd(z)
```

Next, you might keep testing the function with more extreme cases:

```r
y <- c(1, 2, 3, 4, NA)
standardize(y)
standardize(y, na.rm = TRUE)
```

And so on for different types of inputs:

```r
alog <- c(TRUE, FALSE, FALSE, TRUE)
standardize(alog)
```

This approach is fine and encouraged for interactive development, but don't
waste all this energy! Hold on to your testing code for a rainy day.

## Using `testthat` expectations

Instead of just writing a list of more or less informal tests in the R console,
we are going to use the functions provide by `testthat`.

To learn about the testing functions, we'll consider the following test inputs:

- `x <- c(1, 2, 3)`
- `y <- c(1, 2, NA)`
- `w <- c(TRUE, FALSE, TRUE)`
- `q <- letters[1:3]`

### The "happy path": Testing with "normal" input

The core of `testthat` consists of _expectations_; to write expectations you
use functions from the `testthat` package starting with `expect_` such as
`expect_equal()`, `expect_integer()` or `expect_error()`.

```r
x <- c(1, 2, 3)
z <- (x - mean(x)) / sd(x)

expect_equal(standardize(x), z)
expect_length(standardize(x), length(x))
expect_type(standardize(x), 'double')
```

Notice that when an expectation runs successfully, nothing appears to happen.
But that's good news. If an expectation fails, you'll typically get an error,
here are some failed tests:

```r

---

[← zero mean](05-zero-mean.md) · [Up: contents](index.md) · [different expected output →](07-different-expected-output.md)
