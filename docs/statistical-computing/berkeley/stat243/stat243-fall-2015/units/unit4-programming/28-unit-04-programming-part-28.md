---
title: Unit 04 — programming Part 28 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 28 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Why couldn’t we just use _rbind()_ directly? Basically we’re using _do.call()_ to use functions that take “...” as input (i.e., functions accepting an arbitrary number of arguments) and to use the list as the input instead (i.e., to use the list elements).

More generally do.call() is a way to pass arguments to a function where the arguments are a list:

**do.call** (mean, **list** (1:10, na.rm = TRUE)) ## [1] 5.5

37

### **6.2 Inputs**

Arguments can be specifed in the correct order, or given out of order by specifying _name = value_ . R first tries to match arguments by name and then by position. In general the more important arguments are specified first. You can see the arguments and defaults for a function using _args()_ :

**args** (lm) ## function (formula, data, subset, weights, na.action, method = "qr", ## model = TRUE, x = FALSE, y = FALSE, qr = TRUE, singular.ok = TRUE, ## contrasts = NULL, offset, ...) ## NULL

Functions may have unspecified arguments, which are designated using ’...’. Unspecified arguments occurring at the beginning of the argument list are generally a collection of like objects that will be manipulated (consider _paste()_ , _c()_ , and _rbind()_ ), while unspecified arguments occurring at the end are often optional arguments (consider _plot()_ ). These optional arguments are sometimes passed along to a function within the function. For example, here’s my own wrapper for plotting, where any additional arguments specified by the user will get passed along to plot:

pplot <- **function** (x, y, pch = 16, cex = 0.4, ...) { **plot** (x, y, pch = pch, cex = cex, ...) }

If you want to manipulate what the user passed in as the _..._ args, rather than just passing them along, you can extract them (the following code would be used within a function to which _’...’_ is an argument:

myFun <- **function** (...){ **print** (..2) args <- **list** (...) **print** (args[[2]]) } **myFun** (1,3,5,7) ## [1] 3 ## [1] 3

38

You can check if an argument is missing with _missing()_ . Arguments can also have default values, which may be _NULL_ . If you are writing a function and designate the default as _argname = NULL_ , you can check whether the user provided anything using is.null(argname). The default values can also relate to other arguments. As an example, consider _dgamma()_ :

**args** (dgamma) ## function (x, shape, rate = 1, scale = 1/rate, log = FALSE) ## NULL

Functions can be passed in as arguments (e.g., see the variants of _apply()_ ). Note that one does not need to pass in a named function - you can create the function on the spot - this is called an _anonymous function_ (also called a _lambda function_ in some languages such as Python):

mat <- **matrix** (1:9, 3) **apply** (mat, 1, min) _# apply() uses match.fun()_ ## [1] 1 2 3 **apply** (mat, 2, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 1 1 1 ## [3,] 2 2 2 **apply** (mat, 1, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 3 3 3 ## [3,] 6 6 6 _# explain why the result of the last expression is transposed_

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

39

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f) ## $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y **class** ( **formals** (f)) ## [1] "pairlist"

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE) _# what do you think quote does? Why is it needed?_

### **6.3 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function, and allows the function to exit as soon as it is done.

40

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9 **f** (3) _invisible(x)_ will return _x_ and the result can be not be printed if not assigned: f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

### **6.4 Approaches to passing arguments to functions**

#### **6.4.1 Pass by value vs. pass by reference**

When talking about programming languages, one often distinguishes _pass-by-value_ and _pass-byreference_ . Pass-by-value means that when a function is called with one or more arguments, a copy

41

is made of each argument and the function operates on those copies. Pass-by-reference means that the arguments are not copied, but rather that information is passed allowing the function to find and modify the original value of the objects passed into the function. In pass-by-value, changes to an argument made within a function do not affect the value of the argument in the calling environment. In pass-by-reference changes inside a function do affect the object outside of the function. R’s designers chose not to allow pass by reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference later in this Unit.

Pass-by-value is elegant and modular in that functions do not have side effects - the effect of the function occurs only through the return value of the function. However, it can be inefficient in terms of the amount of computation and of memory used. In contrast, pass-by-reference is more efficient, but also more dangerous and less modular. It’s more difficult to reason about code that uses pass-by-reference because effects of calling a function can be hidden inside the function.

