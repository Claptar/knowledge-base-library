---
title: 10. Memory and copies
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) — berkeley-stat243 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 10. Memory and copies

## Overview

The main things to remember when thinking about memory use are: (1)
numeric arrays take 8 bytes per element and (2) we need to keep track
of when large objects are created, including local variables in the
frames of functions. To do (2) we need to know when a copy of an
actual object is created versus when we simply copy the name/label/reference
to an existing object.

```python
x = np.random.normal(size = 5)
x.itemsize # 8 bytes
x.nbytes
```

### Allocating and freeing memory

Unlike compiled languages like C, in Python we do not need to explicitly
allocate storage for objects. (However, we will see that there are times
that we do want to allocate storage in advance, rather than successively
concatenating onto a larger object.)

Python automatically manages memory, releasing memory back to the operating
system when it's not needed via a process called *garbage collection*. Very occasionally
you may want to remove large objects as soon as they are not needed.
`del` does not actually free up memory, it just disassociates the name
from the memory used to store the object. In general Python will quickly
clean up such objects without a reference (i.e., a name), so there is generally
no need to call `gc.collect()` to force
the garbage collection.

In a language like C in which the user allocates and frees up memory,
memory leaks are a major cause of bugs. Basically if you are looping and
you allocate memory at each iteration and forget to free it, the memory
use builds up inexorably and eventually the machine runs out of memory.
In Python, with automatic garbage collection, this is generally not an issue,
but occasionally memory leaks could occur.

### The heap and the stack

The *heap* is the memory that is available for dynamically creating new
objects while a program is executing, e.g., if you create a new object
in Python or call *new* in C++. When more memory is needed the program can
request more from the operating system. When objects are removed in Python, Python
will handle the garbage collection of releasing that memory.

The *stack* is the memory used for local variables when a function is
called. I.e., the stack is the memory associated with function frames.
Hence the term "stack trace" to refer to the active function frames
during execution of code.

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

We can see this via `free -h --si`.

The `-h` is for 'human-readable' for nicer numerical printout and
the `--si` uses gigabytes (base 10) instead of gibibytes (base 2).

```
paciorek@gandalf:~> free -h --si
               total        used        free      shared  buff/cache   available
Mem:            135G         24G         30G        7.8M         80G        110G
Swap:           274G         44G        230G
```

You'll generally be interested in the `Mem` row. (See below for some
comments on `Swap`.) The `shared` column is complicated and probably
won't be of use to you. The `buff/cache` column shows how much space is
used for disk caching and related purposes but is actually available.
Hence the `available` column is the sum of the `free` and `buff/cache`
columns (more or less). In this case 24 GB is in use
(indicated in the `used` column), leaving 110 GB available for use.

`top` (Linux or Mac) shows both total memory use and statistics by process.

Here are some example lines from the first few lines of output from `top`:

```
MiB Mem : 128877.0 total,  28825.9 free,  23856.4 used,  77249.1 buff/cache
MiB Swap: 262144.0 total, 220103.3 free,  42040.7 used. 105020.6 avail Mem
```

We see that this machine has 129 GiB RAM (the 'total' column in the `Mem`
row), with 106 GiB available (29 GiB free plus 77 GiB buff/cache as seen
in the `Mem` row).  24 GiB is in use.

*Swap* is essentially the reverse of disk caching. It is disk space that
is used for memory when the machine runs out of physical memory. You
generally don't want your machine to be using swap for memory because your jobs
can slow to a crawl. As seen above, the `swap` line in
`top` shows 262 GiB swap space (274 GB in `free`), with 42 GiB (44 GB) in use. One would
often hope that little swap space is in use, but this can get complicated.
In this case I'm not sure why 42 GiB of swap is being used given
there is plenty of physical memory available.

Note that some of the numbers differ a bit between `top` and `free`, more
so that can be explained based on gigabytes vs. gibibytes. I'm not sure
why that is, but it doesn't affect our overall assessment of memory used
 and available here.

### Monitoring memory use in Python

