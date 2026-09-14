---
title: Unit 04 — programming Part 43 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 43 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.6 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ . When we discussed R as being call-byvalue in Section 6.4, copy-on-change was one of the reasons that copies of arguments are not always made.

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

f <- **function** (x){ **print** ( **gc** ()) z <- x[1] **.Internal** ( **inspect** (x)) **return** (x) } y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 781779 41.8 1.44e+06 77.1 1.44e+06 77.1

80

---

[← Unit 04 — programming Part 42 —](42-unit-04-programming-part-42.md) · [Up: contents](index.md) · [Vcells 51419471 392.3 1.12e+08 855.5 1.31e+08 1002.4 →](44-vcells-51419471-392-3-1-12e-08-855-5-1-31e-08-1002-4.md)
