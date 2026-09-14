---
title: 8. Memory and copies
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 8. Memory and copies

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

## Overview

The main things to remember when thinking about memory use are: (1)
numeric vectors take 8 bytes per element and (2) we need to keep track
of when large objects are created, including local variables in the
frames of functions.

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

### Monitoring memory use in Python

There are a number of ways to see how much memory is being used. When Python
is actively executing statements, you can use `top` from the UNIX shell.

In Python, we can call out to the system to get the info we want:

```python
import psutil

---

[← SyntaxError: positional argument follows keyword argument](19-syntaxerror-positional-argument-follows-keyword-argument.md) · [Up: contents](index.md) · [Get memory information →](21-get-memory-information.md)
