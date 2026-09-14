---
title: Finish
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Finish

**Source:** [`lab/S08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

stopCluster(cl)
```

### Using `parSapply`

Sometimes we only want to return a simple value and directly get it processed as a vector/matrix.

```r
cl<-makeCluster(no_cores)
clusterExport(cl, "base")
parSapply(cl, 2:4, function(exponent) base^exponent)
stopCluster(cl)
```

Matrix output with names (this is why we need the `as.character`):

```r
cl<-makeCluster(no_cores)
clusterExport(cl, "base")
parSapply(cl, as.character(2:4),
          function(exponent){
            x <- as.numeric(exponent)
            c(base = base^x, self = x^x)
          })
stopCluster(cl)
```


## The `foreach` Package

The idea behind the `foreach` package is to create 'a hybrid of the standard for loop and lapply function' and its ease of use has made it rather popular. The set-up is slightly different, you need "register" the cluster as below:

```r
library(foreach)
library(doParallel)

cl<-makeCluster(no_cores)
registerDoParallel(cl)
stopCluster(cl)
```
Note that you can change the last two lines to:

```r
registerDoParallel(no_cores)
```
But then you need to remember to instead of stopCluster() at the end do:
```r
stopImplicitCluster()
```

In fact for problem 4 on PS6, you should use `registerDoParallel(no_cores)` because using *makeCluster* causes more memory to be used for reasons we need to look into.

The `foreach` function can be viewed as being a more controlled version of the `parSapply` that allows combining the results into a suitable format. By specifying the `.combine` argument we can choose how to combine our results, below is a vector, matrix, and a list example:

```r
base <- 2
cl<-makeCluster(no_cores)
registerDoParallel(cl)
foreach(exponent = 2:4,
        .combine = c)  %dopar%
  base^exponent
stopCluster(cl)
```
Now using `rbind`

```r
base <- 2
cl<-makeCluster(no_cores)
registerDoParallel(cl)
foreach(exponent = 2:4,
        .combine = rbind)  %dopar%
  base^exponent
stopCluster(cl)
```
Now a list,
```r
base <- 2
cl<-makeCluster(no_cores)
registerDoParallel(cl)
foreach(exponent = 2:4,
        .combine = list,
        .multicombine = TRUE)  %dopar%
  base^exponent
stopCluster(cl)
```

Note that the last is the default and can be achieved without any tweaking, just `foreach(exponent = 2:4) %dopar%`. In the example it is worth noting the `.multicombine` argument that is needed to avoid a nested list. The nesting occurs due to the sequential `.combine` function calls, i.e. `list(list(result.1, result.2), result.3)`:

```r
base <- 2
cl<-makeCluster(no_cores)
registerDoParallel(cl)
foreach(exponent = 2:4,
        .combine = list,
        .multicombine = FALSE)  %dopar%
  base^exponent
stopCluster(cl)
```

### Variable Scope

The variable scope constraints are slightly different for the `foreach` package. Variable within the same local environment are by default available:

```r
base <- 2
cl<-makeCluster(2)
registerDoParallel(cl)
foreach(exponent = 2:4,
        .combine = c)  %dopar%
  base^exponent
stopCluster(cl)
```

While variables from a parent environment will not be available, i.e. the following will throw an error:

```r
test <- function (exponent) {
  foreach(exponent = 2:4,
          .combine = c)  %dopar%
    base^exponent
}
cl<-makeCluster(2)
registerDoParallel(cl)
test()
stopCluster(cl)
```

A nice feature is that you can use the `.export` option instead of the `clusterExport`. Note that as it is part of the parallel call it will have the latest version of the variable, i.e. the following change in "base" will work:

```r
base <- 2
cl<-makeCluster(2)
registerDoParallel(cl)

base <- 4
test <- function (exponent) {
  foreach(exponent = 2:4,
          .combine = c,
          .export = "base")  %dopar%
    base^exponent
}
test()

stopCluster(cl)
```

Similarly you can load packages with the .packages option, e.g. `.packages = c("rms", "mice")`. I strongly recommend always exporting the variables you need as it limits issues that arise when encapsulating the code within functions.

## Memory Handling

Unless you are using multiple computers or Windows or planning on sharing your code with someone using a Windows machine, you should try to use `FORK` option. It is leaner on the memory usage by linking to the same address space. Below you can see that the memory address space for variables exported to PSOCK are not the same as the original:

```r
library(pryr, quietly = TRUE) # Used for memory analyses
a <- "o"
cl<-makeCluster(no_cores)
clusterExport(cl, "a")
clusterEvalQ(cl, library(pryr))

parSapply(cl, X = 1:10, function(x) {address(a)}) == address(a)
stopCluster(cl)
```
While they are for FORK clusters:

```r
cl<-makeCluster(no_cores, type="FORK")
parSapply(cl, X = 1:10, function(x) address(a)) == address(a)
stopCluster(cl)
```
Now move on to `intro.md`

---

[← Run](04-run.md) · [Up: contents](index.md)
