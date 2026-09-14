---
title: example functions to see differences in assertthat functions
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/03/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# example functions to see differences in assertthat functions

**Source:** [`sections/03/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

returnStringAssert <- function(x){
  assert_that(is.string(x))

  return(x)
}
returnStringSeeIf <- function(x){
  see_if(is.string(x))

  return(x)
}
returnStringValidate <- function(x){
  validate_that(is.string(x))

  return(x)
}

returnStringAssert("a")
returnStringSeeIf("a")
returnStringValidate("a")
```

When the assertion is `FALSE` the functions have different output and function.  `assert_that` will return an error and halt excecution of the function.  `see_if` and `validate_that` will not stop the excecution.
```r
returnStringAssert(c("a", "b"))
returnStringSeeIf(c("a", "b"))
returnStringValidate(c("a", "b"))
```
However, when called outside of function they will give the error messages as described above.

`assert_that` returns an error
```r
assert_that(is.string(c("a", "b")))
```

`see_if` returns `FALSE` with an error message attribute
```r
see_if(is.string(c("a", "b")))
```

`validate_that` returns the error message as a string
```r
validate_that(is.string(c("a", "b")))
```

### Writing Your Own Assertions

You can also write you own assertions with custom error messages.  There are two ways to do this. The first is using the `on_failure()` function. Below is an example of how this works:

```r
is_odd <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  x %% 2 == 1
}
assert_that(is_odd(2))

on_failure(is_odd) <- function(call, env) {
  paste0(deparse(call$x), " is even")
}
assert_that(is_odd(2))
```


Also note theat the assertions from our original `is_odd()` function flow through the function call from `on_failure()`, so we still get the appropriate error messages when we pass a non-numeric or vector value to `is_odd()`.

Another, option is to add a new assertion that checks whether the number is odd and add a custome message directly to the assertion:
```r
is_odd2 <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  assert_that(x %% 2 == 1, msg = paste(x, "is even"))
  x %% 2 == 1
}
assert_that(is_odd2(2))
```

## Testing

Assertions allow us to check aspects of functions as they are being excuted, while unit tests
help ensure the output from a function is what we expect.  A common approach to testing is to use the command line to informally check whether your code works on a few examples.  Units tests are a more formal framework for testing that allows you to continue running the same tests as you update your function.  Hadley Wickam describes four main areas that proper testings will help improve your code:

  1. **Fewer bugs**: When setting up unit tests you have a formal place that describes your expectation of function behavior.  Having two places where the function is document allows you to check one against the other.
  2. **Better code structure**: Tests should only check accuracy of small portions of code, so that you can easily find the source of error.  This forces you to write more modular code.
  3. **Easier restarts**: Tests help you remember where you left off and what the next step in your code should be.  It is good practice to write tests first, followed by the function to execute the desired result.
  4. **Robust code**: By having tests in place for all portions of your code you can make changes while knowing that you can easily check if those changes produce an error and where to go to fix it.


## `testthat`
The `testthat` package provides a framework for writing and performing tests in R.  There are two pieces of the `testthat` package, which form a hierarchal structure for doing testing.

  1. Tests: tests are the top of the hiercharchy.  Usually for a single function that is being tested there will be multiple tests.  For example, we may have one test that inspects results for normal inputs and another test for inputs with missing values.  Use the `test_that()` function.
  2. Expectations: each test is made up of a series of expectations that describe the expected output of a function (e.g. length, type, value).  Use the `expect_that()` function.

### List of Common Expectation Functions

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


## `testthat` example
To understand how `testthat` works, we will consider the `standardize()`
function, which takes a vector `x`, subtracts the mean of the vector, and then divides by the standard deviation.  Notice the assertions in the function checking pre-conditions!

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
When writing a function, we informally testings usually looks something like this:

```r
a <- c(2, 4, 7, 8, 9)
z <- standardize(a)
z
```

We can check the mean and standard deviation of `z` to make sure `standardize()`
works correctly:

```r

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [zero mean →](03-zero-mean.md)
