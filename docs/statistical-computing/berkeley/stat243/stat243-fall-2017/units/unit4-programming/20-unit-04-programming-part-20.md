---
title: Unit 04 — programming Part 20 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 20 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

16

### **4.3 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x44ef410> ## <environment: namespace:base> x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) _# usual way to pass an argument to a function ## what does the following do?_ out <- **mean** (x <- **c** (3,7)) _# this is allowable, though perhaps not useful_ out <- **mean** (y = **c** (3,7)) **## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default** out <- **mean** (y <- **c** (3,7))

What can you tell me about what is going on in each case above? One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a function, so that R realizes you’re not indicating one of the function arguments, e.g.:

_## NOT OK, system.time() expects its argument to be a complete R expression:_ **system.time** (out = **rnorm** (10000)) **## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))** _# OK:_ **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.000 0.000 0.001

17

Here’s another example:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) ## [1] 0 1 _## What is the side effect of what I have done just above?_ **apply** (mat, 1, sum.isna = **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) _# NOPE_ **## Error in match.fun(FUN): argument "FUN" is missing, with no default**

R often treats integers as numerics, but we can force R to store values as integers:

vals <- **c** (1, 2, 3) **class** (vals) ## [1] "numeric" vals <- 1:3 **class** (vals) ## [1] "integer" vals <- **c** (1L, 2L, 3L) vals ## [1] 1 2 3 **class** (vals) ## [1] "integer"

We convert between classes using variants on _as()_ : e.g.,

**as.character** ( **c** (1,2,3)) ## [1] "1" "2" "3" **as.numeric** ( **c** ("1", "2.73"))

18

---

[← Unit 04 — programming Part 19 —](19-unit-04-programming-part-19.md) · [Up: contents](index.md) · [[1] 1.00 2.73 as.factor ( c ("a", "b", "c")) ## [1] a b c ## Levels: a b c →](21-1-1-00-2-73-as-factor-c-a-b-c-1-a-b-c-levels-a-b-c.md)
