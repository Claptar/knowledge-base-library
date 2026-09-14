---
title: Unit 05 — programming Part 50 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 50 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Challenge** : explain the results of the example above.

**How does copy-on-change work?** R keeps track of how many names refer to an object and only makes copies as needed when multiple names refer to an object. Note the value of REF and the address returned by _.Internal(inspect())_ , or simply use _refs()_ and _address()_ from _pryr_ .

We’ll see this live in class. Unfortunately both knitting and RStudio can give us confusing results, so I’m adding the clean results from just running in R here in comments.

96

a <- **rnorm** (5) _## See below for result without RStudio or knitting messing things up ## .Internal(inspect(a)) ## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) ## refs(a) ## [1] 1_ **address** (a) _## [1] "0x556accc65948"_ b <- a _## See below for result without RStudio or knitting messing things up ## .Internal(inspect(b)) ## @556accc65948 14 REALSXP g0c4 [REF(2)] (len=5, tl=0) ## refs(a) ## [1] 2 ## refs(b) ## [1] 2_ **address** (b) _# [1] "0x556accc65948"_ a[2] <- 0 _## See below for result without RStudio or knitting messing things up ## .Internal(inspect(a)) ## @556accc657f8 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.524365,0,0.700011,-0.621318,-0.924413 ## .Internal(inspect(b)) ## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0)_ a <- **rnorm** (5) b <- a _## refs(a) ## [1] 2_ **rm** (b) _## refs(a) ## [1] 1_

In older versions of R (before R 4.0) there were some shortcomings in how R managed this, and one could see different results than shown below.

97

**How can can copy-on-change be fooled in older versions of R? (Optional)** In older versions of R (before R 4.0), the mechanism for determining whether two names refer to the same object was simplistic. As discussed by Radford Neal, who has worked to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ”

If you’re using an older version of R, you can view the NAMED count either via _.Internal(inspect())_ or by using _pryr::refs()_ .

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

f <- **function** (arg1){ **print** ( **address** (arg1)) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x)) Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C. **library** (inline) src <- ' for (int i = 0; i < *n; i++) { x[i] = exp(x[i]); } ' sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention = ".C") _## sillyExp <- cfunction(signature(n = "integer", x = "numeric"), ## src, convention = ".C")_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] 0.682 out1 <- **sillyExp** (n = len, x = vals) **address** (vals) ## [1] "0x556923c00090"

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

99

**.Internal** ( **inspect** (out1))

---

[← @7ff475a52010 14 REALSXP g1c7 [MARK,REF(7)] (len=10000000, tl=0)](49-7ff475a52010-14-realsxp-g1c7-mark-ref-7-len-10000000-tl-0.md) · [Up: contents](index.md) · [Unit 05 — programming Part 51 — →](51-unit-05-programming-part-51.md)
