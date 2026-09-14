---
title: Unit 05 — programming Part 46 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 46 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The _pryr_ package provides _address()_ or _inspect()_ as an alternative to _.Internal(inspect())_ though as we see here it doesn’t give us the richness of information about complicated objects that _inspect()_ does.

86

obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **address** (x) _# from pryr_ ## [1] "0x5639aeaec6a8" **address** (obj) ## [1] "0x5639b39b54d8" **address** (obj$a) _# doesn't work_

**## Error: x must be the name of an object**

Apparently there is a memory profiler in R, _Rprofmem_ , but it needs to be enabled when R is compiled (i.e., installed on the machine), because it slows R down even when not used. So I’ve never gotten to the point of playing around with it.

**Faster representations of sequences** As mentioned above, as of R 3.5.0, 1:n is not stored in memory as a vector of length _n_ , but rather is represented by the first and last value in the sequence. However, some of the functions we use to determine object size don’t give us the right answer in this case.

**library** (microbenchmark) n <- 1e6 **microbenchmark** (tmp <- 1:n) ## Unit: nanoseconds ## expr min lq mean median uq max neval ## tmp <- 1:n 224 229 360 234 284 10462 100 **object.size** (tmp) _# incorrect as of R 3.5_ ## 4000048 bytes **object_size** (tmp) _# incorrect as of R 3.5_ ## 4 MB **mem_change** (mySeq <- 1:n)

87

---

[← Unit 05 — programming Part 45 —](45-unit-05-programming-part-45.md) · [Up: contents](index.md) · [-4.06 kB length ( serialize (mySeq, NULL )) ## [1] 133 →](47--4-06-kb-length-serialize-myseq-null-1-133.md)
