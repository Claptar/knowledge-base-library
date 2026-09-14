---
title: future Package
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# future Package

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The future package attempts to provide a simple and uniform framework for evaluating expressions on various resources.

```
library(future)
```

```
v%<-%{
```

```
cat("Helloworld!\n")
3.14
```

```
}
```

```
v
```

```
##Helloworld!
```

### `## [1] 3.14`

Notice, the definition is evaluated when the variable is called, instead of when the variable is defined. There are several methods for controlling how futures are evaluated. The types of futures are listed in 1, and implemented as `plan()` s.

Futures can also be evaluated _asynchronously_ in a different R process by setting the `plan()` to one of the _asynchronous_ options.

```
plan(strategy=multiprocess)
```

```
##Warning:[ONE-TIMEWARNING]Forkedprocessing('multicore')isdisabled
```

```
##infuture(>=1.13.0)whenrunningRfromRStudio,becauseitis
```

```
##consideredunstable.Becauseofthis,plan("multicore")willfall
```

```
##backtoplan("sequential"),andplan("multiprocess")willfallbackto
```

```
##plan("multisession")-notplan("multicore")asinthepast.Formoredetails,
```

```
##howtocontrolforkedprocessingornot,andhowtosilencethiswarningin
```

```
##futureRsessions,see?future::supportsMulticore
```

```
w%<-%{
cat("Helloworld!\n")
3.14
}
```

```
w
```

```
##Helloworld!
```

```
##[1]3.14
```

2

The `future` package is extended by the `future.apply` package, which implements the _apply_ family of functions from base `R` .

```
library(future.apply)
#setevaluationplan
#explicitaboutnamespacesoyouknowwherethesefunctionsarecomingfrom.
nCores=2
future::plan(strategy=multiprocess,workers=nCores)
future.apply::future_sapply(X=2:4,FUN=function(exponent){2^exponent})
```

```
##[1]4816
```

### **Variable Scope**

On Mac/Linux, you can set the `plan` to be explicitly `multicore` (this is what `multiprocess` defaults to on Mac/Linux). This creates forked processes, which use the current environmental variables. On Windows, you can set `multisession` , which is the Windows default of `multiprocess` , which creates background `R` sessions. This requires copying all necessary variables to the processes.

The `future` package attempts to handle most of this for you, using the globals package. See below, where the `plan` is explicitly `multisession` , meaning that it should fail because I didn’t explicitly copy `base` to each process. However, `future` identifies that `base` is necessary and supplies it to each child process. It provides a similar service for functions/objects in packages, except that packages are attached to the child process, so no copying is necessary. See the vignette on globals for the `future` package. `nCores = 2 future` **`::plan`** `(strategy = multisession, workers = nCores) base = 2`

```
#shouldfail,butdoesn't
future.apply::future_sapply(X=2:4,FUN=function(exponent){base^exponent})
```

```
##[1]4816
#saferway
globals="base"
future.apply::future_sapply(X=2:4,FUN=function(exponent){base^exponent})
```

```
##[1]4816
```

**Using** **`future_sapply`**

(I DO NOT RECOMMEND SAPPLY STATEMENTS) Sometimes, we only want a simple return value, such as a vector/matrix. Here are a few examples using the `future_sapply` function. _`# setup plan`_ `nCores = 2 future` **`::plan`** `(strategy = multisession, workers = nCores)` _`# setup base and name globals # remember, the globals thing is not necessary`_ `base = 3 globals = "base"`

3

```
#sapply
future.apply::future_sapply(X=2:4,FUN=function(x){base^x})
```

```
##[1]92781
```

Matrix output with names (this is why we need the `as.character` ): `future.apply` **`::future_sapply`** `(X =` **`as.character`** `(2` **`:`** `4), FUN =` **`function`** `(x){ x <-` **`as.numeric`** `(x)` **`c`** `("base" = base` **`^`** `x, "self" = x` **`^`** `x) }) ## 2 3 4 ## base 9 27 81 ## self 4 27 256`

---

[← ParallelR Part 07 —](07-parallelr-part-07.md) · [Up: contents](index.md) · [The foreach Package via doFuture →](09-the-foreach-package-via-dofuture.md)
