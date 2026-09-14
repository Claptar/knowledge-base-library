---
title: Unit 06 — Rprog Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 02 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

On the other hand, big matrix operations can be slow. Suppose you want a new matrix that computes the differences between successive columns of a matrix of arbitrary size. How would you do this as matrix algebra operations? [see demo code] Here it turns out that the _for_ loop is much faster than matrix multiplication. However, there is a way to do it faster as matrix direct subtraction. Comment: the demo code also contains some exploration of different ways of creating patterned matrices. Note that this level of optimization is only worth it if you’re doing something over and over again, or writing code that you will distribute.

When doing matrix algebra, the order in which you do operations can be critical for efficiency. How should I order the following calculation?

n <- 5000 A <- **matrix** ( **rnorm** (5000 * 5000), 5000) B <- **matrix** ( **rnorm** (5000 * 5000), 5000) x <- **rnorm** (5000) res <- A %*% B %*% x

We can use the matrix direct product (i.e., A*B) to do some manipulations much more quickly than using matrix multiplication. **Challenge** : How can I use the direct product to find the trace of a matrix, _XY_ ?

You can generally get much faster results by being smart when using diagonal matrices. The following operations : _X_ + _D_ , _DX_ , _XD_ are mathematically the sum of two matrices and products of two matrices. But we can do the computation without doing using two full matrices. **Challenge** : How?

10

n <- 1000 X <- **matrix** ( **rnorm** (n^2), n) diagvals <- **rnorm** (n) D = **diag** (diagvals) _# there are much faster ways than this_ summedMat <- X + D prodMat1 <- D %*% X prodMat2 <- X %*% D _# How can we do each of those operations much more quickly?_

More generally, sparse matrices and structured matrices (such as block diagonal matrices) can generally be worked with MUCH more efficiently than treating them as arbitrary matrices. The _spam_ (for arbitrary sparse matrices), _bdsmatrix_ (for block-diagonal matrices), and _Matrix_ (for a variety of sparse matrix types) packages in R can help, as can specialized code available in other languages, such as C and Fortran packages.

#### **1.2.5 Fast mapping/lookup tables**

Sometimes you need to map between two vectors. E.g., _yij ∼N_ ( _µj, σ_<sup>2</sup> ) is a basic ANOVA type structure. Here are some efficient ways to aggregate to the cluster level and disaggregate to the observation level.

Disaggregate: Create a vector, _idVec_ , that gives a numeric mapping of the observations to their cluster. Then you can access the _µ_ value relevant for each observation as: mus[idVec]. Aggregate: To find the sample means by cluster: sapply(split(dat$obs, idVec), mean)

As we’ve seen R allows you to look up elements of vector by name. For example:

vals <- **rnorm** (10) **names** (vals) <- letters[1:10] select <- **c** ("h", "h", "a", "c") vals[select] ## h h a c ## -0.09032 -0.09032 -0.51397 0.72879

You can do similar things in terms of looking up by name with dimension names of matrices/arrays, row and column names of dataframes, and named lists.

However, looking things up by name can be slow relative to looking up by index.

11

n = 1e+06 x <- 1:n xL <- **as.list** (x) nms <- **as.character** (x) **names** (x) <- nms **names** (xL) <- nms **benchmark** (x[5e+05], x["500000"], xL[[5e+05]], xL[["500000"]], replications =

|##|test|replica|tions|elapsed|relative|user.self|sys.self|
|---|---|---|---|---|---|---|---|
|##|2<br>x["500000"]||10|0.897|NA|0.840|0.048|
|##|1<br>x[5e+05]||10|0.000|NA|0.000|0.000|
|##|4 xL[["500000"]]||10|0.097|NA|0.096|0.000|
|##|3<br>xL[[5e+05]]||10|0.000|NA|0.000|0.000|
|##|user.child sys|.child||||||
|##|2<br>0|0||||||
|##|1<br>0|0||||||
|##|4<br>0|0||||||
|##|3<br>0|0||||||


Why do you think it is slow to look things up by name?

**Hashing** A hash function is a function that takes as input some data and maps it to a fixed-length output that can be used as a shortened reference to the data. We’ve seen this in the context of git commits where each commit was labeled with a long base-16 number. This also comes up when verifying files on the Internet. You can compute the hash value on the file you get and check that it is the same as the hash value associated with the legitimate copy of the file.

For our purposes here, hashing can allow one to look up values by their name via a hash table. The idea is that you have a set of key-value pairs (sometimes called a dictionary) where the key is the name associated with the value and the value is some arbitrary object. Hashing allows one to quickly determine an index associated with the key and therefore quickly find the relevant value based on the index. For example, one approach is to compute the hash as a function of the key and then take the remainder when dividing by the number of key-value pairs to get the index. Here’s the procedure in pseudocode:

hash = hashfunc(key)

index = hash %% array_size # %% is modulo operator - it gives the remainder

12

In general, there will be collisions [I neglected to make this clear in Unit 2, where I said the result of the hash function would be unique], with multiple keys assigned to the same index, but usually there will be a small number of keys associated with a given index or slot, and determining the correct value within a given index/slot (also called a bucket) is fast. Put another way, the hash function distributes the keys amongst an array of buckets and allows one to look up the appropriate bucket quickly based on the computed index value. When the hash table is properly set up, the cost of looking up a value does not depend on the number of key-value pairs stored.

As can be inferred from ?environment and according to Adler, looking up objects by name (i.e., looking up symbols) within an R environment is implemented using hashing, so it can be very fast (in the example here, it is only slightly slower than looking up by index, with some overhead associated with computing the hash value).

xEnv <- **as.environment** (xL) _# convert from a named list_ xEnv$"500000"

---

[← 1 Efficiency](01-1-efficiency.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 03 — →](03-unit-06-rprog-part-03.md)
