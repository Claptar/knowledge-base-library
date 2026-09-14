---
title: ParallelR Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 06 —

**Source:** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##[1]1
```

These tasks are embarrassingly parallel as the elements are calculated independently, i.e. second element is independent of the result from the first element. After learning to code using `lapply` parallelizing your code is simple.

1

||Table 1: Future Resolution Strategies|
|---|---|
|**Name**|**OS**<br>**Description**|
|_synchronous_|_non-parallel_|
|sequential|all<br>sequentially in current R process|
|transparent|all<br>as sequential w/ early signaling and w/out local|
|_asynchronous_|_parallel_|
|multiprocess|all<br>multicore if possible, multisession otherwise|
|multisession|all<br>background R sessions (current machine)|
|multicore|not Windows/Rstudio<br>forked process|
|cluster|all<br>external R session, current or local machines|
|remote|all<br>remote R sessions|

---

[← ParallelR Part 05 —](05-parallelr-part-05.md) · [Up: contents](index.md) · [future Package →](07-future-package.md)
