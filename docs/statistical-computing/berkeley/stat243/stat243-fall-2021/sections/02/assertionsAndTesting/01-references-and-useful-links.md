---
title: References and useful links
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# References and useful links

```r
knitr::opts_chunk$set(echo = TRUE)
library(assertthat)
library(testthat)
```

* [Testing section](http://r-pkgs.had.co.nz/tests.html) of the R packages tutorial by Hadley Wickham
* [GitHub](https://github.com/hadley/assertthat) for assertthat package by Hadley Wickham
* [Assertions and testing tutorial](https://swcarpentry.github.io/python-novice-inflammation/10-defensive/index.html) in Python

## Learning Objectives
  - Understand the benefits of assertions and testings as well as the differences between the two.
  - Introduction to the R package `assertthat`.
  - Introduction to the R package `testthat`.
  - Practice writing assertions and tests on your own.

## Purpose of Assertions and Testing
We all want our code   to be correct the first time we write it. The unfortunate reality is that we all make mistakes when coding, either because of "silly mistakes" (indexing errors,   incorrect syntax,  using a wrong variable name, etc.) or because of a fundamental misunderstanding of the problem we are trying to solve. While print statements and writing test cases can help reduce coding errors, it is desirable to have a formal, structured way to test our code to ensure that it is functioning how we want it to. It is here that the `assertthat` and `testthat` packages in R prove useful.

---

[Up: contents](index.md) · [Assertion vs. Testing →](02-assertion-vs-testing.md)
