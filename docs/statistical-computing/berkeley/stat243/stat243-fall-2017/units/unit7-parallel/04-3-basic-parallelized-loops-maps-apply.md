---
title: 3 Basic parallelized loops/maps/apply
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit7-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Basic parallelized loops/maps/apply

**Source:** [`units/unit7-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit7-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

All of the functionality discussed here applies ONLY if the iterations/loops of your calculations can be done completely separately and do not depend on one another; i.e., you can do the computation as separate processes without communication between the processes. This scenario is called an _embarrassingly parallel_ computation

### **3.1 Embarrassingly parallel (EP) problems**

An EP problem is one that can be solved by doing independent computations as separate processes without communication between the processes. You can get the answer by doing separate tasks and then collecting the results. Examples in statistics include

1. simulations with many independent replicates

2. bootstrapping

3. stratified analyses

4. random forests

5. cross-validation.

7

The standard setup is that we have the same code running on different datasets. (Note that different processes may need different random number streams, as we will discuss in the Simulation Unit.)

To do parallel processing in this context, you need to have control of multiple processes. Note that on a shared system with queueing/scheduling software set up, this will generally mean requesting access to a certain number of processors and then running your job in such a way that you use multiple processors.

In general, except for some modest overhead, an EP problem can ideally be solved with 1 _/p_ the amount of time for the non-parallel implementation, given _p_ cores. This gives us a speedup of _p_ , which is called linear speedup (basically anytime the speedup is of the form _kp_ for some constant _k_ ).

**Question** : Suppose you have _n_ tasks to do where _n ≫ p_ . How should you divide up the _n_ tasks amongst the _p_ cores?

In the next sections, we’ll see a few approaches in R for dealing with EP problems.

### **3.2 Parallel for loops with foreach**

A simple way to exploit parallelism in R is to use the _foreach_ package to do a for loop in parallel.

The foreach package provides a _foreach_ command that allows you to do this easily. foreach can use a variety of parallel “back-ends”. For our purposes, the main one is use of the _parallel_ package to use shared memory cores. When using _parallel_ as the back-end, you should see multiple processes (as many as you registered; ideally each at 100%) when you monitor CPU usage. The multiple processes are created by forking or using sockets. (foreach can also use _Rmpi_ or _SNOW_ to access cores in a distributed memory setting; please see the tutorial on distributed parallel processing mentioned above.)

Here we’ll parallelize leave-one-out cross-validation for a random forest model. An iteration involves holding out a data point, fitting the model with all the other data points, and then predicting the held-out point. First, here’s the code for doing a cross-validation prediction and for generating some fake data.

**library** (randomForest) _## randomForest 4.6-12 ## Type rfNews() to see new features/changes/bug fixes._ looFit <- **function** (i, Y, X, loadLib = FALSE) { **if** (loadLib) **library** (randomForest)

8

out <- **randomForest** (y = Y[-i], x = X[-i, ], xtest = X[i, ]) **return** (out$test$predicted) } **set.seed** (1) _## training set_ n <- 500 p <- 50 X <- **matrix** ( **rnorm** (n*p), nrow = n, ncol = p) **colnames** (X) <- **paste** ("X", 1:p, sep="") X <- **data.frame** (X) Y <- X[, 1] + **sqrt** ( **abs** (X[, 2] * X[, 3])) + X[, 2] - X[, 3] + **rnorm** (n)

Now here’s how we use foreach to do the computation in parallel:

**require** (parallel) _# one of the core R packages_ **require** (doParallel) _## Loading required package: doParallel ## Loading required package: foreach ## Loading required package: iterators_ **library** (foreach) nCores <- 4 **registerDoParallel** (nCores) nSub <- 30 _# do only first 30 for illustration_ result <- **foreach** (i = 1:nSub) %dopar% { **cat** ('Starting ', i, 'th job.\n', sep = '') output <- **looFit** (i, Y, X) **cat** ('Finishing ', i, 'th job.\n', sep = '') output _# this will become part of the out object_ } **print** (result[1:5]) ## [[1]]

9

---

[← 2 Threading, particularly for linear algebra](03-2-threading-particularly-for-linear-algebra.md) · [Up: contents](index.md) · [Unit 07 — parallel Part 05 — →](05-unit-07-parallel-part-05.md)
