---
title: 8. Memory and copies
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 8. Memory and copies

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Overview

The main things to remember when thinking about memory use are: (1)
numeric vectors take 8 bytes per element and (2) we need to keep track
of when large objects are created, including local variables in the
frames of functions.

In some of our work here we'll use functions from the *pryr* package,
which provides functions to help understand what is going on under the
hood in R.

**In general, don't try to run this code within RStudio, as some of how
RStudio works affects when copies are made. In particular the environment pane
causes there to be an additional reference to each object.
 Also, as noted in the document, some of the output in the PDF
 does not reflect  what is happening
when running code directly within R,
because of effects from the process of rendering the document.**

### Allocating and freeing memory

Unlike compiled languages like C, in R we do not need to explicitly
allocate storage for objects. (However, we will see that there are times
that we do want to allocate storage in advance, rather than successively
concatenating onto a larger object.)

R automatically manages memory, releasing memory back to the operating
system when it's not needed via garbage collection. Very occasionally
you may want to remove large objects as soon as they are not needed.
`rm()` does not actually free up memory, it just disassociates the name
from the memory used to store the object. In general R will quickly
clean up such objects without a reference (i.e., a name), so there is generally
no need to call `gc()` to force
the garbage collection. In particular, calling `gc()` uses some computation so it's generally not
recommended.

In a language like C in which the user allocates and frees up memory,
memory leaks are a major cause of bugs. Basically if you are looping and
you allocate memory at each iteration and forget to free it, the memory
use builds up inexorably and eventually the machine runs out of memory.
In R, with automatic garbage collection, this is generally not an issue,
but occasionally memory leaks do occur.

### The heap and the stack

The *heap* is the memory that is available for dynamically creating new
objects while a program is executing, e.g., if you create a new object
in R or call *new* in C++. When more memory is needed the program can
request more from the operating system. When objects are removed in R, R
will handle the garbage collection of releasing that memory.

The *stack* is the memory used for local variables when a function is
called.

There's a nice discussion of this on [this Stack Overflow
thread](https://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap).


## Monitoring memory use

### Monitoring overall memory use on a UNIX-style computer

To understand how much memory is available on your computer, one needs
to have a clear understanding of disk caching. The operating system will
generally cache files/data in memory when it reads from disk. Then if
that information is still in memory the next time it is needed, it will
be much faster to access it the second time around than if it had to
read the information from disk. While the cached information is using
memory, that same memory is immediately available to other processes, so
the memory is available even though it is "in use".

We can see this via `free -h` (the `-h` is for 'human-readable', i.e.
show in GB (G)) on Linux machine.

```
          total used free shared buff/cache available
    Mem:   251G 998M 221G   2.6G        29G      247G
    Swap:  7.6G 210M 7.4G
```

You'll generally be interested in the `Mem` row. (See below for some
comments on `Swap`.) The `shared` column is complicated and probably
won't be of use to you. The `buff/cache` column shows how much space is
used for disk caching and related purposes but is actually available.
Hence the `available` column is the sum of the `free` and `buff/cache`
columns (more or less). In this case only about 1 GB is in use
(indicated in the `used` column).

`top` (Linux or Mac) and `vmstat` (on Linux) both show overall memory
use, but remember that the amount actually available to you is the
amount free plus any buff/cache usage. Here is some example output
from `vmstat`:

```

    procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
    r b   swpd      free   buff    cache si so bi bo in cs us sy id wa st
    1 0 215140 231655120 677944 30660296  0  0  1  2  0  0 18  0 82  0  0
```

It shows 232 GB free and 31 GB used for cache and therefore available,
for a total of 263 GB available.

Here are some example lines from `top`:

```
    KiB Mem : 26413715+total, 23180236+free, 999704 used, 31335072 buff/cache
    KiB Swap:  7999484 total,  7784336 free, 215148 used. 25953483+avail Mem
```

We see that this machine has 264 GB RAM (the total column in the `Mem`
row), with 259.5 GB available (232 GB free plus 31 GB buff/cache as seen
in the `Mem` row). (I realize the numbers don't quite add up for reasons
I don't fully understand, but we probably don't need to worry about that
degree of exactness.) Only 1 GB is in use.

