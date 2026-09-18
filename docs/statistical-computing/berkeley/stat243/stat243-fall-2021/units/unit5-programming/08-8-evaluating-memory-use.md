---
title: 8 Evaluating memory use
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 8 Evaluating memory use

The main things to remember when thinking about memory use are: (1) numeric vectors take 8 bytes per element and (2) we need to keep track of when large objects are created, including local variables in the frames of functions.

In some of our work here we'll use functions from the pryr package, which provides functions to help understand what is going on under the hood in R.

In general, don't try to run this code within RStudio, as some of how RStudio works affects memory use. Also, some of the output in this PDF is missing or incorrect relative to running the code directly within R, because of effects from the knitting process.

## 8.1 Allocating and freeing memory

Unlike compiled languages like C, in R we do not need to explicitly allocate storage for objects. However, we have seen that there are times that we do want to allocate storage in advance, rather than successively concatenating onto a larger object.

R automatically manages memory, releasing memory back to the operating system when it's not needed via garbage collection. Very occasionally you may want to remove large objects as soon as they are not needed. rm() does not actually free up memory, it just disassociates the name from the memory used to store the object. In general R will quickly clean up such objects without a reference (i.e., a name), but it's possible that very occasionally you might need to call gc() to force the garbage collection. This uses some computation so it's generally not recommended.

In a language like C in which the user allocates and frees up memory, memory leaks are a major cause of bugs. Basically if you are looping and you allocate memory at each iteration and forget to free it, the memory use builds up inexorably and eventually the machine runs out of memory. In R, with automatic garbage collection, this is generally not an issue, but occasionally memory leaks do occur.

## 8.2 Monitoring overall memory use

### 8.2.1 Monitoring use within R

There are a number of ways to see how much memory is being used. When R is actively executing statements, you can use top from the UNIX shell. In R, gc() reports memory use and free memory as *Ncells* and *Vcells*. *Ncells* concerns the overhead of running R and *Vcells* relates to objects created by the user, so you'll want to focus on *Vcells*. You can see the number of Mb currently used (the "used" column of the output) and the maximum used in the session (the "max used" column)". A newer alternative is to use functions in the pryr package such as mem_used() and mem_change().

```r
rm(x)
gc(reset = TRUE)

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1195500 63.9    2300772 123  1195500 63.9
## Vcells 22263269 169.9   34632528 264 22263269 169.9

x <- rnorm(1e8) # should use about 800 Mb
object.size(x)

## 800000048 bytes

object_size(x) # from pryr

## 800 MB

gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1.20e+06 63.9   2.30e+06 123 1.21e+06 64.9
## Vcells 1.22e+08 932.8  1.79e+08 1363 1.22e+08 933.1

mem_used() # from pryr

## 1.05 GB

rm(x)
gc() # note the "max used" column is unchanged

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1195653 63.9    2.30e+06 123 1.21e+06 64.9
## Vcells 22263581 169.9   1.43e+08 1090 1.22e+08 933.1

mem_change(x <- rnorm(1e8)) # from pryr

## 800 MB

mem_change(x <- rnorm(1e7))

## -720 MB
```

You can reset the value given for max used, with `gc(reset = TRUE)`.
In Windows only, `memory.size()` tells how much memory is being used.
You can check the amount of memory used by individual objects with `object.size()`.
Here is a useful function, `ls.sizes()`, that wraps `object.size()` to report the largest n objects in a given environment:

```r
ls.sizes <- function(howMany = 10, minSize = 1){
  pf <- parent.frame()
  obj <- ls(pf) # or ls(sys.frame(-1))
  objSizes <- sapply(obj, function(x) {
    pryr::object_size(get(x, pf))
  })
  ## or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()
  objNames <- names(objSizes)
  howmany <- min(howMany, length(objSizes))
  ord <- order(objSizes, decreasing = TRUE)
  objSizes <- objSizes[ord][1:howMany]
  objSizes <- objSizes[objSizes > minSize]
  objSizes <- matrix(objSizes, ncol = 1)
  rownames(objSizes) <- objNames[ord][1:length(objSizes)]
  colnames(objSizes) <- "bytes"
  cat('object')
  print(format(objSizes, justify = "right", width = 11),
        quote = FALSE)
}
```

Unfortunately with R6 and ReferenceClasses, closures, environments, and other such "containers", it can be hard to see how much memory the object is using, including all the components of the object. Here's a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

