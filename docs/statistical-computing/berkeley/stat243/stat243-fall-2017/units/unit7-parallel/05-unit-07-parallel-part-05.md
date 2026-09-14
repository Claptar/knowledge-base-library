---
title: Unit 07 — parallel Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — parallel Part 05 —

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(Note that the printed statements from ‘cat‘ are not showing up in the creation of this document but should show if you run the code.)

Note that foreach also provides functionality for collecting and managing the results to avoid some of the bookkeeping you would need to do if writing your own standard for loop. The result of foreach will generally be a list, unless we request the results be combined in different way, as we do here using .combine = c.

You can debug by running serially using %do% rather than %dopar%.

### **3.3 Parallel apply functionality**

The _parallel_ package has the ability to parallelize the various apply functions ( _apply()_ , _lapply()_ , _sapply()_ , etc.). It’s a bit hard to find the vignette for the parallel package because _parallel_ is not listed as one of the contributed packages on CRAN (it gets installed with R by default).

We’ll consider parallel _lapply()_ and _sapply()_ . These rely on having started a cluster using _cluster()_ , which uses the PSOCK mechanism as in the SNOW package - starting new jobs via Rscript and communicating via a technology called sockets.

10

**require** (parallel) nCores <- 4 _### using sockets # ## ?clusterApply_ cl <- **makeCluster** (nCores) _# by default this uses sockets # clusterExport(cl, c('x', 'y')) # if the processes need objects # from master's workspace (not needed here as no global vars used)_ input <- **seq_len** (nSub) _# same as 1:nSub but more robust # need to load randomForest package within function # when using par{L,S}apply_ **system.time** ( res <- **parSapply** (cl, input, looFit, Y, X, TRUE) ) ## user system elapsed ## 0.000 0.004 16.569 **system.time** ( res2 <- **sapply** (input, looFit, Y, X) ) ## user system elapsed ## 56.016 0.024 56.043 res <- **parLapply** (cl, input, looFit, Y, X, TRUE)

Here the miniscule user time is probably because the time spent in the worker processes is not counted at the level of the overall master process that dispatches the workers.

For help with these functions and additional related parallelization functions (including _parApply()_ ), see the help on _clusterApply_ .

_mclapply()_ is an alternative that uses forking to start up the worker processes.

11

**system.time** ( res <- **mclapply** (input, looFit, Y, X, mc.cores = nCores) ) ## user system elapsed ## 59.000 0.052 15.863

Note that some R packages can directly interact with the parallelization packages to work with multiple cores. E.g., the _boot_ package can make use of the parallel package directly.

### **3.4 Limitations in Windows**

Forking in R is not possible on Windows, so parallelization on Windows would generally need to use approaches based on sockets and not based on forking.

### **3.5 Loading packages and accessing global variables within your parallel tasks**

Whether you need to explicitly load packages and export global variables from the master process to the parallelized worker processes depends on the details of how you are doing the parallelization.

With foreach with the _doParallel_ backend, parallel apply-style statements (starting the cluster via _makeForkCluster()_ , instead of the default _makeCluster()_ ), and _mclapply()_ , packages and global variables in the main R process are automatically available to the worker tasks without any work on your part. This is because all of these approaches fork the original R process, thereby creating worker processes with the same state as the original R process. Interestingly, this means that global variables in the forked worker processes are just references to the objects in memory in the original R process. So the additional processes do not use additional memory for those objects (despite what is shown in _top_ ) and there is no time involved in making copies. However, if you modify objects in the worker processes then copies are made, as we’ve seen to be generally the case with R.

Let’s experiment with that with foreach where foreach uses forking by default on the machine I’m running this on. Note that this seems to indicate no copy is made until a change is made, but also note what seems strange about the new address of ’x’. I’m not sure what is going on with regard to the latter.

12

**library** (parallel) _# one of the core R packages_ **library** (doParallel) _# loads foreach as a dependency_

nCores <- 4 **registerDoParallel** (nCores) **library** (pryr) x <- **rnorm** (10) **address** (x) ## [1] "0x4e12f98" result <- **foreach** (i = 1:3) %dopar% { **set.seed** (i) tmp <- **address** (x) _# original address_ x[3] <- **rnorm** (1) out <- **c** (orig = tmp, new = **address** (x)) } result ## [[1]] ## orig new ## "0x4e12f98" "0x4bb8e90" ## ## [[2]] ## orig new ## "0x4e12f98" "0x4bb8e90" ## ## [[3]] ## orig new ## "0x4e12f98" "0x4bb8e90" _## note when this is run manually in R, 'x' is not copied ## when x[3] is modified; not sure why the different behavior_ **address** (x) ## [1] "0x4e12f98"

13

x[3] <- 2.1 **address** (x) ## [1] "0x4a79398"

In contrast, when processes are not forked, we can see that a copy is being made for each process from the very beginning:

cl <- **makeCluster** (4) cl _# no forking_ ## socket cluster with 4 nodes on host 'localhost' **registerDoParallel** (cl) x <- **rnorm** (10) **library** (pryr) **address** (x) ## [1] "0x4a75ff8" result <- **foreach** (i = 1:3, .packages = 'pryr') %dopar% { **address** (x) _# print(.Internal(inspect)) doesn't print to screen_ } result ## [[1]] ## [1] "0x26507f8" ## ## [[2]] ## [1] "0x1f7a7f8" ## ## [[3]] ## [1] "0x17e77f8"

In contrast, with parallel apply-style statements when starting the cluster using the default _makeCluster()_ (which sets up a so-called _PSOCK_ cluster, starting the R worker processes via Rscript), one needs to load packages within the code that is executed in parallel. In addition one needs to use _clusterExport()_ to tell R which objects in the global environment should be available

14

to the worker processes. This involves making as many copies of the objects as there are worker processes, so one can easily exceed the physical memory (RAM) on the machine if one has large objects, and the copying of large objects will take time.

---

[← 3 Basic parallelized loops/maps/apply](04-3-basic-parallelized-loops-maps-apply.md) · [Up: contents](index.md) · [4 Parallelization strategies →](06-4-parallelization-strategies.md)