There are a number of ways to see how much memory is being used. When Python
is actively executing statements, you can use `top` from the UNIX shell.

In Python, we can call out to the system to get the info we want:

```python
import psutil

# Get memory information
memory_info = psutil.Process().memory_info()

# Print the memory usage
print("Memory usage:", memory_info.rss/10**6, " MB.")

# Let's turn that into a function for later use:
def mem_used():
    print("Memory usage:", psutil.Process().memory_info().rss/10**6, " MB.")
```

We can see the size of an object (in bytes) with `sys.getsizeof()`.

```python
my_list = [1, 2, 3, 4, 5]
sys.getsizeof(my_list)

x = np.random.normal(size = 10**7) # should use about 80 MB
sys.getsizeof(x)
```

However, we need to be careful about objects that refer to other objects:

```python
y = [3, x]
sys.getsizeof(y)  # Whoops!
```

Here's a
trick where we serialize the object, as if to export it, and then see
how long the binary representation is.

```python
import pickle
ser_object = pickle.dumps(y)
sys.getsizeof(ser_object)
```

There are also some flags that one can start `python` with that allow
one to see information about memory use and allocation. See `man python`.
You could also look into the `memory_profiler` or `pympler` packages.

## How memory is used in Python

### Two key tools: `id` and `is`

We can use the `id` function to see where in
memory an object is stored and `is` to see if two
object are actually the same objects in memory.
It's particularly useful for understanding storage
and memory use for complicated data structures.
We'll also see that they can be handy tools for
seeing where copies are made and where they are not.

```python
x = np.random.normal(size = 10**7)
id(x)
sys.getsizeof(x)
y = x
id(y)
x is y
sys.getsizeof(y)

z = x.copy()
id(z)
sys.getsizeof(z)
```

### Memory use in specific circumstances

#### How lists are stored

Here we can use `id` to determine how the overall list is stored as
well as the elements of the list.

```python
nums = np.random.normal(size = 5)
obj = [nums, nums, np.random.normal(size = 5), ['adfs']]

id(nums)
id(obj)
id(obj[0])
id(obj[1])
id(obj[2])
id(obj[3])
id(obj[3][0])

obj[0] is obj[1]
obj[0] is obj[2]
```

What do we notice?

  - The list itself appears to be a array of references (pointers) to the component elements.
  - Each element has its own address.
  - Two elements of a list can use the same memory (see the first two elements here, whose contents are at the same memory address).
  - A list element can use the same memory as another object (or part of another object).

A note about calling `id` on list elements, e.g., `id(obj[0])`. Running that code causes execution of `obj[0]`, and the result is passed into `id`. That creates a new temporary object that is passed to `id`. The temporary object references the same object that `obj[0]` does, so we find out the id of `obj[0]`.

#### How character strings are stored.

Similar tricks are used for storing strings (and also integers). We may explore this in a problem set problem.

#### How numpy arrays are stored

To do vectorized calculations and linear algebra efficiently, one needs the data in arrays stored contiguously in memory, and this is how numpy arrays are stored. We've seen that a numpy array involves the actual numbers plus 112 bytes of metadata/overhead associated with the object.

We can't usefully call `id` on elements of the array. Consider this:

```python
x = np.random.normal(size=5)
type(x[1])
id(x[1])
tmp1 = x[1]
tmp2 = x[1]
id(tmp1)
id(tmp2)
```

Each time we get the `x[1]` element we are creating a new numpy float64 scalar object. This is because each element of the array is not its own object (unlike a list element) so extracting the element involves copying the value and making a new object.

Another indication of the array being stored contiguously is that if we pickle the array, its size is just a bit more than the size needed just to store the 8-byte numbers. If we instead pickle a list containing those same numbers, the result is more than twice as big, related to the pointers involved in referring to the individual numbers.

#### Modifying elements in place

What do this simple experiment tell us?

```python
x = np.random.normal(size = 5)
id(x)
x[2] = 3.5
id(x)
```

It makes some sense that modifying elements of an object here doesn't cause a copy -- if it did, working with large objects would be very difficult.