```r
## size of a closure
x <- rnorm(1e7)
f <- function(input){
  data <- input
  g <- function(param) return(param * data)
  return(g)
}
myFun <- f(x)
rm(x)
object.size(myFun)

## 1608 bytes

object_size(myFun)

## 80 MB

length(serialize(myFun, NULL))

## [1] 160010892

## note that our discussion of copy-on-change will tell us
## why the 80 MB vs. 160 MB disagreement occurs

## size of an environment
e <- new.env()
e$x <- rnorm(1e7)
object.size(e)

## 56 bytes

object_size(e)

## 80 MB

length(serialize(e, NULL))

## [1] 80000192
```

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you're trying to cancel the statement with Ctrl-C. You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

```bash
> R --max-vsize=1000M
```

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message "Error: vector memory exhausted (limit reached?)". So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven't played around with this much, so offer this with a note of caution.

Apparently there is a memory profiler in R, *Rprofmem*, but it needs to be enabled when R is compiled (i.e., installed on the machine), because it slows R down even when not used. So I've never gotten to the point of playing around with it.

### 8.2.2 Monitoring overall memory use on a UNIX-style computer

To understand how much memory is available on your computer, one needs to have a clear understanding of disk caching. The operating system will generally cache files/data in memory when it reads from disk. Then if that information is still in memory the next time it is needed, it will be much faster to access it the second time around than if it had to read the information from disk. While the cached information is using memory, that same memory is immediately available to other processes, so the memory is available even though it is "in use".

We can see this via `free -h` (the "-h" is for 'human-readable', i.e. show in GB (G)) on Linux machine.

```
total used free shared buff/cache available
Mem: 251G 998M 221G 2.6G 29G 247G
Swap: 7.6G 210M 7.4G
```

You'll generally be interested in the *Memory* row. (See below for some comments on *Swap*.) The *shared* column is complicated and probably won't be of use to you. The *buff/cache* column shows how much space is used for disk caching and related purposes but is actually available. Hence the *available* column is the sum of the *free* and *buff/cache* columns (more or less). In this case only about 1 GB is in use (indicated in the *used* column).

`top` (Linux or Mac) and `vmstat` (on Linux) both show overall memory use, but remember that the amount actually available to you is the amount free plus any buffer/cache usage. Here is some example output from `vmstat`:

```
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r b swpd free buff cache si so bi bo in cs us sy id wa st
1 0 215140 231655120 677944 30660296 0 0 1 2 0 0 18 0 82 0 0
```

It shows 232 GB free and 31 GB used for cache and therefore available, for a total of 263 GB available.

Here are some example lines from top:

```
KiB Mem : 26413715+total, 23180236+free, 999704 used, 31335072 buff/cache
KiB Swap: 7999484 total, 7784336 free, 215148 used. 25953483+avail Mem
```

