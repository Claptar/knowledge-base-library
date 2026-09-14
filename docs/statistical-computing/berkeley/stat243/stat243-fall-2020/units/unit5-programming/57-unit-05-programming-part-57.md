---
title: Unit 05 — programming Part 57 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 57 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.8 Strategies for saving memory**

A couple basic strategies for saving memory include:

- Avoiding unnecessary copies.

- Removing objects that are not being used and, if necessary (not generally needed), do a _gc()_ call.

If you’re really trying to optimize memory use, you may also consider:

- Using R6 classes and similar strategies to pass by reference.

- Substituting integer and logical vectors for numeric vectors when possible.

### **8.9 Example**

Let’s work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We’ll want to consider hidden uses of memory, when copies are made, and lazy evaluation. (In a real example we’d also want to think about when copies are made in calling compiled code, but we don’t do that in class.) This code is courtesy of Yuval Benjamini. For our purposes here, let’s assume that _xvar_ and _yvar_ are very long vectors using a lot of memory.

100

fastcount <- **function** (xvar, yvar) { naline <- **is.na** (xvar) naline[ **is.na** (yvar)] = TRUE xvar[naline] <- 0 yvar[naline] <- 0 useline <- !naline; _# Table must be initialized for -1's_ tablex <- **numeric** ( **max** (xvar)+1) tabley <- **numeric** ( **max** (yvar)+1) **stopifnot** ( **length** (xvar) == **length** (yvar)) res <- **.C** ("fastcount",PACKAGE="GCcorrect", tablex = **as.integer** (tablex), tabley = **as.integer** (tabley), **as.integer** (xvar), **as.integer** (yvar), **as.integer** (useline), **as.integer** ( **length** (xvar))) xuse <- **which** (res$tablex>0) xnames <- xuse - 1 resb <- **rbind** (res$tablex[xuse], res$tabley[xuse]) **colnames** (resb) <- xnames **return** (resb) }

---

[← Unit 05 — programming Part 56 —](56-unit-05-programming-part-56.md) · [Up: contents](index.md) · [9 Computing on the language (optional) →](58-9-computing-on-the-language-optional.md)
