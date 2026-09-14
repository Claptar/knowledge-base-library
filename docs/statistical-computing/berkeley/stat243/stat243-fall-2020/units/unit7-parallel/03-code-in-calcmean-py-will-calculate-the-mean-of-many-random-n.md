---
title: code in calcmean.py will calculate the mean of many random numbers from calcmean
  import
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# code in calcmean.py will calculate the mean of many random numbers from calcmean import

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

import dask.multiprocessing dask.config.set(scheduler='processes', num_workers = 4) futures = [] p = 10 n = 100000000 for i in range(p): futures.append(dask.delayed(calc_mean)(i, n)) # add lazy task futures results = dask.compute(*futures) # compute all in parallel

### **7.4 Final notes**

I’ve only hit a few highlights here, in particular analogous functionality to the future package, but there’s lots more details in the tutorial.

Some additional comments regarding the principles of parallelization already discussed:

1. You can set up nested parallelizations easily using _delayed_ .

2. Dask generally uses dynamic allocation (no prescheduling), which can be a drawback on some cases. You may want to manually break up computations into chunks in some cases.

3. You generally don’t want to call _compute_ separately for multiple steps of a computation, as Dask will generally avoid keeping things in memory. Instead, write out the code for all the steps and then call _compute_ once.

4. Except with the _threads_ scheduler, copies are made of all objects passed to the workers. However if you use the _distributed_ scheduler, you can arrange things so one copy is sent for each worker (rather than for each task).

5. With a bit more work than in the future package in R, you can set up safe parallel random number generation.

23

---

[← code in calcmean.py will calculate the mean of many random numbers from calcmean import](02-code-in-calcmean-py-will-calculate-the-mean-of-many-random-n.md) · [Up: contents](index.md)