We see that this machine has 264 GB RAM (the *total* column in the *Mem* row), with 259.5 GB available (232 GB free plus 31 GB buff/cache as seen in the *Mem* row). (I realize the numbers don't quite add up for reasons I don't fully understand, but we probably don't need to worry about that degree of exactness.) Only 1 GB is in use.

Swap is essentially the reverse of disk caching. It is disk space that is used for memory when the machine runs out of physical memory. You never want your machine to be using swap for memory because your jobs will slow to a crawl. As seen above, the swap line in both *free* and *top* shows 8 GB swap space, with very little in use, as desired.

## 8.3 The heap and the stack

The *heap* is the memory that is available for dynamically creating new objects while a program is executing, e.g., if you create a new object in R or call new in C++. When more memory is needed the program can request more from the operating system. When objects are removed in R, R will handle the garbage collection of releasing that memory.

The *stack* is the memory used for local variables when a function is called.

There's a nice discussion of this on this Stack Overflow thread.

## 8.4 Hidden uses and hidden savings of memory

### 8.4.1 Using inspect() to understand storage and memory use for data structures

We can use an internal function called inspect() to see where in memory an object is stored. We'll see that this can be a handy tool for seeing where copies are made and where they are not.

```r
x <- rnorm(5)
.Internal(inspect(x))

## @55691ae3c4c8 14 REALSXP g0c4 [REF(2)] (len=5, tl=0) 0.228841,0.589767,-0.779353,1.59101,0.291424
```

### 8.4.2 How lists are stored

Here we can use inspect() to see how the overall list is stored as well as the elements of the list and the attributes of the list.

```r
nums <- rnorm(5)
obj <- list(a = nums, b = nums, c = rnorm(5), d = list(some_string = "adfs"))
.Internal(inspect(obj$a))

## @556919e69138 14 REALSXP g0c4 [REF(4)] (len=5, tl=0) 0.27242,-0.464128,-1.10015,0.392426,0.544127

.Internal(inspect(obj$b))

## @556919e69138 14 REALSXP g0c4 [REF(5)] (len=5, tl=0) 0.27242,-0.464128,-1.10015,0.392426,0.544127

.Internal(inspect(obj$c))

## @556919c7fb68 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.507141,1.28773,0.337203,1.17266,-0.113455

.Internal(inspect(obj))

## @55691a84d8a8 19 VECSXP g0c3 [REF(2),ATT] (len=4, tl=0)
##   @556919e69138 14 REALSXP g0c4 [REF(6)] (len=5, tl=0) 0.27242,-0.464128,-1.10015,0.392426,0.544127
##   @556919e69138 14 REALSXP g0c4 [REF(6)] (len=5, tl=0) 0.27242,-0.464128,-1.10015,0.392426,0.544127
##   @556919c7fb68 14 REALSXP g0c4 [REF(2)] (len=5, tl=0) 0.507141,1.28773,0.337203,1.17266,-0.113455
##   @55691e0bb9e8 19 VECSXP g0c1 [REF(1),ATT] (len=1, tl=0)
##     @55691c978ac0 16 STRSXP g0c1 [REF(3)] (len=1, tl=0)
##       @55691c978a88 09 CHARSXP g0c1 [REF(2),gp=0x60] [ASCII] [cached] "adfs"
##     ATTRIB:
##       @55691e0cc698 02 LISTSXP g0c0 [REF(1)]
##         TAG: @556915148970 01 SYMSXP g1c0 [MARK,REF(65535),LCK,gp=0x6000] "names" (has value)
##         @55691e0bb9b0 16 STRSXP g0c1 [REF(1)] (len=1, tl=0)
##           @5569181e6938 09 CHARSXP g0c2 [REF(4),gp=0x61] [ASCII] [cached] "some_string"
## ATTRIB:
##   @55691e0cc628 02 LISTSXP g0c0 [REF(1)]
##     TAG: @556915148970 01 SYMSXP g1c0 [MARK,REF(65535),LCK,gp=0x6000] "names" (has value)
##     @556919a52ec8 16 STRSXP g0c3 [REF(65535)] (len=4, tl=0)
##       @55691542b4a8 09 CHARSXP g1c1 [MARK,REF(426),gp=0x61] [ASCII] [cached] "a"
##       @556915741650 09 CHARSXP g1c1 [MARK,REF(324),gp=0x61] [ASCII] [cached] "b"
##       @556915149cc0 09 CHARSXP g1c1 [MARK,REF(802),gp=0x61] [ASCII] [cached] "c"
##       @5569155e06c8 09 CHARSXP g1c1 [MARK,REF(31),gp=0x61] [ASCII] [cached] "d"
```

The pryr package provides `address()` or `inspect()` as an alternative to `.Internal(inspect())` though as we see here it doesn't give us the richness of information about complicated objects that `inspect()` does.

```r
address(x) # from pryr

## [1] "0x55691ae3c4c8"

address(obj)

## [1] "0x55691a84d8a8"

address(obj$a) # doesn't work

## Error: x must be the name of an object
```

Similar tricks are used for storing character vectors.

### 8.4.3 Replacement functions

* Replacement functions can hide the use of additional memory. How much memory is used here? (Try running in R (not RStudio) on your own computer and note the *max_used* column in the `gc()` result should increase, indicating a copy was made.)

```r
rm(x)
gc(reset = TRUE)
x <- rnorm(1e7)
gc()
dim(x) <- c(1e4, 1e3)
diag(x) <- 1
gc()
```

* Not all replacement functions actually involve creating a new object and replacing the original object. (However for some reason if I run the code via knitr in creating this PDF a copy IS made.) Here '[<-' is a primitive function, so the modification of the vector can be done without a copy. Try it in R (not RStudio) on your own computer.

```r
rm(x)
gc(reset = TRUE)

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1196045 63.9    2.30e+06 123  1196045 63.9
## Vcells 42267187 322.5   1.43e+08 1090 42267187 322.5

x <- rnorm(1e7)
address(x)

## [1] "0x7ff4761ee010"

gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1196068 63.9    2.30e+06 123  1214263 64.9
## Vcells 52267221 398.8   1.43e+08 1090 52298699 399.1

x[5] <- 7
## When run plainly in R, should be the same address as before,
## indicating no copy was made. Knitting the doc messes the
## result up!
address(x)

## [1] "0x7ff4715a2010"

gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 1196108 63.9    2.30e+06 123  1214585 64.9
## Vcells 52267273 398.8   1.43e+08 1090 62298483 475.3
```

### 8.4.4 Fast representations of sequences

As of R 3.5.0, `1:n` is not stored in memory as a vector of length $n$, but rather is represented by the first and last value in the sequence. However, some of the functions we use to determine object size don't give us the right answer in this case.

```r
library(microbenchmark)
n <- 1e6
microbenchmark(tmp <- 1:n)

## Unit: nanoseconds
##         expr min  lq mean median  uq  max neval
##  tmp <- 1:n 197 204  276    209 262 4105   100

object.size(tmp) # incorrect as of R 3.5

## 4000048 bytes

object_size(tmp) # incorrect as of R 3.5

## 4 MB

mem_change(mySeq <- 1:n) # not sure why the result is negative!

## -4.06 kB

length(serialize(mySeq, NULL))

## [1] 133
```

One implication is that in older versions of R, indexing large subsets can involve a lot of memory use.

```r
x <- rnorm(1e7)
y <- x[1:(length(x) - 1)]
```

In this case, in older versions of R, more memory is used than just for $x$ and $y$, because the index sequence itself uses a bunch of memory.

## 8.5 Delayed copying (copy-on-change)

Next we'll see that something like lazy evaluation occurs outside of functions as well with some functionality called *delayed copying* or *copy-on-change*. When we discussed R as being call-by-value in Section 6.5, copy-on-change was one of the reasons that copies of arguments are not always made. (But we didn't talk about it at that time.)

