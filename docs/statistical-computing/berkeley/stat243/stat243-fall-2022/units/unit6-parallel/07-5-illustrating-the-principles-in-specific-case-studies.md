---
title: 5. Illustrating the principles in specific case studies
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit6-parallel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Illustrating the principles in specific case studies

**Source:** [`units/unit6-parallel.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit6-parallel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Scenario 1: one model fit

**Scenario**: You need to fit a single statistical/machine learning
model, such as a random forest or regression model, to your data.

### Scenario 1A:

A given method may have been written to use parallelization and you
simply need to figure out how to invoke the method for it to use
multiple cores.

For example the documentation for the `randomForest` package doesn't
indicate it can use multiple cores, but the `ranger` package can -- note
the `num.threads` argument.

```r
args(ranger::ranger)
```

### Scenario 1B:

If a method does linear algebra computations on large matrices/vectors,
R can call out to parallelized linear algebra packages (the BLAS and
LAPACK).

The BLAS is the library of basic linear algebra operations (written in
Fortran or C). A fast BLAS can greatly speed up linear algebra in R
relative to the default BLAS that comes with R. Some fast BLAS libraries
are

-   Intel's *MKL*; available for educational use for free
-   *OpenBLAS*; open source and free
-   *vecLib* for Macs; provided with your Mac

In addition to being fast when used on a single core, all of these BLAS
libraries are threaded - if your computer has multiple cores and there
are free resources, your linear algebra will use multiple cores,
provided your program is linked against the threaded BLAS installed on
your machine and provided the environment variable OMP_NUM_THREADS is
not set to one. (Macs make use of VECLIB_MAXIMUM_THREADS rather than
OMP_NUM_THREADS.)

Threading in R is limited to linear algebra, provided R is linked
against a threaded BLAS.

Here's some code that illustrates the speed of using a threaded BLAS:

```r
library(RhpcBLASctl)
x <- matrix(rnorm(5000^2), 5000)

blas_set_num_threads(4)
system.time({
   x <- crossprod(x)
   U <- chol(x)
})

##   user  system elapsed
##  8.316   2.260   2.692

blas_set_num_threads(1)
system.time({
   x <- crossprod(x)
   U <- chol(x)
})

##   user  system elapsed
##  6.360   0.036   6.399
```

Here the elapsed time indicates that using four threads gave us a
two-three times (2-3x) speedup in terms of real time, while the user
time indicates that the threaded calculation took a bit more total
processing time (combining time across all processors) because of the
overhead of using multiple threads.

Note that the code also illustrates use of an R package that can control
the number of threads from within R, but you could also have set
OMP_NUM_THREADS before starting R.

To use an optimized BLAS with R, talk to your systems administrator, see
[Section A.3 of the R Installation and Administration Manual](https://cran.r-project.org/doc/manuals/r-release/R-admin.html#BLAS), or see [these instructions](https://statistics.berkeley.edu/computing/blas)
to use vecLib BLAS from Apple's Accelerate framework on your own Mac.

It's also possible to use an optimized BLAS with Python's `numpy` and
`scipy` packages, on either Linux or using the Mac's *vecLib* BLAS.
Details will depend on how you install Python, numpy, and scipy.

## Scenario 2: three different prediction methods on your data

**Scenario**: You need to fit three different statistical/machine
learning models to your data.

What are some options?

-   use one core per model
-   if you have rather more than three cores, apply the ideas here
    combined with Scenario 1 above - with access to a cluster and
    parallelized implementations of each model, you might use one node
    per model

```r
library(future)
ntasks <- 3
plan(multisession, workers = ntasks)

n <- 10000000
system.time({
	fut_p <- future(mean(rnorm(n)), seed = TRUE)
	fut_q <- future(mean(rgamma(n, shape = 1)), seed = TRUE)
	fut_s <- future(mean(rt(n, df = 3)), seed = TRUE)
        p <- value(fut_p)
        q <- value(fut_q)
        s <- value(fut_s)
})

system.time({
	p <- mean(rnorm(n))
	q <- mean(rgamma(n, shape = 1))
	s <- mean(rt(n, df = 3))
})
```

Question: Why might this not have shown a perfect three-fold speedup?

If we look at the future object (e.g., `fut_p`), we see that by default lazy evaluation is off
and that the code executes *asynchronously*. Let's consider these ideas in more detail. The future will
start being evaluated right away -- this is non-lazy evaluation. The future will execute asynchronously,
which means that the worker process will evaluate the future (in the background from the perspective of the
main process) while the main process can continue doing
other things, in particular interacting with the user. This asynchronous evaluation is also called
a *non-blocking* call because execution of the task in the worker process does not block things from happening in the main process.
However the call to `value()` is *synchronous* (and is a *blocking* call)  because it needs to returns a result, so control of the session
does not return to the user until the value is available (i.e., once the future is done being evaluated).

One can change the future to use lazy evaluation.

You could also have used tools like `foreach` and `future_lapply` here
as well, as we'll discuss next.

## Scenario 3: 10-fold CV and 10 or fewer cores

**Scenario**: You are running a prediction method on 10 cross-validation
folds.

This illustrates the idea of running some number of tasks using the
cores available on a single machine.

Here I'll illustrate parallel looping, using this simulated dataset and
basic use of `randomForest()`.


```r
library(randomForest)
```
```r
cvFit <- function(foldIdx, folds, Y, X, loadLib = FALSE) {
    if(loadLib)
        library(randomForest)
    out <- randomForest(y = Y[folds != foldIdx],
                        x = X[folds != foldIdx, ],
                        xtest = X[folds == foldIdx, ])
    return(out$test$predicted)
}

set.seed(23432)
## training set
n <- 1000
p <- 50
X <- matrix(rnorm(n*p), nrow = n, ncol = p)
colnames(X) <- paste("X", 1:p, sep="")
X <- data.frame(X)
Y <- X[, 1] + sqrt(abs(X[, 2] * X[, 3])) + X[, 2] - X[, 3] + rnorm(n)
nFolds <- 10
folds <- sample(rep(seq_len(nFolds), each = n/nFolds), replace = FALSE)
```

### Using a parallelized for loop with `foreach`

The foreach package provides a `foreach` command that allows you to do
this easily. foreach can use a variety of parallel "back-ends", of which
the future package is one back-end (via the `doFuture` package) that
provides a lot of flexibility in what computational resources are used
via `plan()`. For our purposes here, we'll focus on using shared memory
cores.

Note that `foreach` also provides functionality for collecting and
managing the results to avoid some of the bookkeeping you would need to
do if writing your own standard for loop. The result of `foreach` will
generally be a list, unless we request the results be combined in
different way, using the `.combine` argument.

```r
library(doFuture)
library(doRNG)
nCores <- 2
plan(multisession, workers = nCores)
registerDoFuture()

## Use of %dorng% from doRNG relates to parallel random number generation.
## We'll see more in Unit 10 (Simulation)
## If not using random number generation, people usually use %dopar%.

result <- foreach(i = seq_len(nFolds)) %dorng% {
	cat('Starting ', i, 'th job.\n', sep = '')
	output <- cvFit(i, folds, Y, X)
	cat('Finishing ', i, 'th job.\n', sep = '')
	output # this will become part of the out object
}

length(list)
result[[1]][1:5]
```

You can debug by running serially using `%do%` rather than `%dopar%` or
`%dorng%`. Note that you may need to load packages within the `foreach`
construct to ensure a package is available to all of the calculations.

### Alternatively using parallel apply statements

The `future.apply` package also has the ability to parallelize the
various `apply` functions (`apply`, `lapply`, `sapply`, etc.).

We'll consider parallel `future_lapply` and `future_sapply`.

```r
library(future.apply)
nCores <- 2
plan(multisession, workers = nCores)

input <- seq_len(nFolds)
input

system.time(
	res <- future_sapply(input, cvFit, folds, Y, X, future.seed = TRUE)
)
system.time(
	res2 <- sapply(input, cvFit, folds, Y, X)
)
```


Question: why are the user time (and system time) miniscule when using
`future_sapply`?

Now suppose you have 4 cores (and therefore won't have an equal number
of tasks per core). The approach in the next scenario should work
better.

## Scenario 4: parallelizing over prediction methods

**Scenario**: parallelizing over prediction methods or other cases where
execution time varies

If you need to parallelize over prediction methods or in other contexts
in which the computation time for the different tasks varies widely, you
want to avoid having the parallelization tool group the tasks in
advance, because some cores may finish a lot more quickly than others.
However, in many cases, this sort of grouping in advance (called
prescheduling or 'static' allocation of tasks to workers) is the
default. This is also the case with the future package -- the default is
to group the tasks in advance into "chunks", so that each worker
processes one future (one chunk), containing multiple tasks.

First we'll set up an artificial example with four slow tasks and 12
fast tasks and see the speed of running with the default of
prescheduling. Whether to preschedule or not is controlled by either the
`future.chunk.size` or `future.scheduling` arguments.

```r
## @knitr parallel-lapply-preschedule

library(future.apply)
nCores <- 4
plan(multisession, workers = nCores)

## specifically designed to be slow when have four cores and
## and use prescheduling, because
## the slow tasks all assigned to one worker
n <- rep(c(1e7, 1e5, 1e5, 1e5), each = 4)


fun <- function(i) {
    cat("working on ", i, "; ")
    mean(lgamma(exp(rnorm(n[i]))))
}

system.time(fun(1))
system.time(fun(5))

## Static allocation ##

## default - should do static allocation
system.time(
	res <- future_sapply(seq_along(n), fun, future.seed = TRUE)
)
## this is the default: 1 future (and therefore 4 tasks) per worker
system.time(
    res <- future_sapply(seq_along(n), fun, future.scheduling = 1,
                         future.seed = TRUE)
)
## equivalently, 4 tasks per chunk, 1 chunk (1 future) per worker
system.time(
    res <- future_sapply(seq_along(n), fun, future.chunk.size = 4,
                         future.seed = TRUE)
)
```

And here we prevent prescheduling. I find the `future.chunk.size`
argument easier to understand than the `future.scheduling` argument.
`future.chunk.size` says how many tasks to group together. So setting
equal to 1 means no grouping and therefore not using static allocation.

```r
## Dynamic allocation ##

## 1 task per chunk, 4 chunks (4 futures) per worker
system.time(
    res <- future_sapply(seq_along(n), fun, future.chunk.size = 1,
                         future.seed = TRUE)
)

## or, equivalently, we could specify future.scheduling = 4
```


## Scenario 5: 10-fold CV across multiple methods with many more than 10 cores

**Scenario**: You are running an ensemble prediction method such as
SuperLearner or Bayesian model averaging on 10 cross-validation folds,
with many statistical/machine learning methods.

Here you want to take advantage of all the cores you have available, so
you can't just parallelize over folds.

First we'll discuss how to deal with the nestedness of the problem and
then we'll talk about how to make use of many cores across multiple
nodes to parallelize over a large number of tasks.

### Scenario 5A: nested parallelization

One can always flatten the looping, either in a for loop or in similar
ways when using apply-style statements.

```
## original code: multiple loops
for(fold in 1:n) {
  for(method in 1:M) {
     ### code here
  }
}
## revised code: flatten the loops
output <- foreach(idx = 1:(n*M)) %dopar% {
   fold <- idx %/% M + 1
   method <- idx %% M + 1
   ### code here
}
```

Alternatively, `foreach` supports nested parallelization as follows:

```r
output <- foreach(fold = 1:n) %:%
  foreach(method = 1:M) %dopar% {
     ## code here
}
```

The `%:%` basically causes the nesting to be flattened, with `n*M` total
tasks run in parallel.

One can also use nested futures and the future package will just take
care of parallelizing across all the individual tasks. I won't go into
that here, but there is information in the tutorial.

### Scenario 5B: Parallelizing across multiple nodes

If you have access to multiple machines networked together, including a
Linux cluster, you can use the tools in the future package across
multiple nodes (either in a nested parallelization situation with many
total tasks or just when you have lots of unnested tasks to parallelize
over). Here we'll just illustrate how to use multiple nodes, but if you
had a nested parallelization case you can combine the ideas just above
with the use of multiple nodes.

Simply start R as you usually would.

Here we'll use `foreach` with the future-based `doFuture` backend.

```r
library(doFuture)
library(doRNG)

## Specify the machines you have access to and
##    number of cores to use on each:
machines = c(rep("radagast.berkeley.edu", 1),
    rep("gandalf.berkeley.edu", 1),
    rep("arwen.berkeley.edu", 2))

## On the SCF, Savio and other clusters using the SLURM scheduler,
## you can figure out the machine names and set up the input to
## the 'workers' argument of 'plan' like this:
## machines <- system('srun hostname', intern = TRUE)

plan(cluster, workers = machines)

registerDoFuture()

fun = function(i, n = 1e6)
  out = mean(rnorm(n))

nTasks <- 120

print(system.time(out <- foreach(i = 1:nTasks) %dorng% {
	outSub <- fun(i)
	outSub # this will become part of the out object
}))
```

To use `future_lapply`, set up the plan in similar fashion to above. You
can then do:

```r
system.time(
	res <- future_sapply(input, cvFit, folds, Y, X)
)

## And just to check we are actually using the various machines:
future_sapply(seq_along(workers), function(i) Sys.getenv('HOST'))
```


## Scenario 6: Stratified analysis on a very large dataset

**Scenario**: You are doing stratified analysis on a very large dataset
and want to avoid unnecessary copies.

In many of R's parallelization tools, if you try to parallelize this
case on a single node, you end up making copies of the original dataset,
which both takes up time and eats up memory.

Here when we use the `multisession` plan, we make copies for each
worker. And it's even worse if we force each task to be sent separately
so that there is one copy per task.

```r
do_analysis <- function(i) {
    return(mean(x))
}
x <- rnorm(5e7)  # our big "dataset"

options(future.globals.maxSize = 1e9)

plan(multisession, workers = 4) # new processes - copying!
system.time(tmp <- future_sapply(1:100, do_analysis))  # 9 sec.

## even worse if we dynamically allocate the tasks
system.time(tmp <- future_sapply(1:100, do_analysis,
                                 future.chunk.size = 1)) # 23 sec.
```

However, if you are working on a single machine (i.e., with shared
memory) you can avoid this by using parallelization strategies that fork
the original R process (i.e., make a copy of the process) and use the
big data objects in the global environment (yes, this violates the usual
programming best practices of not using global variables). The
`multicore` plan (not available on Windows) allows you to do this.

This creates R worker processes with the same state as the original R
process. Interestingly, this means that global variables in the forked
worker processes are just references to the objects in memory in the
original R process. So the additional processes do not use additional
memory for those objects (despite what is shown in `top`) and there is no
time involved in making copies. However, if you modify objects in the
worker processes then copies are made.

So here we avoid copying the original dataset.

```r
plan(multicore, workers = 4)  # forks (where supported, not Windows); no copying!
system.time(tmp <- future_sapply(1:100, do_analysis))  # 6.5 sec.
```


And here is code you can run to demonstrate that when using multicore,
no copies are made.

```r
x <- c(3.1, 2.5, 7.3)
lobstr::obj_addr(x)

future_sapply(1:2, function(i) {
    ## First, use the global 'x' just in case anything funny going on
    ## before object is used.
    y <- x[1]
    print(lobstr::obj_addr(x))
})
```


## Scenario 7: Simulation study with n=1000 replicates: parallel random number generation

We won't cover this in class and you don't need to worry about this at
the moment. Instead, I will mention the issue in the simulation unit
when we talk about random number generation.

In Section 5, we set the random number seed to different values for
random sample. One danger in setting the seed like that is that the
random numbers in the different samples could overlap somewhat. This is
probably somewhat unlikely if you are not generating a huge number of
random numbers, but it's unclear how safe it is.

The key thing when thinking about random numbers in a parallel context
is that you want to avoid having the same 'random' numbers occur on
multiple processes. On a computer, random numbers are not actually
random but are generated as a sequence of pseudo-random numbers designed
to mimic true random numbers. The sequence is finite (but very long) and
eventually repeats itself. When one sets a seed, one is choosing a
position in that sequence to start from. Subsequent random numbers are
based on that subsequence. All random numbers can be generated from one
or more random uniform numbers, so we can just think about a sequence of
values between 0 and 1.

**Scenario**: You are running a simulation study with n=1000 replicates.

Each replicate involves fitting two statistical/machine learning
methods.

Here, unless you really have access to multiple hundreds of cores, you
might as well just parallelize across replicates.

However, you need to think about random number generation. If you have
overlap in the random numbers the replications may not be fully
independent.

In R, the `rlecuyer` package deals with this. The L'Ecuyer algorithm has
a period of $2^{191}$, which it divides into subsequences of length
$2^{127}$.

Here's how you initialize independent sequences on different processes
when using the `future_lapply`. All you need to do is set the argument
`future.seed`.

```r
library(future.apply)

fun <- function(i) {
    mean(lgamma(exp(rnorm(100))))
}

nCores <- 4
plan(multisession, workers = nCores)

nSims <- 50
res <- future_sapply(seq_len(nSims), fun, future.seed = 1)
```


Dealing with parallel random number generation when using `foreach` or
`future()` is a bit more involved. See the tutorial.

---

[← alternatively, one can also control number of workers](06-alternatively-one-can-also-control-number-of-workers.md) · [Up: contents](index.md) · [6. Additional details and topics (optional) →](08-6-additional-details-and-topics-optional.md)
