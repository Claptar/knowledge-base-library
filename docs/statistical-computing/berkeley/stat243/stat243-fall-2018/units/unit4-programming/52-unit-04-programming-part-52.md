---
title: Unit 04 — programming Part 52 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 52 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can evaluate language types using _eval()_ :

**rm** (x) **eval** (e1) **rm** (x) **eval** (e2) e1mlist <- **as.list** (e1m) e2list <- **as.list** (e2) **eval** ( **as.call** (e2list)) _## here's how to do it if the language object is actually an expression_ **eval** ( **as.expression** (e1mlist))

96

Now let’s look in more detail at the components of R expressions. We’ll be able to get a sense from this of how R evaluates code. We see that when R evaluates a parse tree, the first element says what function to use and the remaining elements are the arguments. But in many cases one or more arguments will themselves be call objects, so there’s recursion.

e1 <- **expression** (x <- 3) _## e1 is one-element list with the element an object of class '<-'_ **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" e1[[1]] ## x <- 3 **as.list** (e1[[1]]) ## [[1]] ## `<-` ## ## [[2]] ## x ## ## [[3]] ## [1] 3 **lapply** (e1[[1]], class) ## [[1]] ## [1] "name" ## ## [[2]] ## [1] "name" ## ## [[3]] ## [1] "numeric" y <- **rnorm** (5) e3 <- **quote** ( **mean** (y)) **print** ( **c** ( **class** (e3), **typeof** (e3)))

97

---

[← Unit 04 — programming Part 51 —](51-unit-04-programming-part-51.md) · [Up: contents](index.md) · [Unit 04 — programming Part 53 — →](53-unit-04-programming-part-53.md)
