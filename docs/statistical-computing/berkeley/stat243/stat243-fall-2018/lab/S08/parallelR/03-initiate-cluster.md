---
title: Initiate cluster
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Initiate cluster

**Source:** [`lab/S08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

cl <- makeCluster(no_cores)
```

Now we just call the parallel version of `lapply`, `parLapply`:

```r
parLapply(cl, 2:4, function(exponent) 2^exponent)
```

Once we are done we need to close the cluster so that resources such as memory are returned to the operating system.

```r
stopCluster(cl)
```

### Variable Scope

On Mac/Linux you have the option of using `makeCluster(no_core, type="FORK")` that automatically contains all environment variables (more details on this below). On Windows you have to use the Parallel Socket Cluster (PSOCK) that starts out with only the base packages loaded (note that PSOCK is default on all systems). You should therefore always specify exactly what variables and libraries that you need for the parallel function to work, e.g. the following fails:

```r
cl<-makeCluster(no_cores)
base <- 2

parLapply(cl,
          2:4,
          function(exponent)
            base^exponent)

stopCluster(cl)
```


This one is correct:
```r
cl<-makeCluster(no_cores)

base <- 2
clusterExport(cl, "base")
parLapply(cl,
          2:4,
          function(exponent)
            base^exponent)

stopCluster(cl)
```

Note that you need the `clusterExport(cl, "base")` in order for the function to see the base variable. If you are using some special packages you will similarly need to load those through `clusterEvalQ`, e.g. `clusterEvalQ(cl, library(rms))` to load the `rms` package. Note that any changes to the variable after clusterExport are ignored:

```r
cl<-makeCluster(no_cores)
clusterExport(cl, "base")
base <- 4

---

[← Calculate the number of cores](02-calculate-the-number-of-cores.md) · [Up: contents](index.md) · [Run →](04-run.md)
