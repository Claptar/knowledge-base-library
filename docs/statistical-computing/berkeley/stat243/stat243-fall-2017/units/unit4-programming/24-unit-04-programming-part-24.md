---
title: Unit 04 — programming Part 24 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 24 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

23

|##|[15] summary.lm|
|---|---|
|##|[16] summary.loess*|
|##|[17] summary.manova|
|##|[18] summary.matrix|
|##|[19] summary.mKrig|
|##|[20] summary.mlm*|
|##|[21] summary.ncdf|
|##|[22] summary.nls*|
|##|[23] summary.packageStatus*|
|##|[24] summary.PDF_Dictionary*|
|##|[25] summary.PDF_Stream*|
|##|[26] summary.POSIXct|
|##|[27] summary.POSIXlt|
|##|[28] summary.ppr*|
|##|[29] summary.prcomp*|
|##|[30] summary.princomp*|
|##|[31] summary.proc_time|
|##|[32] summary.qsreg|
|##|[33] summary.spam|
|##|[34] summary.spam.chol.NgPeyton|
|##|[35] summary,spam.chol.NgPeyton-method|
|##|[36] summary,spam-method|
|##|[37] summary.spatial.design|
|##|[38] summary.spatialProcess|
|##|[39] summary.srcfile|
|##|[40] summary.srcref|
|##|[41] summary.sreg|
|##|[42] summary.stepfun|
|##|[43] summary.stl*|
|##|[44] summary.table|
|##|[45] summary.tukeysmooth*|
|##|see '?methods' for accessing help and source code|


In many cases there will be a default method (here, _mean.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

24

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _bear_ class. In reality, we’d write either _summary.bear()_ or _print.bear()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog)

---

[← Unit 04 — programming Part 23 —](23-unit-04-programming-part-23.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](25-bear-of-age-20-whose-name-is-yogi-the-bear.md)
