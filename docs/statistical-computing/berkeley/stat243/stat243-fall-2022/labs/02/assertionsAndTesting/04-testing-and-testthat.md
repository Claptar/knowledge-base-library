---
title: Testing and testthat
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Testing and testthat

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Assertions allow us to check aspects of function state as the function is being
executed, while unit tests help ensure that the output from a function is what
we expect given some set of inputs.

A common approach to testing is to use the R console to informally check whether
your code works on a few examples. Units tests formalize this approach by
providing a framework for testing that allows you to re-run tests as you update
your functions. You are likely already using the first approach, so there is no
reason to waste your code and energy by not saving it for later use.

Hadley Wickam describes four main areas that proper testings will help improve
your code:

1. **Fewer bugs**: When setting up unit tests you have a formal place that
   describes your expectations for function behavior. This serves as a form of
   internal documentation and helps ensure that your code does what you
   intend.

2. **Better code structure**: Tests should only check accuracy of small portions
   of code, allowing you to easily find sources of error. This forces you to
   write more modular code.

3. **Easier restarts**: Tests help you remember where you left off and what the
   next step in your code should be. It is good practice to write tests first,
   and then write the function that achieves the desired result. This practice
   is called "test-driven development".

4. **Robust code**: By having tests in place for all portions of your code you
   can make changes while knowing that you can easily check if those changes
   produce an error and where to go to fix it.

The `testthat` package provides a framework for writing and performing tests in
R. There are two pieces of the `testthat` package, forming a hierarchical
structure for testing.

1. Tests: tests are the top of the hiercharchy. Usually for a single function
   that is being tested there will be multiple tests. For example, we may have
   one test that inspects results for normal inputs and another test for inputs
   with missing values. Use the `test_that()` function.

2. Expectations: each test is made up of a series of expectations that describe
   the expected output of a function (e.g. length, type, value). Use the
   `expect_that()` function.

## List of Common `testthat` Expectations

| Function                  | Description                             |
|---------------------------|-----------------------------------------|
| `expect_true(x)`          | expects that `x` is `TRUE`              |
| `expect_false(x)`         | expects that `x` is `FALSE`             |
| `expect_null(x)`          | expects that `x` is `NULL`              |
| `expect_type(x)`          | expects that `x` is of type `y`         |
| `expect_is(x, y)`         | expects that `x` is of class `y`        |
| `expect_length(x, y)`     | expects that `x` is of length `y`       |
| `expect_equal(x, y)`      | expects that `x` is equal to `y`        |
| `expect_equivalent(x, y)` | expects that `x` is equivalent to `y`   |
| `expect_identical(x, y)`  | expects that `x` is identical to `y`    |
| `expect_lt(x, y)`         | expects that `x` is less than `y`       |
| `expect_gt(x, y)`         | expects that `x` is greater than `y`    |
| `expect_lte(x, y)`        | expects that `x` is less than or equal to `y` |
| `expect_gte(x, y)`        | expects that `x` is greater than or equal `y` |
| `expect_named(x)`         | expects that `x` has names `y`          |
| `expect_matches(x, y)`    | expects that `x` matches `y` (regex)    |
| `expect_message(x, y)`    | expects that `x` gives message `y`      |
| `expect_warning(x, y)`    | expects that `x` gives warning `y`      |
| `expect_error(x, y)`      | expects that `x` throws error `y`       |


## Motivating Example

To understand how `testthat` works, we will consider the `standardize()`
function, which takes a vector `x`, subtracts the mean of the vector, and then
divides by the standard deviation. Notice the assertions in the function
to check pre-conditions!

```r
standardize <- function(x, na.rm = FALSE) {
  # assertions on input
  assert_that(is.vector(x))
  assert_that(is.flag(na.rm))

  # do computation
  z <- (x - mean(x, na.rm = na.rm)) / sd(x, na.rm = na.rm)
  return(z)
}
```

### Informal testing

When writing a function, the informal process of testing usually looks something
like this, executed line-by-line in the R console:

```r
a <- c(2, 4, 7, 8, 9)
z <- standardize(a)
z
```

Then you might look at the mean and standard deviation of `z` to see if
`standardize()` appears to be working as expected:

```r

---

[← these functions will help us see the differences in assertthat's functions](03-these-functions-will-help-us-see-the-differences-in-assertth.md) · [Up: contents](index.md) · [zero mean →](05-zero-mean.md)
