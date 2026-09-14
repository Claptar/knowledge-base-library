---
title: ParallelR Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/08/parallelR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ParallelR Part 07 —

**Source:** [`sections/08/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/08/parallelR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

[← ParallelR Part 06 —](06-parallelr-part-06.md) · [Up: contents](index.md) · [future Package →](08-future-package.md)
