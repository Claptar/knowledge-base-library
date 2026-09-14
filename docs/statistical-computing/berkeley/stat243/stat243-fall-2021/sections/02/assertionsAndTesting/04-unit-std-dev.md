---
title: unit std-dev
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# unit std-dev

**Source:** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

sd(z)
```

Then we keep testing a function with more extreme cases:

```r
y <- c(1, 2, 3, 4, NA)
standardize(y)
standardize(y, na.rm = TRUE)
```

and even more cases:

```r
alog <- c(TRUE, FALSE, FALSE, TRUE)
standardize(alog)
```

### Using `testthat` instead

Instead of writing a list of more or less informal test, we are going to use
the functions provide by `testthat`.

To learn about the testing functions, we'll consider the following testing vectors:

- `x <- c(1, 2, 3)`
- `y <- c(1, 2, NA)`
- `w <- c(TRUE, FALSE, TRUE)`
- `q <- letters[1:3]`

#### Testing with "normal" Input

The core of `"testthat"` consists of __expectations__; to write expectations
you use functions of the form `expect_xyz()` such as `expect_equal()`,
`expect_integer()` or `expect_error()`.

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

[← zero mean](03-zero-mean.md) · [Up: contents](index.md) · [different expected output →](05-different-expected-output.md)
