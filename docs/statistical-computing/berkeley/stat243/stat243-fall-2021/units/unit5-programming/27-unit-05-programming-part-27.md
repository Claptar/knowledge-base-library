---
title: Unit 05 — programming Part 27 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 27 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also pass in a function based on a a character vector of length one with the name of the function. Here _match.fun()_ is a handy function that extracts a function when the function is passed in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x){ **match.fun** (fxn)(x) } **f** ("mean", x) ## [1] -0.12 **f** (mean, x) ## [1] -0.12

This allows us to write functions in which the user passes in the function (as an example, this works when using _outer()_ ). Caution: one may need to think carefully about scoping issues in such contexts.

Function objects contain three components: an argument list, a body (a parsed R statement), and an environment.

f1 <- **function** (x) y <- x^2 f2 <- **function** (x) { y <- x^2 z <- x^3 **return** ( **list** (y, z)) } **class** (f1)

43

---

[← 6 Functions, frames, and variable scope](26-6-functions-frames-and-variable-scope.md) · [Up: contents](index.md) · [Unit 05 — programming Part 28 — →](28-unit-05-programming-part-28.md)
