---
title: Unit 05 — programming Part 31 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 31 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Why couldn’t we just use _rbind()_ directly? Basically we’re using _do.call()_ to use functions that take “...” as input (i.e., functions accepting an arbitrary number of arguments) and to use the list as the input instead (i.e., to use the list elements).

More generally do.call() is a way to pass arguments to a function where the arguments are a list:

**do.call** (mean, **list** (1:10, na.rm = TRUE)) ## [1] 5.5

44

### **6.2 Inputs**

Arguments can be specifed in the correct order, or given out of order by specifying _name = value_ . R first tries to match arguments by name and then by position. In general the more important arguments are specified first. You can see the arguments and defaults for a function using _args()_ :

**args** (lm) ## function (formula, data, subset, weights, na.action, method = "qr", ## model = TRUE, x = FALSE, y = FALSE, qr = TRUE, singular.ok = TRUE, ## contrasts = NULL, offset, ...) ## NULL

You can’t generally tell directly which arguments are required; in general you’d need to look at the documentation. R will error out if it is expecting an argument, rather than looking for that argument elsewhere.

x <- 1 y <- 2 myfun <- **function** (x) { **print** (y) **print** (x) } **myfun** () ## [1] 2

**## Error in print(x): argument "x" is missing, with no default**

Functions may have unspecified arguments, which are designated using ’...’. Unspecified arguments occurring at the beginning of the argument list are generally a collection of like objects that will be manipulated (consider _paste()_ , _c()_ , and _rbind()_ ), while unspecified arguments occurring at the end are often optional arguments (consider _plot()_ ). These optional arguments are sometimes passed along to a function within the function. For example, here’s my own wrapper for plotting, where any additional arguments specified by the user will get passed along to plot:

pplot <- **function** (x, y, pch = 16, cex = 0.4, ...) { **plot** (x, y, pch = pch, cex = cex, ...) }

45

If you want to manipulate what the user passed in as the _..._ args, rather than just passing them along, you can extract them (the following code would be used within a function to which _’...’_ is an argument:

myFun <- **function** (...){ **print** (..2) args <- **list** (...) **print** (args[[2]]) } **myFun** (1,3,5,7) ## [1] 3 ## [1] 3

You can check if an argument is missing with _missing()_ . Arguments can also have default values, which may be _NULL_ . If you are writing a function and designate the default as _argname = NULL_ , you can check whether the user provided anything using is.null(argname). The default values can also relate to other arguments. As an example, consider _dgamma()_ :

**args** (dgamma) ## function (x, shape, rate = 1, scale = 1/rate, log = FALSE) ## NULL

As we’ve seen, functions can be passed in as arguments (e.g., see the variants of _apply()_ ). Note that one does not need to pass in a named function - you can create the function on the spot - this is called an _anonymous function_ (also called a _lambda function_ in some languages such as Python):

mat <- **matrix** (1:9, 3) **apply** (mat, 1, min) _# apply() uses match.fun()_ ## [1] 1 2 3 **apply** (mat, 2, **function** (vec) vec - vec[1]) ## [,1] [,2] [,3] ## [1,] 0 0 0 ## [2,] 1 1 1 ## [3,] 2 2 2

46

**apply** (mat, 1, **function** (vec) vec - vec[1])

---

[← 6 Functions, variable scope, and frames](30-6-functions-variable-scope-and-frames.md) · [Up: contents](index.md) · [Unit 05 — programming Part 32 — →](32-unit-05-programming-part-32.md)
