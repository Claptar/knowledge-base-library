---
title: Unit 06 — Rprog Part 11 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 11 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

29

### **3.3 Hidden uses of memory**

- Replacement functions can hide the use of additional memory. How much memory is used here?

x <- **rnorm** (1e+07) **gc** () **dim** (x) <- **c** (10000, 1000) **diag** (x) <- 1 **gc** ()

- Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.)

x <- **rnorm** (1e+07) **.Internal** ( **inspect** (x)) ## @7fad5d1d7010 14 REALSXP g0c7 [NAM(2)] (len=10000000, tl=0) x[5] <- 7 _# when run plainly in R, should be the same address as before_ **.Internal** ( **inspect** (x)) ## @7fad5858b010 14 REALSXP g0c7 [NAM(1)] (len=10000000, tl=0) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 5533129 295.6 8125770 434 8125770 434 ## Vcells 102376726 781.1 212429759 1621 192393222 1468

- Indexing large subsets can involve a lot of memory use.

30

x <- **rnorm** (1e+07) **gc** () y <- x[1:( **length** (x) - 1)] **gc** ()

Why was more memory used than just for _x_ and _y_ ? Note that this is a limitation of R. Note that R could be designed to avoid this problem (see our discussion of _pqR_ earlier in this Unit).

### **3.4 Passing objects to compiled code**

As we’ve already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead.

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting. Here’s an example of calling compiled code:

res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex), tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar), as.integer(useline), as.integer(length(xvar)))

Let’s consider when copies are made in casts:

f <- **function** (arg1) { **print** ( **.Internal** ( **inspect** (arg1))) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x))

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

31

**library** (inline) src <- "\n\tfor (int i = 0; i < *n; i++) {\n\t\tx[i] = exp(x[i]);\n\t}\n" sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention _# sillyExp <- cfunction(signature(n = 'integer', x = 'numeric'), src, # convention = '.C')_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] 1.052 out1 <- **sillyExp** (n = len, x = vals) **.Internal** ( **inspect** (vals)) ## @23555100 14 REALSXP g0c7 [NAM(2)] (len=100, tl=0) **.Internal** ( **inspect** (out1$x)) ## @235718a0 14 REALSXP g0c7 [NAM(2)] (len=100, tl=0)

### **3.5 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ .

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

f <- **function** (x) { **print** ( **gc** ()) z <- x[1] **.Internal** ( **inspect** (x)) **return** (x) } y <- **rnorm** (1e+07) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb)

32

---

[← 3 Evaluating memory use](10-3-evaluating-memory-use.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 12 — →](12-unit-06-rprog-part-12.md)
