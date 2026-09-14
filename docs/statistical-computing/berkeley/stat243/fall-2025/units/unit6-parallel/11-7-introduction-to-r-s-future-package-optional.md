---
title: 7. Introduction to R's future package (optional)
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Introduction to R's future package (optional)

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Before we illustrate implementation of various kinds of parallelization,
I'll give an overview of the `future` package, which we'll use for many
of the implementations. The future package has been developed over the
last few years and provides some nice functionality that is easier to
use and more cohesive than the various other approaches to
parallelization in R.

Other approaches include `parallel::parLapply`, `parallel::mclapply`,
the use of `foreach` without `future`, and the `partools` package.
The `partools` package is interesting. It tries to take the parts of
Spark/Hadoop most relevant for statistics-related work -- a distributed
file system and distributed data objects -- and discard the parts that
are a pain/not useful -- fault tolerance when using many, many
nodes/machines.

## Overview: Futures and the R future package

What is a *future*? It's basically a flag used to tag a given operation
such that when and where that operation is carried out is controlled at
a higher level. If there are multiple operations tagged then this allows
for parallelization across those operations.

According to Henrik Bengtsson (the `future` package developer) and those
who developed the concept:

-   a future is an abstraction for a value that will be available later
-   the value is the result of an evaluated expression
-   the state of a future is either unresolved or resolved

Why use futures? The `future` package allows one to write one's
computational code without hard-coding whether or how parallelization
would be done. Instead one writes the code in a generic way and at the
beginning of one's code sets the 'plan' for how the parallel computation
should be done given the computational resources available. Simply
changing the 'plan' changes how parallelization is done for any given
run of the code.

More concisely, the key ideas are:

-   Separate what to parallelize from how and where the parallelization
    is actually carried out.
-   Different users can run the same code on different computational
    resources (without touching the actual code that does the
    computation).

## Overview of parallel backends

One uses `plan()` to control how parallelization is done, including what
machine(s) to use and how many cores on each machine to use.

For example,

```r
#| eval: false
plan(multiprocess)
## spreads work across multiple cores

---

[← 6. Additional details and topics (optional)](10-6-additional-details-and-topics-optional.md) · [Up: contents](index.md) · [alternatively, one can also control number of workers →](12-alternatively-one-can-also-control-number-of-workers.md)
