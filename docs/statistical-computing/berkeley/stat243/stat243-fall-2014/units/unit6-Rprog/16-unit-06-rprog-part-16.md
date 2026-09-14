---
title: Unit 06 — Rprog Part 16 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 16 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As discussed by Radford Neal, who is working to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ”

34

Here are examples of how the NAMED count can be fooled into making a copy unnecessarily. Why do I say these copies are unnecessary and why is NAMED fooled?

**rm** (x, y) f <- **function** (x) **sum** (x^2) y <- **rnorm** (10) **f** (y) ## [1] 12.88 **.Internal** ( **inspect** (y)) ## @237f7688 14 REALSXP g0c6 [NAM(2)] (len=10, tl=0) y[3] <- 2 **.Internal** ( **inspect** (y)) ## @2353d098 14 REALSXP g0c6 [NAM(1)] (len=10, tl=0) -0.332636,0.12636,2,-1.60154,1.04408,... a <- 1:5 b <- a **.Internal** ( **inspect** (a)) ## @23684858 13 INTSXP g0c3 [NAM(2)] (len=5, tl=0) 1,2,3,4,5 **.Internal** ( **inspect** (b)) ## @23684858 13 INTSXP g0c3 [NAM(2)] (len=5, tl=0) 1,2,3,4,5 a[2] <- 0 b[2] <- 4 **.Internal** ( **inspect** (a)) ## @23357c30 14 REALSXP g0c4 [NAM(1)] (len=5, tl=0) 1,0,3,4,5 **.Internal** ( **inspect** (b)) ## @2328dc58 14 REALSXP g0c4 [NAM(1)] (len=5, tl=0) 1,4,3,4,5

We can use the _tracemem()_ function to assess what is going on without all those _inspect()_ calls. Anything surprising in what you see?

35

a <- 1:10 **tracemem** (a) ## [1] "<0x267d0f80>" _## b and a share memory_ b <- a b[1] <- 1 ## tracemem[0x267d0f80 -> 0x23215f08]: eval eval withVisible withCallingHandlers ## tracemem[0x23215f08 -> 0x23214390]: eval eval withVisible withCallingHandlers _## result when done through knitr is not as in plain R_ **untracemem** (a) **.Internal** ( **inspect** (a)) ## @267d0f80 13 INTSXP g0c4 [NAM(2)] (len=10, tl=0) 1,2,3,4,5,... **.Internal** ( **inspect** (b)) ## @23214390 14 REALSXP g0c6 [NAM(1),TR] (len=10, tl=0) 1,2,3,4,5,... Given our understanding of copy-on-change, explain what happens here:

y <- 1:5 **.Internal** ( **inspect** (y)) ## @1f758a08 13 INTSXP g0c3 [NAM(2)] (len=5, tl=0) 1,2,3,4,5 x <- y **.Internal** ( **inspect** (x)) ## @1f758a08 13 INTSXP g0c3 [NAM(2)] (len=5, tl=0) 1,2,3,4,5 y[2] <- 4 **.Internal** ( **inspect** (y)) ## @1f77ff78 14 REALSXP g0c4 [NAM(1)] (len=5, tl=0) 1,4,3,4,5 **.Internal** ( **inspect** (x)) ## @1f758a08 13 INTSXP g0c3 [NAM(2)] (len=5, tl=0) 1,2,3,4,5

36

**Challenge** : How much memory is used in the following calculation?

x <- **rnorm** (1e+07) myfun <- **function** (y) { z <- y **return** ( **mean** (z)) } **myfun** (x) ## [1] 0.0004207

How about here? What is going on?

x <- **rnorm** (1e+07) x[1] <- NA myfun <- **function** (y) { **return** ( **mean** (y, na.rm = TRUE)) } **myfun** (x) ## [1] -7.429e-05

This makes sense if we look at _mean.default()_ . Consider where additional memory is used.

### **3.6 Strategies for saving memory**

A couple basic strategies for saving memory include:

- Avoiding unnecessary copies

- Removing objects that are not being used and, if necessary (not generally needed), do a _gc()_ call.

If you’re really trying to optimize memory use, you may also consider:

- Using reference classes and similar strategies to pass by reference

- Substituting integer and logical vectors for numeric vectors when possible

37

### **3.7 Example**

Let’s work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We’ll want to consider hidden uses of memory, passing objects to compiled code, and lazy evaluation. This code is courtesy of Yuval Benjamini. For our purposes here, let’s assume that _xvar_ and _yvar_ are very long vectors using a lot of memory.

fastcount <- **function** (xvar, yvar) { naline <- **is.na** (xvar) naline[ **is.na** (yvar)] = TRUE xvar[naline] <- 0 yvar[naline] <- 0 useline <- !naline _# Table must be initialized for -1's_ tablex <- **numeric** ( **max** (xvar) + 1) tabley <- **numeric** ( **max** (yvar) + 1) **stopifnot** ( **length** (xvar) == **length** (yvar)) res <- **.C** ("fastcount", PACKAGE = "GCcorrect", tablex = **as.integer** (tablex), tabley = **as.integer** (tabley), **as.integer** (xvar), **as.integer** (yvar), **as.integer** ( **length** (xvar))) xuse <- **which** (res$tablex > 0) xnames <- xuse - 1 resb <- **rbind** (res$tablex[xuse], res$tabley[xuse]) **colnames** (resb) <- xnames **return** (resb)

}

---

[← @7fad5d1d7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)](15-7fad5d1d7010-14-realsxp-g1c7-mark-nam-2-len-10000000-tl-0.md) · [Up: contents](index.md) · [4 Object-oriented programming (OOP) →](17-4-object-oriented-programming-oop.md)
