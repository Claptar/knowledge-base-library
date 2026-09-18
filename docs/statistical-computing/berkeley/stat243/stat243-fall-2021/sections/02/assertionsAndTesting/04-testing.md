---
title: Testing
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/02/assertionsAndTesting.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/02/assertionsAndTesting.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/02/assertionsAndTesting.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Testing

Assertions allow us to check aspects of functions as they are being excuted, while unit tests
help ensure the output from a function is what we expect.  A common approach to testing is to use the command line to informally check whether your code works on a few examples.  Units tests are a more formal framework for testing that allows you to continue running the same tests as you update your function.  Hadley Wickam describes four main areas that proper testings will help improve your code:

  1. **Fewer bugs**: When setting up unit tests you have a formal place that describes your expectation of function behavior.  Having two places where the function is document allows you to check one against the other.
  2. **Better code structure**: Tests should only check accuracy of small portions of code, so that you can easily find the source of error.  This forces you to write more modular code.
  3. **Easier restarts**: Tests help you remember where you left off and what the next step in your code should be.  It is good practice to write tests first, followed by the function to execute the desired result.
  4. **Robust code**: By having tests in place for all portions of your code you can make changes while knowing that you can easily check if those changes produce an error and where to go to fix it.

---

[← Assertions and assertthat](03-assertions-and-assertthat.md) · [Up: contents](index.md) · [testthat →](05-testthat.md)
