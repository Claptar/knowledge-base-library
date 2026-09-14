---
title: lapply Refresher
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# lapply Refresher

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

`lapply` takes one parameter (a vector/list), feeds that variable into the function, and returns a list:

```
lapply(1:3,function(x)c(x,x^2,x^3))
```

```
##[[1]]
##[1]111

---

[← 14 October, 2020](02-14-october-2020.md) · [Up: contents](index.md) · [ParallelR Part 04 — →](04-parallelr-part-04.md)
