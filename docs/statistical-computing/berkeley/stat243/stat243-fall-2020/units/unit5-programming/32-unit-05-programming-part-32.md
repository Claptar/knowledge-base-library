---
title: Unit 05 — programming Part 32 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 32 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f) ## $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y **class** ( **formals** (f)) ## [1] "pairlist"

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

47

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE) _## what do you think quote does? Why is it needed?_

### **6.3 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function, and allows the function to exit as soon as it is done.

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9 **f** (3)

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

48

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

### **6.4 Frames and the call stack**

R keeps track of the call stack, which is the series of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). Each function call is associated with a _frame_ that contains the local variables for that function call.

There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the frame from which a function was called.

Some terminology: for our purposes we’ll use the terms _frame_ and _environment_ somewhat interchangeably for the moment. A _frame_ or _environment_ is a collection of named objects. (Note that when we talk about variable scope in Section 6.6, we’ll have to be more careful with our terminology.) So in the context of a function call, the frame is the set of local variables available in the function, including arguments passed to the function.

_sys.nframe()_ returns the number of the current frame/environment and _sys.parent()_ the number of the parent, while _parent.frame()_ gives the name of the frame/environment of the parent (i.e., the calling) frame. _sys.frame()_ gives the name of the frame/environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the frame/environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

_## NOTE: run this chunk outside RStudio as RStudio seems to ## inject additional frames_ **sys.nframe** () f <- **function** () { **cat** ('in f: Frame number is ', **sys.nframe** (), '; parent frame number is ', **sys.parent** (), '.\n', sep = '')

49

**cat** ('in f: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('in f: Parent is ') **print** ( **parent.frame** ()) **cat** ('in f: Two frames up is ') **print** ( **sys.frame** (-2)) } **f** () ff <- **function** () { **cat** ('in ff: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('in ff: Parent is ') **print** ( **parent.frame** ()) **f** () } **ff** ()

Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ .

_## exploring functions that give us information the frames in the stack ## Here's a recursive function, so we'll get a lot of function calls on the_ g <- **function** (y) { **if** (y > 0) **g** (y-1) **else gg** () } _## Ultimately, gg() is called, and it prints out info about the call stack_ gg <- **function** () { _## this gives us the information from sys.calls(), ## sys.parents() and sys.frames() as one object ## Rather than running print(sys.status()), ## which would involve adding print() to the call stack, ## we'll run sys.status and then print the result out._ tmp <- **sys.status** () **print** (tmp)

50

}

**g** (3)

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **6.5 Approaches to passing arguments to functions**

#### **6.5.1 Pass by value vs. pass by reference**

When talking about programming languages, one often distinguishes _pass-by-value_ and _pass-byreference_ . Pass-by-value means that when a function is called with one or more arguments, a copy is made of each argument and the function operates on those copies. Pass-by-reference means that the arguments are not copied, but rather that information is passed allowing the function to find and modify the original value of the objects passed into the function. In pass-by-value, changes to an argument made within a function do not affect the value of the argument in the calling environment. In pass-by-reference changes inside a function do affect the object outside of the function. R is (roughly) pass-by-value. R’s designers chose not to allow pass-by-reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference later in this Unit (and also note our discussion of R6 classes).

Pass-by-value is elegant and modular in that functions do not have side effects - the effect of the function occurs only through the return value of the function. However, it can be inefficient in terms of the amount of computation and of memory used. In contrast, pass-by-reference is more efficient, but also more dangerous and less modular. It’s more difficult to reason about code that uses pass-by-reference because effects of calling a function can be hidden inside the function.

An important exception is _par()_ . If you change graphics parameters by calling _par()_ in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** (){ oldpar <- **par** () **par** (cex = 2) _# body of code_ **par** () <- oldpar }

51

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot. Can you think of other R functions that have side effects?

**Pointers** By way of contrast to a pass-by-value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3;

int* ptr; ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here _ptr_ is the address of the integer _x_ . Vectors in C are really pointers to a block of memory: int x[10];

In this case _x_ will be the address of the first element of the vector. We can access the first element as x[0] or *x.

Why have we gone into this? In C, you can pass a pointer as an argument to a function. The result is that only the scalar address is copied and not the entire vector, and inside the function, one can modify the original vector, with the new value persisting on exit from the function. For example:

int myCal(int* ptr){

*<sup>ptr=</sup> *<sup>ptr+</sup> *<sup>ptr;</sup> }

When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C. For example, using the old .C syntax, here’s an example:

out <- rep(0, n)

out <- .C(“logLik”, out = as.double(out),

theta = as.double(theta))$out

In C, the function definition looks like this:

void logLik(double* out, double* theta)

**Pointers in R?** Are there pointers in R? From a user perspective, one might say ’no’, because an R programmer can’t use pointers explicitly. But pointer-like behavior is occurring behind the scenes in lots of ways:

- Lists in R are essentially vectors of pointers to the elements of the list

- Character vectors in R are essentially pointers to the individual character strings.

52

- R6 objects behave like pointers and are passed by reference rather than by copy, as seen in Section 4.4.3.

- Environments (see Section 6.9) behave like pointers and are passed by reference rather than by copy.

#### **6.5.2 Promises and lazy evaluation**

In actuality, R is not quite pass-by-value; rather it is _call-by-value_ . Copying of arguments is delayed in two ways. The first is the idea of promises and lazy evaluation, described here. The second is the idea of _copy-on-change_ , described in Section 8. Basically, with copy-on-change, copies of arguments are only made if the argument is changed within the function. Until then the object in the function just refers back to the original object.

Let’s see what a _promise_ object is. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called _lazy evaluation_ . Instead the formal arguments are of a special type called a _promise_ . Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- **log** (a); **return** (a*b) } **f** (7) d <- 100 **f** (7)

What’s strange about that? Another example:

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1000000))) ## user system elapsed ## 0.106 0.004 0.110 **system.time** ( **f** (3))

53

---

[← Unit 05 — programming Part 31 —](31-unit-05-programming-part-31.md) · [Up: contents](index.md) · [Unit 05 — programming Part 33 — →](33-unit-05-programming-part-33.md)