Let's see what goes on within a function in terms of memory use in different situations. Ignore the `gc()` results in the pdf, as we'll start R fresh to get a clean view of memory use during the class demo.

```r
rm(x)
rm(y)
gc(reset = TRUE)

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259733 121    4.29e+06 229  2259733 121
## Vcells 44055962 336   1.43e+08 1090 44055962 336

f <- function(x){
  print(gc())
  print(x[1])
  print(gc())
  .Internal(inspect(x))
  return(x)
}

y <- rnorm(1e7)
gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259718 121    4.29e+06 229  2277701 122
## Vcells 54055965 412   1.43e+08 1090 54087108 413

.Internal(inspect(y))

## @7ff475a52010 14 REALSXP g1c7 [MARK,REF(2)] (len=10000000, tl=0) 1.04969,0.0161469,0.270741,-0.202048,-0.970419,...

out <- f(y)

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259748 121    4.29e+06 229  2277701 122
## Vcells 54056017 412   1.43e+08 1090 54087108 413
## [1] 1.05
##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259770 121    4.29e+06 229  2277701 122
## Vcells 54056043 412   1.43e+08 1090 54087108 413
## @7ff475a52010 14 REALSXP g1c7 [MARK,REF(4)] (len=10000000, tl=0) 1.04969,0.0161469,0.270741,-0.202048,-0.970419,...

.Internal(inspect(y))

## @7ff475a52010 14 REALSXP g1c7 [MARK,REF(6)] (len=10000000, tl=0) 1.04969,0.0161469,0.270741,-0.202048,-0.970419,...

.Internal(inspect(out))

## @7ff475a52010 14 REALSXP g1c7 [MARK,REF(7)] (len=10000000, tl=0) 1.04969,0.0161469,0.270741,-0.202048,-0.970419,...
```

We see that y, the local x, and out all use the same memory, so no copies are made here. Note that in this example, if you use `address()` instead of `.Internal(inspect())` it's not really clear what is going on.

In fact, this occurs outside function calls as well. Copies of objects are not made until one of the objects is actually modified. Initially, the copy points to the same memory location as the original object.

