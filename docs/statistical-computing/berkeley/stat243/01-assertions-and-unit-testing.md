---
title: "1. Assertions and Unit Testing"
course: "Berkeley Stat 243"
chapter: 1
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Assertions and Unit Testing

## What this covers

Code is rarely correct on the first try, whether from a slip (an indexing error, the wrong
variable name) or from a real misunderstanding of the problem. This chapter covers two
complementary, structured ways of catching those errors in R, rather than relying on scattered
`print()` statements: **assertions**, which check a function's own internal state while it runs,
and **tests**, which check that a function produces the output you expect on given inputs. It
works through the packages `assertthat` and `testthat`, using a single running example — a
function `standardize()` — to show how the two disciplines fit together. It assumes only that you
can already write an R function.

## Assertions versus tests

An **assertion** checks the internal state of a function as it executes. Take a function
`add(x, y)` that returns `x + y` and assumes `x` is numeric: an assertion inside `add` would
confirm that assumption and raise an error if it failed. A **test**, by contrast, checks that a
function produces the output you expect for a given input from the outside — for instance, that
`add(1, 2)` really does return `3`. Tests can even include checks that the assertions inside a
function are firing correctly.

The two overlap in spirit — both are part of defensive programming, and both should check a small
piece of behaviour while giving an error message that says exactly where the problem is — but they
differ in what they see and what they cost:

| Assertions | Tests |
|---|---|
| Depend only on the object and the function's own parameters | Can depend on global variables |
| Document properties of the function that are not public | Can only check externally visible properties |
| Run against live data, so in effect check infinitely many cases | Check a fixed, small number of cases |
| Run inside every function call, so the computation they do must be cheap | Run separately, so can be more expensive |

## Assertions with `assertthat`

An assertion is a statement that must be true for the function to continue. There are three kinds:

1. **Pre-conditions** — must hold at the start of the function, typically that the inputs are of
   the expected form.
2. **Invariants** — must hold at some intermediate point, e.g. checking a value is positive before
   passing it to `sqrt()`.
3. **Post-conditions** — must hold at the end, e.g. that a function promised to return a
   length-`n` vector of positive numbers actually does.

The `assertthat` package (Hadley Wickham) adds assertions to functions with useful error messages.
`assert_that()` plays the same role as base R's `stopifnot()`:

```r
x <- 1:10
stopifnot(is.character(x))
assert_that(is.character(x))
assert_that(length(x) == 5)
assert_that(is.numeric(x))
```

Beyond the error message, an assertion **documents** what the function expects — useful when you
return to your own code after a while and need to recall exactly what it assumes. Install it from
CRAN (stable) or GitHub (dev version):

```r
install.packages('assertthat')
devtools::install_github("hadley/assertthat")
```

### Useful built-in assertions

On top of the base R predicates, `assertthat` supplies:

- `is.flag(x)` — is `x` a single `TRUE`/`FALSE`?
- `is.string(x)` — is `x` a length-1 character vector?
- `has_name(x, nm)`, `x %has_name% nm` — does `x` have component `nm`?
- `has_attr(x, attr)`, `x %has_attr% attr` — does `x` have attribute `attr`?
- `is.count(x)` — is `x` a single positive integer?
- `are_equal(x, y)` — are `x` and `y` equal?
- `not_empty(x)` — are all dimensions of `x` greater than 0?
- `noNA(x)` — is `x` free of missing values?
- `is.dir(path)` — is `path` a directory?
- `is.writeable(path)` / `is.readable(path)` — is `path` writeable/readable?
- `has_extension(path, extension)` — does the file have the given extension?

### Three ways to fire an assertion

`assertthat` gives three functions that behave differently when the condition fails:

- `assert_that()` — signals an error and halts execution.
- `see_if()` — returns a logical value, with the error message attached as an attribute.
- `validate_that()` — returns `TRUE` on success, and the error message as a string on failure.

When the condition holds, all three simply return `TRUE` and execution continues:

