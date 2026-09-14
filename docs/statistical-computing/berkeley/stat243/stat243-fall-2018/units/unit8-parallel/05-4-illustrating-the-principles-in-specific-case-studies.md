---
title: 4 Illustrating the principles in specific case studies
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Illustrating the principles in specific case studies

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Scenario 1: one model fit**

**Scenario** : You need to fit a single statistical/machine learning model, such as a random forest or regression model, to your data.

#### **4.1.1 Scenario 1A:**

A given method may have been written to use parallelization and you simply need to figure out how to invoke the method for it to use multiple cores.

For example the documentation for the _randomForest_ package doesn’t indicate it can use mul-

tiple cores, but the _ranger_ package can – note the _num.threads_ argument.

**<mark>args</mark>** <mark>(ranger::ranger)</mark>

7

- ## function (formula = NULL, data = NULL, num.trees = 500, mtry = NULL, ## importance = "none", write.forest = TRUE, probability = FALSE, ## min.node.size = NULL, replace = TRUE, sample.fraction = ifelse(replace, ## 1, 0.632), case.weights = NULL, class.weights = NULL, ## splitrule = NULL, num.random.splits = 1, alpha = 0.5, minprop = 0.1, ## split.select.weights = NULL, always.split.variables = NULL, ## respect.unordered.factors = NULL, scale.permutation.importance = FALSE, ## keep.inbag = FALSE, holdout = FALSE, quantreg = FALSE, num.threads = ## save.memory = FALSE, verbose = TRUE, seed = NULL, dependent.variable.name ## status.variable.name = NULL, classification = NULL) ## NULL

#### **4.1.2 Scenario 1B:**

If a method does linear algebra computations on large matrices/vectors, R can call out to parallelized linear algebra packages (the BLAS and LAPACK).

The BLAS is the library of basic linear algebra operations (written in Fortran or C). A fast BLAS can greatly speed up linear algebra in R relative to the default BLAS that comes with R. Some fast BLAS libraries are

- Intel’s _MKL_ ; available for educational use for free

- _OpenBLAS_ ; open source and free

- _vecLib_ for Macs; provided with your Mac

In addition to being fast when used on a single core, all of these BLAS libraries are threaded - if your computer has multiple cores and there are free resources, your linear algebra will use multiple cores, provided your program is linked against the threaded BLAS installed on your machine and provided the environment variable OMP_NUM_THREADS is not set to one. (Macs make use of VECLIB_MAXIMUM_THREADS rather than OMP_NUM_THREADS.)

Threading in R is limited to linear algebra, provided R is linked against a threaded BLAS. Here’s some code that illustrates the speed of using a threaded BLAS:

**library** (RhpcBLASctl) x <- **matrix** ( **rnorm** (5000^2), 5000)

**blas_set_num_threads** (4)

8

**system.time** ({ x <- **crossprod** (x) U <- **chol** (x) }) _## user system elapsed ## 8.316 2.260 2.692_ **blas_set_num_threads** (1) **system.time** ({ x <- **crossprod** (x) U <- **chol** (x) }) _## user system elapsed ## 6.360 0.036 6.399_

Here the elapsed time indicates that using four threads gave us a two-three times (2-3x) speedup in terms of real time, while the user time indicates that the threaded calculation took a bit more total processing time (combining time across all processors) because of the overhead of using multiple threads.

Note that the code also illustrates use of an R package that can control the number of threads from within R, but you could also have set OMP_NUM_THREADS before starting R.

