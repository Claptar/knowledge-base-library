---
title: Unit 05 — programming Part 33 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 33 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

47

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f) ## $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y **class** ( **formals** (f)) ## [1] "pairlist"

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE) _## what do you think quote does? Why is it needed?_

### **6.3 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function,

48

and allows the function to exit as soon as it is done.

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9 **f** (3)

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

### **6.4 Frames and the call stack**

R keeps track of the call stack, which is the series of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when

49

it finishes, it is removed (popped). Each function call is associated with a _frame_ that contains the local variables for that function call.

There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the frame from which a function was called.

Some terminology: for our purposes we’ll use the terms _frame_ and _environment_ somewhat interchangeably for the moment. A _frame_ or _environment_ is a collection of named objects. (Note that when we talk about variable scope in Section 6.6, we’ll have to be more careful with our terminology.) So in the context of a function call, the frame is the set of local variables available in the function, including arguments passed to the function.

_sys.nframe()_ returns the number of the current frame/environment and _sys.parent()_ the number of the parent, while _parent.frame()_ gives the name of the frame/environment of the parent (i.e., the calling) frame. _sys.frame()_ gives the name of the frame/environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the frame/environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

_## NOTE: run this chunk outside RStudio as RStudio seems to ## inject additional frames_ **sys.nframe** () f <- **function** () { **cat** ('in f: Frame number is ', **sys.nframe** (), '; parent frame number is ', **sys.parent** (), '.\n', sep = '') **cat** ('in f: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('in f: Parent is ') **print** ( **parent.frame** ()) **cat** ('in f: Two frames up is ') **print** ( **sys.frame** (-2)) } **f** () ff <- **function** () { **cat** ('in ff: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('in ff: Parent is ') **print** ( **parent.frame** ())

50

**f** () } **ff** ()

Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ .

_## exploring functions that give us information the frames in the stack ## Here's a recursive function, so we'll get a lot of function calls on the_ g <- **function** (y) { **if** (y > 0) **g** (y-1) **else gg** () } _## Ultimately, gg() is called, and it prints out info about the call stack_ gg <- **function** () { _## this gives us the information from sys.calls(), ## sys.parents() and sys.frames() as one object ## Rather than running print(sys.status()), ## which would involve adding print() to the call stack, ## we'll run sys.status and then print the result out._ tmp <- **sys.status** () **print** (tmp) } **g** (3)

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **6.5 Approaches to passing arguments to functions**

#### **6.5.1 Pass by value vs. pass by reference**

When talking about programming languages, one often distinguishes _pass-by-value_ and _pass-byreference_ . Pass-by-value means that when a function is called with one or more arguments, a copy is made of each argument and the function operates on those copies. Pass-by-reference means that

51

the arguments are not copied, but rather that information is passed allowing the function to find and modify the original value of the objects passed into the function. In pass-by-value, changes to an argument made within a function do not affect the value of the argument in the calling environment. In pass-by-reference changes inside a function do affect the object outside of the function. R is (roughly) pass-by-value. R’s designers chose not to allow pass-by-reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference later in this Unit (and also note our discussion of R6 classes).

Pass-by-value is elegant and modular in that functions do not have side effects - the effect of the function occurs only through the return value of the function. However, it can be inefficient in terms of the amount of computation and of memory used. In contrast, pass-by-reference is more efficient, but also more dangerous and less modular. It’s more difficult to reason about code that uses pass-by-reference because effects of calling a function can be hidden inside the function.

An important exception is _par()_ . If you change graphics parameters by calling _par()_ in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** (){ oldpar <- **par** () **par** (cex = 2) _# body of code_ **par** () <- oldpar }

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot. Can you think of other R functions that have side effects?

**Pointers** By way of contrast to a pass-by-value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3; int* ptr; ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here _ptr_ is the address of the integer _x_ . Vectors in C are really pointers to a block of memory: int x[10];

52

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

- R6 objects behave like pointers and are passed by reference rather than by copy, as seen in Section 4.4.3.

- Environments (see Section 6.9) behave like pointers and are passed by reference rather than by copy.

#### **6.5.2 Promises and lazy evaluation**

In actuality, R is not quite pass-by-value; rather it is _call-by-value_ . Copying of arguments is delayed in two ways. The first is the idea of promises and lazy evaluation, described here. The second is the idea of _copy-on-change_ , described in Section 8. Basically, with copy-on-change, copies of arguments are only made if the argument is changed within the function. Until then the object in the function just refers back to the original object.

53

Let’s see what a _promise_ object is. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called _lazy evaluation_ . Instead the formal arguments are of a special type called a _promise_ . Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- a*3; **return** (a*b) } **f** (5) d <- 100 **f** (5)

