---
title: run from R console
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S02/testingAssertion.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# run from R console

**Source:** [`lab/S02/testingAssertion.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/testingAssertion.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

library(testthat)
test_file("tests.R")
```

If all tests are okay, you should be able to see some output similar to the
screenshot below:

![Basic R-GUI console](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2018/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S02/test-report.png)

## Exercise

### Write your own context file

Write a test file for the `standardize()` function which contains at least 2 tests and each test contains 2 expectations. Create a folder `lab`, under which create `S02`, then push this test file into that directory.

### Problem 3 of PS1

What assertions and unit tests can you think of for this problem?

---

[← (assuming that your working directory is "code/")](11-assuming-that-your-working-directory-is-code.md) · [Up: contents](index.md)