*Swap* is essentially the reverse of disk caching. It is disk space that
is used for memory when the machine runs out of physical memory. You
never want your machine to be using swap for memory because your jobs
will slow to a crawl. As seen above, the `swap` line in both `free` and
`top` shows 8 GB swap space, with very little in use, as desired.

### Monitoring memory use in R

There are a number of ways to see how much memory is being used. When R
is actively executing statements, you can use `top` from the UNIX shell.
In R, you can use `gc()`.

```r
gc()
```

`gc()` reports memory use and free memory as `Ncells` and
`Vcells`. `Ncells` concerns the overhead of running R and `Vcells`
relates to objects created by the user, so you'll want to focus on
`Vcells`. You can see the number of Mb currently used (the "`used`"
column of the output) and the maximum used in the session (the "`max
used`" column)".

We can see the size of an object with `object.size()` from base R or `object_size` from pryr:

```r
x <- rnorm(1e8) # should use about 800 Mb
object.size(x)
pryr::object_size(x)
```

A newer alternative to `gc()` is to use functions in the `pryr`
package such as `mem_used()` and `mem_change()`.

```r
library(pryr)
mem_used()
gc()
rm(x)
mem_used()
gc() # note the "max used" column is unchanged
mem_change(x <- rnorm(1e8))
mem_change(x <- rnorm(1e7))
```

You can reset the value given for `max used`, with `gc(reset = TRUE)`.

In Windows only, `memory.size()` tells how much memory is being used.


Here is a useful function, `ls_sizes()`, that wraps `object.size()` to
report the largest $n$ objects in a given environment:

```r
ls_sizes <- function(howMany = 10, minSize = 1){
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

Unfortunately with R6 and ReferenceClasses, closures, environments, and
other such "containers", it can be hard to see how much memory the
object is using, including all the components of the object. Here's a
trick where we serialize the object, as if to export it, and then see
how long the binary representation is. In this case the object is a closure
that contains a large vector.

```r
library(pryr)
x <- rnorm(1e7)
f <- function(input){
	data <- input
	g <- function(param) return(param * data)
	return(g)
}
myFun <- f(x)
rm(x)
object.size(myFun)
object_size(myFun)
length(serialize(myFun, NULL))
```

Note that  our discussion of copy-on-modify should help us understand
why the serialized object is 160 MB, but only 80 MB is used to store the 10,000,000 numbers.

Here we examine the size of an environment:

```r
e <- new.env()
e$x <- rnorm(1e7)
object.size(e)
object_size(e)
length(serialize(e, NULL))
```

One frustration with memory management is that if your code bumps up
against the memory limits of the machine, it can be very slow to respond
even when you're trying to cancel the statement with `Ctrl-C`. You can
impose memory limits in Linux by starting R (from the UNIX prompt) in a
fashion such as this

```bash
R --max-vsize=1000M
```

Then if you try to create an object that will push you over that limit
or execute code that involves going over the limit, it will simply fail
with the message "*Error: vector memory exhausted (limit reached?)*". So
this approach may be a nice way to avoid paging/swapping by setting the
maximum in relation to the physical memory of the machine. It might also
help in debugging memory leaks because the program would fail at the
point that memory use was increasing. I haven't played around with this
much, so I offer this with a note of caution.

Apparently there is a memory profiler in R, *Rprofmem*, but it needs to
be enabled when R is compiled (i.e., installed on the machine), because
it slows R down even when not used. So I've never gotten to the point of
playing around with it.

## How memory is used in R

### A secret weapon: `inspect`

We can use an internal function called `inspect` to see where in
memory an object is stored. It's particularly useful for understanding storage
and memory use for complicated data structures.
We'll also see that this can be a handy tool for
seeing where copies are made and where they are not.

```r
x <- rnorm(5)
.Internal(inspect(x))
```

The first output is the address in memory (in hexadecimal) of the vector. The `REALSXP` indicates that the vector
is stored as a real-valued "S" object under the hood in C. `REF(2)` indicates that two variables are referring to this particular memory location (more on this in much detail in a bit).


### Memory use in specific circumstances

#### How lists are stored

Here we can use `inspect()` to see how the overall list is stored as
well as the elements of the list and the attributes of the list.

```r
nums <- rnorm(5)
obj <- list(a = nums, b = nums, c = rnorm(5), d = list(some_string = "adfs"))
.Internal(inspect(obj$a))
.Internal(inspect(obj$b))
.Internal(inspect(obj$c))
.Internal(inspect(obj))
```

What do we notice?

  - The list itself is a vector of pointers to the component elements and a pointer to the attributes information.
  - Each element has its own address.
  - Attributes are themselves stored in particular locations.
  - Two elements of a list can use the same memory (see `a` and `b` here, whose contents are at the same memory address).


The *pryr* package provides `address()` or `inspect()` as an alternative
to `.Internal(inspect())` though even `pryr::inspect()` doesn't give us the
richness of information about complicated objects that `.Internal(inspect())` does.

```r
address(obj)
inspect(obj)
try(address(obj$a)) # doesn't work
```


#### How character strings are stored.

Similar tricks are used for storing character vectors.
We'll explore this in a problem on PS4 using `inspect()`.

#### Replacement functions

Replacement functions can hide the use of additional memory. How
    much memory is used here? (Try running in R (not RStudio) on your
    own computer and note the `max_used` column in the `gc()` result
    should increase after we modify the dimensionality of `x`, indicating a copy was made.)

```r
rm(x)
gc(reset = TRUE)

x <- rnorm(1e7)
gc()
dim(x) <- c(1e4, 1e3)
diag(x) <- 1
gc()
```

However, not all replacement functions actually involve creating a new object
    and replacing the original object.  Here
    `[<-` is a primitive function, so the modification of the vector
    can be done without a copy in the underlying execution in C.

> **Warning**: For some reason when I compile this document a copy is made. Try it in R (not RStudio) on your own computer,
and you should see that the address of `x` is unchanged and no additional memory has been used.

```r
rm(x)
gc(reset = TRUE)

x <- rnorm(1e7)
address(x)
gc()
x[5] <- 7
`[<-`
## When run plainly in R, should be the same address as before,
## indicating no copy was made. Rendering the doc messes the
## result up!
address(x)
gc()
```

It makes some sense that modifying elements of a vector doesn't cause a copy usually -- if it did, working with large vectors would be very difficult.

#### Fast representations of sequences

As of R 3.5.0, `1:n` is not stored in memory as a vector of length *n*,
but rather is represented by the first and last value in the sequence.
However, some of the functions we use to determine object size don't
give us the right answer in this case.

```r
library(microbenchmark)

n <- 1e6
microbenchmark(tmp <- 1:n)
object.size(tmp)  # incorrect
object_size(tmp)  # correct
mem_change(mySeq <- 1:n)  # not sure why the result is negative!
length(serialize(mySeq, NULL))
```

One implication is that in older versions of R, indexing large subsets
can involve a lot of memory use.

```r
x <- rnorm(1e7)
y <- x[1:(length(x) - 1)]
```

In this case, in old versions of R, more memory was used than just for
`x` and `y`, because the index sequence itself used a bunch of memory.

### Copy-on-modify

Next we'll see that something like lazy evaluation occurs as well with some functionality called *delayed copying* or
*copy-on-modify*. When we discussed R as being call-by-value, copy-on-modify was one of the
reasons that copies of arguments are not always made. (But we didn't
talk about it at that time.)

#### Copy-on-modify in function calls

Let's see what goes on within a function in terms of memory use in
different situations.

```r
rm(x)
gc(reset = TRUE)

f <- function(x){
    print(gc())
    print(x[1])
    print(gc())
    .Internal(inspect(x))
    ## print(address(x))  ## this gives the wrong answer; not sure why
    print(lobstr::obj_addr(x)) ## fixed in lobstr, which supercedes pryr
    return(x)
}

y <- rnorm(1e7)
gc()
.Internal(inspect(y))
out <- f(y)
.Internal(inspect(y))
.Internal(inspect(out))
```

We see that `y`, the local variable `x` in the function frame, and `out` all use the same memory, so no
copies are made here. The `gc()` output confirms that no additional memory was used.

Only if `x` is changed do the addresses change and a copy in memory get made. (Note that we already saw this with the `diag<-` replacement function example.

```r
f <- function(x){
    .Internal(inspect(x))
    x[2] <- 7
    .Internal(inspect(x))
    return(x)
}

y <- rnorm(1e7)
.Internal(inspect(y))
out <- f(y)
.Internal(inspect(y))
.Internal(inspect(out))
```

#### Copy-on-modify in general

In fact, copy-on-modify occurs outside function calls as well. Copies of objects
are not made until one of the objects is actually modified. Initially,
the copy points to the same memory location as the original object.

```r
rm(y); rm(out)
gc(reset = TRUE)

y <- rnorm(1e7)
gc()
address(y)
x <- y
gc()
object_size(x, y)  # from pryr
address(x)
x[1] <- 5
gc()
address(x)
object_size(x, y)
rm(x)
x <- y
address(x)
address(y)
y[1] <- 5
address(x)
address(y)
```

Or we can see this using `mem_change()`.

```r
library(pryr)
rm(x)
rm(y)
mem_change(x <- rnorm(1e7))
address(x)
mem_change(x[3] <- 8)
address(x)
mem_change(y <- x)
address(y)
mem_change(x[3] <- 8)
address(x)
address(y)
```

**Challenge**: explain the results of the example above.

#### How does copy-on-modify work?

R keeps track of how many names refer to an object and only makes copies
as needed when multiple names refer to an object. Note the value of REF
and the address returned by `.Internal(inspect())`, or simply use
`refs()` and `address()` from `pryr`.

We'll see this live in class. Unfortunately both rendering and RStudio
can give us confusing results for `refs()`, so I'm adding the clean results from just
running in R as comments here.

```r
a <- rnorm(5)
address(a)
## refs(a)  ## 1
b <- a
address(b)
## refs(a)  ## 2
## refs(b)  ## 2
rm(b)
## refs(a)  ## 1

b <- a
a[2] <- 0
address(a)
address(b)
## refs(a)  ## 1
## refs(b)  ## 1
```

This notion of reference counting occurs in other contexts, such as
shared pointers in C++ and garbage collection (deletion of unused objects) in Python and R.

In older versions of R (before R 4.0) there were some shortcomings in
how R managed this, and one could see different results than shown
above.

## Strategies for saving memory

A couple basic strategies for saving memory include:

-   Avoiding unnecessary copies.
-   Removing objects that are not being used, at which point the R garbage collector should free up the memory.

If you're really trying to optimize memory use, you may also consider:

-   Using R6 classes and similar strategies to pass by reference.
-   Substituting integer and logical vectors for numeric vectors when
    possible.

## Example

Let's work through a real example where we keep a running tally of
current memory in use and maximum memory used in a function call. We'll
want to consider hidden uses of memory, when copies are made, and lazy
evaluation.  This
code is courtesy of Yuval Benjamini. For our purposes here, let's assume
that `xvar` and `yvar` are very long vectors using a lot of memory. The
use of `.C()` calls out to some user-written C code. (In a real example we'd also want to think about when copies
are made in calling compiled code, but we don't do that here.)

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
    tabley <- numeric(max(yvar)+1)
    stopifnot(length(xvar) == length(yvar))
    res <- .C("fastcount",PACKAGE="GCcorrect",
              tablex = as.integer(tablex), tabley = as.integer(tabley),
              as.integer(xvar), as.integer(yvar), as.integer(useline),
              as.integer(length(xvar)))
    xuse <- which(res$tablex>0)
    xnames <- xuse - 1
    resb <- rbind(res$tablex[xuse], res$tabley[xuse])
    colnames(resb) <- xnames
    return(resb)
}
```

---

[← for loop: needs storage set up and multiple lines](16-for-loop-needs-storage-set-up-and-multiple-lines.md) · [Up: contents](index.md) · [9. Efficiency →](18-9-efficiency.md)