What’s strange about that? Another example:

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1000000))) ## user system elapsed ## 0.068 0.000 0.069 **system.time** ( **f** (3)) ## [1] "hi" ## user system elapsed ## 0.001 0.000 0.000 **system.time** ( **f** ( **mean** ( **rnorm** (1000000)))) ## [1] "hi" ## user system elapsed ## 0.001 0.000 0.001

Lazy evaluation is not just an R thing. It also occurs in Spark and in the Python Dask package. The basic idea is to delay executation until it’s really needed, with the goal that if one does so,

54

the system may be able to better optimize a series of multiple steps as a joint operation relative to executing them one by one.

**Where are arguments evaluated?** User-supplied arguments are evaluated in the calling frame (why?), while default arguments are evaluated in the frame of the function (why?):

z <- 3 x <- 100 f <- **function** (x, y = x*3) {x+y} **f** (z*5) ## [1] 60

Here, when _f()_ is called, promises for z*5 and x*3 are created. Then when the code is evaluated, _z_ is evaluated in the calling frame and z*5 is assigned to _x_ in the frame of the function, while x*3 is evaluated in the frame of the function and assigned to _y_ .

### **6.6 Variable scope**

In this section, we seek to understand what happens in the following circumstance. Namely, where does R get the value for the object ’x’?

f <- **function** (y) { **return** (x + y) } **f** (3) ## [1] 103

To consider variable scope, we need to define the terms _environment_ and _frame_ . Environments and frames are closely related.

- A _frame_ is a collection of named objects.

- An _environment_ is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

Variables in the enclosing environment (also called the parent environment) are available within a function. This is the analog of _global variables_ in other languages. The enclosing environment

55

is the environment in which a function is defined, not the environment from which a function is called.

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice to use variables that are taken from environments outside that of a function, but in some cases it can be useful. Here are some examples of using variables outside of the frame of a function.

x <- 3 f <- **function** () {x <- x^2; **print** (x)} **f** () x _# what do you expect?_ f <- **function** () { **assign** ('x', x^2, env = .GlobalEnv) } _## careful: could be dangerous as a variable is changed as a side effect_ **f** () x f <- **function** (x) { x <<- x^2 } _## careful: could be dangerous as a variable is changed as a side effect_ **f** (5) x

Let’s dig deeper to understand where R looks for non-local variables. **R looks for variables that are not local to a function in the** **_enclosing environment_ of the function. The** **_enclosing environment_ is the environment in which the function was** **_defined_ .** Note that the enclosing/parent environment is NOT the environment from which the function was called. This approach is called _lexical scoping_ .

Here are some examples to illustrate scope:

x <- 3 f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () _# what will happen?_ x <- 3 f <- **function** () {

56

f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () _# what will happen?_ x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () _# what will happen?_

Here’s a somewhat tricky example:

y <- 100 fun_constructor <- **function** (){ y <- 10 g <- **function** (x) { **return** (x + y) } **return** (g) } _## fun_constructor() creates functions_ myfun <- **fun_constructor** () **myfun** (3) ## [1] 13

Let’s work through this:

1. What is the enclosing environment of the function _g()_ ?

2. What does _g()_ use for _y_ ?

3. When _fun_constructor()_ finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of _myfun()_ ?

57

This code helps explain things, but it’s a bit confusing because _environment()_ gives back different results depending on whether it is given a function as its argument. If given a function, it returns the enclosing environment for that function. If given no argument, it returns the current execution environment.

**environment** (myfun) _# enclosing environment of h()_ ## <environment: 0x55691d1732f8> **ls** ( **environment** (myfun)) _# objects in that environment_ ## [1] "g" "y" fun_constructor <- **function** (){ **print** ( **environment** ()) _# execution environment of fun_constructor()_ y <- 10 g <- **function** (x) x + y **return** (g) } myfun <- **fun_constructor** () ## <environment: 0x55691d896180> **environment** (myfun) ## <environment: 0x55691d896180> **myfun** (3) ## [1] 13 **environment** (myfun)$y ## [1] 10 _## advanced: explain this:_ **environment** (myfun)$g ## function(x) x + y ## <environment: 0x55691d896180>

