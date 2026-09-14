---
title: 6. Additional details and topics (optional)
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Additional details and topics (optional)

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Avoiding repeated calculations by calling `.compute` once

As far as I can tell, Dask avoids keeping all the pieces of a distributed object or computation in memory. However, in many cases this can mean repeating computations or re-reading data if you need to do multiple operations on a dataset.

For example, if you are creating a Dask distributed dataset from data on disk, I think this means that every distinct set of computations (each computational graph) will involve reading the data from disk again.

One implication is that if you can include all computations on a large dataset within a single computational graph (i.e., a call to compute) that may be much more efficient than making separate calls.

Here’s an example with Dask dataframe on some air traffic delay data, where we make sure to do all our computations as part of one graph:

```python
#| eval: false
import dask
dask.config.set(scheduler='processes', num_workers = 6)
import dask.dataframe as ddf
air = ddf.read_csv(path + '*.csv.bz2',
      compression = 'bz2',
      encoding = 'latin1', # (unexpected) latin1 value(s) in TailNum field in 2001
      dtype = {'Distance': 'float64', 'CRSElapsedTime': 'float64',
      'TailNum': 'object', 'CancellationCode': 'object', 'DepDelay': 'float64',
      'ActualElapsedTime': 'float64', 'ArrDelay': 'float64', 'ArrTime': 'float64',
       'DepTime': 'float64'})

import time
t0 = time.time()
air.DepDelay.min().compute()   # about 200 seconds.
print(time.time()-t0)
t0 = time.time()
air.DepDelay.max().compute()   # about 200 seconds.
print(time.time()-t0)
t0 = time.time()
(mn, mx) = dask.compute(air.DepDelay.max(), air.DepDelay.min())  # about 200 seconds
print(time.time()-t0)
```

## Setting the number of threads (cores used) in threaded code (including parallel linear algebra in Python and R)

In general, threaded code will detect the number of cores available on a
machine and make use of them. However, you can also explicitly control
the number of threads available to a process.

For most threaded code (that based on the openMP protocol), the number
of threads can be set by setting the `OMP_NUM_THREADS` environment
variable (use `VECLIB_MAXIMUM_THREADS` on a Mac). E.g., to set it for four
threads in the bash shell:

```bash
#| eval: false
export OMP_NUM_THREADS=4
```

Do this before starting your R or Python session or before running your
compiled executable.

Alternatively, you can set OMP_NUM_THREADS as you invoke your job, e.g.,
here with R:

```bash
#| eval: false
OMP_NUM_THREADS=4 R CMD BATCH --no-save job.R job.out
```


### Cautions about speed and threaded BLAS

In many cases, using multiple threads for linear algebra operations will
outperform using a single thread, but there is no guarantee that this
will be the case, in particular for operations with small matrices and
vectors. You can compare speeds by setting `OMP_NUM_THREADS` to different
values. In cases where threaded linear algebra is slower than
unthreaded, you would want to set `OMP_NUM_THREADS` to 1.

More generally, if you are using the parallel tools in Section 4 to
simultaneously carry out many independent calculations (tasks), it is
likely to be more effective to use the fixed number of cores available
on your machine so as to split up the tasks, one per core, without
taking advantage of the threaded BLAS (i.e., restricting each process to
a single thread).

---

[← First host is the scheduler.](09-first-host-is-the-scheduler.md) · [Up: contents](index.md) · [7. Introduction to R's future package (optional) →](11-7-introduction-to-r-s-future-package-optional.md)
