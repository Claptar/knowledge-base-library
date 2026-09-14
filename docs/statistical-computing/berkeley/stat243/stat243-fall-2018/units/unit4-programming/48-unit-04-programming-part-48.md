---
title: Unit 04 — programming Part 48 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 48 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

86

Or we can see this using _mem_change()_ .

**library** (pryr) **rm** (x) **mem_change** (x <- **rnorm** (1e7)) ## 80 MB **address** (x) ## [1] "0x7fe89e6db010" **mem_change** (x[3] <- 8) ## 448 B **address** (x) ## [1] "0x7fe89e6db010" **mem_change** (y <- x) ## -80 MB **address** (y) ## [1] "0x7fe89e6db010" **mem_change** (x[3] <- 8) ## 80 MB **address** (x) ## [1] "0x7fe886540010" **address** (y) ## [1] "0x7fe89e6db010"

**Challenge** : explain the results of the example above.

87

**How does copy-on-change work and how can it be fooled?** As discussed by Radford Neal, who is working to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ” I believe some improvements have been made in recent versions of R in this regard.

Here are examples of how the NAMED count can be fooled into making a copy unnecessarily. Why do I say these copies are unnecessary and why is NAMED fooled?

a <- 1:5 **refs** (a) ## [1] 2 b <- a **address** (a) ## [1] "0x63ada80" **address** (b) ## [1] "0x63ada80" **refs** (a) ## [1] 2 **refs** (b) ## [1] 2 a[2] <- 0 b[2] <- 4 **address** (a) ## [1] "0x4e53ce0" **address** (b) ## [1] "0x4e52bc0"

88

We can use the _tracemem()_ function to assess what is going on without all those _inspect()_ calls. Anything surprising in what you see?

a <- 1:10 **tracemem** (a) ## [1] "<0x66b0758>" _## b and a share memory_ b <- a b[1] <- 1 ## tracemem[0x66b0758 -> 0x7e78288]: eval eval withVisible withCallingHandlers ## tracemem[0x7e78288 -> 0x65bdff8]: eval eval withVisible withCallingHandlers _## result when done through knitr is not as in plain R_ **untracemem** (a) **address** (a) ## [1] "0x66b0758" **address** (b) ## [1] "0x65bdff8" **rm** (x, y) f <- **function** (x) **sum** (x^2) y <- **rnorm** (10) _## result of next line should be 1 if executed in clean R session_ **refs** (y) _# from pryr - reports on the NAMED count_ ## [1] 2 **f** (y) ## [1] 7.37 **refs** (y) ## [1] 2

89

**address** (y) ## [1] "0x66499e8" y[3] <- 2 **address** (y) ## [1] "0x6613a78"

**Challenge** : How much memory is used in the following calculation?

x <- **rnorm** (1e7) myfun <- **function** (y){ z <- y **return** ( **mean** (z)) } **myfun** (x) ## [1] 7.44e-05

How about here? What is going on?

x <- **rnorm** (1e7) x[1] <- NA myfun <- **function** (y){ **return** ( **mean** (y, na.rm = TRUE)) } **myfun** (x) ## [1] -0.000168

This makes sense if we look at _mean.default()_ . Consider where additional memory is used.

### **8.7 Deep copies and lists and character strings**

Prior to R 3.1.0, modifying an element of a list caused the entire list to be copied, basically what is called a _deep copy_ . In more recent versions of R, only the components that need to get copied are copied.

You can explore this using _.Internal(inspect())_ on a list.

90

R is also clever about saving copying when it works with character strings. We might explore this in a problem set problem.

### **8.8 Strategies for saving memory**

A couple basic strategies for saving memory include:

- Avoiding unnecessary copies.

- Removing objects that are not being used and, if necessary (not generally needed), do a _gc()_ call.

If you’re really trying to optimize memory use, you may also consider:

- Using R6 classes and similar strategies to pass by reference.

- Substituting integer and logical vectors for numeric vectors when possible.

### **8.9 Example**

Let’s work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We’ll want to consider hidden uses of memory, passing objects to compiled code, and lazy evaluation. This code is courtesy of Yuval Benjamini. For our purposes here, let’s assume that _xvar_ and _yvar_ are very long vectors using a lot of memory.

fastcount <- **function** (xvar, yvar) { naline <- **is.na** (xvar) naline[ **is.na** (yvar)] = TRUE xvar[naline] <- 0 yvar[naline] <- 0 useline <- !naline; _# Table must be initialized for -1's_ tablex <- **numeric** ( **max** (xvar)+1) tabley <- **numeric** ( **max** (yvar)+1) **stopifnot** ( **length** (xvar) == **length** (yvar)) res <- **.C** ("fastcount",PACKAGE="GCcorrect", tablex = **as.integer** (tablex), tabley = **as.integer** (tabley), **as.integer** (xvar), **as.integer** (yvar), **as.integer** (useline), **as.integer** ( **length** (xvar)))

91

xuse <- **which** (res$tablex>0) xnames <- xuse - 1 resb <- **rbind** (res$tablex[xuse], res$tabley[xuse]) **colnames** (resb) <- xnames **return** (resb) }

---

[← @7fe88b18c010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)](47-7fe88b18c010-14-realsxp-g1c7-mark-nam-2-len-10000000-tl-0.md) · [Up: contents](index.md) · [9 Computing on the language →](49-9-computing-on-the-language.md)
