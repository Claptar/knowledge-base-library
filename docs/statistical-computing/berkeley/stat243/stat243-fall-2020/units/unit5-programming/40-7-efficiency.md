---
title: 7 Efficiency
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Efficiency

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In part because R is an interpreted language and in part because R is very dynamic (objects can be modified essentially arbitrarily after being created), R can be slow. Hadley Wickham’s Advanced R book has a section on Performance that discusses this in detail. However, there are a variety of ways that one can write efficient R code.

In general, make use of R’s built-in functions, as these tend to be implemented internally (i.e., via compiled code in C or Fortran). In particular, if R is linked to optimized BLAS and Lapack code (e.g. Intel’s _MKL_ , _OpenBLAS_ [on BCE and the SCF Linux servers], AMD’s _ACML_ [on the SCF Linux cluster, _vecLib_ for Macs [on the SCF Macs]), you should have good performance (potentially comparable to Matlab and to coding in C). Sometimes you can figure out a trick to take your problem and transform it to make use of the built-in functions.

Note that I run a lot of iterative algorithms so I pay attention to making sure my calculations are fast as they are done repeatedly. Similarly, one would want to pay attention to speed when doing large simulations and bootstrapping, and in some cases for optimization. And if you’re distributing code, it’s good to have it be efficient. But in other contexts, it may not be worth your time. Also, it’s good practice to code it transparently first to reduce bugs and then to use tricks to speed it up and make sure the fast version works correctly.

Results can vary with with your system setup and version of R, so the best thing to do is figure out where the bottlenecks are in your code (e.g., with _Rprof()_ or just some basic use of _system.time()_ and _benchmark()_ ), and then play around with alternative specifications. And as you gain more experience, you’ll get some intuition for what approaches might improve speed, but even with experience I find myself often surprised by what matters and what doesn’t. It’s often worth trying out a bunch of different ideas; _system.time()_ and _benchmark()_ are your workhorse tools in this context.

For material on efficient R coding, including tools for timing and profiling your code to understand where the bottlenecks are, see the tutorial, _Writing efficient R code._

### **7.1 A note on hashing**

In the tutorial on efficient R coding, I mention that looking up objects by name in an R environment occurs via hashing, so it can be very fast. I’ll briefly describe what hashing is here.

74

A hash function is a function that takes as input some data and maps it to a fixed-length output that can be used as a shortened reference to the data. We’ve seen this in the context of git commits where each commit was labeled with a long base-16 number. This also comes up when verifying files on the Internet. You can compute the hash value on the file you get and check that it is the same as the hash value associated with the legitimate copy of the file.

For our purposes here, hashing can allow one to look up values by their name via a hash table. The idea is that you have a set of key-value pairs (sometimes called a dictionary) where the key is the name associated with the value and the value is some arbitrary object. Hashing allows one to quickly determine an index associated with the key and therefore quickly find the relevant value based on the index. For example, one approach is to compute the hash as a function of the key and then take the remainder when dividing by the number of key-value pairs to get the index. Here’s the procedure in pseudocode:

hash = hashfunc(key) index = hash %% array_size

---

[← Unit 05 — programming Part 39 —](39-unit-05-programming-part-39.md) · [Up: contents](index.md) · [%% is modulo operator - it gives the remainder →](41-is-modulo-operator---it-gives-the-remainder.md)
