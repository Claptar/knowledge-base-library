---
title: Unit 05 — programming Part 47 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 47 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The _pryr_ package provides _address()_ or _inspect()_ as an alternative to _.Internal(inspect())_ though as we see here it doesn’t give us the richness of information about complicated objects that _inspect()_ does.

**address** (x) _# from pryr_ ## [1] "0x55691ae3c4c8"

89

**address** (obj) ## [1] "0x55691a84d8a8" **address** (obj$a) _# doesn't work_

**## Error: x must be the name of an object**

Similar tricks are used for storing character vectors.

#### **8.4.3 Replacement functions**

- Replacement functions can hide the use of additional memory. How much memory is used here? (Try running in R (not RStudio) on your own computer and note the _max_used_ column in the _gc()_ result should increase, indicating a copy was made.)

**rm** (x) **gc** (reset = TRUE) x <- **rnorm** (1e7) **gc** () **dim** (x) <- **c** (1e4, 1e3) **diag** (x) <- 1 **gc** ()

- Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.) Here ‘[<-‘ is a primitive function, so the modification of the vector can be done without a copy. Try it in R (not RStudio) on your own computer.

**rm** (x) **gc** (reset = TRUE) ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 1196045 63.9 2.30e+06 123 1196045 63.9 ## Vcells 42267187 322.5 1.43e+08 1090 42267187 322.5

90

x <- **rnorm** (1e7) **address** (x) ## [1] "0x7ff4761ee010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 1196068 63.9 2.30e+06 123 1214263 64.9 ## Vcells 52267221 398.8 1.43e+08 1090 52298699 399.1 x[5] <- 7 _## When run plainly in R, should be the same address as before, ## indicating no copy was made. Knitting the doc messes the ## result up!_ **address** (x) ## [1] "0x7ff4715a2010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 1196108 63.9 2.30e+06 123 1214585 64.9 ## Vcells 52267273 398.8 1.43e+08 1090 62298483 475.3

#### **8.4.4 Fast representations of sequences**

As of R 3.5.0, 1:n is not stored in memory as a vector of length _n_ , but rather is represented by the first and last value in the sequence. However, some of the functions we use to determine object size don’t give us the right answer in this case.

**library** (microbenchmark) n <- 1e6 **microbenchmark** (tmp <- 1:n) ## Unit: nanoseconds ## expr min lq mean median uq max neval ## tmp <- 1:n 197 204 276 209 262 4105 100

91

**object.size** (tmp) _# incorrect as of R 3.5_ ## 4000048 bytes **object_size** (tmp) _# incorrect as of R 3.5_ ## 4 MB **mem_change** (mySeq <- 1:n) _# not sure why the result is negative!_ ## -4.06 kB **length** ( **serialize** (mySeq, **NULL** )) ## [1] 133

One implication is that in older versions of R, indexing large subsets can involve a lot of memory use.

x <- **rnorm** (1e7) y <- x[1:( **length** (x) - 1)]

In this case, in older versions of R, more memory is used than just for _x_ and _y_ , because the index sequence itself uses a bunch of memory.

### **8.5 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ . When we discussed R as being call-byvalue in Section 6.5, copy-on-change was one of the reasons that copies of arguments are not always made. (But we didn’t talk about it at that time.)

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

**rm** (x) **rm** (y) **gc** (reset = TRUE)

92

---

[← Unit 05 — programming Part 46 —](46-unit-05-programming-part-46.md) · [Up: contents](index.md) · [Unit 05 — programming Part 48 — →](48-unit-05-programming-part-48.md)
