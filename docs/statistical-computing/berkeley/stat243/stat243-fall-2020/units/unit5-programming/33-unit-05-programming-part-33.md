---
title: Unit 05 — programming Part 33 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 33 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lazy evaluation is not just an R thing. It also occurs in Spark and in the Python Dask package. The basic idea is to delay executation until it’s really needed, with the goal that if one does so, the system may be able to better optimize a series of multiple steps as a joint operation relative to executing them one by one.

**Where are arguments evaluated?** User-supplied arguments are evaluated in the calling frame, while default arguments are evaluated in the frame of the function:

z <- 3 x <- 100 f <- **function** (x, y = x*3) {x+y} **f** (z*5) ## [1] 60

Here, when _f()_ is called, _z_ is evaluated in the calling frame and z*5 is assigned to _x_ in the frame of the function, while y = x*3 is evaluated in the frame of the function.

Challenge: How could I experimentally determine if the default argument is treated as a promise as well?

### **6.6 Variable scope**

In this section, we seek to understand what happens in the following circumstance. Namely, where does R get the value for the object ’x’?

f <- **function** (y) { **return** (x + y) }

54

**f** (3) ## [1] 103

To consider variable scope, we need to define the terms _environment_ and _frame_ . Environments and frames are closely related.

- A _frame_ is a collection of named objects.

- An _environment_ is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

Variables in the enclosing environment (also called the parent environment) are available within a function. This is the analog of _global variables_ in other languages. The enclosing environment is the environment in which a function is defined, not the environment from which a function is called.

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice to use variables that are taken from environments outside that of a function, but in some cases it can be useful. Here are some examples of using variables outside of the frame of a function.

x <- 3 f <- **function** () {x <- x^2; **print** (x)} **f** () x _# what do you expect?_ f <- **function** () { **assign** ('x', x^2, env = .GlobalEnv) } _## careful: could be dangerous as a variable is changed as a side effect_ **f** () x f <- **function** (x) { x <<- x^2 } _## careful: could be dangerous as a variable is changed as a side effect_ **f** (5) x

Let’s dig deeper to understand where R looks for non-local variables. **R looks for variables that are not local to a function in the** **_enclosing environment_ of the function. The** **_enclosing environment_ is the environment in which the function was** **_defined_ .** Note that the enclosing/parent

55

environment is NOT the environment from which the function was called. This approach is called _lexical scoping_ .

Here are some examples to illustrate scope:

x <- 3 f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () _# what will happen?_ x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () _# what will happen?_ x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () _# what will happen?_ Here’s a somewhat tricky example: y <- 100 fun_constructor <- **function** (){ y <- 10 g <- **function** (x) { **return** (x + y) } **return** (g) }

56

_## fun_constructor() creates functions_ myfun <- **fun_constructor** () **myfun** (3) ## [1] 13

Let’s work through this:

1. What is the enclosing environment of the function _g()_ ?

2. What does _g()_ use for _y_ ?

3. When _fun_constructor()_ finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of _myfun()_ ?

This code helps explain things, but it’s a bit confusing because _environment()_ gives back different results depending on whether it is given a function as its argument. If given a function, it returns the enclosing environment for that function. If given no argument, it returns the current execution environment.

**environment** (myfun) _# enclosing environment of h()_ ## <environment: 0x5639b1bc3ec0> **ls** ( **environment** (myfun)) _# objects in that environment_ ## [1] "g" "y" fun_constructor <- **function** (){ **print** ( **environment** ()) _# execution environment of fun_constructor()_ y <- 10 g <- **function** (x) x + y **return** (g) } myfun <- **fun_constructor** () ## <environment: 0x5639b2dc4fd8> **environment** (myfun)

57

---

[← Unit 05 — programming Part 32 —](32-unit-05-programming-part-32.md) · [Up: contents](index.md) · [Unit 05 — programming Part 34 — →](34-unit-05-programming-part-34.md)
