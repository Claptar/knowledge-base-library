---
title: Unit 05 — programming Part 53 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 53 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

93

Or we can see this using _mem_change()_ .

**library** (pryr) **rm** (x) **rm** (y) **mem_change** (x <- **rnorm** (1e7)) ## 80 MB **address** (x) ## [1] "0x7f023c43c010" **mem_change** (x[3] <- 8) ## 320 B **address** (x) ## [1] "0x7f023c43c010" **mem_change** (y <- x) ## 376 B **address** (y) ## [1] "0x7f023c43c010" **mem_change** (x[3] <- 8) ## 80 MB **address** (x) ## [1] "0x7f02377f0010" **address** (y) ## [1] "0x7f023c43c010"

**Challenge** : explain the results of the example above.

94

**How does copy-on-change work?** R keeps track of how many names refer to an object and only makes copies as needed when multiple names refer to an object. Note the value of REF and the address returned by _.Internal(inspect())_ , or simply use _refs()_ and _address()_ from _pryr_ .

In older versions of R (before R 4.0) there were some shortcomings in how R managed this, and I am compiling this PDF on an older version of R (R 3.6). So I need to insert comments showing examples of what the results would be in R 4.0. Also, knitting to PDF contaminates things.

a <- **rnorm** (5) _## .Internal(inspect(a)) ## see below for result in R 4.0 ## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) ## refs(a) ## [1] 1_ **address** (a) ## [1] "0x5639b778e3a8" _## [1] "0x556accc65948"_ b <- a _## .Internal(inspect(b)) ## see below for result in R 4.0 ## @556accc65948 14 REALSXP g0c4 [REF(2)] (len=5, tl=0) ## refs(a) ## [1] 2 ## refs(b) ## [1] 2_ **address** (b) ## [1] "0x5639b778e3a8" _# [1] "0x556accc65948"_ a[2] <- 0 _## .Internal(inspect(a)) ## @556accc657f8 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.524365,0,0.700011,-0.621318,-0.924413 ## .Internal(inspect(b)) ## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0)_ a <- **rnorm** (5) b <- a

95

_## refs(a) ## [1] 2_ **rm** (b) _## refs(a) ## [1] 1_

**How can can copy-on-change be fooled in older versions of R? (Optional)** In older versions of R (before R 4.0), the mechanism for determining whether two names refer to the same object was simplistic. As discussed by Radford Neal, who has worked to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ”

If you’re using an older version of R, you can view the NAMED count either via _.Internal(inspect())_ or by using _pryr::refs()_ .

Here are examples of how the NAMED count can be fooled into making a copy unnecessarily. Why do I say these copies are unnecessary and why is NAMED fooled?

We can use the _tracemem()_ function to assess what is going on without all those _inspect()_ calls. Anything surprising in what you see?

a <- 1:10 **tracemem** (a)

---

[← @7f02491a0010 14 REALSXP g1c7 [MARK,NAM(7)] (len=10000000, tl=0)](52-7f02491a0010-14-realsxp-g1c7-mark-nam-7-len-10000000-tl-0.md) · [Up: contents](index.md) · [[1] "<0x5639b3906dc8>" ## b and a share memory b <- a b[1] <- 1 →](54-1-0x5639b3906dc8-b-and-a-share-memory-b---a-b-1---1.md)
