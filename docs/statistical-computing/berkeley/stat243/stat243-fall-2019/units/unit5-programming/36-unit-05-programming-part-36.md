---
title: Unit 05 — programming Part 36 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 36 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can check if an argument is missing with _missing()_ . Arguments can also have default values, which may be _NULL_ . If you are writing a function and designate the default as _argname = NULL_ , you can check whether the user provided anything using is.null(argname). The default values can also relate to other arguments. As an example, consider _dgamma()_ :

45

**args** (dgamma) ## function (x, shape, rate = 1, scale = 1/rate, log = FALSE) ## NULL

As we’ve seen, functions can be passed in as arguments (e.g., see the variants of _apply()_ ). Note that one does not need to pass in a named function - you can create the function on the spot - this is called an _anonymous function_ (also called a _lambda function_ in some languages such as Python):

mat <- **matrix** (1:9, 3) **apply** (mat, 1, min) _# apply() uses match.fun()_ ## [1] 1 2 3 **apply** (mat, 2, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 1 1 1 ## [3,] 2 2 2 **apply** (mat, 1, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 3 3 3 ## [3,] 6 6 6 _## explain why the result of the last expression is transposed_

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f)

46

---

[← Unit 05 — programming Part 35 —](35-unit-05-programming-part-35.md) · [Up: contents](index.md) · [$x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist" →](37-y-1-2-z-3-y-class-formals-f-1-pairlist.md)
