---
title: ParallelR Part 10 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 10 —

**Source:** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

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
baseˆexponent
}
```

```
##[[1]]
##[[1]][[1]]
##[1]9

---

[← ParallelR Part 09 —](09-parallelr-part-09.md) · [Up: contents](index.md) · [ParallelR Part 11 — →](11-parallelr-part-11.md)
