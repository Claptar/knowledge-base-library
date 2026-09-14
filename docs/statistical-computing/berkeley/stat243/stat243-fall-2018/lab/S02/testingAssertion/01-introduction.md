---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S02/testingAssertion.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`lab/S02/testingAssertion.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
require(assertthat)
require(testthat)
```

Thanks to Dr. Sanchez and the Berkeley SCF upon whose tutorials, the following material is based.

## Assertion vs. Testing

One uses assertions to check inputs and the state of the program during execution, while tests check that a function behaves as expected given a set of inputs (including checking that the assertions work and that what should be errors are indeed errors).

Tests and Assertions are similar in that,

  - Both are part of specification.
  - They are helpful during design, but in different ways. See below.

Tests and Assertions are different in that,

  - Usually, assertions have a smaller span, because an assertion in a method must depend only on the object and method parameters, otherwise you get too many dependencies.
  - Assertions belong to the class, so can document class properties and assumptions that are not public. Unit tests can only check externally visible properties.
  - Assertions are part of executing code, so the amount of computation you can do in an assertion is limited. You can eliminate assertions from product code in the name of speed, but then you sacrifice graceful error handling.
  - Tests only test a small number of cases. Assertions work with live data, which can be more varied and more realistic. They purport to cover infinitely many cases; they establish universal truths rather then point truths.

## Assertions and `"assertthat"`


assertthat provides a drop in replacement for stopifnot() that makes it easy to check the pre- and post-conditions of a function, while producing useful error messages.
```r
x <- 1:10
stopifnot(is.character(x))
assert_that(is.character(x))
assert_that(length(x) == 5)
assert_that(is.numeric(x))
```

This is a good defensive programming technique, and is useful as source-code documentation: you can see exactly what your function expects when you come back to it in the future. It is partly a response to the lack of static typing in R.

assertthat can be installed either from CRAN:

```r
install.packages('assertthat')
```

### Some Useful Assertions

As well as all the functions provided by R, assertthat provides a few more that are useful:

  - is.flag(x): is x TRUE or FALSE? (a boolean flag)
  - is.string(x): is x a length 1 character vector?
  - has_name(x, nm), x %has_name% nm: does x have component nm?
  - has_attr(x, attr), x %has_attr% attr: does x have attribute attr?
  - is.count(x): is x a single positive integer?
  - are_equal(x, y): are x and y equal?
  - not_empty(x): are all dimensions of x greater than 0?
  - noNA(x): is x free from missing values?
  - is.dir(path): is path a directory?
  - is.writeable(path)/is.readable(path): is path writeable/readable?
  - has_extension(path, extension): does file have given extension?

### assert_that, see_if and validate_that

There are three main functions in assertthat:

  - assert_that() signal an error

  - see_if() returns a logical value, with the error message as an attribute.

  - validate_that() returns TRUE on success, otherwise returns the error as a string.


### Writing your own assertions

If you're writing your own assertions, you can provide custom error messages using the on_failure() helper:

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


The on_failure callback is called with two arguments, the unevaluated function call , and env, and the environment in which the assertion was executed. This allows you to choose between displaying values or names in your error messages.

Also note the use of assert_that() in the new function: assertions flow through function calls ensuring that you get a useful error message at the top level:

```r
assert_that(is_odd("b"))

assert_that(is_odd(1:2))
```


## Testing and  The R Package `"testthat"`


> ### Learning Objectives
>
> - Benefits of Unit Tests
> - Introduction to the R package "testthat"
> - Write simple functions and their unit tests
> - Test your code

-----

Now you'll learn how to graduate from using informal ad hoc testing, done at the command line, to formal automated testing (aka unit testing). While turning casual interactive tests into reproducible scripts requires a little more work up front, it pays off in four ways:

* Fewer bugs. Because you're explicit about how your code should behave
  you will have fewer bugs. The reason why is a bit like the reason double
  entry book-keeping works: because you describe the behaviour of your code in
  two places, both in your code and in your tests, you are able to check one against
  the other. By following this approach to testing, you can be sure that bugs
  that you've fixed in the past will never come back to haunt you.

* Better code structure. Code that's easy to test is usually better designed.
  This is because writing tests forces you to break up complicated parts of
  your code into separate functions that can work in isolation. This reduces
  duplication in your code. As a result, functions will be easier to test,
  understand and work with (it'll be easier to combine them in new ways).

* Easier restarts. If you always finish a coding session by creating a failing
  test (e.g. for the next feature you want to implement), testing makes it
  easier for you to pick up where you left off: your tests will let you know
  what to do next.

* Robust code. If you know that all the major functionality of your package has
  an associated test, you can confidently make big changes without worrying
  about accidentally breaking something. For me, this is particularly useful
  when I think I have a simpler way to accomplish a task (usually the reason my
  solution is simpler is that I've forgotten an important use case!).


`"testthat"` is one of the packages in R that helps you write tests for your functions. One of the main references is the paper
_testthat: Get Started with Testing_ by Hadley Wickham (see link below).
This paper clearly describes the philisoply and workflow of `"testthat"`. But
keep in mind that since the introduction of the package, many more functions
haven been added to it.

[https://journal.r-project.org/archive/2011-1/RJournal_2011-1_Wickham.pdf](https://journal.r-project.org/archive/2011-1/RJournal_2011-1_Wickham.pdf)


## About `"testthat"`

- `"testthat"` provides a testing framework for R that is easy to learn and use
- `"testthat"` has a hierarchical structure made up of:
    + expectations
    + tests
    + contexts
- A __context__ involves __tests__ formed by groups of __expectations__
- Each structure has associated functions:
    + `expect_that()` for expectations
    + `test_that()` for groups of tests
    + `context()` for contexts


```r

---

[Up: contents](index.md) · [remember to install "testthat" →](02-remember-to-install-testthat.md)
