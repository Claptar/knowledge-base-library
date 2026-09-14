---
title: 7 Efficiency
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Efficiency

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In part because R is an interpreted language and in part because R is very dynamic (objects can be modified essentially arbitrarily after being created), R can be slow. Hadley Wickham’s Advanced R book has a section on Performance that discusses this in detail. However, there are a variety of ways that one can write efficient R code.

In general, make use of R’s built-in functions, as these tend to be implemented internally (i.e., via compiled code in C or Fortran). In particular, if R is linked to optimized BLAS and Lapack code (e.g. Intel’s _MKL_ , _OpenBLAS_ [on BCE and the SCF Linux servers], AMD’s _ACML_ [on the SCF Linux cluster, _vecLib_ for Macs [on the SCF Macs]), you should have good performance (potentially comparable to Matlab and to coding in C). Sometimes you can figure out a trick to take your problem and transform it to make use of the built-in functions.

Note that I run a lot of iterative algorithms so I pay attention to making sure my calculations are fast as they are done repeatedly. Similarly, one would want to pay attention to speed when doing large simulations and bootstrapping, and in some cases for optimization. And if you’re distributing code, it’s good to have it be efficient. But in other contexts, it may not be worth your time. Also, it’s good practice to code it transparently first to reduce bugs and then to use tricks to speed it up and make sure the fast version works correctly.

Results can vary with with your system setup and version of R, so the best thing to do is figure out where the bottlenecks are in your code (e.g., with _Rprof()_ or just some basic use of _system.time()_ and _(micro)benchmark()_ ), and then play around with alternative specifications. And as you gain more experience, you’ll get some intuition for what approaches might improve speed, but even with experience I find myself often surprised by what matters and what doesn’t. It’s often worth trying out a bunch of different ideas; _system.time(), microbenchmark()_ (or _benchmark()_ ) are your workhorse tools in this context.

### **7.1 Writing efficient code**

For material on efficient R coding, including tools for timing and profiling your code to understand where the bottlenecks are, see the tutorial, _Writing efficient R code._

### **7.2 A note on hashing**

In the tutorial on efficient R coding, I mention that looking up objects by name in an R environment occurs via hashing, so it can be very fast. I’ll briefly describe what hashing is here.

A hash function is a function that takes as input some data and maps it to a fixed-length output that can be used as a shortened reference to the data. We’ve seen this in the context of git commits

75

where each commit was labeled with a long base-16 number. This also comes up when verifying files on the Internet. You can compute the hash value on the file you get and check that it is the same as the hash value associated with the legitimate copy of the file.

For our purposes here, hashing can allow one to look up values by their name via a hash table. The idea is that you have a set of key-value pairs (sometimes called a dictionary) where the key is the name associated with the value and the value is some arbitrary object. Hashing allows one to quickly determine an index associated with the key and therefore quickly find the relevant value based on the index. For example, one approach is to compute the hash as a function of the key and then take the remainder when dividing by the number of key-value pairs to get the index. Here’s the procedure in pseudocode:

hash = hashfunc(key) index = hash %% array_size ## %% is modulo operator - it gives the remainder

In general, there will be collisions, with multiple keys assigned to the same index, but usually there will be a small number of keys associated with a given index or slot, and determining the correct value within a given index/slot (also called a bucket) is fast. Put another way, the hash function distributes the keys amongst an array of buckets and allows one to look up the appropriate bucket quickly based on the computed index value. When the hash table is properly set up, the cost of looking up a value does not depend on the number of key-value pairs stored.

### **7.3 Other approaches to speeding up R (optional)**

#### **7.3.1 pqR and other R engines**

Radford Neal, a prominent statistician/computer scientist has been working on a project called _pqR_ (pretty quick R) to rewrite some aspects of R to make them faster. There are also a few other projects that aim to reimplement the “R engine” such that one could run one’s R code with different back ends.

Here are some of the highlights of _pqR_ (from a couple years ago) in terms of efficiency, as discussed at

http://radfordneal.github.io/pqR/:

1. When R runs code such as just below, it actually creates a vector 1,2,....,n, (which can be computationally and memory intensive for large n) and then iterates over the values in the vector. pqR avoids this vector creation. As discussed and illustrated in Section 8, **this improvement is incorporated into R 3.5.0 and later versions** .

76

for(i in 1:n) { } vec[1:n]

2. pqR automatically uses multiple cores for some calculations.

3. pqR avoid some checks for NA and NaN and the like in matrix calculations in which such checking would be slow and it doesn’t make sense to check for them anyway.

#### **7.3.2 Byte compiling**

R now allows you to compile R code, which goes by the name of byte compiling. Byte-compiled code is a special representation that can be executed more efficiently because it is in the form of compact codes that encode the results of parsing and semantic analysis of scoping and other complexities of the R source code. This byte code can be executed faster than the original R code because it skips the stage of having to be interpreted by the R interpreter.

The functions in the _base_ and _stats_ packages are now byte-compiled by default. (If you print out a function that is byte-compiled, you’ll see something like _<bytecode: 0x243a368>_ at the bottom.

We can byte compile our own functions using _cmpfun()_ . Here’s an example (silly since as experienced R programmers, we would use vectorized calculation here rather than this unvectorized code.)

**library** (compiler); **library** (rbenchmark) f <- **function** (vals){ x <- **as.numeric** (NA) **length** (x) <- **length** (vals) **for** (i **in seq_along** (vals)) x[i] <- **exp** (vals[i]) **return** (x) } fc <- **cmpfun** (f) fc _# notice the indication that the function is byte compiled._ ## function(vals){ ## x <- as.numeric(NA) ## length(x) <- length(vals) ## for(i in seq_along(vals)) x[i] <- exp(vals[i]) ## return(x) ## }

77

---

[← Unit 05 — programming Part 40 —](40-unit-05-programming-part-40.md) · [Up: contents](index.md) · [Unit 05 — programming Part 42 — →](42-unit-05-programming-part-42.md)
