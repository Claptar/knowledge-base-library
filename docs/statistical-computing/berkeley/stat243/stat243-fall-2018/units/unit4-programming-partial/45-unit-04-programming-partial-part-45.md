---
title: Unit 04 — programming partial Part 45 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 45 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can see the arguments using args() and extract the arguments using formals(). formals() can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f) ## $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y **class** ( **formals** (f)) ## [1] "pairlist"

A pairlist is like a list, but with pairing that in this case pairs argument names with default values.

match.call() will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE)

44

<mark>## what do you think quote does? Why is it needed?</mark>

### 6.3 Outputs

return(x) will specify x as the output of the function. By default, if return() is not specified, the output is the result of the last evaluated statement. return() can occur anywhere in the function, and allows the function to exit as soon as it is done.

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9 **f** (3)

invisible(x) will return x and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with lm() and many other functions.

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

45

### 6.4 Frames and the call stack

R keeps track of the call stack, which is the series of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the frame from which a function was called.

Some terminology: for our purposes we’ll use the terms frame and environment somewhat interchangeably for the moment. A frame or environment is a collection of named objects. (Note that when we talk about variable scope in Section 6.8, we’ll have to be more careful with our terminology.)

sys.nframe() returns the number of the current frame/environment and sys.parent() the number of the parent, while parent.frame() gives the name of the frame/environment of the parent (i.e., the calling) frame. sys.frame() gives the name of the frame/environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the frame/environment. I won’t print the results here because knitr messes up the frame counting somehow.

---

[← Unit 04 — programming partial Part 44 —](44-unit-04-programming-partial-part-44.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 46 — →](46-unit-04-programming-partial-part-46.md)
