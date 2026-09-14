---
title: '[1] "0x5a193b8" address (obj$a)'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "0x5a193b8" address (obj$a)

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**## Error: x must be the name of an object**

Apparently there is a memory profiler in R, _Rprofmem_ , but it needs to be enabled when R is compiled (i.e., installed on the machine), because it slows R down even when not used. So I’ve never gotten to the point of playing around with it.

**Faster representations of sequences** As mentioned above, as of R 3.5.0, 1:n is not stored in memory as a vector of length _n_ , but rather is represented by the first and last value in the sequence. However, some of the functions we use to determine object size don’t give us the right answer in this case. I haven’t run this when generating this document as my current machine is still using R 3.4.3.

**library** (microbenchmark)

n <- 1e6 **microbenchmark** (tmp <- 1:n)

79

**object.size** (tmp) _# incorrect as of R 3.5_ **object_size** (tmp) _# incorrect as of R 3.5_ **mem_change** (tmp2 <- 1:n) **length** ( **serialize** (tmp, **NULL** )) _# expands the object out_

One implication is that in older versions of R, indexing large subsets can involve a lot of memory use.

x <- **rnorm** (1e7) **gc** () y <- x[1:( **length** (x) - 1)] **gc** ()

In this case, in older versions of R, more memory is used than just for _x_ and _y_ , because the index sequence itself uses a bunch of memory.

#### **8.2.2 Monitoring overall memory use**

To understand how much memory is available on your computer, one needs to have a clear understanding of disk caching. The operating system will generally cache files/data in memory when it reads from disk. Then if that information is still in memory the next time it is needed, it will be much faster to access it the second time around than if it had to read the information from disk. While the cached information is using memory, that same memory is immediately available to other processes, so the memory is available even though it is “in use”.

We can see this via free -h (the “-h” is for ’human-readable’, i.e. show in GB (G)) on Linux machine.

total used free shared buff/cache available Mem: 251G 998M 221G 2.6G 29G 247G Swap: 7.6G 210M 7.4G

You’ll generally be interested in the _Memory_ row. (See below for some comments on _Swap_ .) The _shared_ column is complicated and probably won’t be of use to you. The _buff/cache_ column shows how much space is used for disk caching and related purposes but is actually available. Hence the _available_ column is the sum of the _free_ and _buff/cache_ columns (more or less). In this case only about 1 GB is in use (indicated in the _used_ column).

_top_ (Linux or Mac) and _vmstat_ (on Linux) both show overall memory use, but remember that the amount actually available to you is the amount free plus any buffer/cache usage. Here is some example output from _vmstat_ :

80

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

x <- **rnorm** (1e7) **gc** () **dim** (x) <- **c** (1e4, 1e3)

81

**diag** (x) <- 1 **gc** ()

- Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.) Here ‘[<-‘ is a primitive function, so the modification of the vector can be done without a copy.

x <- **rnorm** (1e7) **address** (x) ## [1] "0x7fe88b38e010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 831046 44.4 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 41472277 316.5 1.12e+08 856.1 1.31e+08 1003.1 x[5] <- 7 _## when run plainly in R, should be the same address as before_ **address** (x) ## [1] "0x7fe89e6db010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 831071 44.4 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 41472317 316.5 1.12e+08 856.1 1.31e+08 1003.1

### **8.5 Passing objects to compiled code**

As we’ve already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead.

82

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting. Here’s an example of calling compiled code:

res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex), tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar), as.integer(useline), as.integer(length(xvar)))

Let’s consider when copies are made in casts:

f <- **function** (arg1){ **print** ( **address** (arg1)) **return** ( **mean** (arg1)) } x <- **rnorm** (10) **class** (x) **debug** (f) **f** (x) **f** ( **as.numeric** (x)) **f** ( **as.integer** (x)) Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C. **library** (inline) src <- ' for (int i = 0; i < *n; i++) { x[i] = exp(x[i]); } ' sillyExp <- **cfunction** ( **signature** (n = "integer", x = "numeric"), src, convention = ".C") _## sillyExp <- cfunction(signature(n = "integer", x = "numeric"), ## src, convention = ".C")_ len <- **as.integer** (100) _# or 100L_ vals <- **rnorm** (len) vals[1] ## [1] 1.56

Next we’ll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We’ll use the _inline_ package to work directly with C code in R and the .C functionality for interfacing with C.

83

out1 <- **sillyExp** (n = len, x = vals) **address** (vals) ## [1] "0x4b79600" **.Internal** ( **inspect** (out1)) ## @7e773b0 19 VECSXP g0c2 [NAM(2),ATT] (len=2, tl=0) ## @778ff18 13 INTSXP g0c1 [] (len=1, tl=0) 100 ## @7b58280 14 REALSXP g0c7 [] (len=100, tl=0) 4.75164,2.18798,0.25021,1.76176,3.01826,... ## ATTRIB: ## @65091f0 02 LISTSXP g0c0 [] ## TAG: @1a1b3f0 01 SYMSXP g1c0 [MARK,NAM(2),LCK,gp=0x6000] "names" (has ## @7e773e8 16 STRSXP g0c2 [] (len=2, tl=0) ## @1a81488 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "n" ## @1a818d8 09 CHARSXP g1c1 [MARK,gp=0x61] [ASCII] [cached] "x" **.Internal** ( **inspect** (out1$x)) ## @7b58280 14 REALSXP g0c7 [NAM(2)] (len=100, tl=0) 4.75164,2.18798,0.25021,1.76176,3.01826,...

### **8.6 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ . When we discussed R as being call-byvalue in Section 6.7, copy-on-change was one of the reasons that copies of arguments are not always made.

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

f <- **function** (x){ **print** ( **gc** ()) **.Internal** ( **inspect** (x)) **return** (x) } y <- **rnorm** (1e7)

84

**gc** ()

---

[← Unit 04 — programming Part 43 —](43-unit-04-programming-part-43.md) · [Up: contents](index.md) · [Unit 04 — programming Part 45 — →](45-unit-04-programming-part-45.md)
