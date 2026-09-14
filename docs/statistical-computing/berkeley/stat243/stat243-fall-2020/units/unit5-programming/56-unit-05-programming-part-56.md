---
title: Unit 05 — programming Part 56 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 56 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

How about here? What is going on?

97

x <- **rnorm** (1e7) x[1] <- NA myfun <- **function** (y){ **return** ( **mean** (y, na.rm = TRUE)) } **myfun** (x) ## [1] -0.000165

This makes sense if we look at _mean.default()_ . Consider where additional memory is used.

### **8.6 Deep copies and lists and character strings**

Prior to R 3.1.0, modifying an element of a list caused the entire list to be copied, basically what is called a _deep copy_ . In more recent versions of R, only the components that need to get copied are copied.

You can explore this using _.Internal(inspect())_ on a list.

R is also clever about saving copying when it works with character strings. Character vectors are handled in a similar way as lists.

### **8.7 Passing objects to compiled code (optional)**

This subsection is out-of-date and doesn’t reflect that most people these days use the _Rcpp_ package rather than the older .C and .Call interfaces to compiled code. We won’t cover this subsection in class and don’t expect you to know this material. However, if you do end up interfacing to external code, thinking about whether copies are made when calling out to external code can be important if you’re working with large objects.

As we’ve already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead. (However, a previous GSI commented to me that in Rcpp, one can pass by reference and avoid having copies made.)

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting. Here’s an example of calling compiled code:

res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex), tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar),

98

as.integer(useline), as.integer(length(xvar))) Let’s consider when copies are made in casts:

f <- **function** (arg1){ **print** ( **address** (arg1)) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x))

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

**library** (inline) src <- ' for (int i = 0; i < *n; i++) { x[i] = exp(x[i]); } ' sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention = ".C") _## sillyExp <- cfunction(signature(n = "integer", x = "numeric"), ## src, convention = ".C")_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] 0.143 out1 <- **sillyExp** (n = len, x = vals) **address** (vals) ## [1] "0x5639b8b81b20"

99

**.Internal** ( **inspect** (out1))

---

[← Unit 05 — programming Part 55 —](55-unit-05-programming-part-55.md) · [Up: contents](index.md) · [Unit 05 — programming Part 57 — →](57-unit-05-programming-part-57.md)
