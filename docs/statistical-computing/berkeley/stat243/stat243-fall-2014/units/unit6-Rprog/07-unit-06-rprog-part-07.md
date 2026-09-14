---
title: Unit 06 — Rprog Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 07 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **object.size** (myFun2) ## 1560 bytes

**Question** : When would it be useful to have an object carried along with a function as done here?

20

### **2.3 Operators**

Operators, such as ’ _+_ ’, ’ _[_ ’ are just functions, but their arguments can occur both before and after the function call:

a <- 7; b <- 3 _# let's think about the following as a mathematical function # -- what's the function call?_ a + b ## [1] 10 **`+`** (a, b) ## [1] 10 In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘. Finally, since an operator is just a function, you can use it as an argument in various places: myList = **list** ( **list** (a = 1:5, b = "sdf"), **list** (a = 6:10, b = "wer")) myMat = **sapply** (myList, `[[`, 1) _# note that the index '1' is the additional argument to the [[ function_ x <- 1:3 y <- **c** (100, 200, 300) **outer** (x, y, `+`) ## [,1] [,2] [,3] ## [1,] 101 201 301 ## [2,] 102 202 302 ## [3,] 103 203 303 You can define your own _binary_ operator (an operator taking two arguments) using a string inside _%_ symbols: `%2%` <- **function** (a, b) { 2 * (a + b) }

21

3 %2% 7 ## [1] 20

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. We’ve already briefly seen the _drop_ argument to the ‘[‘ operator:

mat <- **matrix** (1:4, 2, 2) mat[, 1] ## [1] 1 2 mat[, 1, drop = FALSE] _# what's the difference?_ ## [,1] ## [1,] 1 ## [2,] 2

### **2.4 Unexpected functions and replacement functions**

All code in R can be viewed as a function call.

What do you think is the functional version of the following code? What are the arguments?

**if** (x > 27) { **print** (x) } **else** { **print** ("too small") }

Assignments that involve functions or operators on the left-hand side (LHS) are called _replacement expressions_ or _replacement functions._ These can be quite handy. Here are a few examples:

**diag** (mat) <- **c** (3, 2) **is.na** (vec) <- 3 **names** (df) <- **c** ("var1", "var2")

Replacement expressions are actually function calls. The R interpreter calls the replacement function (which often creates a new object that includes the replacement) and then assigns the result to the name of the original object.

22

mat <- **matrix** ( **rnorm** (4), 2, 2) **diag** (mat) <- **c** (3, 2) mat <- **`diag<-`** (mat, **c** (10, 21)) base::`diag<-` ## function (x, value) ## { ## dx <- dim(x) ## if (length(dx) != 2L) ## stop("only matrix diagonals can be replaced") ## len.i <- min(dx) ## len.v <- length(value) ## if (len.v != 1L && len.v != len.i) ## stop("replacement diagonal has wrong length") ## if (len.i) { ## i <- seq_len(len.i) ## x[cbind(i, i)] <- value ## } ## x ## } ## <bytecode: 0x3d56238> ## <environment: namespace:base>

The old version of _mat_ still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’ _mat_ ’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

You can define your own replacement functions like this, with the requirements that the last argument be named ’ _value_ ’ and that the function return the entire object:

ourClass <- **list** (name = "stat243", numStudents = 40) `name<-` <- **function** (obj, value) { obj$name <- value **return** (obj) } **name** (ourClass) <- "Statistics 243"

23

### **2.5 Functions as objects**

Note that a function is just an object.

x <- 3 **x** (2) **## Error: could not find function "x"** x <- **function** (z) z^2 **x** (2) ## [1] 4

We can call a function based on the text name of the function.

myFun = "mean" x = **rnorm** (10) **eval** ( **as.name** (myFun))(x) ## [1] -0.4761

We can also pass a function into another function either as the actual function object or as a character vector of length one with the name of the function. Here _match.fun()_ is a handy function that extracts a function when the function is passed in as an argument of a function. It looks in the calling environment for the function and can handle when the function is passed in as a function object or as a character vector of length 1 giving the function name.

f <- **function** (fxn, x) { **match.fun** (fxn)(x) } **f** ("mean", x) ## [1] -0.4761

This allows us to write functions in which the user passes in the function (as an example, this works when using _outer()_ ). Caution: one may need to think carefully about scoping issues in such contexts.

Function objects contain three components: an argument list, a body (a parsed R statement), and an environment.

24

f1 <- **function** (x) y <- x^2 f2 <- **function** (x) { y <- x^2 z <- x^3 **return** ( **list** (y, z)) } **class** (f1) ## [1] "function" **typeof** ( **body** (f1)) ## [1] "language" **class** ( **body** (f1)) ## [1] "<-" **typeof** ( **body** (f2)) ## [1] "language" **class** ( **body** (f2)) ## [1] "{"

We’ll see more about objects relating to the R language and parsed code in a later section. For now, just realize that the parsed code itself is treated as an object(s) with certain types and certain classes.

We can extract the argument object as

f4 <- **function** (x, y = 2, z = 1/y) { x + y + z } args <- **formals** (f4) args ## $x ##

25

---

[← Unit 06 — Rprog Part 06 —](06-unit-06-rprog-part-06.md) · [Up: contents](index.md) · [$y ## [1] 2 ## ## $z ## 1/y class (args) ## [1] "pairlist" →](08-z-1-y-class-args-1-pairlist.md)
