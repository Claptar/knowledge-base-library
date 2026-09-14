---
title: Overview
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Overview

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## References and useful links

* [Testing section](http://r-pkgs.had.co.nz/tests.html) of the R packages tutorial by Hadley Wickham
* [GitHub](https://github.com/hadley/assertthat) for assertthat package by Hadley Wickham
* [Assertions and testing tutorial](https://swcarpentry.github.io/python-novice-inflammation/10-defensive/index.html) in Python

## Learning Objectives
  - Understand the benefits of assertions and testing as well as the differences between the two.
  - Introduction to the R package `assertthat`.
  - Introduction to the R package `testthat`.
  - Practice writing assertions and tests on your own.

## Purpose of Assertions and Testing

We all want our code to be correct the first time we write it. The unfortunate
reality is that we all make mistakes when coding, either because of "silly
mistakes" (indexing errors, incorrect syntax, using a wrong variable name, etc.)
or because of a fundamental misunderstanding of the problem we are trying to
solve. While print statements and writing test cases can help reduce coding
errors, it is desirable to have a formal, structured way to test our code to
ensure that it is functioning how we want it to. It is here that the
`assertthat` and `testthat` packages in R prove useful.


## Assertion vs. Testing

Assertions check the internal state of a function. For example, consider a
function `add(x, y)` which returns `x + y`. The function assumes `x`
is numeric, and an assertion within the body of the function would confirm that
this is in the case and return an error if not.

On the other hand, tests (sometimes referred to as "unit tests") check that a
function produces the expected output for various inputs. For example, ensuring
that `add(1, 2)` returns the number 3. Tests may include checks that assertions
are working properly, for example by confirming that an error is thrown when the
user calls `add("potato", 2)`.

Tests and assertions are similar in that,

- Both are part of ensuring programs run correctly and aspects of defensive programming.
- Both should check small pieces of the code while providing useful error messages, so they tell you exactly where the issue arises.

Here's a summary table comparing the two:

| Assertions | Tests |
|--------------------------------------------------------------------------|------------------------------------------------|
| Take the perspective of the developer. | Take the perspective of the user. |
| Assert that the developer knows what they're doing. | Test what the user can do. |
| Check internal function states. | Check function results given a specific input. |
| Typically found within a function alongside source code. | Typically kept in a directory separate from source code. |
| Can run every time the code is called. | Run periodically during development at specific moments (e.g., before creating a git commit). |
| Amount of computation should be limited to avoid slowing down source code. | For large packages with many functions, can take many minutes or even hours to run. |
| Should depend only on local states (e.g., the function's arguments and internal variables). | Can depend on global state (e.g., global options). |
| Double as inline documentation of source code. | Can be helpful for the code design process (i.e., test-driven development). |

---

[Up: contents](index.md) · [Assertions and assertthat →](02-assertions-and-assertthat.md)
