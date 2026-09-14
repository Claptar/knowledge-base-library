---
title: '-4.06 kB length ( serialize (mySeq, NULL )) ## [1] 133'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# -4.06 kB length ( serialize (mySeq, NULL )) ## [1] 133

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

_top_ (Linux or Mac) and _vmstat_ (on Linux) both show overall memory use, but remember that the amount actually available to you is the amount free plus any buffer/cache usage. Here is some example output from _vmstat_ :

88

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

- Replacement functions can hide the use of additional memory. How much memory is used here? (Try running in R (not RStudio) on your own computer and note the _max_used_ column in the _gc()_ result should increase, indicating a copy was made.)

89

**rm** (x) **gc** (reset = TRUE) x <- **rnorm** (1e7) **gc** () **dim** (x) <- **c** (1e4, 1e3) **diag** (x) <- 1 **gc** ()

- Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.) Here ‘[<-‘ is a primitive function, so the modification of the vector can be done without a copy. Try it in R (not RStudio) on your own computer.

**rm** (x) **gc** (reset = TRUE) ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2021964 108 3.81e+06 203 2021964 108 ## Vcells 43674877 333 1.42e+08 1087 43674877 333 x <- **rnorm** (1e7) **address** (x) ## [1] "0x7f02491a0010" **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2021993 108 3.81e+06 203 2040532 109 ## Vcells 53674921 410 1.42e+08 1087 53706483 410 x[5] <- 7 _## When run plainly in R, should be the same address as before, ## indicating no copy was made. Knitting the doc messes the ## result up!_ **address** (x)

90

---

[← Unit 05 — programming Part 46 —](46-unit-05-programming-part-46.md) · [Up: contents](index.md) · [Unit 05 — programming Part 48 — →](48-unit-05-programming-part-48.md)