```r
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

When the condition fails, the three diverge: `assert_that` raises an error and stops the function;
`see_if` and `validate_that` do not stop execution, they simply report the failure.

```r
returnStringAssert(c("a", "b"))
returnStringSeeIf(c("a", "b"))
returnStringValidate(c("a", "b"))
```

Called directly (outside a function) the same distinction shows up in what each one hands back —
an error, a `FALSE` with an attached message, or a string:

```r
assert_that(is.string(c("a", "b")))     # raises an error
see_if(is.string(c("a", "b")))          # FALSE, with the message as an attribute
validate_that(is.string(c("a", "b")))   # the message, as a string
```

### Writing your own assertions

You can define a custom assertion with its own error message in two ways. The first attaches an
`on_failure()` method to a predicate function:

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

Note that the assertions already inside `is_odd()` (numeric, length 1) still fire and still give
their own messages when they are the ones that fail — `on_failure()` only supplies the message for
the case where `is_odd` itself returns `FALSE`.

The second way is to add a message directly at the point of the check, without a separate
predicate function:

```r
is_odd2 <- function(x) {
  assert_that(is.numeric(x), length(x) == 1)
  assert_that(x %% 2 == 1, msg = paste(x, "is even"))
  x %% 2 == 1
}
assert_that(is_odd2(2))
```

## Why test, and the shape of `testthat`

Assertions check a function while it runs; unit tests check, from outside, that a function's
output is what you expect — and let you re-run exactly the same checks every time you change the
function. Hadley Wickham lists four things a formal testing framework buys you over ad hoc checking
at the command line:

1. **Fewer bugs.** A test is a second, independent statement of what the function should do, so
   you can check the code against the test rather than only against itself.
2. **Better code structure.** A test should check a small piece of behaviour, which pushes you
   toward writing smaller, more modular functions — otherwise you cannot isolate what broke.
3. **Easier restarts.** Tests record where you left off and what the next piece of work is, so
   picking a project back up does not mean re-deriving your own intentions.
4. **Robust code.** With tests in place for every part of the code, you can make a change and know
   immediately whether it broke something, and roughly where.

The `testthat` package structures testing as a two-level hierarchy:

1. **Tests**, built with `test_that()`, sit at the top. A single function usually needs several —
   one for typical input, one for missing values, one for an edge case — each grouped separately.
2. **Expectations**, built with the various `expect_*()` functions, are the individual checks
   inside a test: does the output have the right length, the right type, the right value?

### Common expectation functions

| Function | Checks |
|---|---|
| `expect_true(x)` | `x` is `TRUE` |
| `expect_false(x)` | `x` is `FALSE` |
| `expect_null(x)` | `x` is `NULL` |
| `expect_type(x, y)` | `x` is of type `y` |
| `expect_is(x, y)` | `x` is of class `y` |
| `expect_length(x, y)` | `x` is of length `y` |
| `expect_equal(x, y)` | `x` is equal to `y` |
| `expect_equivalent(x, y)` | `x` is equivalent to `y` |
| `expect_identical(x, y)` | `x` is identical to `y` |
| `expect_lt(x, y)` / `expect_gt(x, y)` | `x` is less/greater than `y` |
| `expect_lte(x, y)` / `expect_gte(x, y)` | `x` is less/greater than or equal to `y` |
| `expect_named(x)` | `x` has the expected names |
| `expect_matches(x, y)` | `x` matches the regular expression `y` |
| `expect_message(x, y)` | `x` produces the message `y` |
| `expect_warning(x, y)` | `x` produces the warning `y` |
| `expect_error(x, y)` | `x` throws the error `y` |

## Worked example: testing `standardize()`

Take a function that subtracts the mean of a vector and divides by its standard deviation, with
two pre-condition assertions guarding the input:

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

### Informal testing first

Before reaching for a formal framework, the natural thing is to try it on a few examples from the
console:

```r
a <- c(2, 4, 7, 8, 9)
z <- standardize(a)
z

mean(z)   # should be (numerically) zero
sd(z)     # should be one
```

then push on more extreme cases — a vector with a missing value, and a logical vector:

```r
y <- c(1, 2, 3, 4, NA)
standardize(y)
standardize(y, na.rm = TRUE)

alog <- c(TRUE, FALSE, FALSE, TRUE)
standardize(alog)
```

This is exactly the kind of checking that a formal test suite replaces: informal, not repeatable
without retyping, and easy to lose track of.

### Turning the checks into expectations

Fix four test vectors — a plain numeric vector, one with a missing value, a logical vector, and a
character vector — and write down what `standardize()` should do to each, as `expect_*()` calls.
For ordinary numeric input:

```r
x <- c(1, 2, 3)
z <- (x - mean(x)) / sd(x)

