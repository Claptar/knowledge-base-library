---
title: 1. Some scenarios for parallelization
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Some scenarios for parallelization

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

-   You need to fit a single statistical/machine learning model, such as
    a random forest or regression model, to your data.
-   You need to fit three different statistical/machine learning models
    to your data.
-   You are running a prediction method on 10 cross-validation folds,
    possibly using multiple statistical/machine learning models to do
    prediction.
-   You are running an ensemble prediction method such as *SuperLearner*
    or *Bayesian model averaging* over 10 cross-validation folds, with
    30 statistical/machine learning methods used for each fold.
-   You are running stratified analyses on a very large dataset (e.g.,
    running regression models once for each subgroup within a dataset).
-   You are running a simulation study with n=1000 replicates. Each
    replicate involves fitting 10 statistical/machine learning methods.

Given you are in such a situation, can you do things in parallel? Can
you do it on your laptop or a single computer? Will it be useful (i.e.,
faster or provide access to sufficient memory) to use multiple
computers, such as multiple nodes in a Linux cluster?

All of the functionality discussed in this Unit applies ONLY if the
iterations/loops of your calculations can be done completely separately
and do not depend on one another; i.e., you can do the computation as
separate processes without communication between the processes. This
scenario is called an *embarrassingly parallel* computation.

## Embarrassingly parallel (EP) problems

An EP problem is one that can be solved by doing independent
computations in separate processes without communication between the
processes. You can get the answer by doing separate tasks and then
collecting the results. Examples in statistics include

1.  simulations with many independent replicates
2.  bootstrapping
3.  stratified analyses
4.  random forests
5.  cross-validation.

The standard setup is that we have the same code running on different
datasets. (Note that different processes may need different random
number streams, as we will discuss in the Simulation Unit.)

To do parallel processing in this context, you need to have control of
multiple processes. Note that on a shared system with
queueing/scheduling software set up, this will generally mean requesting
access to a certain number of processors and then running your job in
such a way that you use multiple processors.

In general, except for some modest overhead, an EP problem can ideally
be solved with $1/p$ the amount of time for the non-parallel
implementation, given $p$ CPUs. This gives us a speedup of $p$, which is
called linear speedup (basically anytime the speedup is of the form $kp$
for some constant $k$).

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. Overview of parallel processing →](03-2-overview-of-parallel-processing.md)
