---
title: '$x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist"'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist"

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE) _## what do you think quote does? Why is it needed?_

### **6.3 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function, and allows the function to exit as soon as it is done.

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9

47

**<mark>f</mark>** <mark>(3)</mark>

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

### **6.4 Frames and the call stack**

R keeps track of the call stack, which is the series of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the frame from which a function was called.

Some terminology: for our purposes we’ll use the terms _frame_ and _environment_ somewhat interchangeably for the moment. A _frame_ or _environment_ is a collection of named objects. (Note that when we talk about variable scope in Section 6.8, we’ll have to be more careful with our terminology.)

_sys.nframe()_ returns the number of the current frame/environment and _sys.parent()_ the number of the parent, while _parent.frame()_ gives the name of the frame/environment of the parent (i.e., the calling) frame. _sys.frame()_ gives the name of the frame/environment for a given frame number (for

48

non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the frame/environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

_## NOTE: run this chunk outside RStudio as it seems to ## inject additional frames_ **sys.nframe** () f <- **function** () { **cat** ('f: Frame number is ', **sys.nframe** (), '; parent frame number is ', **sys.parent** (), '.\n', sep = '') **cat** ('f: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f: Parent is ') **print** ( **parent.frame** ()) **cat** ('f: Two frames up is ') **print** ( **sys.frame** (-2)) } **f** () f2 <- **function** () { **cat** ('f2: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f2: Parent is ') **print** ( **parent.frame** ()) **f** () } **f2** ()

Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ .

_## exploring functions that give us information the frames in the stack_ g <- **function** (y) { gg <- **function** () { _## this gives us the information from sys.calls(), ## sys.parents() and sys.frames() as one object ## print(sys.status())_ tmp <- **sys.status** ()

49

**print** (tmp) } **if** (y > 0) **g** (y-1) **else gg** () } **g** (3)

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **6.5 Operators**

