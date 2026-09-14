---
title: 10. Memory and copies
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 10. Memory and copies

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

---

[← SyntaxError: positional argument follows keyword argument](23-syntaxerror-positional-argument-follows-keyword-argument.md) · [Up: contents](index.md) · [Get memory information →](25-get-memory-information.md)
