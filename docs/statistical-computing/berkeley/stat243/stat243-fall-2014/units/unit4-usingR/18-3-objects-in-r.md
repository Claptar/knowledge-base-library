---
title: 3 Objects in R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Objects in R

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

out = **mean** ( **rnorm** (7)) _# OK_ **system.time** (out = **rnorm** (10000)) **## Error: unused argument (out = rnorm(10000))** _# NOT OK, system.time() expects its argument to be a # complete R expression_ **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.000 0.000 0.001

Let’s look at these examples to understand the distinction between ’=’ and ’<-’ when passing arguments to a function.

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x2f2bfb8> ## <environment: namespace:base> x <- 0 y <- 0 out <- **mean** (x = **c** (3, 7)) _# usual way to pass an argument to a function # what does the following do?_ out <- **mean** (x <- **c** (3, 7)) _# this is allowable, though perhaps not useful_ out <- **mean** (y = **c** (3, 7)) **## Error: argument "x" is missing, with no default** out <- **mean** (y <- **c** (3, 7))

10

What can you tell me about what is going on in each case above?

One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a function, so that R realizes you’re not indicating one of the function arguments, e.g.:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec))) }) ## [1] 0 1 _# What is the side effect of what I have done here?_ **apply** (mat, 1, sum.isna = **function** (vec) { **return** ( **sum** ( **is.na** (vec))) }) _# NOPE_ **## Error: argument "FUN" is missing, with no default**

R often treats integers as numerics, but we can force R to store values as integers:

vals <- **c** (1, 2, 3) **class** (vals) ## [1] "numeric" vals <- 1:3 **class** (vals) ## [1] "integer" vals <- **c** (1L, 2L, 3L) vals ## [1] 1 2 3 **class** (vals) ## [1] "integer"

We convert between classes using variants on _as()_ : e.g.,

11

**as.character** ( **c** (1, 2, 3)) ## [1] "1" "2" "3" **as.numeric** ( **c** ("1", "2.73")) ## [1] 1.00 2.73 **as.factor** ( **c** ("a", "b", "c")) ## [1] a b c ## Levels: a b c

Some common conversions are converting numbers that are being interpreted as characters into actual numbers, converting between factors and characters, and converting between logical TRUE/FALSE vectors and numeric 1/0 vectors. In some cases R will automatically do conversions behind the scenes in a smart way (or occasionally not so smart way). We saw see implicit conversion (also called coercion) when we read in characters into R using _read.table()_ - strings are often automatically coerced to factors. Consider these examples of implicit coercion:

x <- **rnorm** (5) x[3] <- "hat" _# What do you think is going to happen?_ indices = **c** (1, 2.73) myVec = 1:10 myVec[indices] ## [1] 1 2

In other languages, converting between different classes is sometimes called _casting_ a variable. Here’s an example we can work through that will help illustrate how type conversions occur behind the scenes in R.

n <- 5 df <- **data.frame** ( **rep** ("a", n), **rnorm** (n), **rnorm** (n)) **apply** (df, 1, **function** (x) x[2] + x[3])

**## Error: non-numeric argument to binary operator** _# why does that not work?_ **apply** (df[, 2:3], 1, **function** (x) x[1] + x[2])

12

---

[← Unit 04 — usingR Part 17 —](17-unit-04-usingr-part-17.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 19 — →](19-unit-04-usingr-part-19.md)
