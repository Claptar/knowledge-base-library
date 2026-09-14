---
title: ParallelR Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 04 —

**Source:** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

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

[← ParallelR Part 03 —](03-parallelr-part-03.md) · [Up: contents](index.md) · [ParallelR Part 05 — →](05-parallelr-part-05.md)
