---
title: 6 Functions, frames, and variable scope
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Functions, frames, and variable scope

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators (such as addition, subtraction, etc.), printing to the screen, etc.

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to officially as _closures_ (this is their _type_ ) - this terminology sometimes comes up in error messages.

What happens when an R function is evaluated? The user-provided function arguments are evaluated in the calling environment and the results are matched to the argument names in the function definition. A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments. The body of the function is evaluated in the environment. Any look-up of variables not found in the environment is done using R’s lexical scoping rules to look in the series of enclosing environments. When the function finishes, the return value is passed back to the calling frame and the function frame is taken off the stack. The environment is removed, unless the environment serves as the enclosing environment of another environment.

I’m not expecting you to fully understand that previous paragraph and all the terms in it. We’ll see all the details in this section.

41

### **6.1 Functions as objects**

Everything in R is an object, including functions. We can assign functions to variables in the same way we assign numeric and other values.

x <- 3 **class** (x); **typeof** (x) ## [1] "numeric" ## [1] "double" **x** (2) **## Error in x(2): could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4 **class** (x); **typeof** (x) ## [1] "function" ## [1] "closure"

We can call a function based on the text name of the function.

myFun <- 'mean'; x <- **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] 0.347

We can also pass a function into another function as the actual function object. This is one aspect of R being a functional programming language.

x <- **rnorm** (10) f <- **function** (fxn, x) { **fxn** (x) } **f** (mean, x)

42

---

[← Error : Must group by variables found in .data . ## Column groupvar is not found.](25-error-must-group-by-variables-found-in-data-column-groupvar.md) · [Up: contents](index.md) · [Unit 05 — programming Part 27 — →](27-unit-05-programming-part-27.md)
