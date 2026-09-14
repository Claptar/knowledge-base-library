---
title: ParallelR Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 05 —

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##[1]3927
```

You can feed it additional values by adding named parameters:

```
lapply(1:3/3,round,digits=3)
```

```
##[[1]]
##[1]0.333

---

[← ParallelR Part 04 —](04-parallelr-part-04.md) · [Up: contents](index.md) · [ParallelR Part 06 — →](06-parallelr-part-06.md)
