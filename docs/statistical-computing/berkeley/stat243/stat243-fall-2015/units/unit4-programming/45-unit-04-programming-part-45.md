---
title: Unit 04 — programming Part 45 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 45 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The parse tree for _out3_ is different than those for _out1_ and _out2_ , but when _out3_ is evaluated the result is the same as for _out1_ and _out2_ :

**eval** (out1) animals ## [1] "cat" "dog" "rat" "rat"

93

animals[4] <- 'mouse' _# reset things to original state_ **eval** (out3) ## [1] "cat" "dog" "rat" "rat" animals _# both do the same thing_ ## [1] "cat" "dog" "rat" "rat"

Why? When R evaluates a call to ‘<-‘, if the first argument is a name, then it does the assignment, but if the first argument (i.e. what’s on the left-hand side of the “assignment”) is a call then it calls the appropriate replacement function. The second argument (the value being assigned) is evaluated first. Ultimately in all of these cases, the replacement function is used.

### **9.5 substitute()**

The substitute function acts like _quote()_ :

**identical** ( **quote** (z <- x^2), **substitute** (z <- x^2)) ## [1] TRUE

But if you also pass _substitute()_ an environment, it will replace symbols with their object values in that environment.

e <- **new.env** (); e$x <- 3 **substitute** (z <- x^2, e) ## z <- 3^2

This can do non-sensical stuff:

e$z <- 5 **substitute** (z <- x^2, e) ## 5 <- 3^2

Let’s see a practical example of substituting for variables in statements:

plot(x = rnorm(5), y = rgamma(5, 1)) # how does plot get the axis label names?

In the _plot()_ function, you can see this syntax:

94

xlabel <- if(!missing(x)) deparse(substitute(x))

So what’s going on is that within _plot.default()_ , it substitutes in for ’ _x_ ’ with the statement that was passed in as the _x_ argument, and then uses _deparse()_ to convert to character. The fact that _x_ still has _rnorm(5)_ associated with it rather than the five numerical values from evaluating _rnorm()_ has to do with lazy evaluation and promises. Here’s the same idea in action in a stripped down example:

f <- **function** (obj){ objName <- **deparse** ( **substitute** (obj)) **print** (objName) } **f** (y) ## [1] "y"

More generally, we can substitute into _expression_ and _call_ objects by providing a named list (or an environment) - the substition happens within the context of this list.

**substitute** (a + b, **list** (a = 1, b = **quote** (x))) ## 1 + x

Things can get intricate quickly:

e1 <- **quote** (x + y) e2 <- **substitute** (e1, **list** (x = 3))

The problem is that _substitute()_ doesn’t evaluate its first argument, “ _e1_ ”, so it can’t replace the parsed elements in _e1_ . Instead, we’d need to do the following, where we force the evaluation of _e1_ :

e2 <- **substitute** ( **substitute** (e, **list** (x = 3)), **list** (e = e1)) **substitute** ( **substitute** (e, **list** (x = 3)), **list** (e = e1))

---

[← Unit 04 — programming Part 44 —](44-unit-04-programming-part-44.md) · [Up: contents](index.md) · [Unit 04 — programming Part 46 — →](46-unit-04-programming-part-46.md)
