---
title: Unit 05 — programming Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 19 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

25

|##|[13] summary.glm|
|---|---|
|##|[14] summary.infl*|
|##|[15] summary.lm|
|##|[16] summary.loess*|
|##|[17] summary.manova|
|##|[18] summary.matrix|
|##|[19] summary.mlm*|
|##|[20] summary.nls*|
|##|[21] summary.packageStatus*|
|##|[22] summary.POSIXct|
|##|[23] summary.POSIXlt|
|##|[24] summary.ppr*|
|##|[25] summary.prcomp*|
|##|[26] summary.princomp*|
|##|[27] summary.proc_time|
|##|[28] summary.rlang_error*|
|##|[29] summary.rlang_trace*|
|##|[30] summary.srcfile|
|##|[31] summary.srcref|
|##|[32] summary.stepfun|
|##|[33] summary.stl*|
|##|[34] summary.table|
|##|[35] summary.tukeysmooth*|
|##|[36] summary.vctrs_sclr*|
|##|[37] summary.vctrs_vctr*|
|##|[38] summary.warnings|
|##|see '?methods' for accessing help and source code|


In many cases there will be a default method (here, _summary.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

26

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _bear_ class. In reality, we’d write either _summary.bear()_ or _print.bear()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog)

---

[← Unit 05 — programming Part 18 —](18-unit-05-programming-part-18.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](20-bear-of-age-20-whose-name-is-yogi-the-bear.md)
