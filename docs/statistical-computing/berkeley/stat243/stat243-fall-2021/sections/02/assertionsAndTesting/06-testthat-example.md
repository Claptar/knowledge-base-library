---
title: testthat example
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# testthat example

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
# zero mean
mean(z)

# unit std-dev
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
# different expected output
expect_equal(standardize(x), x)
```

```r
# different expected length
expect_length(standardize(x), 2)
```

```r
# different expected type
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
# (assuming that your working directory is "sections/03/")
# run from R console
test_file("tests/tests-standardize.R")
```
We see that all 11 of the tests were passed, so it seems like our function is working as expected.

To see what the output of `test_file()` looks like when tests fail I included a version of `standarize` which adds a 1 to the end of function called `standarizeWrong` in the `functions.R` file.  In this case we expect the tests to fail and that is what we see:
```r
# (assuming that your working directory is "sections/03/")
# run from R console
test_file("tests/tests-standardize-wrong.R")
```

Here we see that 3 tests failed, namely that our output is not equal to the value that we expect it to be.  This allows us to go back to the function and assess what may be going wrong.

## Practice problems

Although it is not required to code in this manner, we are going to practice working in a test-driven format.  It is a coding practice where you first write the tests, then write a function that will pass those tests, and update the function and tests as needed.   Coding in this way is called [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development).

Suppose we want to write a function `calculator(x, y, operation)` that takes in two numbers `x` and `y` as well as a string `operation` indicating whether to perform addition, subtraction, multiplication, or division.  This function should return a numeric value.

1. Write a test that will check whether `calculator` (which you have not written yet) returns an error when `x` and `y` are not numeric and when `operation` is not in the expected set of operations (i.e. addition, subtraction, multiplication, and division). Save these tests in a file called `tests-calculator.R`.  Hint: use the expectation `expect_error()`.  You may want to write custom error messages in your assertions.

2. Start writing your `calculator` function to pass the tests written in 1).  Use the `assertthat` package to produce errors if `x` or `y` are not numeric or when `operation` is not in the expected set of operations.  You can choose what you expect the user to call each operation in the function.  Save this function as `calculator.R`

3. Use the `test_files("tests-calculator.R")` to see if your function is operating as you hope. Note this assumes you are in the directory that holds `tests-calculator.R`.

4. Write a test that checks whether the addition piece of your calculator produces the correct results with the following input:

    1. `x = 1` and `y = 9`
    2.  `x = 100`, `y = -5`
Also, check that the value returned is a scalar.  Save these tests in a file called `tests-calculator.R`.  If you think of any other tests feel free to add them.

5. Add the addition functionality to `calculator()` and call `test_files("tests-calculator.R")` again.

6. Continue iterating through this process for substraction, multiplication, and division.  Make sure your function elegantly handles division when the demoninator is 0.

7.  If you have time, add new functionality to your calulator (e.g. square root).

---

[← testthat](05-testthat.md) · [Up: contents](index.md)
