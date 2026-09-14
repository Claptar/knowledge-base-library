---
title: Unit 04 — programming partial Part 48 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 48 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can define your own binary operator (an operator taking two arguments) using a string inside % symbols. Here’s how we could do Python-style string addition:

`%+%` <- **function** (a, b) **paste0** (a, b, collapse = '') "Hi " %+% "there" ## [1] "Hi there"

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. Here’s how to pass a sometimes useful argument to the bracket operator (in this case avoiding conversion from a matrix to a vector, which can mess up subsequent code).

mat <- **matrix** (1:4, 2, 2) mat[ , 1] ## [1] 1 2 mat[ , 1, drop = FALSE] # what's the difference? ## [,1] ## [1,] 1 ## [2,] 2

### 6.6 Unexpected functions and replacement functions

All code in R can be viewed as a function call.

What do you think is the functional version of the following code? What are the arguments?

**if** (x > 27){ **print** (x) } **else** { **print** ("too small") }

49

Assignments that involve functions or operators on the left-hand side (LHS) are called replacement expressions or replacement functions. These can be quite handy. Here are a few examples:

**diag** (mat) <- **c** (3, 2) **is.na** (vec) <- 3 **names** (df) <- **c** ('var1', 'var2')

Replacement expressions are actually function calls. The R interpreter calls the replacement function (which often creates a new object that includes the replacement) and then assigns the result to the name of the original object.

mat <- **matrix** ( **rnorm** (4), 2, 2) **diag** (mat) <- **c** (3, 2) mat <- **`diag<-`** (mat, **c** (10, 21)) base::`diag<-` ## function (x, value) ## { ## dx <- dim(x) ## if (length(dx) != 2L) ## stop("only matrix diagonals can be replaced") ## len.i <- min(dx) ## len.v <- length(value) ## if (len.v != 1L && len.v != len.i) ## stop("replacement diagonal has wrong length") ## if (len.i) { ## i <- seq_len(len.i) ## x[cbind(i, i)] <- value ## } ## x ## } ## <bytecode: 0x4ae8ff0> ## <environment: namespace:base>

The old version of mat still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’mat’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

50

You can define your own replacement functions like this, with the requirements that the last argument be named ’value’ and that the function return the entire object:

yog <- **list** (firstName = 'Yogi', lastName = 'Bear') `firstName<-` <- **function** (obj, value){ obj$firstName <- value **return** (obj) } **firstName** (yog) <- 'Yogisandra'

### 6.7 Approaches to passing arguments to functions

#### 6.7.1 Pass by value vs. pass by reference

When talking about programming languages, one often distinguishes pass-by-value and pass-byreference. Pass-by-value means that when a function is called with one or more arguments, a copy is made of each argument and the function operates on those copies. Pass-by-reference means that the arguments are not copied, but rather that information is passed allowing the function to find and modify the original value of the objects passed into the function. In pass-by-value, changes to an argument made within a function do not affect the value of the argument in the calling environment. In pass-by-reference changes inside a function do affect the object outside of the function. R is (roughly) pass-by-value. R’s designers chose not to allow pass-by-reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference later in this Unit (and also note our discussion of R6 classes).

Pass-by-value is elegant and modular in that functions do not have side effects - the effect of the function occurs only through the return value of the function. However, it can be inefficient in terms of the amount of computation and of memory used. In contrast, pass-by-reference is more efficient, but also more dangerous and less modular. It’s more difficult to reason about code that uses pass-by-reference because effects of calling a function can be hidden inside the function.

An important exception is par(). If you change graphics parameters by calling par() in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** (){ oldpar <- **par** () **par** (cex = 2) # body of code

51

**par** () <- oldpar }

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot. Can you think of other R functions that have side effects?

Pointers By way of contrast to a pass-by-value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3; int* ptr; ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here ptr is the address of the integer x. Vectors in C are really pointers to a block of memory: int x[10];

In this case x will be the address of the first element of the vector. We can access the first element as x[0] or *x.

Why have we gone into this? In C, you can pass a pointer as an argument to a function. The result is that only the scalar address is copied and not the entire vector, and inside the function, one can modify the original vector, with the new value persisting on exit from the function. For example:

