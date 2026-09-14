---
title: alternatively, one can also control number of workers
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# alternatively, one can also control number of workers

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

plan(multiprocess, workers = 4)
```

This table gives an overview of the different plans.

|       Type     |                 Description                |  Multi-node |   Copies of objects made?   |
|  --------------| -------------------------------------------| ------------| ----------------------------|
|   multisession |  uses additional R sessions as the workers |      no     |             yes |
|    multicore   |   uses forked R processes as the workers   |      no     |  not if object not modified |
|     cluster    |     uses R sessions on other machine(s)    |     yes     |             yes |

## Accessing variables and workers in the worker processes

The future package usually does a good job of identifying the packages and (global) variables
you use in your parallelized code and loading those packages on the workers and copying necessary variables to the workers.
It uses the `globals` package to do this.

Here's a toy example that shows that `n` and `MASS::geyser` are automatically available in the worker processes.

```r
library(future)
library(future.apply)

plan(multisession)

library(MASS)
n <- nrow(geyser)

myfun <- function(idx) {
   # geyser is in MASS package
   return(sum(geyser$duration) / n)
}

future_sapply(1:5, myfun)
```

In other contexts in R (or other languages) you may need to explicitly copy objects to the workers (or load packages on the workers). This is sometimes called *exporting* variables.

---

[← 7. Introduction to R's future package (optional)](11-7-introduction-to-r-s-future-package-optional.md) · [Up: contents](index.md)
