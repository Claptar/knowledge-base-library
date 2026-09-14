---
title: Unit 05 — programming Part 54 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 54 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One implication is that in older versions of R, indexing large subsets can involve a lot of memory use.

x <- **rnorm** (1e7) y <- x[1:( **length** (x) - 1)]

In this case, in older versions of R, more memory is used than just for _x_ and _y_ , because the index sequence itself uses a bunch of memory.

#### **8.2.2 Monitoring overall memory use**

To understand how much memory is available on your computer, one needs to have a clear understanding of disk caching. The operating system will generally cache files/data in memory when it reads from disk. Then if that information is still in memory the next time it is needed, it will be much faster to access it the second time around than if it had to read the information from disk. While the cached information is using memory, that same memory is immediately available to other processes, so the memory is available even though it is “in use”.

We can see this via free -h (the “-h” is for ’human-readable’, i.e. show in GB (G)) on Linux machine.

total used free shared buff/cache available Mem: 251G 998M 221G 2.6G 29G 247G Swap: 7.6G 210M 7.4G

You’ll generally be interested in the _Memory_ row. (See below for some comments on _Swap_ .) The _shared_ column is complicated and probably won’t be of use to you. The _buff/cache_ column shows how much space is used for disk caching and related purposes but is actually available. Hence the _available_ column is the sum of the _free_ and _buff/cache_ columns (more or less). In this case only about 1 GB is in use (indicated in the _used_ column).

84

_top_ (Linux or Mac) and _vmstat_ (on Linux) both show overall memory use, but remember that the amount actually available to you is the amount free plus any buffer/cache usage. Here is some example output from _vmstat_ :

procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----r b swpd free buff cache si so bi bo in cs us sy id wa st 1 0 215140 231655120 677944 30660296 0 0 1 2 0 0 18 0 82 0 0

It shows 232 GB free and 31 GB used for cache and therefore available, for a total of 263 GB available.

Here are some example lines from _top_ :

KiB Mem : 26413715+total, 23180236+free, 999704 used, 31335072 buff/cache KiB Swap: 7999484 total, 7784336 free, 215148 used. 25953483+avail Mem

We see that this machine has 264 GB RAM (the total column in the _Mem_ row), with 259.5 GB available (232 GB free plus 31 GB buff/cache as seen in the _Mem_ row). (I realize the numbers don’t quite add up for reasons I don’t fully understand, but we probably don’t need to worry about that degree of exactness.) Only 1 GB is in use.

_Swap_ is essentially the reverse of disk caching. It is disk space that is used for memory when the machine runs out of physical memory. You never want your machine to be using swap for memory because your jobs will slow to a crawl. As seen above, the _swap_ line in both _free_ and _top_ shows 8 GB swap space, with very little in use, as desired.

### **8.3 The heap and the stack**

The _heap_ is the memory that is available for dynamically creating new objects while a program is executing, e.g., if you create a new object in R or call _new_ in C++. When more memory is needed the program can request more from the operating system. When objects are removed in R, R will handle the garbage collection of releasing that memory.

The _stack_ is the memory used for local variables when a function is called.

There’s a nice discussion of this on this Stack Overflow thread.

### **8.4 Hidden uses of memory**

- Replacement functions can hide the use of additional memory. How much memory is used here?

85

x <- **rnorm** (1e7) **gc** () **dim** (x) <- **c** (1e4, 1e3) **diag** (x) <- 1 **gc** ()

- Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.) Here ‘[<-‘ is a primitive function, so the modification of the vector can be done without a copy.

x <- **rnorm** (1e7) **address** (x) ## [1] "0x7ff6a0d8b010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2013877 108 3.79e+06 202 3.22e+06 172 ## Vcells 43652625 333 1.14e+08 870 1.32e+08 1006 x[5] <- 7 _## when run plainly in R, should be the same address as before_ **address** (x) ## [1] "0x7ff692aa8010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2013902 108 3.79e+06 202 3.22e+06 172 ## Vcells 43652687 333 1.14e+08 870 1.32e+08 1006

### **8.5 Passing objects to compiled code**

This subsection is out-of-date and doesn’t reflect that most people these days use the _Rcpp_ package rather than the older .C and .Call interfaces to compiled code. We won’t cover this subsection in

86

class and don’t expect you to know this material. However, if you do end up interfacing to external code, thinking about whether copies are made when calling out to external code can be important if you’re working with large objects.

As we’ve already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead. (However, Jared commented to me that in Rcpp, one can pass by reference and avoid having copies made.)

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting. Here’s an example of calling compiled code:

res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex), tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar), as.integer(useline), as.integer(length(xvar)))

Let’s consider when copies are made in casts:

f <- **function** (arg1){ **print** ( **address** (arg1)) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x))

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

**library** (inline) src <- ' for (int i = 0; i < *n; i++) { x[i] = exp(x[i]); } '

87

sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention = ".C") _## sillyExp <- cfunction(signature(n = "integer", x = "numeric"), ## src, convention = ".C")_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] 0.588 out1 <- **sillyExp** (n = len, x = vals) **address** (vals) ## [1] "0x556102053440" **.Internal** ( **inspect** (out1)) ## @5560fee14558 19 VECSXP g0c2 [NAM(7),ATT] (len=2, tl=0) ## @5560fd78a360 13 INTSXP g0c1 [] (len=1, tl=0) 100 ## @5560f7de3df0 14 REALSXP g0c7 [] (len=100, tl=0) 1.79952,2.71942,0.762483,3.6801,0.81796,... ## ATTRIB: ## @5560f874ffe8 02 LISTSXP g0c0 [] ## TAG: @5560f4b200b0 01 SYMSXP g1c0 [MARK,NAM(7),LCK,gp=0x6000] "names" ## @5560fee14598 16 STRSXP g0c2 [] (len=2, tl=0) ## @5560f4b706e0 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "n" ## @5560f4b70be8 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "x" **.Internal** ( **inspect** (out1$x)) ## @5560f7de3df0 14 REALSXP g0c7 [NAM(7)] (len=100, tl=0)

### **8.6 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ . When we discussed R as being call-byvalue in Section 6.7, copy-on-change was one of the reasons that copies of arguments are not always made.

88

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

f <- **function** (x){ **print** ( **gc** ()) **.Internal** ( **inspect** (x)) **return** (x) } y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2037919 109 3.79e+06 202 3.22e+06 172 ## Vcells 53696385 410 1.14e+08 870 1.32e+08 1006

**.Internal** ( **inspect** (y)) ## @7ff6a0d8b010 14 REALSXP g1c7 [MARK,NAM(7)] (len=10000000, tl=0) out <- **f** (y)

---

[← [1] "0x5560f7d89248"](53-1-0x5560f7d89248.md) · [Up: contents](index.md) · [Unit 05 — programming Part 55 — →](55-unit-05-programming-part-55.md)
