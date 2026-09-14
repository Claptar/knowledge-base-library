---
title: Unit 04 — programming Part 39 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 39 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given our understanding of copy-on-change, explain what happens here:

y <- 1:5 **address** (y) ## [1] "0x5a87178" x <- y **address** (x) ## [1] "0x5a87178" y[2] <- 4 **address** (y) ## [1] "0x5773f68"

80

**address** (x) ## [1] "0x5a87178"

**Challenge** : How much memory is used in the following calculation?

x <- **rnorm** (1e7) myfun <- **function** (y){ z <- y **return** ( **mean** (z)) } **myfun** (x) ## [1] 0.000227

How about here? What is going on?

x <- **rnorm** (1e7) x[1] <- NA myfun <- **function** (y){ **return** ( **mean** (y, na.rm = TRUE)) } **myfun** (x) ## [1] 0.000218

This makes sense if we look at _mean.default()_ . Consider where additional memory is used.

### **8.6 Deep copies and lists**

Prior to R 3.1.0, modifying an element of a list caused the entire list to be copied, basically what is called a _deep copy_ . In more recent versions of R, only the components that need to get copied are copied.

You can explore this using _.Internal(inspect())_ on a list.

### **8.7 Strategies for saving memory**

A couple basic strategies for saving memory include:

81

- Avoiding unnecessary copies.

- Removing objects that are not being used and, if necessary (not generally needed), do a _gc()_ call.

If you’re really trying to optimize memory use, you may also consider:

- Using reference classes and similar strategies to pass by reference.

- Substituting integer and logical vectors for numeric vectors when possible.

### **8.8 Example**

Let’s work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We’ll want to consider hidden uses of memory, passing objects to compiled code, and lazy evaluation. This code is courtesy of Yuval Benjamini. For our purposes here, let’s assume that _xvar_ and _yvar_ are very long vectors using a lot of memory.

fastcount <- **function** (xvar,yvar) { naline <- **is.na** (xvar) naline[ **is.na** (yvar)] = TRUE xvar[naline] <- 0 yvar[naline] <- 0 useline <- !naline; _# Table must be initialized for -1's_ tablex <- **numeric** ( **max** (xvar)+1) tabley <- **numeric** ( **max** (yvar)+1) **stopifnot** ( **length** (xvar) == **length** (yvar)) res <- **.C** ("fastcount",PACKAGE="GCcorrect", tablex = **as.integer** (tablex), tabley = **as.integer** (tabley), **as.integer** (xvar), **as.integer** (yvar), **as.integer** (useline), **as.integer** ( **length** (xvar))) xuse <- **which** (res$tablex>0) xnames <- xuse - 1 resb <- **rbind** (res$tablex[xuse], res$tabley[xuse]) **colnames** (resb) <- xnames **return** (resb)

}

82

---

[← Unit 04 — programming Part 38 —](38-unit-04-programming-part-38.md) · [Up: contents](index.md) · [9 Computing on the language →](40-9-computing-on-the-language.md)
