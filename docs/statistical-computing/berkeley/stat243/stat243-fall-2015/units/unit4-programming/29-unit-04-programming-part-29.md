---
title: Unit 04 — programming Part 29 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 29 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The old version of _mat_ still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’ _mat_ ’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

You can define your own replacement functions like this, with the requirements that the last argument be named ’ _value_ ’ and that the function return the entire object:

yog <- **list** (firstName = 'Yogi', lastName = 'Bear') `firstName<-` <- **function** (obj, value){ obj$firstName <- value **return** (obj) } **firstName** (yog) <- 'Yogisandra'

### **6.7 Variable scope**

In this section, we seek to understand what happens in the following circumstance. Namely, where does R get the value for the object ’x’?

47

f <- **function** (y) { **return** (x + y) } **f** (3) ## [1] 4 5 6

To consider variable scope, we need to define the terms _environment_ and _frame_ . Environments and frames are closely related.

- A _frame_ is a collection of named objects.

- An _environment_ is a frame, with a pointer to the ’enclosing environment’, i.e., the next environment to look for something in. (Be careful as this is different than the parent frame of a function.)

Variables in the enclosing environment (the environment in which a function is defined, also called the parent environment) are available within a function. This is the analog of _global variables_ in other languages. Note that the enclosing/parent environment is NOT the environment from which the function was called. R’s use of enclosing environments as the approach to looking for variables is called _lexical scoping_ .

Be careful when using variables from the enclosing environment as the value of that variable in the enclosing environment may well not be what you expect it to be. In general it’s bad practice to use variables that are taken from environments outside that of a function, but it some cases it can be useful.

x <- 3 f <- **function** () {x <- x^2; **print** (x)} **f** () x _# what do you expect?_ f <- **function** () { **assign** ('x', x^2, env = .GlobalEnv) } _# careful, this could be dangerous as a variable is changed as a side effect_ **f** () x f <- **function** (x) { x <<- x^2 } _# careful, this could be dangerous as a variable is changed as a side effect_ **f** (5) x

48

Here are some examples to illustrate scope:

x <- 3 f <- **function** () { f2 <- **function** () { **print** (x) } **f2** () } **f** () _# what will happen?_ f <- **function** () { f2 <- **function** () { **print** (x) } x <- 7 **f2** () } **f** () _# what will happen?_ f2 <- **function** () **print** (x) f <- **function** () { x <- 7 **f2** () } **f** () _# what will happen?_

Here’s a somewhat tricky example:

y <- 100 f <- **function** (){ y <- 10 g <- **function** (x) x + y **return** (g) } _# you can think of f() as a function constructor_ h <- **f** () **h** (3) ## [1] 13

Let’s work through this:

49

1. What is the enclosing environment of the function _g()_ ?

2. What does _g()_ use for _y_ ?

3. When _f()_ finishes, does its environment disappear? What would happen if it did?

4. What is the enclosing environment of _h()_ ?

This code helps explain things, but it’s a bit confusing because _environment()_ gives back different results depending on whether it is given a function as its argument. If given a function, it returns the enclosing environment for that function. If given no argument, it returns the current execution environment.

**environment** (h) _# enclosing environment of h()_ ## <environment: 0x52f1ae8> **ls** ( **environment** (h)) _# objects in that environment_ ## [1] "g" "y" f <- **function** (){ **print** ( **environment** ()) _# execution environment of f()_ y <- 10 g <- **function** (x) x + y **return** (g) } h <- **f** () ## <environment: 0x403df20> **environment** (h) ## <environment: 0x403df20> **h** (3) ## [1] 13 **environment** (h)$y ## [1] 10 _# advanced: explain this:_ **environment** (h)$g ## function(x) x + y ## <environment: 0x403df20>

50

**Comprehension problem** Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (0) **rnorm** (1) ## [1] 1.26 **save** (.Random.seed, file = 'tmp.Rda') **rnorm** (1) ## [1] -0.326 tmp <- **function** () { **load** ('tmp.Rda') **print** ( **rnorm** (1)) } **tmp** () ## [1] 1.33

Question: what was I hoping that code to do, and why didn’t it work?

### **6.8 Environments and the search path**

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve seen, these environments are not the environments of the calling function(s) - i.e., they are _not_ the frames on the stack (see the next Section).

By default objects are created in the global environment, _.GlobalEnv_ . As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and based on lexical scoping this is next place that is searched if an object can’t be found in the frame of the function call. As an example, if an object couldn’t be found within the environment of an _lm()_ function call, R would first look in the environment (i.e., the _namespace_ ) of the stats package (since this is the

51

environment where _lm()_ is defined and is therefore the enclosing environment for _lm()_ ), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with _search()_ . The search path is a set of additional environments. Generally packages are created with namespaces, i.e., each has its own environment, as we see based on _search()_ .

**search** ()

---

[← Unit 04 — programming Part 28 —](28-unit-04-programming-part-28.md) · [Up: contents](index.md) · [Unit 04 — programming Part 30 — →](30-unit-04-programming-part-30.md)
