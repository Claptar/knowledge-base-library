---
title: run from R console
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/02/assertionsAndTesting.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# run from R console

**Source:** [`labs/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/02/assertionsAndTesting.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

test_file("tests/tests-standardize.R")
```
We see that all 11 of the tests were passed, so it seems like our function is working as expected.

To see what the output of `test_file()` looks like when tests fail I included a version of `standarize` which adds a 1 to the end of function called `standarizeWrong` in the `functions.R` file.  In this case we expect the tests to fail and that is what we see:
```r

---

[← (assuming that your working directory is "sections/03/")](10-assuming-that-your-working-directory-is-sections-03.md) · [Up: contents](index.md) · [(assuming that your working directory is "sections/03/") →](12-assuming-that-your-working-directory-is-sections-03.md)
