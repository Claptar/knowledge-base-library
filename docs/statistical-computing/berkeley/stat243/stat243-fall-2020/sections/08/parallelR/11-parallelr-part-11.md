---
title: ParallelR Part 11 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 11 —

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##[1]81
```

Note that the last is the default and can be achieved without any tweaking, just `foreach(exponent = 2:4) %dopar%` . In the example it is worth noting the `.multicombine` argument that is needed to avoid a nested list. The nesting occurs due to the sequential `.combine` function calls, i.e. `list(list(result.1, result.2), result.3)` :

```
foreach(exponent=2:4,
.combine=list,
.multicombine=FALSE)%dopar%{
base^exponent
}
##[[1]]
##[[1]][[1]]
##[1]9

---

[← ParallelR Part 10 —](10-parallelr-part-10.md) · [Up: contents](index.md) · [ParallelR Part 12 — →](12-parallelr-part-12.md)
