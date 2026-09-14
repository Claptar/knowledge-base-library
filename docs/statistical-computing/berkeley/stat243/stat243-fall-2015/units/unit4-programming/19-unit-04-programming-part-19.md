---
title: Unit 04 — programming Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 19 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.3 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

out <- **mean** ( **rnorm** (7)) _# OK_ **system.time** (out = **rnorm** (10000))

**## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))** _# NOT OK, system.time() expects its argument to be a complete R expression_ **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.000 0.000 0.001

16

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x4d026a0> ## <environment: namespace:base> x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) _# usual way to pass an argument to a function # what does the following do?_ out <- **mean** (x <- **c** (3,7)) _# this is allowable, though perhaps not useful_ out <- **mean** (y = **c** (3,7))

**## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default** out <- **mean** (y <- **c** (3,7))

What can you tell me about what is going on in each case above?

One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a function, so that R realizes you’re not indicating one of the function arguments, e.g.:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) ## [1] 0 1 _# What is the side effect of what I have done here?_ **apply** (mat, 1, sum.isna = **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) _# NOPE_ **## Error in match.fun(FUN): argument "FUN" is missing, with no default**

R often treats integers as numerics, but we can force R to store values as integers:

vals <- **c** (1, 2, 3) **class** (vals)

17

---

[← Unit 04 — programming Part 18 —](18-unit-04-programming-part-18.md) · [Up: contents](index.md) · [Unit 04 — programming Part 20 — →](20-unit-04-programming-part-20.md)
