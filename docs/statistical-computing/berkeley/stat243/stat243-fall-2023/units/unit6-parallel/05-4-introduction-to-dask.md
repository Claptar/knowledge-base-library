---
title: 4. Introduction to Dask
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit6-parallel.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Introduction to Dask

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Before we illustrate implementation of various kinds of parallelization,
I'll give an overview of the `Dask` package, which we'll use for many
of the implementations.

Dask has similar functionality to R's future package for parallelizing
across one or more machines/nodes. In addition, it has the important
feature of handling distributed datasets - datasets that are split into
chunks/shareds and operated on in parallel. We'll see more about
distributed datasets in Unit 7 but here we'll introduce the basic
functionality.

There are lots (and lots) of other packages in Python that also provide
functionality for parallel processing, including `ipyparallel`, `ray`,
`multiprocessing`, and `pp`.

## Overview: Key idea

A key idea in Dask (and in R's `future` package and the `ray` package for Python) involve abstracting (i.e, divorcing/separating)
the specification of the  parallelization in the code away from the computational resources that the
code will be run on. We want to:

-   Separate what to parallelize from how and where the parallelization
    is actually carried out.
-   Allow different users to run the same code on different computational
    resources (without touching the actual code that does the
    computation).

The computational resources on which the code is run is sometimes called the *backend*.

## Overview of parallel backends

One sets the *scheduler* to control how parallelization is done, whether
to run code on multiple machines, and how many cores on each machine to use.

For example to parallelize across multiple cores via separate Python
processes, we'd do this.

```python
#| eval: false
import dask
dask.config.set(scheduler='processes', num_workers = 4)
```

This table shows the different types of schedulers.

|      Type     |               Description              |  Multi-node |  Copies of objects made? |
|  -------------| ---------------------------------------| ------------| -------------------------|
|   synchronous |        not in parallel (serial)        |      no     |            no |
|    threads (1)|threads within current Python session   |      no     |            no |
|    processes  |       background Python sessions       |      no     |            yes |
|distributed (2)|Python sessions across multiple nodes   |     yes     |            yes |


Comments:

1.  Note that because of Python's Global Interpreter Lock (GIL) (which
    prevents threading of Python code), many computations done in pure
    Python code won't be parallelized using the 'threads' scheduler;
    however computations on numeric data in numpy arrays, Pandas
    dataframes and other C/C++/Cython-based code will parallelize.
2.  It's fine to use the distributed scheduler on one machine, such as
    your laptop. According to the Dask documentation, it has advantages
    over multiprocessing, including the diagnostic dashboard (see the
    tutorial) and better handling of when copies need to be made. In
    addition, one needs to use it for parallel map operations (see next
    section).

## Accessing variables and workers in the worker processes

Dask usually does a good job of identifying the packages and (global) variables
you use in your parallelized code and importing those packages on the workers and copying necessary variables to the workers.

Here's a toy example that shows that the `numpy` package and a global variable `n` are automatically available in the worker processes without any action on our part.

Note the use of the `@delayed` decorator to flag the function so that it operates in a lazy manner for use with Dask's parallelization capabilities.

```python
import dask
dask.config.set(scheduler='processes', num_workers = 4, chunksize = 1)

import numpy as np
n = 10

@dask.delayed
def myfun(idx):
   return np.random.normal(size = n)


tasks = []
p = 8
for i in range(p):
    tasks.append(myfun(i))  # add lazy task

tasks
results = dask.compute(tasks)  # compute all in parallel
```

In other contexts (in various languages) you may need to explicitly copy objects to the workers (or load packages on the workers). This is sometimes called *exporting* variables.

We don't have to flag the function in advanced with `@delayed`. We could also have directly called the decorator like this, which as the advantage of allowing us to run the function in the normal way if we simply invoke it.

```python
#| eval: false
tasks.append(dask.delayed(myfun)(i))
```

---

[← 3. Parallelization strategies](04-3-parallelization-strategies.md) · [Up: contents](index.md) · [5. Illustrating the principles in specific case studies →](06-5-illustrating-the-principles-in-specific-case-studies.md)
