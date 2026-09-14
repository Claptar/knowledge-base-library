---
title: 7. Using Dask in Python
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit6-parallel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Using Dask in Python

**Source:** [`units/unit6-parallel.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Dask has similar functionality to R's future package for parallelizing
across one or more machines/nodes. In addition, it has the important
feature of handling distributed datasets - datasets that are split into
chunks/shareds and operated on in parallel. We'll see more about
distributed datasets in Unit 7 but here we'll introduce the basic
functionality.

## Scheduler

The scheduler is the analogue of plan in the R future package. For
example to parallelize across multiple cores via separate Python
processes, we'd do this.

```python
import dask.multiprocessing
dask.config.set(scheduler='processes', num_workers = 4)
```

This table shows the different types of schedulers.

|      Type     |               Description              |  Multi-node |  Copies of objects made? |
|  -------------| ---------------------------------------| ------------| -------------------------|
|   synchronous |        not in parallel (serial)        |      no     |            no |
|    threaded   |  threads within current Python session |      no     |            no |
|    processes  |       background Python sessions       |      no     |            yes |
|   distributed |  Python sessions across multiple nodes |     yes     |            yes |


Comments:

1.  Note that because of Python's Global Interpreter Lock (GIL) (which
    prevents threading of Python code), many computations done in pure
    Python code won't be parallelized using the 'threaded' scheduler;
    however computations on numeric data in numpy arrays, Pandas
    dataframes and other C/C++/Cython-based code will parallelize.
2.  It's fine to use the distributed scheduler on one machine, such as
    your laptop. According to the Dask documentation, it has advantages
    over multiprocessing, including the diagnostic dashboard (see the
    tutorial) and better handling of when copies need to be made. In
    addition, one needs to use it for parallel map operations (see next
    section).

## Parallel map

This is the analog of apply/lapply/sapply type functions in R. As we've discussed
those are examples of map operations.

To do a parallel map, we need to use the distributed scheduler, but it's
fine to do that with multiple cores on a single machine (such as a
laptop).

```python
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = 4)
c = Client(cluster)

---

[← 6. Additional details and topics (optional)](08-6-additional-details-and-topics-optional.md) · [Up: contents](index.md) · [code in calcmean.py will calculate the mean of many random numbers →](10-code-in-calcmean-py-will-calculate-the-mean-of-many-random-n.md)
