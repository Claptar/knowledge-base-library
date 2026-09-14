---
title: Unit 04 — usingR Part 30 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 30 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Functions may have unspecified arguments, which is designated using ’...’. Unspecified arguments occurring at the beginning of the argument list are generally a collection of like objects that will be manipulated (consider _paste()_ , _c()_ , and _rbind()_ ), while unspecified arguments occurring at the end are often optional arguments (consider _plot()_ ). These optional arguments are sometimes passed along to a function within the function. For example, here’s my own wrapper for plotting, where any additional arguments specified by the user will get passed along to plot:

pplot <- **function** (x, y, pch = 16, cex = 0.4, ...) { **plot** (x, y, pch = pch, cex = cex, ...) }

If you want to manipulate what the user passed in as the _..._ args, rather than just passing them along, you can extract them (the following code would be used within a function to which _’...’_ is an argument:

myFun <- **function** (...) { **print** (..2) args <- **list** (...) **print** (args[[2]]) } **myFun** (1, 3, 5, 7) ## [1] 3 ## [1] 3

You can check if an argument is missing with _missing()_ . Arguments can also have default values, which may be _NULL_ . If you are writing a function and designate the default as _argname = NULL_ , you can check whether the user provided anything using is.null(argname). The default values can also relate to other arguments. As an example, consider _dgamma()_ :

42

**args** (dgamma) ## function (x, shape, rate = 1, scale = 1/rate, log = FALSE) ## NULL

Functions can be passed in as arguments (e.g., see the variants of _apply()_ ). Note that one does not need to pass in a named function - you can create the function on the spot - this is called an _anonymous function_ (also called a _lambda function_ in some languages such as Python):

mat <- **matrix** (1:9, 3) **apply** (mat, 2, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 1 1 1 ## [3,] 2 2 2 **apply** (mat, 1, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 3 3 3 ## [3,] 6 6 6 _# explain why the result of the last expression is # transposed_

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3/y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f)

43

---

[← 7 Functions, variable scoping, and frames](29-7-functions-variable-scoping-and-frames.md) · [Up: contents](index.md) · [$x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist" →](31-y-1-2-z-3-y-class-formals-f-1-pairlist.md)
