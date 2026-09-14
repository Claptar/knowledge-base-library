---
title: '$names ## [1] "x" "y" ## ## $row.names ## [1] 1 2 ## ## $class ## [1] "data.frame"'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $names ## [1] "x" "y" ## ## $row.names ## [1] 1 2 ## ## $class ## [1] "data.frame"

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

15

**row.names** (mat) <- **c** ("first", "second") mat ## x y ## first 1 3 ## second 2 4 **attributes** (mat) ## $names ## [1] "x" "y" ## ## $row.names ## [1] "first" "second" ## ## $class ## [1] "data.frame" vec <- **c** (first = 7, second = 1, third = 5) vec['first'] ## first ## 7 **attributes** (vec) ## $names ## [1] "first" "second" "third"

### 4.3 Assignment and coercion

We assign into an object using either ’=’ or ’<-’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’=’ is fine, but otherwise use ’<-’.

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

16

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x45af208> ## <environment: namespace:base> x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) # usual way to pass an argument to a function ## what does the following do? out <- **mean** (x <- **c** (3,7)) # this is allowable, though perhaps not useful out <- **mean** (y = **c** (3,7))

**## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default** out <- **mean** (y <- **c** (3,7))

What can you tell me about what is going on in each case above?

One situation in which you want to use ’<-’ is if it is being used as part of an argument to a

function, so that R realizes you’re not indicating one of the function arguments, e.g.:

---

[← Unit 04 — programming partial Part 18 —](18-unit-04-programming-partial-part-18.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 20 — →](20-unit-04-programming-partial-part-20.md)
