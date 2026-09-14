---
title: 3 Explicit parallel code in R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Explicit parallel code in R

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Before we get into some functionality, let’s define some terms more explicitly.

- _threading_ : multiple paths of execution within a single process; the OS sees the threads as a single process, but one can think of them as ’lightweight’ processes

- _forking_ : child processes are spawned that are identical to the parent, but with different process IDs and their own memory

7

- _sockets_ : some of R’s parallel functionality involves creating new R processes and communicating with them via a communication technology called sockets

### **3.1** **_foreach_**

A simple way to exploit parallelism in R when you have an EP problem is to use the _foreach_ package to do a for loop in parallel. For example, bootstrapping, random forests, simulation studies, cross-validation and many other statistical methods can be handled in this way. You would not want to use _foreach_ if the iterations were not independent of each other.

The _foreach_ package provides a _foreach_ command that allows you to do this easily. _foreach_ can use a variety of parallel “back-ends”. It can use _Rmpi_ to access cores in a distributed memory setting when MPI is available or (our focus here) the _parallel_ or _multicore_ packages to use shared memory cores. When using _parallel_ or _multicore_ as the back-end, you should see multiple processes (as many as you registered; ideally each at 100%) when you look at _top_ . The multiple processes are generally created by forking.

**require** (parallel) _# one of the core R packages_ **require** (doParallel) _# require(multicore); require(doMC) # alternative to parallel/doParallel # require(Rmpi); require(doMPI) # when Rmpi is available as the back-end_ **library** (foreach) **library** (iterators) taskFun <- **function** () { mn <- **mean** ( **rnorm** (1e+07)) **return** (mn) } nCores <- 4 _# set based on the machine to be used_ **registerDoParallel** (nCores) _# registerDoMC(nCores) # alternative to registerDoParallel cl <- # startMPIcluster(nCores); registerDoMPI(cl) # when using Rmpi as the # back-end_ out <- **foreach** (i = 1:100, .combine = c) %dopar% { **cat** ("Starting ", i, "th job.\n", sep = "") outSub <- **taskFun** () **cat** ("Finishing ", i, "th job.\n", sep = "") outSub _# this will become part of the out object_

8

<mark>}</mark>

The result of _foreach_ will generally be a list, unless _foreach_ is able to put it into a simpler R object. Here I’ve explicitly told _foreach_ to combine the results with _c()_ ( _cbind()_ and _rbind()_ are other common choices), but it will often be smart enough to figure it out on its own. Note that _foreach_ also provides some additional functionality for collecting and managing the results that mean that you don’t have to do some of the bookkeeping you would need to do if writing your own for loop.

You can debug by running serially using _%do%_ rather than _%dopar%_ .

Note that you may need to load packages within the _foreach_ code block to ensure a package is available to all of the calculations.

**Warning** (repeated from before): There are sometimes conflicts between _foreach_ and the threaded BLAS, so before running an R job that does linear algebra within a call to _foreach_ , you may need to set _OMP_NUM_THREADS_ to 1 to prevent the BLAS from doing threaded calculations.

### **3.2 Parallel apply and vectorization (parallel package)**

The _parallel_ package has the ability to (1) parallelize the various _apply()_ functions ( _apply()_ , _lapply()_ , _sapply()_ , etc.) and (2) parallelize vectorized functions, among other things. The _multicore_ package also has this ability and _parallel_ is built upon _multicore_ . _parallel_ is a core R package so we’ll explore the functionality in that setting. Here’s the vignette for the parallel package – it’s hard to find because _parallel_ is not listed as one of the contributed packages on CRAN.

First let’s consider parallel _apply()_ .

**require** (parallel) nCores <- 4 _### using sockets ?clusterApply_ cl <- **makeCluster** (nCores) _# by default this uses sockets_ nSims <- 60 testFun <- **function** (i) { mn <- **mean** ( **rnorm** (1e+06)) **return** (mn) } _# if the processes need objects (x and y, here) from the master's workspace: # clusterExport(cl, c('x', 'y'))_ **system.time** (res <- **parSapply** (cl, 1:nSims, testFun))

9

**system.time** (res2 <- **sapply** (1:nSims, testFun)) myList <- **as.list** (1:nSims) res <- **parLapply** (cl, myList, testFun)

_### using forking_ **system.time** (res <- **mclapply** ( **seq_len** (nSims), testFun, mc.cores = nCores))

In _mclapply()_ , there is an option, _mc.preschedule_ , that if set to TRUE (the default), causes the jobs to be divided in advance amongst the cores. For individual tasks with high variation in completion time, setting this to FALSE is a good idea. Why? Similarly, there are ’load-balancing’ versions of _par{S,L}apply()_ : _par{L,S}applyLB()_ .

Now let’s consider parallel evaluation of a vectorized function. _exp()_ is not a great example, because it’s quite fast anyway, so I also show an example with _Matern()_ , which calculates correlation as a parameterized function of distance (e.g., time lag) in a vectorized fashion.

**require** (parallel) nCores <- 4 x <- **rnorm** (1e+07) expx <- **pvec** (x, exp, mc.cores = nCores) **library** (fields) ds <- **runif** (6e+06, 0.1, 10) **system.time** (corVals <- **pvec** (ds, Matern, 0.1, 2, mc.cores = nCores)) **system.time** (corVals <- **Matern** (ds, 0.1, 2))

Note that some R packages can directly interact with the parallelization packages to work with multiple cores. E.g., the _boot_ package can make use of the _multicore_ package directly.

### **3.3 Explicit parallel programming in R: mcparallel and forking**

Now let’s discuss some functionality in which one more explicitly controls the parallelization.

#### **3.3.1 Using mcparallel to dispatch blocks of code to different processes**

First one can use _mcparallel()_ in the _parallel_ package to send different chunks of code to different processes.

10

**library** (parallel) n <- 1e+07 **system.time** ({ p <- **mcparallel** ( **mean** ( **rnorm** (n))) q <- **mcparallel** ( **mean** ( **rgamma** (n, shape = 1))) res <- **mccollect** ( **list** (p, q)) }) **system.time** ({ p <- **mean** ( **rnorm** (n)) q <- **mean** ( **rgamma** (n, shape = 1)) })

#### **3.3.2 Explicitly forking code in R**

The _fork_ package and _fork()_ function in R provide an implementation of the UNIX _fork_ system call for forking a process. Note that the code here does not handle passing information back from the child very well. One approach is to use sockets – the help page for _fork()_ has a bit more information.

**library** (fork) _# mode 1 of how to use fork()_ pid <- **fork** (slave = myfun) _# mode 2 of how to use fork() this set of braces is REQUIRED when you don't # pass a function to the slave argument of fork()_ { pid <- **fork** (slave = **NULL** ) **if** (pid == 0) { **cat** ("Starting child process execution.\n") tmpChild <- **mean** ( **rnorm** (1e+07)) **cat** ("Result is ", tmpChild, "\n", sep = "") **save** (tmpChild, file = "child.RData") _# clunky_ **cat** ("Finishing child process execution.\n") **exit** () } **else** { **cat** ("Starting parent process execution.\n") tmpParent <- **mean** ( **rnorm** (1e+07))

11

**cat** ("Finishing parent process execution.\n") **wait** (pid) _# wait til child is finished so can read # in updated child.RData below_ } } **load** ("child.RData") _# clunky_ **print** ( **c** (tmpParent, tmpChild))

Note that if we were really running the above code, we’d want to be careful about the random number generation (RNG). As it stands, it will use the same random numbers in both child and parent processes.

12

---

[← 2 Parallelization](03-2-parallelization.md) · [Up: contents](index.md)
