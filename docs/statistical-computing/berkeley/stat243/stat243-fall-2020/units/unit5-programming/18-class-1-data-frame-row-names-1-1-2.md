---
title: '$names ## [1] "x" "y" ## ## $class ## [1] "data.frame" ## ## $row.names ##
  [1] 1 2'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $names ## [1] "x" "y" ## ## $class ## [1] "data.frame" ## ## $row.names ## [1] 1 2

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

17

**row.names** (mat) <- **c** ("first", "second") mat ## x y ## first 1 3 ## second 2 4 **attributes** (mat) ## $names ## [1] "x" "y" ## ## $class ## [1] "data.frame" ## ## $row.names ## [1] "first" "second" vec <- **c** (first = 7, second = 1, third = 5) vec['first'] ## first ## 7 **attributes** (vec) ## $names ## [1] "first" "second" "third"

### **4.3 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

18

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x5639abb4a310> ## <environment: namespace:base> x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) _# usual way to pass an argument to a function by name_ out <- **mean** ( **c** (3,7)) _# or by position ## what does the following do?_ out <- **mean** (x <- **c** (3,7)) _# this is allowable, but confusing_ out <- **mean** (y = **c** (3,7)) _# why doesn't this work?_

**## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default** out <- **mean** (y <- **c** (3,7)) _# again, allowable, but confusing_

What can you tell me about what is going on in each case above?

One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a function, so that R realizes you’re not indicating one of the function arguments, e.g.:

_## NOT OK, system.time() expects its argument to be a complete R expression:_ **system.time** (out = **rnorm** (10000))

**## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))** _# OK:_ **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.001 0.000 0.001

Here’s another example:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))})

19

---

[← Unit 05 — programming Part 17 —](17-unit-05-programming-part-17.md) · [Up: contents](index.md) · [Unit 05 — programming Part 19 — →](19-unit-05-programming-part-19.md)
