---
title: Unit 04 — programming Part 42 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 42 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Indexing large subsets can involve a lot of memory use.

x <- **rnorm** (1e7) **gc** () y <- x[1:( **length** (x) - 1)] **gc** ()

Why was more memory used than just for _x_ and _y_ ? Note that this is a limitation of R. Note that R could be designed to avoid this problem (see our discussion of _pqR_ earlier in this Unit).

### **8.5 Passing objects to compiled code**

As we’ve already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead.

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting. Here’s an example of calling compiled code:

res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex), tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar), as.integer(useline), as.integer(length(xvar)))

78

Let’s consider when copies are made in casts:

f <- **function** (arg1){ **print** ( **address** (arg1)) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x))

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

**library** (inline) src <- ' for (int i = 0; i < *n; i++) { x[i] = exp(x[i]); } ' sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention = ".C") _## sillyExp <- cfunction(signature(n = "integer", x = "numeric"), ## src, convention = ".C")_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] -0.0867 out1 <- **sillyExp** (n = len, x = vals) **address** (vals) ## [1] "0x41535d0"

79

**.Internal** ( **inspect** (out1))

---

[← [1] "0x4bc6358"](41-1-0x4bc6358.md) · [Up: contents](index.md) · [Unit 04 — programming Part 43 — →](43-unit-04-programming-part-43.md)