To use an optimized BLAS with R, talk to your systems administrator, see Section A.3 of the R Installation and Administration Manual (https://cran.r-project.org/manuals.html), or see these instructions to use vecLib BLAS from Apple’s Accelerate framework on your own Mac: http://statistics.berkeley.edu/computing/blas.

It’s also possible to use an optimized BLAS with Python’s _numpy_ and _scipy_ packages, on either Linux or using the Mac’s vecLib BLAS. Details will depend on how you install Python, numpy, and scipy.

### **4.2 Scenario 2: three different prediction methods on your data**

**Scenario** : You need to fit three different statistical/machine learning models to your data. What are some options?

- use one core per model

9

- if you have rather more than three cores, apply the ideas here combined with Scenario 1 above - with access to a cluster and parallelized implementations of each model, you might use one node per model

**library** (parallel) n <- 10000000 **system.time** ({ p <- **mcparallel** ( **mean** ( **rnorm** (n))) q <- **mcparallel** ( **mean** ( **rgamma** (n, shape = 1))) s <- **mcparallel** ( **mean** ( **rt** (n, df = 3))) res <- **mccollect** ( **list** (p,q, s)) }) ## user system elapsed ## 2.832 0.180 2.545 **system.time** ({ p <- **mean** ( **rnorm** (n)) q <- **mean** ( **rgamma** (n, shape = 1)) s <- **mean** ( **rt** (n, df = 3)) }) ## user system elapsed ## 5.036 0.060 5.098

Why might this not have shown a perfect three-fold speedup?

You could also have used tools like _foreach_ and _parLapply_ here as well, as we’ll discuss next.

### **4.3 Scenario 3: 10-fold CV and 10 or fewer cores**

**Scenario** : You are running a prediction method on 10 cross-validation folds.

Here I’ll illustrate parallel looping, using this simulated dataset and basic use of _randomForest()_ .

**library** (randomForest) _## randomForest 4.6-14 ## Type rfNews() to see new features/changes/bug fixes._

10

cvFit <- **function** (foldIdx, folds, Y, X, loadLib = FALSE) { **if** (loadLib) **library** (randomForest) out <- **randomForest** (y = Y[folds != foldIdx], x = X[folds != foldIdx, ], xtest = X[folds == foldIdx, ]) **return** (out$test$predicted) }

**set.seed** (23432) _## training set_ n <- 1000 p <- 50 X <- **matrix** ( **rnorm** (n*p), nrow = n, ncol = p) **colnames** (X) <- **paste** ("X", 1:p, sep="") X <- **data.frame** (X) Y <- X[, 1] + **sqrt** ( **abs** (X[, 2] * X[, 3])) + X[, 2] - X[, 3] + **rnorm** (n) nFolds <- 10 folds <- **sample** ( **rep** ( **seq_len** (nFolds), each = n/nFolds), replace = FALSE)

#### **4.3.1 Using a parallelized for loop with** **_foreach_**

The foreach package provides a _foreach_ command that allows you to do this easily. foreach can use a variety of parallel “back-ends”. For our purposes, the main one is use of the _parallel_ package to use shared memory cores. When using _parallel_ as the back-end, you should see multiple processes (as many as you registered; ideally each at 100%) when you monitor CPU usage. The multiple processes are created by forking or using sockets.

Note that _foreach_ also provides functionality for collecting and managing the results to avoid some of the bookkeeping you would need to do if writing your own standard for loop. The result of _foreach_ will generally be a list, unless we request the results be combined in different way, using the _.combine_ argument.

**library** (doParallel) _# uses parallel package, a core R package ## Loading required package: foreach ## Loading required package: iterators_

11

nCores <- 4 **registerDoParallel** (nCores)

result <- **foreach** (i = **seq_len** (nFolds)) %dopar% { **cat** ('Starting ', i, 'th job.\n', sep = '') output <- **cvFit** (i, folds, Y, X) **cat** ('Finishing ', i, 'th job.\n', sep = '') output _# this will become part of the out object_ } **length** (list) ## [1] 1 result[[1]][1:5] ## 3 9 12 27 29 ## 0.4122723 2.9946570 -0.2290716 2.5510170 1.0017545

You can debug by running serially using %do% rather than %dopar%. Note that you may need to load packages within the _foreach_ construct to ensure a package is available to all of the calculations.

(Note that the printed statements from _cat_ are not showing up in the creation of this document but should show if you run the code.)

#### **4.3.2 Alternatively using parallel apply statements**

The _parallel_ package has the ability to parallelize the various _apply_ functions ( _apply_ , _lapply_ , _sapply_ , etc.). It’s a bit hard to find the vignette for the parallel package (http://stat.ethz.ch/R-manual/Rdevel/library/parallel/doc/parallel.pdf) because _parallel_ is not listed as one of the contributed packages on CRAN (it gets installed with R by default).

We’ll consider parallel _lapply_ and _sapply_ . These rely on having started a cluster using _makeCluster_ , which starts new jobs via _Rscript_ and communicates via a technology called sockets.

**library** (parallel) nCores <- 4 cl <- **makeCluster** (nCores)

12

_## clusterExport(cl, c('x', 'y')) # if the processes need objects ## from main R workspace (not needed here as no global vars used)_ input <- **seq_len** (nFolds) _## need to load randomForest package within function ## when using par{L,S}apply, the last) argument being ## set to TRUE causes this to happen (see cvFit())_ **system.time** ( res <- **parSapply** (cl, input, cvFit, folds, Y, X, loadLib = TRUE) ) ## user system elapsed ## 0.004 0.004 14.046 **system.time** ( res2 <- **sapply** (input, cvFit, folds, Y, X) ) ## user system elapsed ## 42.880 0.004 42.884

Here the miniscule user time is probably because the time spent in the worker processes is not counted at the level of the overall master process that dispatches the workers.

For help with these functions and additional related parallelization functions (including _parApply()_ ), see the help on _clusterApply_ .

Now suppose you have 4 cores (and therefore won’t have an equal number of tasks per core). The approach in the next scenario should work better.

### **4.4 Scenario 4: parallelizing over prediction methods**

**Scenario** : parallelizing over prediction methods or other cases where execution time varies

If you need to parallelize over prediction methods or in other contexts in which the computation time for the different tasks varies widely, you want to avoid having the parallelization tool group the tasks in advance, because some cores may finish a lot more quickly than others. In many cases, this sort of prescheduling or ’static’ allocation of tasks to workers is the default.

_mclapply()_ is an alternative to _parSapply/parLapply_ that uses forking to start up the worker processes. Here we see how to use _mclapply_ to avoid prescheduling in a toy example.

13

**library** (parallel) nCores <- 4 _## specifically designed to be slow when have four cores and ## and use prescheduling, because ## the slow tasks all assigned to one worker_ n <- **rep** ( **c** (1e7, 1e5, 1e5, 1e5), 4) fun <- **function** (n) { **cat** ("working on ", n, "\n") **mean** ( **rnorm** (n)) } **system.time** ( res <- **mclapply** (n, fun, mc.cores = nCores) ) ## user system elapsed ## 13.856 0.040 3.545 **system.time** ( res <- **mclapply** (n, fun, mc.cores = nCores, mc.preschedule = FALSE) ) ## user system elapsed ## 6.416 0.460 1.127

### **4.5 Scenario 5: 10-fold CV across multiple methods with many more than 10 cores**

**Scenario** : You are running an ensemble prediction method such as SuperLearner or Bayesian model averaging on 10 cross-validation folds, with many statistical/machine learning methods.

Here you want to take advantage of all the cores you have available, so you can’t just parallelize over folds. There are a couple ways we can deal with such nested parallelization.

14

#### **4.5.1 Scenario 5A: nested parallelization**

One can always flatten the looping, either in a for loop or in similar ways when using apply-style statements.

_## original code: multiple loops_ **for** (fold **in** 1:n) { **for** (method **in** 1:M) { _### code here_ } } _## revised code: flatten the loops_ output <- **foreach** (idx = 1:(n*M)) %dopar% { fold <- idx %/% M + 1 method <- idx %% M + 1 _### code here_ }

Alternatively, _foreach_ supports nested parallelization as follows:

output <- **foreach** (fold = 1:n) %:% **foreach** (method = 1:M) %dopar% { _## code here_ }

The ‘%:%‘ basically causes the nesting to be flattened, with n*M total tasks run in parallel.

#### **4.5.2 Scenario 5B: Parallelizing across multiple nodes**

If you have access to multiple machines networked together, including a Linux cluster, you can use _foreach_ across multiple nodes.

The _doSNOW_ backend has the advantage over _doMPI_ in that it doesn’t need to have MPI installed on the system. MPI can be tricky to install and keep working, so this is an easy approach to using foreach across multiple machines.

Simply start R as you usually would.

Here’s R code for using doSNOW as the back-end to foreach. Make sure to use the type = "SOCK" argument or doSNOW will actually use MPI behind the scenes.

15

**library** (doSNOW) _## Specify the machines you have access to and ## number of cores to use on each:_ machines = **c** ( **rep** ("beren.berkeley.edu", 1), **rep** ("gandalf.berkeley.edu", 1), **rep** ("arwen.berkeley.edu", 2)) _## On Savio and other clusters using the SLURM scheduler: ## machines <- system('srun hostname', intern = TRUE)_ cl = **makeCluster** (machines, type = "SOCK") cl **registerDoSNOW** (cl) fun = **function** (i, n = 1e6) out = **mean** ( **rnorm** (n)) nTasks <- 120 **print** ( **system.time** (out <- **foreach** (i = 1:nTasks) %dopar% { outSub <- **fun** (i) outSub _# this will become part of the out object_ })) **stopCluster** (cl)

To use parallel variations on apply/sapply/lapply:

**library** (parallel) machines = **c** ( **rep** ("beren.berkeley.edu", 1), **rep** ("gandalf.berkeley.edu", 1), **rep** ("arwen.berkeley.edu", 2)) cl = **makeCluster** (machines)

16

cl n = 1e7 _## copy global variable to workers_ **clusterExport** (cl, **c** ('n')) fun = **function** (i) out = **mean** ( **rnorm** (n)) result <- **parSapply** (cl, 1:20, fun) result[1:5] **stopCluster** (cl)

### **4.6 Scenario 6: Stratified analysis on a very large dataset**

**Scenario** : You are doing stratified analysis on a very large dataset and want to avoid unnecessary copies.

In many of R’s parallelization tools, if you try to parallelize this case on a single node, you end up making copies of the original dataset, which both takes up time and eats up memory. Here R copies ’data’ when it passes it in as the argument to the calls to _testfun()_ .

**library** (parallel) testfun <- **function** (i, data, ids) { **return** ( **mean** (data[ids[[i]], 2])) } nStrata <- 100 n <- 3e7 data <- **cbind** ( **rep** ( **seq_len** (nStrata), each = n/nStrata), **rnorm** (n)) **object.size** (data) ids <- **lapply** ( **seq_len** (nStrata), **function** (i) **which** (data[,1] == i))

17

_## in terminal monitor memory use with: watch -n 0.1 free -h_ cl <- **makeCluster** (4) **parSapply** (cl, **seq_len** (nStrata), testfun, data, ids) **stopCluster** (cl)

However, if you are working on a single machine (i.e., with shared memory) you can avoid this by using parallelization strategies that fork the original R process (i.e., make a copy of the process) and use the big data objects in the global environment (yes, this violates the usual programming best practices of not using global variables). So here we avoid copying the original dataset.

testfun_global <- **function** (i) { **return** ( **mean** (data[ids[[i]], 2])) } _## in terminal monitor memory use with: watch -n 0.1 free -h ## Forked processes do not make copies of 'data'_ cl <- **makeCluster** (4, type = "FORK") **parSapply** (cl, **seq_len** (nStrata), testfun_global) **stopCluster** (cl) _## To contrast, we see what happens if not using ## a fork-based cluster. ## Note that this would also require exporting the global variable(s)._ cl <- **makeCluster** (4) _## This errors because 'data' not available on workers_ **parSapply** (cl, **seq_len** (nStrata), testfun_global) **clusterExport** (cl, 'data') **parSapply** (cl, **seq_len** (nStrata), testfun_global) **stopCluster** (cl)

Parallelizing across nodes requires copying any big data across machines (one can’t fork processes across nodes), which will be slow.

18

### **4.7 Scenario 7: Simulation study with n=1000 replicates: parallel random number generation**

We won’t cover this in class, though I will mention the issue in the simulation unit when we talk about random number generation.

In the previous example, we set the random number seed to different values for each bootstrap sample. One danger in setting the seed like that is that the random numbers in the different bootstrap samples could overlap somewhat. This is probably somewhat unlikely if you are not generating a huge number of random numbers, but it’s unclear how safe it is.

The key thing when thinking about random numbers in a parallel context is that you want to avoid having the same ’random’ numbers occur on multiple processes. On a computer, random numbers are not actually random but are generated as a sequence of pseudo-random numbers designed to mimic true random numbers. The sequence is finite (but very long) and eventually repeats itself. When one sets a seed, one is choosing a position in that sequence to start from. Subsequent random numbers are based on that subsequence. All random numbers can be generated from one or more random uniform numbers, so we can just think about a sequence of values between 0 and 1.

**Scenario** : You are running a simulation study with n=1000 replicates.

Each replicate involves fitting 20 statistical/machine learning methods.

Here, unless you really have access to multiple hundreds of cores, you might as well just parallelize across replicates.

However, you need to think about random number generation. If you have overlap in the random numbers the replications may not be fully independent.

In R, the _rlecuyer_ package deals with this. The L’Ecuyer algorithm has a period of $2^{191}$, which it divides into subsequences of length $2^{127}$.

Here’s how you initialize independent sequences on different processes when using the _parallel_ package’s parallel apply functionality (illustrated here with _parSapply_ ).

**library** (parallel) **library** (rlecuyer) nSims <- 250 taskFun <- **function** (i){ val <- **runif** (1) **return** (val) }

19

nCores <- 4 **RNGkind** () ## [1] "Mersenne-Twister" "Inversion" cl <- **makeCluster** (nCores) iseed <- 1 **clusterSetRNGStream** (cl = cl, iseed = iseed) **RNGkind** () _# clusterSetRNGStream sets RNGkind as L'Ecuyer-CMRG_ ## [1] "Mersenne-Twister" "Inversion" _## but it doesn't show up here on the master_ res <- **parSapply** (cl, 1:nSims, taskFun) _## now redo with same master seed to see results are the same_ **clusterSetRNGStream** (cl = cl, iseed = iseed) res2 <- **parSapply** (cl, 1:nSims, taskFun) **identical** (res,res2) ## [1] TRUE **stopCluster** (cl)

---

[← 3 Parallelization strategies](04-3-parallelization-strategies.md) · [Up: contents](index.md) · [5 Additional details and topics →](06-5-additional-details-and-topics.md)