expect_equal(standardize(x), z)
expect_length(standardize(x), length(x))
expect_type(standardize(x), 'double')
```

A passing expectation produces no output — silence is success. A failing one raises an error, for
example if the expected value, length, or type is deliberately wrong:

```r
expect_equal(standardize(x), x)          # wrong expected output
expect_length(standardize(x), 2)         # wrong expected length
expect_type(standardize(x), 'character') # wrong expected type
```

The same pattern covers missing values, matching the two `na.rm` behaviours against `mean()` and
`sd()`'s own `na.rm` argument:

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

and a logical vector, which R will coerce to numeric before the arithmetic runs:

```r
w <- c(TRUE, FALSE, TRUE)
z <- (w - mean(w)) / sd(w)

expect_equal(standardize(w), z)
expect_length(standardize(w), length(w))
expect_type(standardize(w), 'double')
```

### Grouping expectations with `test_that()`

Each of the three blocks above is really one test — "does `standardize` behave correctly on this
kind of input?" — made of several expectations. `test_that()` takes a string describing what is
being tested, followed by the block of expectations:

```r
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

### Running the suite

Formally, tests live in a separate script, e.g. `tests-standardize.R`, and are run with
`test_file()`. Assuming the working directory holds that file:

```r
test_file("tests/tests-standardize.R")
```

All 11 expectations across the three tests pass, which is evidence — not proof — that the function
behaves as intended. To see what a failure looks like, replace `standardize()` with a broken
version, `standardizeWrong`, that adds 1 to the result, and run the corresponding test file:

```r
test_file("tests/tests-standardize-wrong.R")
```

Three tests now fail, each because the output is not equal to the value expected — and the failure
report points straight back to which expectation broke, which is the point of writing the tests as
separate, named expectations rather than one large check.

## Exercises

A standard workflow — **test-driven development** — writes the tests before the function: you
first write a test that describes the behaviour you want, then write just enough of the function to
pass it, and iterate. The following exercises practice that workflow on a function
`calculator(x, y, operation)`, which takes two numbers `x` and `y` and a string `operation` naming
which of addition, subtraction, multiplication, or division to perform, and returns a numeric
value.

1. Before writing `calculator`, write tests (in a file `tests-calculator.R`) that check it raises
   an error when `x` or `y` is not numeric, and when `operation` is not one of the four expected
   operations. Use `expect_error()`, and consider writing custom error messages for the assertions
   you will later add.
2. Write `calculator` to pass those tests, using `assertthat` to raise the errors on bad `x`, `y`,
   or `operation`. You choose what string names each operation.
3. Run `test_file("tests-calculator.R")` (from the directory containing it) and check the function
   behaves as intended.
4. Add tests to `tests-calculator.R` for the addition case specifically: `x = 1, y = 9` and
   `x = 100, y = -5`, checking both the correct numeric result and that the returned value is a
   scalar.
5. Implement addition in `calculator()` and re-run the test file.
6. Repeat the write-tests-then-implement cycle for subtraction, multiplication, and division —
   handling division by zero sensibly.
7. Time permitting, extend `calculator` with a new operation of your choice (e.g. square root),
   again writing the tests first.

## Sources

All material is from the STAT 243 (UC Berkeley, Fall 2021) section on assertions and testing,
converted from `sections/02/assertionsAndTesting.Rmd` in the `berkeley-stat243/stat243-fall-2021`
repository (CC0-1.0). No slide deck or lecture transcript was supplied for this session — the
source is the section handout itself, split across:

- `01-references-and-useful-links.md` — the external references (Hadley Wickham's "Testing"
  chapter, the `assertthat` GitHub repo, the Software Carpentry defensive-programming tutorial in
  Python — none of these were read in for this chapter, only cited as pointers) and the framing
  purpose of assertions and testing.
- `02-assertion-vs-testing.md` — the assertion-versus-test distinction and comparison table.
- `03-assertions-and-assertthat.md` — the three kinds of assertion, `assertthat` usage, the useful
  built-in assertions, `assert_that`/`see_if`/`validate_that`, and writing custom assertions.
- `04-testing.md` — the motivation for unit testing.
- `05-testthat.md` — the `testthat` hierarchy (tests and expectations) and the expectation
  function table.
- `06-testthat-example.md` — the `standardize()` worked example and the calculator practice
  problems, reproduced above as exercises.

---

[Contents](index.md) · [2. Bash Shell Tutorial and Exercises →](02-bash-shell-tutorial-and-exercises.md)
