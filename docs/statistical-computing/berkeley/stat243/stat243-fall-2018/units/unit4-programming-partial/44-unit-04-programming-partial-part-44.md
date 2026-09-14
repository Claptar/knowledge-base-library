---
title: Unit 04 — programming partial Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 44 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Functions may have unspecified arguments, which are designated using ’...’. Unspecified arguments occurring at the beginning of the argument list are generally a collection of like objects that will be manipulated (consider paste(), c(), and rbind()), while unspecified arguments occurring at the end are often optional arguments (consider plot()). These optional arguments are sometimes passed along to a function within the function. For example, here’s my own wrapper for plotting, where any additional arguments specified by the user will get passed along to plot:

pplot <- **function** (x, y, pch = 16, cex = 0.4, ...) { **plot** (x, y, pch = pch, cex = cex, ...) }

If you want to manipulate what the user passed in as the ... args, rather than just passing them along, you can extract them (the following code would be used within a function to which ’...’ is an argument:

42

myFun <- **function** (...){ **print** (..2) args <- **list** (...) **print** (args[[2]]) } **myFun** (1,3,5,7) ## [1] 3 ## [1] 3

You can check if an argument is missing with missing(). Arguments can also have default values, which may be NULL. If you are writing a function and designate the default as argname = NULL, you can check whether the user provided anything using is.null(argname). The default values can also relate to other arguments. As an example, consider dgamma():

**args** (dgamma) ## function (x, shape, rate = 1, scale = 1/rate, log = FALSE) ## NULL

As we’ve seen, functions can be passed in as arguments (e.g., see the variants of apply()). Note that one does not need to pass in a named function - you can create the function on the spot - this is called an anonymous function (also called a lambda function in some languages such as Python):

mat <- **matrix** (1:9, 3) **apply** (mat, 1, min) # apply() uses match.fun() ## [1] 1 2 3 **apply** (mat, 2, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 1 1 1 ## [3,] 2 2 2 **apply** (mat, 1, **function** (vec) vec - vec[1])

43

---

[← Unit 04 — programming partial Part 43 —](43-unit-04-programming-partial-part-43.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 45 — →](45-unit-04-programming-partial-part-45.md)
