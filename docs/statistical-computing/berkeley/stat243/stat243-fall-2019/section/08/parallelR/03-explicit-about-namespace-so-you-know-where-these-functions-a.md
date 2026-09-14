---
title: explicit about namespace so you know where these functions are coming from.
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# explicit about namespace so you know where these functions are coming from.

**Source:** [`section/08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

nCores = 2
future::plan(strategy = multiprocess, workers = nCores)

future.apply::future_sapply(X = 2:4, FUN = function(exponent){2^exponent})


```


### Variable Scope

On Mac/Linux, you can set the `plan` to be explicitly `multicore` (this is what
`multiprocess` defaults to on Mac/Linux). This creates forked processes, which use
the current environmental variables. On Windows, you can set `multisession`, which is
the Windows default of `multiprocess`, which creates background `R` sessions. This
requires copying all necessary variables to the processes.

The `future` package attempts to handle most of this for you, using the [globals](https://cran.r-project.org/web/packages/globals/index.html)
package. See below, where the `plan` is explicitly `multisession`, meaning that it
should fail because I didn't explicitly copy `base` to each process. However, `future`
identifies that `base` is necessary and supplies it to each child process.
It provides a similar service for functions/objects in packages, except that packages
are attached to the child process, so no copying is necessary. See the [vignette](https://cran.r-project.org/web/packages/future/vignettes/future-4-issues.html)
on globals for the `future` package.

```r
nCores = 2
future::plan(strategy = multisession, workers = nCores)
base = 2

---

[← set evaluation plan](02-set-evaluation-plan.md) · [Up: contents](index.md) · [should fail, but doesn't →](04-should-fail-but-doesn-t.md)
