---
title: lapply Refresher
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# lapply Refresher

**Source:** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

`lapply` takes one parameter (a vector/list), feeds that variable into the function, and returns a list:

```
lapply(1:3,function(x)c(x,xˆ2,xˆ3))
```

```
##[[1]]
##[1]111

---

[← Andrew Vaughn](01-andrew-vaughn.md) · [Up: contents](index.md) · [ParallelR Part 03 — →](03-parallelr-part-03.md)
