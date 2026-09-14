---
title: '$x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist"'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist"

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE) _# what do you think quote does? Why is it needed?_

**Pass by value vs. pass by reference** Note that R makes a copy of all objects that are arguments to a function, with the copy residing in the frame (the environment) of the function (we’ll see more about frames just below). This is a case of _pass by value_<sup>1</sup> . In other languages it is also possible to _pass by reference_ , in which case, changes to the object made within the function affect the value of the argument in the calling environment. R’s designers chose not to allow pass by reference because they didn’t like the idea that a function could have the side effect of changing an object. However, passing by reference can sometimes be very helpful, and we’ll see ways of passing by reference in Unit 6 on R programming.

An important exception is _par()_ . If you change graphics parameters by calling _par()_ in a userdefined function, they are changed permanently outside of the function. One trick is as follows:

f <- **function** () { oldpar <- **par** () **par** (cex = 2)

> 1calling it pass by value is actually a simplification of what really happens, but a useful one, until we discuss copy-on-change, promises, and lazy evaluation in Unit 6

44

_# body of code_ **par** () <- oldpar }

Note that changing graphics parameters within a specific plotting function - e.g., plot(x, y, pch = ’+’), doesn’t change things except for that particular plot.

### **7.2 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function, and allows the function to exit as soon as it is done.

f <- **function** (x) { res <- x^2 } **f** (3) a <- **f** (3) a ## [1] 9

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x) { **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

45

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

### **7.3 Variable scope**

To consider variable scope, we need to define the terms _environment_ and _frame_ . Environments and frames are closely related.

- A _frame_ is a collection of named objects.

- An _environment_ is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

Variables in the enclosing environment (the environment in which a function is defined, also called the parent environment) are available within a function. This is the analog of _global variables_ in other languages. Note that enclosing/parent environment is NOT the environment from which the function was called. This is called _lexical scoping_ .

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice to use variables that are taken from environments outside that of a function, but it some cases it can be useful.

x <- 3 f <- **function** () { x <- x^2 **print** (x) } **f** () x _# what do you expect?_ f <- **function** () { **assign** ("x", x^2, env = .GlobalEnv)

46

} _# careful, this could be dangerous as a variable is # changed as a side effect_

Here are some examples to illustrate scope:

x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () _# what will happen?_ f <- **function** () { f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () _# what will happen?_ f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () _# what will happen?_

Here’s a somewhat tricky example:

y <- 100 f <- **function** () { y <- 10 g <- **function** (x) x + y

47

**return** (g) } _# you can think of f() as a function constructor_ h <- **f** () **h** (3) ## [1] 13

Let’s work through this:

1. What is the enclosing environment of the function _g()_ ?

2. What does _g()_ use for _y_ ?

3. When _f()_ finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of _h()_ ?

This code helps explain things, but it’s a bit confusing because _environment()_ gives back different results depending on whether it is given a function as its argument.

**environment** (h) _# enclosing environment of h()_ ## <environment: 0x2efa758> **ls** ( **environment** (h)) _# objects in that environment_ ## [1] "g" "y" f <- **function** () { **print** ( **environment** ()) _# environment of f()_ y <- 10 g <- **function** (x) x + y **return** (g) } h <- **f** () ## <environment: 0x2ba3e30> **environment** (h)

48

---

[← Unit 04 — usingR Part 30 —](30-unit-04-usingr-part-30.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 32 — →](32-unit-04-usingr-part-32.md)