```r
rm(y)
gc(reset = TRUE)

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259834 121    4.29e+06 229  2259834 121
## Vcells 54047280 412   1.43e+08 1090 54047280 412

y <- rnorm(1e7)
gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259849 121    4.29e+06 229  2271922 121
## Vcells 64047304 489   1.43e+08 1090 64068225 489

address(y)

## [1] "0x7ff467d08010"

x <- y
gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259875 121    4.29e+06 229  2277907 122
## Vcells 64047349 489   1.43e+08 1090 64078472 489

object_size(x, y) # from pryr

## 80 MB

address(x)

## [1] "0x7ff467d08010"

x[1] <- 5
gc()

##          used (Mb) gc trigger (Mb) max used (Mb)
## Ncells 2259908 121    4.29e+06 229  2284745 122
## Vcells 74047397 565   1.43e+08 1090 74089212 565

address(x)

## [1] "0x7ff4630bc010"

object_size(x, y)

## 160 MB

rm(x)
x <- y
address(x)

## [1] "0x7ff467d08010"

address(y)

## [1] "0x7ff467d08010"

y[1] <- 5
address(x)

## [1] "0x7ff467d08010"

address(y)

## [1] "0x7ff45e470010"
```

Or we can see this using `mem_change()`.

```r
library(pryr)
rm(x)
rm(y)
mem_change(x <- rnorm(1e7))

## 80 MB

address(x)

## [1] "0x7ff467d08010"

mem_change(x[3] <- 8)

## 320 B

address(x)

## [1] "0x7ff467d08010"

mem_change(y <- x)

## 376 B

address(y)

## [1] "0x7ff467d08010"

mem_change(x[3] <- 8)

## 80 MB

address(x)

## [1] "0x7ff4630bc010"

address(y)

## [1] "0x7ff467d08010"
```

**Challenge**: explain the results of the example above.

**How does copy-on-change work?** R keeps track of how many names refer to an object and only makes copies as needed when multiple names refer to an object. Note the value of REF and the address returned by `.Internal(inspect())`, or simply use `refs()` and `address()` from pryr.

We'll see this live in class. Unfortunately both knitting and RStudio can give us confusing results, so I'm adding the clean results from just running in R here in comments.

```r
a <- rnorm(5)
## See below for result without RStudio or knitting messing things up
## .Internal(inspect(a))
## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.524365,0.55554,0.700011,-0.621318,-0.924413
## refs(a)
## [1] 1
address(a)
## [1] "0x556accc65948"
b <- a
## See below for result without RStudio or knitting messing things up
## .Internal(inspect(b))
## @556accc65948 14 REALSXP g0c4 [REF(2)] (len=5, tl=0) 0.524365,0.55554,0.700011,-0.621318,-0.924413
## refs(a)
## [1] 2
## refs(b)
## [1] 2
address(b)
# [1] "0x556accc65948"
a[2] <- 0
## See below for result without RStudio or knitting messing things up
## .Internal(inspect(a))
## @556accc657f8 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.524365,0,0.700011,-0.621318,-0.924413
## .Internal(inspect(b))
## @556accc65948 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) 0.524365,0.55554,0.700011,-0.621318,-0.924413

a <- rnorm(5)
b <- a
## refs(a)
## [1] 2
rm(b)
## refs(a)
## [1] 1
```

In older versions of R (before R 4.0) there were some shortcomings in how R managed this, and one could see different results than shown below.

**How can can copy-on-change be fooled in older versions of R? (Optional)** In older versions of R (before R 4.0), the mechanism for determining whether two names refer to the same object was simplistic. As discussed by Radford Neal, who has worked to improve the efficiency of R in a project called pqR, "So R doesn't copy all the time. Instead, it maintains a count, called *NAMED*, of how many "names" refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren't made when necessary."

If you're using an older version of R, you can view the *NAMED* count either via `.Internal(inspect())` or by using `pryr::refs()`.

## 8.6 Deep copies and lists and character strings

Prior to R 3.1.0, modifying an element of a list caused the entire list to be copied, basically what is called a *deep copy*. In more recent versions of R, only the components that need to get copied are copied.

You can explore this using `.Internal(inspect())` on a list.

R is also clever about saving copying when it works with character strings. Character vectors are handled in a similar way as lists.

## 8.7 Passing objects to compiled code (optional)

This subsection is out-of-date and doesn't reflect that most people these days use the *Rcpp* package rather than the older .C and .Call interfaces to compiled code. We won't cover this subsection in class and don't expect you to know this material. However, if you do end up interfacing to external code, thinking about whether copies are made when calling out to external code can be important if you're working with large objects.

