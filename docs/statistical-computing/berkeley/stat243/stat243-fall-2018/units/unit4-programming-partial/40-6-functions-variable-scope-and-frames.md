---
title: 6 Functions, variable scope, and frames
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Functions, variable scope, and frames

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators, printing to the screen, etc.

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to officially as closures (this is their type) - this terminology sometimes comes up in error messages.

38

### 6.1 Functions as objects

Everything in R is an object, including functions.

x <- 3 **x** (2) **## Error in x(2): could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4 **class** (x); **typeof** (x) ## [1] "function" ## [1] "closure"

We can call a function based on the text name of the function.

myFun <- 'mean'; x <- **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] 0.347

We can also pass a function into another function either as the actual function object. This is one aspect of R being a functional programming language.

x <- **rnorm** (10) f <- **function** (fxn, x) { **fxn** (x) } **f** (mean, x) ## [1] -0.12

We can also pass in a function based on a a character vector of length one with the name of the function. Here match.fun() is a handy function that extracts a function when the function is passed

39

in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x){ **match.fun** (fxn)(x) } **f** ("mean", x) ## [1] -0.12 **f** (mean, x) ## [1] -0.12

This allows us to write functions in which the user passes in the function (as an example, this works when using outer()). Caution: one may need to think carefully about scoping issues in such contexts.

Function objects contain three components: an argument list, a body (a parsed R statement), and an environment.

f1 <- **function** (x) y <- x^2 f2 <- **function** (x) {y <- x^2; z <- x^3; **return** ( **list** (y, z))} **class** (f1) ## [1] "function" **body** (f2) ## { ## y <- x^2 ## z <- x^3 ## return(list(y, z)) ## } **typeof** ( **body** (f1)); **class** ( **body** (f1)) ## [1] "language" ## [1] "<-"

40

**typeof** ( **body** (f2)); **class** ( **body** (f2))

---

[← Unit 04 — programming partial Part 39 —](39-unit-04-programming-partial-part-39.md) · [Up: contents](index.md) · [[1] "language" ## [1] "{" →](41-1-language-1.md)