58

**Comprehension problem** Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (1) **rnorm** (1) ## [1] -0.626 **save** (.Random.seed, file = 'tmp.Rda') **rnorm** (1) ## [1] 0.184 tmp <- **function** () { **load** ('tmp.Rda') **print** ( **rnorm** (1)) } **tmp** () ## [1] -0.836

Question: what was I hoping that code to do, and why didn’t it work?

**Detecting non-local variables** We can use _codetools::findGlobals_ to detect non-local variables when we are programming.

**library** (codetools) f <- **function** () { y <- 3 **print** (x + y) } **findGlobals** (f) ## [1] "{" "+" "<-" "print" "x"

Is that result what you would expect? What does it say about my statement that using non-local variables is a bad idea?

59

**Closures** One way to avoid passing data by value is to associate data with a function, using a _closure_ . This is a functional programming way to achieve something like an OOP class. This Wikipedia entry nicely summarizes the idea, which is not an R-specific construct. This involves creating one (or more functions) within a function call and returning the function(s) as the output. When one executes the original function, the new function(s) is created and returned and one can then call that new function(s). The new function then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the enclosing environment, to which the function (or the multiple functions) have access. The nice thing about this compared to using a global variable is that the data in the closure is bound up with the function(s) and is protected from being changed by the user of the closure. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) scaler_constructor <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } scaler <- **scaler_constructor** (x) **rm** (x) _# to demonstrate we no longer need x_ **scaler** (3) ## [1] 4.786 0.989 -2.461 1.462 2.215 1.727 -0.916 ## [8] 4.535 1.170 -1.864 x <- **rnorm** (1e7) scaler <- **scaler_constructor** (x) **object.size** (scaler) _# hmmm_ ## 3800 bytes **object.size** ( **environment** (scaler)$data) ## 80000048 bytes **library** (pryr) **object_size** (scaler) _# that's better!_ ## 80 MB

60

Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick:

make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** { x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[ , 1] _# Old Faithful geyser eruption lengths_ **for** (i **in** 1:nboot) **bootmeans** ( **mean** ( **sample** (data, **length** (data), replace=TRUE))) _## this will place results in x in the function env't and you can grab it out_ **bootmeans** () ## [1] 3.59 3.41 3.47 3.46 3.43 3.48 3.51 3.48 3.50 3.46 ## [11] 3.41 3.62 3.46 3.46 3.49 3.50 3.56 3.50 3.58 3.60 ## [21] 3.46 3.45 3.50 3.41 3.46 3.59 3.35 3.50 3.51 3.37 ## [31] 3.46 3.38 3.58 3.52 3.45 3.58 3.50 3.47 3.54 3.57 ## [41] 3.53 3.58 3.40 3.50 3.50 3.56 3.41 3.45 3.50 3.53 ## [51] 3.49 3.57 3.46 3.50 3.43 3.48 3.54 3.45 3.53 3.53 ## [61] 3.46 3.36 3.41 3.58 3.58 3.47 3.51 3.50 3.56 3.48 ## [71] 3.39 3.48 3.62 3.54 3.51 3.52 3.47 3.49 3.43 3.45 ## [81] 3.40 3.52 3.43 3.49 3.51 3.56 3.55 3.46 3.30 3.56 ## [91] 3.47 3.49 3.41 3.40 3.46 3.43 3.43 3.44 3.45 3.42

61

### **6.7 Environments and the search path**

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve seen, these environments are not the environments of the calling function(s) - i.e., they are _not_ the frames on the stack (see the next Section).

By default objects are created in the global environment, _.GlobalEnv_ . As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and based on lexical scoping this is next place that is searched if an object can’t be found in the frame of the function call. As an example, if an object couldn’t be found within the environment of an _lm()_ function call, R would first look in the environment (i.e., the _namespace_ ) of the stats package (since this is the environment where _lm()_ is defined and is therefore the enclosing environment for _lm()_ ), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with _search()_ . The search path is a set of additional environments. Generally packages are created with namespaces, i.e., each has its own environment, as we see based on _search()_ .

**search** ()

---

[← Unit 05 — programming Part 32 —](32-unit-05-programming-part-32.md) · [Up: contents](index.md) · [Unit 05 — programming Part 34 — →](34-unit-05-programming-part-34.md)
