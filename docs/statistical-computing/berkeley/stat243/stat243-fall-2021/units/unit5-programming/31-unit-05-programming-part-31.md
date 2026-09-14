---
title: Unit 05 — programming Part 31 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 31 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

45

You can’t generally tell directly which arguments are required; in general you’d need to look at the documentation. R will error out if it is expecting an argument, rather than looking for that argument elsewhere.

x <- 1 y <- 2 myfun <- **function** (x) { **print** (y) **print** (x) } **myfun** () ## [1] 2 **## Error in h(simpleError(msg, call)): error in evaluating the argument ’x’ in selecting a method for function ’print’: argument "x" is missing, with no default**

Functions may have unspecified arguments, which are designated using ’...’. Unspecified arguments occurring at the beginning of the argument list are generally a collection of like objects that will be manipulated (consider _paste()_ , _c()_ , and _rbind()_ ), while unspecified arguments occurring at the end are often optional arguments (consider _plot()_ ). These optional arguments are sometimes passed along to a function within the function. For example, here’s my own wrapper for plotting, where any additional arguments specified by the user will get passed along to plot:

pplot <- **function** (x, y, pch = 16, cex = 0.4, ...) { **plot** (x, y, pch = pch, cex = cex, ...) }

If you want to manipulate what the user passed in as the _..._ args, rather than just passing them along, you can extract them (the following code would be used within a function to which _’...’_ is an argument:

myFun <- **function** (...){ **print** (..2) args <- **list** (...) **print** (args[[2]]) }

46

**myFun** (1,3,5,7)

---

[← Unit 05 — programming Part 30 —](30-unit-05-programming-part-30.md) · [Up: contents](index.md) · [Unit 05 — programming Part 32 — →](32-unit-05-programming-part-32.md)