An important exception is _par()_ . If you change graphics parameters by calling _par()_ in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** (){ oldpar <- **par** () **par** (cex = 2) _# body of code_ **par** () <- oldpar }

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot. Can you think of other R functions that have side effects?

**Pointers** By way of contrast to a pass-by-value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3; int* ptr; ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here _ptr_ is the address of the integer _x_ . Vectors in C are really pointers to a block of memory:

int x[10];

42

In this case _x_ will be the address of the first element of the vector. We can access the first element as x[0] or *x.

Why have we gone into this? In C, you can pass a pointer as an argument to a function. The result is that only the scalar address is copied and not the entire vector, and inside the function, one can modify the original vector, with the new value persisting on exit from the function. For example:

int myCal(int *ptr){

*<sup>ptr=</sup> *<sup>ptr+</sup> *<sup>ptr;</sup> }

When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C. Let’s see an example:

out <- rep(0, n) out <- .C(“logLik”, out = as.double(out), theta = as.double(theta))$out

In C, the function definition looks like this:

void logLik(double* out, double* theta)

#### **6.4.2 Promises and lazy evaluation**

In actuality, R is not quite pass-by-value; rather it is _call-by-value_ . Copying of arguments is delayed in two ways. The first is the idea of promises and lazy evaluation, described here. The second is the idea of _copy-on-change_ , described in Section 8. Basically, with copy-on-change, copies of arguments are only made if the argument is changed within the function. Until then the object in the function just refers back to the original object.

Let’s see what a _promise_ object is. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called _lazy evaluation_ . Instead the formal arguments are of a special type called a _promise_ . Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- **log** (a); **return** (a*b) } **f** (7)

What’s strange about that? Another example:

43

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1000000))) ## user system elapsed ## 0.112 0.004 0.117 **system.time** ( **f** (3)) ## [1] "hi" ## user system elapsed ## 0 0 0 **system.time** ( **f** ( **mean** ( **rnorm** (1000000)))) ## [1] "hi" ## user system elapsed ## 0 0 0

**Where are arguments evaluated?** User-supplied arguments are evaluated in the calling frame, while default arguments are evaluated in the frame of the function:

z <- 3 x <- 100 f <- **function** (x, y = x*3) {x+y} **f** (z*5) ## [1] 60

Here, when _f()_ is called, _z_ is evaluated in the calling frame and z*5 is assigned to _x_ in the frame of the function, while y = x*3 is evaluated in the frame of the function.

### **6.5 Operators**

Operators, such as ’ _+_ ’, ’ _[_ ’ are just functions, but their arguments can occur both before and after the function call:

44

a <- 7; b <- 3 _# let's think about the following as a mathematical function # -- what's the function call?_ a + b ## [1] 10 **`+`** (a, b) ## [1] 10

In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘.

Finally, since an operator is just a function, you can use it as an argument in various places:

myList <- **list** ( **list** (a = 1:5, b = "sdf"), **list** (a = 6:10, b = "wer")) myMat <- **sapply** (myList, `[[`, 1) _# note that the index "1" is the additional argument to the [[ function_ x <- 1:3; y <- **c** (100,200,300) **outer** (x, y, `+`) ## [,1] [,2] [,3] ## [1,] 101 201 301 ## [2,] 102 202 302 ## [3,] 103 203 303

You can define your own _binary_ operator (an operator taking two arguments) using a string inside _%_ symbols:

`%+%` <- **function** (a, b) **paste0** (a, b, collapse = '') "Hi " %+% "there" ## [1] "Hi there"

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. Here’s how to pass a sometimes useful argument to the bracket operator (in this case avoiding conversion from a matrix to a vector, which can mess up subsequent code).

45

mat <- **matrix** (1:4, 2, 2) mat[ , 1] ## [1] 1 2 mat[ , 1, drop = FALSE] _# what's the difference?_ ## [,1] ## [1,] 1 ## [2,] 2

### **6.6 Unexpected functions and replacement functions**

All code in R can be viewed as a function call.

What do you think is the functional version of the following code? What are the arguments?

**if** (x > 27){ **print** (x) } **else** { **print** ("too small") }

Assignments that involve functions or operators on the left-hand side (LHS) are called _replacement expressions_ or _replacement functions._ These can be quite handy. Here are a few examples:

**diag** (mat) <- **c** (3, 2) **is.na** (vec) <- 3 **names** (df) <- **c** ('var1', 'var2')

Replacement expressions are actually function calls. The R interpreter calls the replacement function (which often creates a new object that includes the replacement) and then assigns the result to the name of the original object.

mat <- **matrix** ( **rnorm** (4), 2, 2) **diag** (mat) <- **c** (3, 2) mat <- **`diag<-`** (mat, **c** (10, 21)) base::`diag<-`

46

---

[← [1] 0.238 f (mean, x) ## [1] 0.238](27-1-0-238-f-mean-x-1-0-238.md) · [Up: contents](index.md) · [Unit 04 — programming Part 29 — →](29-unit-04-programming-part-29.md)
