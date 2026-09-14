---
title: '%% is modulo operator - it gives the remainder'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# %% is modulo operator - it gives the remainder

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In general, there will be collisions, with multiple keys assigned to the same index, but usually there will be a small number of keys associated with a given index or slot, and determining the correct value within a given index/slot (also called a bucket) is fast. Put another way, the hash function distributes the keys amongst an array of buckets and allows one to look up the appropriate bucket quickly based on the computed index value. When the hash table is properly set up, the cost of looking up a value does not depend on the number of key-value pairs stored.

### **7.2 Other approaches to speeding up R (optional)**

#### **7.2.1 pqR and other R engines**

Radford Neal, a prominent statistician/computer scientist has been working on a project called _pqR_ (pretty quick R) to rewrite some aspects of R to make them faster. There are also a few other projects that aim to reimplement the “R engine” such that one could run one’s R code with different back ends.

Here are some of the highlights of _pqR_ in terms of efficiency, as discussed at http://radfordneal.github.io/pqR/:

1. When R runs code such as just below, it actually creates a vector 1,2,....,n, (which can be computationally and memory intensive for large n) and then iterates over the values in the vector. pqR avoids this vector creation. As discussed and illustrated in Section 8, **this improvement is incorporated into R 3.5.0 and later versions** .

75

for(i in 1:n) { } vec[1:n]

2. As we’ll see in Section 8.5, R often avoids making copies of objects when it is not necessary. However, the scheme used to do this can be improved so that even fewer copies are made.

3. pqR automatically uses multiple cores for some calculations.

4. pqR avoid some checks for NA and NaN and the like in matrix calculations in which such checking would be slow and it doesn’t make sense to check for them anyway.

#### **7.2.2 Byte compiling**

R now allows you to compile R code, which goes by the name of byte compiling. Byte-compiled code is a special representation that can be executed more efficiently because it is in the form of compact codes that encode the results of parsing and semantic analysis of scoping and other complexities of the R source code. This byte code can be executed faster than the original R code because it skips the stage of having to be interpreted by the R interpreter.

The functions in the _base_ and _stats_ packages are now byte-compiled by default. (If you print out a function that is byte-compiled, you’ll see something like _<bytecode: 0x243a368>_ at the bottom.

We can byte compile our own functions using _cmpfun()_ . Here’s an example (silly since as experienced R programmers, we would use vectorized calculation here rather than this unvectorized code.)

**library** (compiler); **library** (rbenchmark) f <- **function** (vals){ x <- **as.numeric** (NA) **length** (x) <- **length** (vals) **for** (i **in seq_along** (vals)) x[i] <- **exp** (vals[i]) **return** (x) } fc <- **cmpfun** (f) fc _# notice the indication that the function is byte compiled._ ## function(vals){ ## x <- as.numeric(NA) ## length(x) <- length(vals) ## for(i in seq_along(vals)) x[i] <- exp(vals[i])

76

---

[← 7 Efficiency](40-7-efficiency.md) · [Up: contents](index.md) · [Unit 05 — programming Part 42 — →](42-unit-05-programming-part-42.md)
