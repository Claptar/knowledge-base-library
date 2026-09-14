---
title: The foreach Package via doFuture
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The foreach Package via doFuture

**Source:** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The idea behind the `foreach` package is to create ‘a hybrid of the standard for loop and lapply function’ and its ease of use has made it rather popular. The set-up is slightly different, you need “register” the the plan as below:

```
#library(foreach)
library(doFuture)
```

```
##Loadingrequiredpackage:foreach
```

```
nCores=2
plan(strategy=multiprocess,workers=nCores)
registerDoFuture()
```

The `foreach` function can be viewed as being a more controlled version of the `future_sapply` that allows combining the results into a suitable format. By specifying the `.combine` argument we can choose how to combine our results, below is a vector, matrix, and a list example:

4

```
foreach(exponent=2:4,
.combine=c)%dopar%{
baseˆexponent
}
```

`## [1] 9 27 81` Now using `rbind` . `foreach(exponent = 2:4, .combine = rbind) %dopar% { baseˆexponent } ## [,1] ## result.1 9 ## result.2 27 ## result.3 81` Now a list. `foreach(exponent = 2:4, .combine = list, .multicombine = TRUE) %dopar% { baseˆexponent }`

```
##[[1]]
##[1]9

---

[← future Package](07-future-package.md) · [Up: contents](index.md) · [ParallelR Part 09 — →](09-parallelr-part-09.md)
