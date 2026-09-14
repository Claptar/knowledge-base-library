---
title: sapply
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# sapply

**Source:** [`section/08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

future.apply::future_sapply(X = 2:4, FUN = function(x){base^x})
```

Matrix output with names (this is why we need the `as.character`):

```r
future.apply::future_sapply(X = as.character(2:4), FUN = function(x){
  x <- as.numeric(x)
  c("base" = base^x, "self" = x^x)
})


```


## The `foreach` Package via `doFuture`

The idea behind the `foreach` package is to create 'a hybrid of the standard for
loop and lapply function' and its ease of use has made it rather popular. The set-up
is slightly different, you need "register" the the plan as below:

```r
#library(foreach)
library(doFuture)

nCores = 2
plan(strategy = multiprocess, workers = nCores)
registerDoFuture()

```

The `foreach` function can be viewed as being a more controlled version of the
`future_sapply` that allows combining the results into a suitable format. By specifying
the `.combine` argument we can choose how to combine our results, below is a vector,
matrix, and a list example:

```r
foreach(exponent = 2:4,
        .combine = c) %dopar% {
          base^exponent
        }
```

Now using `rbind`.

```r
foreach(exponent = 2:4,
        .combine = rbind)  %dopar% {
            base^exponent
        }
```


Now a list.

```r
foreach(exponent = 2:4,
        .combine = list,
        .multicombine = TRUE)  %dopar% {
          base^exponent
        }
```

Note that the last is the default and can be achieved without any tweaking, just
`foreach(exponent = 2:4) %dopar%`. In the example it is worth noting the `.multicombine`
argument that is needed to avoid a nested list. The nesting occurs due to the
sequential `.combine` function calls, i.e. `list(list(result.1, result.2), result.3)`:

```r
foreach(exponent = 2:4,
        .combine = list,
        .multicombine = FALSE)  %dopar% {
          base^exponent
        }
```


### Variable Scope

The variable scope constraints are slightly different for the `foreach` package.
Variable within the same local environment are by default available:

```r
foreach(exponent = 2:4,
        .combine = c)  %dopar%
  base^exponent
```

While variables from a parent environment should not be available, i.e. the
following will throw an error using a different parallel backend. However, `future`
ensures that all globals necessary inside the function are available.

```r
test <- function() {
  foreach(exponent = 2:4,
          .combine = c)  %dopar%  {
           base^exponent
          }
}

test()
```

A nice feature is that you can use the `.export` option within `foreach` to ensure
variables are exported to child processes. Note that as it is part of the parallel
call it will have the latest version of the variable, i.e. the following change
in "base" will work:

```r
base <- 4

test <- function () {
  foreach(exponent = 2:4,
          .combine = c,
          .export = "base")  %dopar%  {
            base^exponent
          }
}

test()
```

Similarly you can load packages with the .packages option, e.g. `.packages = c("rms", "mice")`.
I strongly recommend always exporting the variables you need as it limits issues
that arise when encapsulating the code within functions.

Now move on to `scfOverview.pdf`

---

[← remember, the globals thing is not necessary](08-remember-the-globals-thing-is-not-necessary.md) · [Up: contents](index.md)