Operators, such as ’ _+_ ’, ’ _[_ ’ are just functions, but their arguments can occur both before and after the function call:

a <- 7; b <- 3 _# let's think about the following as a mathematical function # -- what's the function call?_ a + b ## [1] 10 **`+`** (a, b) ## [1] 10

In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘.

Finally, since an operator is just a function, you can use it as an argument in various places:

x <- 1:3; y <- **c** (100,200,300) **outer** (x, y, `+`) ## [,1] [,2] [,3] ## [1,] 101 201 301 ## [2,] 102 202 302 ## [3,] 103 203 303

50

|my|List|<- **list**(**list**(a = 'new york', b = 1:5), **list**(a = 'california', b = 6:1|
|---|---|---|
|re|sult|<- **lapply**(myList, `[[`, 2)|
|re|sult||
|##|[[1]|]|
|##|[1]|1 2 3 4 5|
|##|||
|##|[[2]|]|
|##|[1]|6<br>7<br>8<br>9 10|
|_## _|_note_|_that the index "2" is the additional argument to the [[ function_|
|my|Mat <|- **sapply**(myList, `[[`, 2)|
|my|Mat||
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|
|##|[3,]|3<br>8|
|##|[4,]|4<br>9|
|##|[5,]|5<br>10|
|**cb**|**ind**(m|yList[[1]][[2]], myList[[2]][[2]])<br>_## equivalent but doesn't scale_|
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|
|##|[3,]|3<br>8|
|##|[4,]|4<br>9|
|##|[5,]|5<br>10|


You can define your own _binary_ operator (an operator taking two arguments) using a string inside _%_ symbols. Here’s how we could do Python-style string addition:

`%+%` <- **function** (a, b) **paste0** (a, b, collapse = '') "Hi " %+% "there" ## [1] "Hi there"

51

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. Here’s how to pass a sometimes useful argument to the bracket operator (in this case avoiding conversion from a matrix to a vector, which can mess up subsequent code).

mat <- **matrix** (1:4, 2, 2) mat[ , 1] ## [1] 1 2 mat[ , 1, drop = FALSE] _# what's the difference?_ ## [,1] ## [1,] 1 ## [2,] 2

### **6.6 Unexpected functions and replacement functions**

All code in R can be viewed as a function call.

What do you think is the functional version of the following code? What are the arguments?

**if** (x > 27){ **print** (x) } **else** { **print** ("too small") }

Assignments that involve functions or operators on the left-hand side (LHS) are called _replacement expressions_ or _replacement functions._ These can be quite handy. Here are a few examples:

**diag** (mat) <- **c** (3, 2) **is.na** (vec) <- 3 **names** (df) <- **c** ('var1', 'var2')

Replacement expressions are actually function calls. The R interpreter calls the replacement function (which often creates a new object that includes the replacement) and then assigns the result to the name of the original object.

52

mat <- **matrix** ( **rnorm** (4), 2, 2) **diag** (mat) <- **c** (3, 2) mat <- **`diag<-`** (mat, **c** (10, 21)) base::`diag<-` ## function (x, value) ## { ## dx <- dim(x) ## if (length(dx) != 2L) ## stop("only matrix diagonals can be replaced") ## len.i <- min(dx) ## len.v <- length(value) ## if (len.v != 1L && len.v != len.i) ## stop("replacement diagonal has wrong length") ## if (len.i) { ## i <- seq_len(len.i) ## x[cbind(i, i)] <- value ## } ## x ## } ## <bytecode: 0x5560f7532110> ## <environment: namespace:base>

The old version of _mat_ still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’ _mat_ ’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

You can define your own replacement functions like this, with the requirements that the last argument be named ’ _value_ ’ and that the function return the entire object:

yog <- **list** (firstName = 'Yogi', lastName = 'Bear') `firstName<-` <- **function** (obj, value){ obj$firstName <- value **return** (obj) } **firstName** (yog) <- 'Yogisandra'

53

### **6.7 Approaches to passing arguments to functions**

#### **6.7.1 Pass by value vs. pass by reference**

When talking about programming languages, one often distinguishes _pass-by-value_ and _pass-byreference_ . Pass-by-value means that when a function is called with one or more arguments, a copy is made of each argument and the function operates on those copies. Pass-by-reference means that the arguments are not copied, but rather that information is passed allowing the function to find and modify the original value of the objects passed into the function. In pass-by-value, changes to an argument made within a function do not affect the value of the argument in the calling environment. In pass-by-reference changes inside a function do affect the object outside of the function. R is (roughly) pass-by-value. R’s designers chose not to allow pass-by-reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference later in this Unit (and also note our discussion of R6 classes).

Pass-by-value is elegant and modular in that functions do not have side effects - the effect of the function occurs only through the return value of the function. However, it can be inefficient in terms of the amount of computation and of memory used. In contrast, pass-by-reference is more efficient, but also more dangerous and less modular. It’s more difficult to reason about code that uses pass-by-reference because effects of calling a function can be hidden inside the function.

An important exception is _par()_ . If you change graphics parameters by calling _par()_ in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** (){ oldpar <- **par** () **par** (cex = 2) _# body of code_ **par** () <- oldpar }

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot. Can you think of other R functions that have side effects?

**Pointers** By way of contrast to a pass-by-value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3; int* ptr;

54

ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here _ptr_ is the address of the integer _x_ . Vectors in C are really pointers to a block of memory:

int x[10];

In this case _x_ will be the address of the first element of the vector. We can access the first element as x[0] or *x.

Why have we gone into this? In C, you can pass a pointer as an argument to a function. The result is that only the scalar address is copied and not the entire vector, and inside the function, one can modify the original vector, with the new value persisting on exit from the function. For example:

int myCal(int* ptr){

*<sup>ptr=</sup> *<sup>ptr+</sup> *<sup>ptr;</sup> }

When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C. For example, using the old .C syntax, here’s an example:

out <- rep(0, n)

out <- .C(“logLik”, out = as.double(out), theta = as.double(theta))$out

In C, the function definition looks like this:

void logLik(double* out, double* theta)

**Pointers in R?** Are there pointers in R? From a user perspective, one might say ’no’, because an R programmer can’t use pointers explicitly. But pointer-like behavior is occurring behind the scenes in lots of ways:

- Lists in R are essentially vectors of pointers to the elements of the list

- Character vectors in R are essentially pointers to the individual character strings.

- Environments (see Section 6.11) behave like pointers and are passed by reference rather than by copy.

#### **6.7.2 Promises and lazy evaluation**

In actuality, R is not quite pass-by-value; rather it is _call-by-value_ . Copying of arguments is delayed in two ways. The first is the idea of promises and lazy evaluation, described here. The second is the idea of _copy-on-change_ , described in Section 8. Basically, with copy-on-change, copies of

55

arguments are only made if the argument is changed within the function. Until then the object in the function just refers back to the original object.

Let’s see what a _promise_ object is. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called _lazy evaluation_ . Instead the formal arguments are of a special type called a _promise_ . Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- **log** (a); **return** (a*b) } **f** (7) d <- 100 **f** (7)

What’s strange about that? Another example:

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1000000))) ## user system elapsed ## 0.070 0.004 0.074 **system.time** ( **f** (3)) ## [1] "hi" ## user system elapsed ## 0.001 0.000 0.001 **system.time** ( **f** ( **mean** ( **rnorm** (1000000)))) ## [1] "hi" ## user system elapsed ## 0.001 0.000 0.001

Lazy evaluation is not just an R thing. It also occurs in Spark and in the Python Dask package. The basic idea is to delay executation until it’s really needed, with the goal that if one does so,

56

the system may be able to better optimize a series of multiple steps as a joint operation relative to executing them one by one.

**Where are arguments evaluated?** User-supplied arguments are evaluated in the calling frame, while default arguments are evaluated in the frame of the function:

