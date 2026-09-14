---
title: run from R console
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# run from R console

**Source:** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

test_file("tests/tests-standardize.R")
```
We see that all 11 of the tests were passed, so it seems like our function is working as expected.

To see what the output of `test_file()` looks like when tests fail I included a version of `standarize` which adds a 1 to the end of function called `standarizeWrong` in the `functions.R` file.  In this case we expect the tests to fail and that is what we see:
```r

---

[← (assuming that your working directory is "sections/03/")](08-assuming-that-your-working-directory-is-sections-03.md) · [Up: contents](index.md) · [(assuming that your working directory is "sections/03/") →](10-assuming-that-your-working-directory-is-sections-03.md)
