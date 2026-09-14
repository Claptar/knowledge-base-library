---
title: these functions will help us see the differences in assertthat's functions
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# these functions will help us see the differences in assertthat's functions

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

When the assertion is `FALSE` the functions have different behaviors.
`assert_that()` will throw an error, halting furthering execution of the
function immediately. `see_if()` and `validate_that()` will not stop the
execution, allowing the function to continue with bad state.

```r
returnStringAssert(c("a", "b"))
returnStringSeeIf(c("a", "b"))
returnStringValidate(c("a", "b"))
```

However, all three will give the error message

`assert_that` signals an error:

```r
assert_that(is.string(c("a", "b")))
```

`see_if` returns `FALSE` with the error message as an attribute:

```r
see_if_result <- see_if(is.string(c("a", "b")))
see_if_result
attr(see_if_result, "msg")
```

`validate_that` returns the error message as a string:

```r
validate_that(is.string(c("a", "b")))
```

While in general `assert_that()` is likely to be your go-to, you might prefer to
use `see_if()` or `validate_that()` in cases where you first want to inspect the
error message and perhaps check other aspects of your function's state before
eventually signaling an error (e.g., using `stop()` with a custom message) so
that function execution does not continue with the bad state.

```r
err_msg <- attr(see_if_result, "msg")
stop("see_if() returned FALSE because ", err_msg, call. = FALSE)
```

## Writing Your Own Assertions

While you could use `see_if()` or `validate_that()` to create custom error
messages as in the previous example, `assertthat` already provides a couple of
ways to do so.

The first is by adding a new assertion that checks whether the number is odd and
add a custom message directly to the assertion:

```r
is_odd <- function(x) {
  # your custom assertion checking functions can have their own assertions!
  # you can check multiple conditions by separating them with a ,
  assert_that(is.numeric(x), length(x) == 1)

  # here is the main assertion
  assert_that(x %% 2 == 1, msg = paste("x =", x, "is even"))
}

assert_that(is_odd(2))
```

The second is to using the `on_failure()` function, which allows you to use more
complex logic to create your assertion failure messages. Below is an example of
how this works:

```r
is_odd2 <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  x %% 2 == 1
}
attributes(is_odd2)

assert_that(is_odd2(2))

on_failure(is_odd2) <- function(call, env) {
  paste("x =", deparse(call$x), " is even")
}
attributes(is_odd2)

assert_that(is_odd2(2))
```

The assertions from our original `is_odd()` function flow through the function
we assigned to the `fail` attribute of `is_odd()` by using `on_failure()`, so we
still get the appropriate error messages when we pass a non-numeric or vector
value to `is_odd()`.


## Some Additional Useful Assertions

`assertthat` provides a few additional assertions above and beyond what base R
provides that can be quite useful:

  - `is.flag(x)`: is `x` `TRUE` or `FALSE`? (a boolean flag)
  - `is.string(x)`: is `x` a length 1 character vector?
  - `has_name(x, nm)`, `x %has_name% nm`: does `x` have component `nm`?
  - `has_attr(x, attr)`, `x %has_attr% attr`: does `x` have attribute `attr`?
  - `is.count(x)`: is `x` a single positive integer?
  - `are_equal(x, y)`: are `x` and `y` equal?
  - `not_empty(x)`: are all dimensions of `x` greater than 0?
  - `noNA(x)`: is `x` free from missing values?
  - `is.dir(path)`: is path a directory?
  - `is.writeable(path)`/`is.readable(path)`: is `path` writeable/readable?
  - `has_extension(path, extension)`: does `file` have given `extension`?

---

[← Assertions and assertthat](02-assertions-and-assertthat.md) · [Up: contents](index.md) · [Testing and testthat →](04-testing-and-testthat.md)
