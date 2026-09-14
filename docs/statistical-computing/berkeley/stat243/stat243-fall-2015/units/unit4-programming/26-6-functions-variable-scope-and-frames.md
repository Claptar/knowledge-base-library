---
title: 6 Functions, variable scope, and frames
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Functions, variable scope, and frames

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators, printing to the screen, etc.

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

34

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to offically as _closures_ (this is their _type_ ) - this terminology sometimes comes up in error messages.

### **6.1 Functions as objects**

Everything in R is an object, including functions.

x <- 3 **x** (2)

**## Error in eval(expr, envir, enclos): could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4 **class** (x); **typeof** (x) ## [1] "function" ## [1] "closure"

We can call a function based on the text name of the function.

myFun <- 'mean'; x <- **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] 0.238

We can also pass a function into another function either as the actual function object or as a character vector of length one with the name of the function. Here _match.fun()_ is a handy function that extracts a function when the function is passed in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x){ **match.fun** (fxn)(x) } **f** ("mean", x)

35

---

[← 5 Standard dataset manipulations](25-5-standard-dataset-manipulations.md) · [Up: contents](index.md) · [[1] 0.238 f (mean, x) ## [1] 0.238 →](27-1-0-238-f-mean-x-1-0-238.md)
