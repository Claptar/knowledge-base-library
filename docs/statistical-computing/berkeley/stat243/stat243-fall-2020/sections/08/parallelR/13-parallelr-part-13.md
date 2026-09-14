---
title: ParallelR Part 13 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 13 —

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##[[2]]
##[1]81
```

### **Variable Scope**

The variable scope constraints are slightly different for the `foreach` package. Variable within the same local environment are by default available:

```
foreach(exponent=2:4,
.combine=c)%dopar%
base^exponent
```

```
##[1]92781
```

While variables from a parent environment should not be available, i.e. the following will throw an error using a different parallel backend. However, `future` ensures that all globals necessary inside the function are available.

```
test<-function(){
foreach(exponent=2:4,
.combine=c)%dopar%{
base^exponent
}
}
```

5

```
test()
```

```
##[1]92781
```

A nice feature is that you can use the `.export` option within `foreach` to ensure variables are exported to child processes. Note that as it is part of the parallel call it will have the latest version of the variable, i.e. the following change in “base” will work: `base <- 4 test <-` **`function`** `() {` **`foreach`** `(exponent = 2` **`:`** `4, .combine = c, .export = "base")` **`%dopar%`** `{ base` **`^`** `exponent } }` **`test`** `()`

```
##[1]1664256
```

Similarly you can load packages with the .packages option, e.g. `.packages = c("rms", "mice")` . I strongly recommend always exporting the variables you need as it limits issues that arise when encapsulating the code within functions.

Now move on to `scfOverview.pdf`

6

---

[← ParallelR Part 12 —](12-parallelr-part-12.md) · [Up: contents](index.md)
