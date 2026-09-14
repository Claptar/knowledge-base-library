---
title: different expected type
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# different expected type

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

expect_type(standardize(x), 'character')
```

### Edge cases: Testing function robustness

It's important to be creative when testing and get into the mindset of the user
of your code. You might be the only user, but your perspective when developing
code vs. when you use it later on are not one in the same. Think about the range
of inputs the user might give your functions and how your function should behave
in cases that don't fall directly on the happy path.

#### Testing inputs with `NA`

Let's include a vector with missing values, which we want to handle.

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

#### Testing with logical input

Let's now test `standardize()` with a logical vector:

```r
w <- c(TRUE, FALSE, TRUE)
z <- (w - mean(w)) / sd(w)

expect_equal(standardize(w), z)
expect_length(standardize(w), length(w))
expect_type(standardize(w), 'double')
```

You may be able to think of other edge cases that would be helpful to test for
this function. While it is not practical to attempt to write a test for every
possible input, you should think carefully about how your users may reasonably
interact with your code and what sorts of inputs may lead to unexpected bugs or
shortcomings even when the inputs are reasonable.

### Testing for expected errors

While we might assume that `standardize()` will already rightly throw an error
when given the character vector `q`, it's still a good idea to test for the
failures that we expect. This is especially important for catching bad bugs
where an error should be thrown but isn't, allowing function execution to
continue with incorrect state. Even if we try to guard against bad state with
assertions, testing can still help catch any incorrect logic in those
assertions.

Here's the current error we get when calling `standardize()` with character
vector input. (Notice the warning signaled by using `mean()` on a character
vector.)

```r
q <- letters[1:3]
standardize(q)
```

We can confirm that an error is signaled using `expect_error()`:

```r
expect_error(standardize(q))
```

!!! important "Important"
## Always use the regexp argument when using `expect_error()`

Using `expect_error()` without the `regexp` argument, as in the above example,
is almost never what you want!

:::

`expect_error()` will pass if _any_ error is signaled, including ones that we
aren't expecting! Therefore, it's good practice to use the `regexp` argument in
`expect_error()` to match the error message you expect to see. In this case,
we'll also use `fixed = TRUE` to exactly match the error message, rather than
use a more general regular expression.

```r
expected_msg <- "non-numeric argument to binary operator"
expect_error(standardize(q), regexp = expected_msg, fixed = TRUE)
```

Together with the `class` and `...` arguments (see `?testthat::expect_error`), it's
possible to create very sophisticated logic for matching specific errors.

## Combining multiple expectations into a test with `test_that()`

Now that you've seen how the expectation functions work, the next thing to
talk about is the function `test_that()` which you'll use to group a set
of expectations.

Looking at the previous test examples with the normal input vector, all the
expectations can be wrapped inside a call to `test_that()`. The first argument
of `test_that()` is a string indicating what is being tested, followed by an R
expression with the expectations.

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

## Running tests

The formal way to implement the tests is to include them in a separate `R`
script file, e.g. `tests-function-name.R`.  Then you

If your working directory is the `sections/03/` directory, then you could run the tests in `tests-standardize.R` from the R console using the function `test_file()`

```r

---

[← different expected length](08-different-expected-length.md) · [Up: contents](index.md) · [(assuming that your working directory is "sections/03/") →](10-assuming-that-your-working-directory-is-sections-03.md)