int myCal(int* ptr){

*<sup>ptr=</sup> *<sup>ptr+</sup> *<sup>ptr;</sup> }

When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C. Let’s see an example:

out <- rep(0, n)

out <- .C(“logLik”, out = as.double(out),

theta = as.double(theta))$out

In C, the function definition looks like this:

void logLik(double* out, double* theta)

#### 6.7.2 Promises and lazy evaluation

In actuality, R is not quite pass-by-value; rather it is call-by-value. Copying of arguments is delayed in two ways. The first is the idea of promises and lazy evaluation, described here. The second is

52

the idea of copy-on-change, described in Section 8. Basically, with copy-on-change, copies of arguments are only made if the argument is changed within the function. Until then the object in the function just refers back to the original object.

Let’s see what a promise object is. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called lazy evaluation. Instead the formal arguments are of a special type called a promise. Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- **log** (a); **return** (a*b) } **f** (7)

What’s strange about that? Another example:

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1000000))) ## user system elapsed ## 0.124 0.008 0.131 **system.time** ( **f** (3)) ## [1] "hi" ## user system elapsed ## 0 0 0 **system.time** ( **f** ( **mean** ( **rnorm** (1000000)))) ## [1] "hi" ## user system elapsed ## 0.004 0.000 0.001

Where are arguments evaluated? User-supplied arguments are evaluated in the calling frame, while default arguments are evaluated in the frame of the function:

53

z <- 3 x <- 100 f <- **function** (x, y = x*3) {x+y} **f** (z*5) ## [1] 60

Here, when f() is called, z is evaluated in the calling frame and z*5 is assigned to x in the frame of the function, while y = x*3 is evaluated in the frame of the function.

Challenge: How could I experimentally determine if the default argument is treated as a promise as well?

### 6.8 Variable scope

In this section, we seek to understand what happens in the following circumstance. Namely, where does R get the value for the object ’x’?

f <- **function** (y) { **return** (x + y) } **f** (3) ## [1] 103

To consider variable scope, we need to define the terms environment and frame. Environments and frames are closely related.

- A frame is a collection of named objects.

- An environment is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

Variables in the enclosing environment (also called the parent environment) are available within a function. This is the analog of global variables in other languages. The enclosing environment is the environment in which a function is defined, not the environment from which a function is called.

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice

54

to use variables that are taken from environments outside that of a function, but in some cases it can be useful. Here are some examples of using variables outside of the frame of a function.

x <- 3 f <- **function** () {x <- x^2; **print** (x)} **f** () x # what do you expect? f <- **function** () { **assign** ('x', x^2, env = .GlobalEnv) } ## careful: could be dangerous as a variable is changed as a side effect **f** () x f <- **function** (x) { x <<- x^2 } ## careful: could be dangerous as a variable is changed as a side effect **f** (5) x

Let’s dig deeper to understand where R looks for non-local variables. R looks for variables that are not local to a function in the enclosing environment of the function, where the enclosing environment is the environment in which the function was defined. Note that the enclosing/parent environment is NOT the environment from which the function was called. This approach is called lexical scoping.

Here are some examples to illustrate scope:

x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () # what will happen? f <- **function** () { f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () # what will happen?

55

f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () # what will happen?

Here’s a somewhat tricky example:

y <- 100 f <- **function** (){ y <- 10 g <- **function** (x) x + y **return** (g) } ## you can think of f() as a function constructor h <- **f** () **h** (3) ## [1] 13

Let’s work through this:

1. What is the enclosing environment of the function g()?

2. What does g() use for y?

3. When f() finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of h()?

This code helps explain things, but it’s a bit confusing because environment() gives back different results depending on whether it is given a function as its argument. If given a function, it returns the enclosing environment for that function. If given no argument, it returns the current execution environment.

**environment** (h) # enclosing environment of h()

---

[← Unit 04 — programming partial Part 47 —](47-unit-04-programming-partial-part-47.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 49 — →](49-unit-04-programming-partial-part-49.md)
