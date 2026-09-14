---
title: 6 Functions, variable scope, and frames
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Functions, variable scope, and frames

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators, printing to the screen, etc.

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

39

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to officially as _closures_ (this is their _type_ ) - this terminology sometimes comes up in error messages.

### **6.1 Functions as objects**

Everything in R is an object, including functions. Perhaps unexpectedly, one can have a nonfunction

x <- 3 **class** (x); **typeof** (x) ## [1] "numeric" ## [1] "double" **x** (2)

**## Error in x(2): could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4 **class** (x); **typeof** (x) ## [1] "function" ## [1] "closure"

We can call a function based on the text name of the function.

myFun <- 'mean'; x <- **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] 0.347

We can also pass a function into another function as the actual function object. This is one aspect of R being a functional programming language.

40

x <- **rnorm** (10) f <- **function** (fxn, x) { **fxn** (x) } **f** (mean, x) ## [1] -0.12 _## lapply/sapply operate similarly_ **sapply** (x, abs) ## [1] 0.636 0.462 1.432 0.651 0.207 0.393 0.320 0.279 ## [9] 0.494 0.177

We can also pass in a function based on a a character vector of length one with the name of the function. Here _match.fun()_ is a handy function that extracts a function when the function is passed in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x){ **match.fun** (fxn)(x) } **f** ("mean", x) ## [1] -0.12 **f** (mean, x) ## [1] -0.12

This allows us to write functions in which the user passes in the function (as an example, this works when using _outer()_ ). Caution: one may need to think carefully about scoping issues in such contexts.

Function objects contain three components: an argument list, a body (a parsed R statement), and an environment.

41

f1 <- **function** (x) y <- x^2 f2 <- **function** (x) { y <- x^2 z <- x^3 **return** ( **list** (y, z)) } **class** (f1) ## [1] "function" **body** (f2) ## { ## y <- x^2 ## z <- x^3 ## return(list(y, z)) ## } **typeof** ( **body** (f1)); **class** ( **body** (f1)) ## [1] "language" ## [1] "<-" **typeof** ( **body** (f2)); **class** ( **body** (f2)) ## [1] "language" ## [1] "{"

We’ll see more about objects relating to the R language and parsed code in Section 9. For now, just realize that the parsed code itself is treated as an object(s) with certain types and certain classes.

#### **_do.call()_**

The _do.call()_ function will apply a function to the elements of a list. For example, we can _rbind()_ together (if compatible) the elements of a list of vectors instead of having to loop over the elements or manually type them in:

42

myList <- **list** (a = 1:3, b = 11:13, c = 21:23) **args** (rbind) ## function (..., deparse.level = 1) ## NULL **rbind** (myList$a, myList$b, myList$c) ## [,1] [,2] [,3] ## [1,] 1 2 3 ## [2,] 11 12 13 ## [3,] 21 22 23 **rbind** (myList) ## a b c ## myList Integer,3 Integer,3 Integer,3 **do.call** (rbind, myList) ## [,1] [,2] [,3] ## a 1 2 3 ## b 11 12 13 ## c 21 22 23

Why couldn’t we just use _rbind()_ directly? Basically we’re using _do.call()_ to use functions that take “...” as input (i.e., functions accepting an arbitrary number of arguments) and to use the list as the input instead (i.e., to use the list elements).

More generally do.call() is a way to pass arguments to a function where the arguments are a list:

**do.call** (mean, **list** (1:10, na.rm = TRUE)) ## [1] 5.5

### **6.2 Inputs**

Arguments can be specifed in the correct order, or given out of order by specifying _name = value_ . R first tries to match arguments by name and then by position. In general the more important

43

arguments are specified first. You can see the arguments and defaults for a function using _args()_ :

**args** (lm) ## function (formula, data, subset, weights, na.action, method = "qr", ## model = TRUE, x = FALSE, y = FALSE, qr = TRUE, singular.ok = TRUE, ## contrasts = NULL, offset, ...) ## NULL

Sometimes it can be hard to tell what arguments are required. Consider this:

**print** (sum) ## function (..., na.rm = FALSE) .Primitive("sum") **sum** () ## [1] 0 **print** (quantile) ## function (x, ...) ## UseMethod("quantile") ## <bytecode: 0x5560f687cd18> ## <environment: namespace:stats> **quantile** () **## Error in is.factor(x): argument "x" is missing, with no default**

**Challenge** : figure out where the final error actually occurs.

That said, R will error out if it is expecting an argument, rather than looking for that argument elsewhere.

x <- 1 y <- 2 myfun <- **function** (x) { **print** (y) **print** (x) }

44

**myfun** ()

---

[← 6 1965 Austra~ 95.7 24.9 4.97 1.15 ## # ... with 1 more variable: meanunemp](33-6-1965-austra-95-7-24-9-4-97-1-15-with-1-more-variable-meanu.md) · [Up: contents](index.md) · [Unit 05 — programming Part 35 — →](35-unit-05-programming-part-35.md)