As we've already discussed, when R objects are passed to compiled code (e.g., C or C++), they are passed as pointers and the compiled code uses the memory allocated by R (though it could also allocate additional memory if allocation is part of the code). However, a copy of the object is made, so when calling a C function from R there is some memory overhead. (However, a previous GSI commented to me that in Rcpp, one can pass by reference and avoid having copies made.)

Furthermore, we need to be aware of any casting that occurs, because the compiled code requires that the R object types match those that the function in the compiled code is expecting.

Here's an example of calling compiled code:

```r
res <- .C("fastcount", PACKAGE="GCcorrect", tablex = as.integer(tablex),
          tabley = as.integer(tabley), as.integer(xvar), as.integer(yvar),
          as.integer(useline), as.integer(length(xvar)))
```

Let's consider when copies are made in casts:

```r
f <- function(arg1){
  print(address(arg1))
  return(mean(arg1))
}
x <- rnorm(10)
class(x)
debug(f)
f(x)
f(as.numeric(x))
f(as.integer(x))
```

Next we'll see that C calls do involve a copy, even though it looks like we are just using the same object allocated by R. We'll use the inline package to work directly with C code in R and the .C functionality for interfacing with C.

```r
library(inline)
src <- '
for (int i = 0; i < *n; i++) {
  x[i] = exp(x[i]);
}
'
sillyExp <- cfunction(signature(n = "integer", x = "numeric"),
                      src, convention = ".C")
## sillyExp <- cfunction(signature(n = "integer", x = "numeric"),
##                       src, convention = ".C")
len <- as.integer(100) # or 100L
vals <- rnorm(len)
vals[1]

## [1] 0.682

out1 <- sillyExp(n = len, x = vals)
address(vals)

## [1] "0x556923c00090"

.Internal(inspect(out1))

## @5569224e8c18 19 VECSXP g0c2 [REF(2),ATT] (len=2, tl=0)
##   @556915ddb620 13 INTSXP g0c1 [REF(1)] (len=1, tl=0) 100
##   @55691c5b8f80 14 REALSXP g0c7 [REF(1)] (len=100, tl=0) 1.97714,0.709209,1.78726,1.79355,2.30681,...
## ATTRIB:
##   @556924158358 02 LISTSXP g0c0 [REF(1)]
##     TAG: @556915148970 01 SYMSXP g1c0 [MARK,REF(65535),LCK,gp=0x6000] "names" (has value)
##     @5569224e8bd8 16 STRSXP g0c2 [REF(1)] (len=2, tl=0)
##       @556915198d50 09 CHARSXP g1c1 [MARK,REF(551),gp=0x61] [ASCII] [cached] "n"
##       @556915199108 09 CHARSXP g1c1 [MARK,REF(12928),gp=0x61] [ASCII] [cached] "x"

.Internal(inspect(out1$x))

## @55691c5b8f80 14 REALSXP g0c7 [REF(1)] (len=100, tl=0) 1.97714,0.709209,1.78726,1.79355,2.30681,...
```

## 8.8 Strategies for saving memory

A couple basic strategies for saving memory include:

* Avoiding unnecessary copies.

* Removing objects that are not being used and, if necessary (not generally needed), do a `gc()` call.

If you're really trying to optimize memory use, you may also consider:

* Using R6 classes and similar strategies to pass by reference.

* Substituting integer and logical vectors for numeric vectors when possible.

## 8.9 Example

Let's work through a real example where we keep a running tally of current memory in use and maximum memory used in a function call. We'll want to consider hidden uses of memory, when copies are made, and lazy evaluation. (In a real example we'd also want to think about when copies are made in calling compiled code, but we don't do that in class.) This code is courtesy of Yuval Benjamini. For our purposes here, let's assume that *xvar* and *yvar* are very long vectors using a lot of memory.

```r
fastcount <- function(xvar, yvar) {
  print(xvar[1])
  print(yvar[1])
  naline <- is.na(xvar)
  naline[is.na(yvar)] = TRUE
  xvar[naline] <- 0
  yvar[naline] <- 0
  useline <- !naline
  ## We'll ignore the rest of the code.
  ## Table must be initialized for -1's
  tablex <- numeric(max(xvar)+1)
```

---

← 6 Functions, frames, and variable scope · [Up: contents](index.md)
