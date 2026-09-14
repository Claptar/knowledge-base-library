---
title: Unit 05 — programming Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 44 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can reset the value given for max used, with gc(reset = TRUE). In Windows only, _memory.size()_ tells how much memory is being used. You can check the amount of memory used by individual objects with _object.size()_ . Here is a useful function, _ls.sizes()_ , that wraps _object.size()_ to report the largest _n_ objects in a given environment:

ls.sizes <- **function** (howMany = 10, minSize = 1){ pf <- **parent.frame** () obj <- **ls** (pf) _# or ls(sys.frame(-1))_

84

objSizes <- **sapply** (obj, **function** (x) { pryr:: **object_size** ( **get** (x, pf)) }) _## or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()_ objNames <- **names** (objSizes) howmany <- **min** (howMany, **length** (objSizes)) ord <- **order** (objSizes, decreasing = TRUE) objSizes <- objSizes[ord][1:howMany] objSizes <- objSizes[objSizes > minSize] objSizes <- **matrix** (objSizes, ncol = 1) **rownames** (objSizes) <- objNames[ord][1: **length** (objSizes)] **colnames** (objSizes) <- "bytes" **cat** ('object') **print** ( **format** (objSizes, justify = "right", width = 11), quote = FALSE) }

Unfortunately with R6 and ReferenceClasses, closures, environments, and other such “containers”, it can be hard to see how much memory the object is using, including all the components of the object. Here’s a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

_## size of a closure_ x <- **rnorm** (1e7) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) **object.size** (myFun) ## 1608 bytes **object_size** (myFun) ## 80 MB

85

**length** ( **serialize** (myFun, **NULL** )) ## [1] 160010892 _## note that our discussion of copy-on-change will tell us ## why the 80 MB vs. 160 MB disagreement occurs ## size of an environment_ e <- **new.env** () e$x <- **rnorm** (1e7) **object.size** (e) ## 56 bytes **object_size** (e) ## 80 MB **length** ( **serialize** (e, **NULL** )) ## [1] 80000192

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you’re trying to cancel the statement with _Ctrl-C_ . You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

> R --max-vsize=1000M

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message “ _Error: vector memory exhausted (limit reached?)_ ”. So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven’t played around with this much, so offer this with a note of caution.

Apparently there is a memory profiler in R, _Rprofmem_ , but it needs to be enabled when R is compiled (i.e., installed on the machine), because it slows R down even when not used. So I’ve never gotten to the point of playing around with it.

86

#### **8.2.2 Monitoring overall memory use on a UNIX-style computer**

To understand how much memory is available on your computer, one needs to have a clear understanding of disk caching. The operating system will generally cache files/data in memory when it reads from disk. Then if that information is still in memory the next time it is needed, it will be much faster to access it the second time around than if it had to read the information from disk. While the cached information is using memory, that same memory is immediately available to other processes, so the memory is available even though it is “in use”.

We can see this via free -h (the “-h” is for ’human-readable’, i.e. show in GB (G)) on Linux machine.

total used free shared buff/cache available Mem: 251G 998M 221G 2.6G 29G 247G Swap: 7.6G 210M 7.4G

You’ll generally be interested in the _Memory_ row. (See below for some comments on _Swap_ .) The _shared_ column is complicated and probably won’t be of use to you. The _buff/cache_ column shows how much space is used for disk caching and related purposes but is actually available. Hence the _available_ column is the sum of the _free_ and _buff/cache_ columns (more or less). In this case only about 1 GB is in use (indicated in the _used_ column).

_top_ (Linux or Mac) and _vmstat_ (on Linux) both show overall memory use, but remember that the amount actually available to you is the amount free plus any buffer/cache usage. Here is some example output from _vmstat_ :

procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----r b swpd free buff cache si so bi bo in cs us sy id wa st 1 0 215140 231655120 677944 30660296 0 0 1 2 0 0 18 0 82 0 0

It shows 232 GB free and 31 GB used for cache and therefore available, for a total of 263 GB available.

Here are some example lines from _top_ :

KiB Mem : 26413715+total, 23180236+free, 999704 used, 31335072 buff/cache KiB Swap: 7999484 total, 7784336 free, 215148 used. 25953483+avail Mem

We see that this machine has 264 GB RAM (the total column in the _Mem_ row), with 259.5 GB available (232 GB free plus 31 GB buff/cache as seen in the _Mem_ row). (I realize the numbers don’t quite add up for reasons I don’t fully understand, but we probably don’t need to worry about that degree of exactness.) Only 1 GB is in use.

87

_Swap_ is essentially the reverse of disk caching. It is disk space that is used for memory when the machine runs out of physical memory. You never want your machine to be using swap for memory because your jobs will slow to a crawl. As seen above, the _swap_ line in both _free_ and _top_ shows 8 GB swap space, with very little in use, as desired.

### **8.3 The heap and the stack**

The _heap_ is the memory that is available for dynamically creating new objects while a program is executing, e.g., if you create a new object in R or call _new_ in C++. When more memory is needed the program can request more from the operating system. When objects are removed in R, R will handle the garbage collection of releasing that memory.

The _stack_ is the memory used for local variables when a function is called.

There’s a nice discussion of this on this Stack Overflow thread.

### **8.4 Hidden uses and hidden savings of memory**

#### **8.4.1 Using inspect() to understand storage and memory use for data structures**

We can use an internal function called _inspect()_ to see where in memory an object is stored. We’ll see that this can be a handy tool for seeing where copies are made and where they are not.

x <- **rnorm** (5) **.Internal** ( **inspect** (x)) ## @55691ae3c4c8 14 REALSXP g0c4 [REF(2)] (len=5, tl=0)

_### 8.4.2 How lists are stored_

#### **8.4.2 How lists are stored**

Here we can use _inspect()_ to see how the overall list is stored as well as the elements of the list and the attributes of the list.

nums <- **rnorm** (5) obj <- **list** (a = nums, b = nums, c = **rnorm** (5), d = **list** (some_string = "adfs" **.Internal** ( **inspect** (obj$a))

---

[← 8 Evaluating memory use](43-8-evaluating-memory-use.md) · [Up: contents](index.md) · [@556919e69138 14 REALSXP g0c4 [REF(4)] (len=5, tl=0) →](45-556919e69138-14-realsxp-g0c4-ref-4-len-5-tl-0.md)