z <- 3 x <- 100 f <- **function** (x, y = x*3) {x+y} **f** (z*5) ## [1] 60

Here, when _f()_ is called, _z_ is evaluated in the calling frame and z*5 is assigned to _x_ in the frame of the function, while y = x*3 is evaluated in the frame of the function.

Challenge: How could I experimentally determine if the default argument is treated as a promise as well?

### **6.8 Variable scope**

In this section, we seek to understand what happens in the following circumstance. Namely, where does R get the value for the object ’x’?

f <- **function** (y) { **return** (x + y) } **f** (3) ## [1] 103

To consider variable scope, we need to define the terms _environment_ and _frame_ . Environments and frames are closely related.

- A _frame_ is a collection of named objects.

- An _environment_ is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

57

Variables in the enclosing environment (also called the parent environment) are available within a function. This is the analog of _global variables_ in other languages. The enclosing environment is the environment in which a function is defined, not the environment from which a function is called.

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice to use variables that are taken from environments outside that of a function, but in some cases it can be useful. Here are some examples of using variables outside of the frame of a function.

x <- 3 f <- **function** () {x <- x^2; **print** (x)} **f** () x _# what do you expect?_ f <- **function** () { **assign** ('x', x^2, env = .GlobalEnv) } _## careful: could be dangerous as a variable is changed as a side effect_ **f** () x f <- **function** (x) { x <<- x^2 } _## careful: could be dangerous as a variable is changed as a side effect_ **f** (5) x

Let’s dig deeper to understand where R looks for non-local variables. **R looks for variables that are not local to a function in the enclosing environment of the function, where the enclosing environment is the environment in which the function was defined.** Note that the enclosing/parent environment is NOT the environment from which the function was called. This approach is called _lexical scoping_ .

Here are some examples to illustrate scope:

f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () _# what will happen?_ f <- **function** () {

58

f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () _# what will happen?_ x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () _# what will happen?_

Here’s a somewhat tricky example:

y <- 100 f <- **function** (){ y <- 10 g <- **function** (x) { **return** (x + y + **rnorm** (1)) } **return** (g) } _## you can think of f() as a function constructor_ h <- **f** () **h** (3) ## [1] 14

Let’s work through this:

1. What is the enclosing environment of the function _g()_ ?

2. What does _g()_ use for _y_ ?

3. When _f()_ finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of _h()_ ?

59

This code helps explain things, but it’s a bit confusing because _environment()_ gives back different results depending on whether it is given a function as its argument. If given a function, it returns the enclosing environment for that function. If given no argument, it returns the current execution environment.

**environment** (h) _# enclosing environment of h()_ ## <environment: 0x5560fab103c8> **ls** ( **environment** (h)) _# objects in that environment_ ## [1] "g" "y" f <- **function** (){ **print** ( **environment** ()) _# execution environment of f()_ y <- 10 g <- **function** (x) x + y **return** (g) } h <- **f** () ## <environment: 0x5560fc48e7c0> **environment** (h) ## <environment: 0x5560fc48e7c0> **h** (3) ## [1] 13 **environment** (h)$y ## [1] 10 _## advanced: explain this:_ **environment** (h)$g ## function(x) x + y ## <environment: 0x5560fc48e7c0>

60

**Comprehension problem** Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (1) **rnorm** (1) ## [1] -0.626 **save** (.Random.seed, file = 'tmp.Rda') **rnorm** (1) ## [1] 0.184 tmp <- **function** () { **load** ('tmp.Rda') **print** ( **rnorm** (1)) } **tmp** () ## [1] -0.836

Question: what was I hoping that code to do, and why didn’t it work?

**Detecting non-local variables** We can use _codetools::findGlobals_ to detect non-local variables when we are programming.

**library** (codetools) f <- **function** () { y <- 3 **print** (x + y) } **findGlobals** (f) ## [1] "{" "+" "<-" "print" "x"

Is that result what you would expect? What does it say about my statement that using non-local variables is a bad idea?

61

### **6.9 Environments and the search path**

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve seen, these environments are not the environments of the calling function(s) - i.e., they are _not_ the frames on the stack (see the next Section).

By default objects are created in the global environment, _.GlobalEnv_ . As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and based on lexical scoping this is next place that is searched if an object can’t be found in the frame of the function call. As an example, if an object couldn’t be found within the environment of an _lm()_ function call, R would first look in the environment (i.e., the _namespace_ ) of the stats package (since this is the environment where _lm()_ is defined and is therefore the enclosing environment for _lm()_ ), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with _search()_ . The search path is a set of additional environments. Generally packages are created with namespaces, i.e., each has its own environment, as we see based on _search()_ .

**search** ()

---

[← Unit 05 — programming Part 36 —](36-unit-05-programming-part-36.md) · [Up: contents](index.md) · [Unit 05 — programming Part 38 — →](38-unit-05-programming-part-38.md)
