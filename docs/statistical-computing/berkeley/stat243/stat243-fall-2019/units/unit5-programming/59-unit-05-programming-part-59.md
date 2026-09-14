---
title: Unit 05 — programming Part 59 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 59 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Challenge** : How much memory is used in the following calculation?

x <- **rnorm** (1e7) myfun <- **function** (y){ z <- y **return** ( **mean** (z)) } **myfun** (x) ## [1] 6.88e-05

94

How about here? What is going on?

x <- **rnorm** (1e7) x[1] <- NA myfun <- **function** (y){ **return** ( **mean** (y, na.rm = TRUE)) } **myfun** (x) ## [1] -0.000164

This makes sense if we look at _mean.default()_ . Consider where additional memory is used.

### **8.7 Deep copies and lists and character strings**

Prior to R 3.1.0, modifying an element of a list caused the entire list to be copied, basically what is called a _deep copy_ . In more recent versions of R, only the components that need to get copied are copied.

You can explore this using _.Internal(inspect())_ on a list.

R is also clever about saving copying when it works with character strings. Character vectors are handled in a similar way as lists.

### **8.8 Strategies for saving memory**

A couple basic strategies for saving memory include:

- Avoiding unnecessary copies.

- Removing objects that are not being used and, if necessary (not generally needed), do a _gc()_ call.

If you’re really trying to optimize memory use, you may also consider:

- Using R6 classes and similar strategies to pass by reference.

- Substituting integer and logical vectors for numeric vectors when possible.

95

### **8.9 Example**

Let’s work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We’ll want to consider hidden uses of memory, passing objects to compiled code, and lazy evaluation. This code is courtesy of Yuval Benjamini. For our purposes here, let’s assume that _xvar_ and _yvar_ are very long vectors using a lot of memory.

fastcount <- **function** (xvar, yvar) { naline <- **is.na** (xvar) naline[ **is.na** (yvar)] = TRUE xvar[naline] <- 0 yvar[naline] <- 0 useline <- !naline; _# Table must be initialized for -1's_ tablex <- **numeric** ( **max** (xvar)+1) tabley <- **numeric** ( **max** (yvar)+1) **stopifnot** ( **length** (xvar) == **length** (yvar)) res <- **.C** ("fastcount",PACKAGE="GCcorrect", tablex = **as.integer** (tablex), tabley = **as.integer** (tabley), **as.integer** (xvar), **as.integer** (yvar), **as.integer** (useline), **as.integer** ( **length** (xvar))) xuse <- **which** (res$tablex>0) xnames <- xuse - 1 resb <- **rbind** (res$tablex[xuse], res$tabley[xuse]) **colnames** (resb) <- xnames **return** (resb) }

---

[← Unit 05 — programming Part 58 —](58-unit-05-programming-part-58.md) · [Up: contents](index.md) · [9 Computing on the language →](60-9-computing-on-the-language.md)
