---
title: 6 Functions, variable scope, and frames
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Functions, variable scope, and frames

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators (such as addition, subtraction, etc.), printing to the screen, etc.

40

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to officially as _closures_ (this is their _type_ ) - this terminology sometimes comes up in error messages.

What happens when an R function is evaluated? The user-provided function arguments are evaluated in the calling environment and the results are matched to the argument names in the function definition. A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments. The body of the function is evaluated in the environment. Any look-up of variables not found in the environment is done using R’s lexical scoping rules to look in the series of enclosing environments. When the function finishes, the return value is passed back to the calling frame and the function frame is taken off the stack. The environment is removed, unless the environment serves as the enclosing environment of another environment.

I’m not expecting you to fully understand that previous paragraph and all the terms in it. We’ll see all the details in this section.

### **6.1 Functions as objects**

Everything in R is an object, including functions. We can assign functions to variables in the same way we assign numeric and other values.

x <- 3 **class** (x); **typeof** (x) ## [1] "numeric" ## [1] "double" **x** (2) **## Error in x(2): could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4 **class** (x); **typeof** (x) ## [1] "function" ## [1] "closure"

41

We can call a function based on the text name of the function.

myFun <- 'mean'; x <- **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] 0.347

We can also pass a function into another function as the actual function object. This is one aspect of R being a functional programming language.

x <- **rnorm** (10) f <- **function** (fxn, x) { **fxn** (x) } **f** (mean, x) ## [1] -0.12 _## lapply/sapply operate similarly_ **sapply** (x, abs) ## [1] 0.636 0.462 1.432 0.651 0.207 0.393 0.320 0.279 ## [9] 0.494 0.177

We can also pass in a function based on a a character vector of length one with the name of the function. Here _match.fun()_ is a handy function that extracts a function when the function is passed in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x){ **match.fun** (fxn)(x) } **f** ("mean", x) ## [1] -0.12 **f** (mean, x) ## [1] -0.12

42

This allows us to write functions in which the user passes in the function (as an example, this works when using _outer()_ ). Caution: one may need to think carefully about scoping issues in such contexts.

Function objects contain three components: an argument list, a body (a parsed R statement), and an environment.

f1 <- **function** (x) y <- x^2 f2 <- **function** (x) { y <- x^2 z <- x^3 **return** ( **list** (y, z)) } **class** (f1) ## [1] "function" **body** (f2) ## { ## y <- x^2 ## z <- x^3 ## return(list(y, z)) ## } **typeof** ( **body** (f1)); **class** ( **body** (f1)) ## [1] "language" ## [1] "<-" **typeof** ( **body** (f2)); **class** ( **body** (f2)) ## [1] "language" ## [1] "{"

We’ll see more about objects relating to the R language and parsed code in Section 9. For now, just realize that the parsed code itself is treated as an object(s) with certain types and certain classes.

43

#### **_do.call()_**

The _do.call()_ function will apply a function to the elements of a list. For example, we can _rbind()_ together (if compatible) the elements of a list of vectors instead of having to loop over the elements or manually type them in:

myList <- **list** (a = 1:3, b = 11:13, c = 21:23) **args** (rbind) ## function (..., deparse.level = 1) ## NULL **rbind** (myList$a, myList$b, myList$c)

---

[← Unit 05 — programming Part 29 —](29-unit-05-programming-part-29.md) · [Up: contents](index.md) · [Unit 05 — programming Part 31 — →](31-unit-05-programming-part-31.md)
