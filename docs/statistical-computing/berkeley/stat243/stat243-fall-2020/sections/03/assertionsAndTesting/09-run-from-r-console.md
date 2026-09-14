---
title: run from R console
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/03/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# run from R console

**Source:** [`sections/03/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

test_file("tests/tests-standardize.R")
```
We see that all 11 of the tests were passed, so it seems like our function is working as expected.

To see what the output of `test_file()` looks like when tests fail I included a version of `standarize` which adds a 1 to the end of function called `standarizeWrong` in the `functions.R` file.  In this case we expect the tests to fail and that is what we see:
```r

---

[← (assuming that your working directory is "sections/03/")](08-assuming-that-your-working-directory-is-sections-03.md) · [Up: contents](index.md) · [(assuming that your working directory is "sections/03/") →](10-assuming-that-your-working-directory-is-sections-03.md)