#### Shallow copying

A *shallow* copy only makes a new top-level object. The elements within the object are still shared with the original object.

```python
x = [3, [1,2,3]]
y = x.copy()
id(x)
id(y)
x[0] = 9
y[0]

id(x[1])
id(y[1])
y[1][2] = 99
x
```

We can force a *deep* copy such that nothing is shared between the objects.

```python
import copy
x = [3, [1,2,3]]
y = copy.deepcopy(x)

id(x[1])
id(y[1])
y[1][2] = 99
x
```

### When are copies made?

Let's try to understand when Python uses additional memory for objects, and how it knows when it can delete memory.
We'll use large objects so that we can use `free` or `top` to see how memory use by the Python process changes.

```python
x = np.random.normal(size = 10**8)
id(x)
y = x
id(y)

x = np.random.normal(size = 10**8)
id(x)
```

Only if we re-assign `x` to reference a different object does additional memory get used.

#### How does Python know when it can free up memory?

Python keeps track of how many names refer to an object and only
removes memory when there are no remaining references to an object.

```python
import sys

x = np.random.normal(size = 10**8)
y = x
sys.getrefcount(y)

del x
sys.getrefcount(y)
del y
```

We can see the number of references using `sys.getrefcount`.
Confusingly, the number is one higher than we'd expect,
because it includes the temporary reference from passing
the object as the argument to `getrefcount`.

```python
x = np.random.normal(size = 5)
sys.getrefcount(x)  # In reality, only 1.
y = x
sys.getrefcount(x)  # In reality, 2.
sys.getrefcount(y)  # In reality, 2.

del y
sys.getrefcount(x)  # In reality, only 1.

y = x
x = np.random.normal(size = 5)
sys.getrefcount(y)  # In reality, only 1.
sys.getrefcount(x)  # In reality, only 1.
```

This notion of reference counting occurs in other contexts, such as
shared pointers in C++ and in how R handles copying and garbage collection.

## Strategies for saving memory

A few basic strategies for saving memory include:

-   Avoiding unnecessary copies.
-   Removing objects that are not being used, at which point the Python garbage collector should free up the memory.
-   Use iterators (e.g., `range()`) and [generators](https://wiki.python.org/moin/Generators) to avoid building long lists that are iterated over.

If you're really trying to optimize memory use, you may also consider:

-   Using types that take up less memory (e.g., `Bool`, `Int16`, `Float32`) when
    possible.
    ```python
    x = np.array(np.random.normal(size = 5), dtype = "float32")
    x.itemsize
    x = np.array([3,4,2,-2], dtype = "int16")
    x.itemsize
    ```
-   Reading data in from files in chunks rather than reading the entire dataset (more in Unit 7).
-   Exploring packages such as `arrow` for efficiently using memory, as discussed in [Unit 2](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-dataTech.html#reading-data-quickly-arrow-and-polars).

## Example

Let's work through a real example where we keep a running tally of
current memory in use and maximum memory used in a function call. We'll
want to consider hidden uses of memory and when copies of the object are made rather than simply creating a new reference to an existing object.  This
code (translated from the original R code) comes from a PhD student's research. For our purposes here, let's assume
that the input `x` and `y` are very long numpy arrays using a lot of memory.

`np.isnan` returns an boolean array of True/False values indicating whether each input element is a NaN (not a number).

```python
#| eval: false
def fastcount(xvar, yvar):
    naline = np.isnan(xvar)
    naline[np.isnan(yvar)] = True
    localx = xvar.copy()
    localy = yvar.copy()
    localx[naline] = 0
    localy[naline] = 0
    useline = ~naline
    ## We'll ignore the rest of the code.
    ## ....

fastcount(x, y) # Assume x, y are existing large numpy arrays.

```

!!! tip "Tip"
In the code above, note all the places where new memory must be allocated.
:::

---

[← 9. Functional programming](10-9-functional-programming.md) · [Up: contents](index.md) · 11. Efficiency →
