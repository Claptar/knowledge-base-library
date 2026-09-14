---
title: The following lines are very inefficient
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The following lines are very inefficient

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

summedMat = X + D
prodMat1 = D @ X
prodMat2 = X @ D
```

!!! tip "Tip"
Consider either $X+D$, $DX$, or $XD$. How can I use vectorization to do this much more quickly than the direct, naive translation of the math into code?
:::

!!! important "Important"
More generally, sparse matrices and structured matrices (such as block
diagonal matrices) can generally be worked with MUCH more efficiently
than treating them as arbitrary matrices. The `scipy.sparse` package (for both structured and arbitrary
sparse matrices)  can help, as can specialized code available in other languages,
such as C and Fortran packages.
:::

### Speed of lookup operations

There are lots of situations in which we need to retrieve values for subsequent computations. In some cases we might be retrieving elements of an array or looking up values in a dictionary.

Let's compare the speed of some different approaches to lookup.

```python
n = 1000
x = list(np.random.normal(size = n))
labels = [str(v) for v in range(n)]
xD = dict(zip(labels, x))

timeit.timeit("x[500]", number = 10**6, globals = {'x':x})
timeit.timeit("xD['500']", number=10**6, globals = {'xD':xD})
```

How is it that Python can look up by key in the dictionary at essentially the same speed as jumping to an index position? It uses hashing, which allows O(1) lookup. In contrast, if one has to look through each label (key) in turn, that is O(n), which is much slower:

```python
timeit.timeit("x[labels.index('500')]", number = 10**6, globals = {'x':x, 'labels': labels})
```

As a further point of contrast, if we look up elements by name in R in named vectors or lists, that is much slower than looking up by index, because R doesn't use hashing in that context and  has to scan through the objects one by one until it finds the one with the name it is looking for. This stands in contrast to R and Python being able to directly go to the position of interest based on the index of an array, or to the hash-based lookup in a Python dictionary or an R environment.

### Hashing (including name lookup)

Above I mentioned that Python uses hashing to store and lookup values
by key in a dictionary.
I'll briefly describe what hashing is here, because it is a commonly-used
strategy in programming in general.

A hash function is a function that takes as input some data (some input of arbitrary length) and maps it
to a fixed-length output that can be used as a shortened reference to
the data. (The function should be deterministic, always returing the same
output for a given input.) We've seen this in the context of git commits where each
commit was labeled with a long base-16 number. This also comes up when
verifying files on the Internet. You can compute the hash value on the
file you get and check that it is the same as the hash value associated
with the legitimate copy of the file. Even small changes in the file will result
in a different hash value.

While there are various uses of hashing, for our purposes here, hashing can allow one to look up values by their
name via a hash table. The idea is that you have a set of key-value
pairs (sometimes called a dictionary) where the key is the name
associated with the value and the value is some arbitrary object.
You want to be able to quickly find the value/object quickly.

Hashing allows one to quickly determine an index associated with the key
and therefore quickly find the relevant value based on the index. For
example, one approach is to compute the hash as a function of the key
and then take the remainder when dividing by the number of possible results
(here the fact that the result is a fixed-length output is important) to get the index.
Here's the procedure in pseudocode:

```
    hash = hashfunc(key)
    index = hash %% array_size
    ## %% is modulo operator - it gives the remainder
```

In general, there will be collisions -- multiple keys will be assigned to the
same index (this is unavoidable because of the fact that the hash function returns a fixed length output). However with a good hash function, usually there will be a small number of keys associated
with a given bucket. So each bucket will contain a list of a small number of values and the associated keys.
(The buckets might contain the actual values or they might contain the addresses of where the values are actually stored
if the values are complicated objects.) Then determining the correct value (or the required address) within
a given bucket is fast even with simple linear search through the items one by one.
Put another way, the
hash function distributes the keys amongst an array of buckets and
allows one to look up the appropriate bucket quickly based on the
computed index value. When the hash table is properly set up, the cost
of looking up a value does not depend on the number of key-value pairs
stored.

Python uses hashing to look up the value  based on the key in a given dictionary, and similarly when looking up variables in namespaces. This allows Python to retrieve objects very quickly.


## Additional general strategies for efficiency

It's also useful to be aware of some other strategies for improving efficiency.

### Cache-aware programming

In addition to main memory (what we usually mean when we talk about RAM), computers also have memory caches, which are small amounts of fast memory that can be accessed very quickly by the processor. For example your computer might have L1, L2, and L3 caches, with L1 the smallest and fastest and L3 the largest and slowest. The idea is to try to have the data that is most used by the processor in the cache.

If the next piece of data needed for computation is available in the cache, this is a *cache hit* and the data can be accessed very quickly. However, if the data is not available in the cache, this is a *cache miss* and the speed of access will be a lot slower. *Cache-aware programming* involves writing your code to minimize cache misses. Generally when data is read from memory it will be read in chunks, so values that are contiguous will be read together.

How does this inform one's programming? For example, if you have a matrix of values stored in row-major order, computing on a row will be a lot faster than computing on a column, because the row can be read into the cache from main memory and then accessed in the cache. In contrast, if the matrix is large and therefore won't fit in the cache, when you access the values of a column, you'll have to go to main memory repeatedly to get the values for the column because the values in the column are not stored contiguously.

There's a nice example of the importance of the cache at [the bottom of this blog post](https://wrathematics.github.io/2016/10/28/comparing-symmetric-eigenvalue-performance/).

If you know the size of the cache, you can try to design your code so that in a given part of your code you access data structures that will fit in the cache. This sort of thing is generally more relevant if you're coding in a language like C. But it can matter sometimes in interpreted languages too.

Let's see what happens in Python. By default, matrices in numpy are row-major, also called "C order".
I'll create a long matrix with a small number of very long columns and a wide matrix with a small number of very long rows.

```python
nr = 800000
nc = 100

A = np.random.normal(size=(nr, nc))   # long matrix
tA = np.random.normal(size=(nc, nr))  # wide matrix

## Verify that A is row-major using `.flags` (notice the `C_CONTIGUOUS: True`).
A.flags
```

Note that I didn't use `A.T` or `np.transpose` as that doesn't make a copy in memory and so the transposed
matrix doesn't end up being row-major. You can use `A.flags` and A.T.flags` to see this.

Now let's time calculating the sum by column in the long matrix vs. the sum by row in the wide matrix. Exactly the same number of arithmetic operations needs to be done in an equivalent manner for the two cases.
We want to use a large enough matrix so the entire matrix doesn't fit in the cache,
but not so large that the example takes a long time or a huge amount of memory.
We'll use a rectangular matrix, such that the summation for a single column of the long matrix
or a single row of the wide matrix involves many numbers, but there are a limited number of such
summations. This focuses the example on the efficiency of the column-wise vs. row-wise summation
rather than any issues that might be involved in managing large numbers of such summations (e.g.,
doing many, many summations that involve just a few numbers).

```python

---

[← 9. Efficiency](24-9-efficiency.md) · [Up: contents](index.md) · [Define the sum calculations as functions →](26-define-the-sum-calculations-as-functions.md)
