---
title: code in calcmean.py will calculate the mean of many random numbers
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit6-parallel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# code in calcmean.py will calculate the mean of many random numbers

**Source:** [`units/unit6-parallel.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

from calc_mean import *

import dask.multiprocessing
dask.config.set(scheduler='processes', num_workers = 4)

futures = []
p = 10
n = 100000000
for i in range(p):
    futures.append(dask.delayed(calc_mean)(i, n))  # add lazy task

futures
results = dask.compute(futures)  # compute all in parallel
```

## Final notes

I've only hit a few highlights here, in particular analogous
functionality to the future package, but there's lots more details in
the tutorial.

Some additional comments regarding the principles of parallelization
already discussed:

1.  You can set up nested parallelizations easily using `delayed`.
2.  Dask generally uses dynamic allocation (no prescheduling), which can
    be a drawback on some cases. You may want to manually break up
    computations into chunks in some cases.
3.  You generally don't want to call `compute` separately for multiple
    steps of a computation, as Dask will generally avoid keeping things
    in memory. Instead, write out the code for all the steps and then
    call `compute` once.
4.  Except with the `threads` scheduler, copies are made of all objects
    passed to the workers. However if you use the `distributed`
    scheduler, you can arrange things so one copy is sent for each
    worker (rather than for each task).
5.  With a bit more work than in the future package in R, you can set up
    safe parallel random number generation.

---

[← execute the function across the array of input values](12-execute-the-function-across-the-array-of-input-values.md) · [Up: contents](index.md)
