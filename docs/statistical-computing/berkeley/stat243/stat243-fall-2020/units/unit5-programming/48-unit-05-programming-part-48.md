---
title: Unit 05 — programming Part 48 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 48 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.5 Delayed copying (copy-on-change)**

Next we’ll see that something like lazy evaluation occurs outside of functions as well with some functionality called _delayed copying_ or _copy-on-change_ . When we discussed R as being call-byvalue in Section 6.5, copy-on-change was one of the reasons that copies of arguments are not always made. (But we didn’t talk about it at that time.)

Let’s see what goes on within a function in terms of memory use in different situations. Ignore the _gc()_ results in the pdf, as we’ll start R fresh to get a clean view of memory use during the class demo.

**rm** (y) **gc** (reset = TRUE) ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2022014 108 3.81e+06 203 2022014 108 ## Vcells 53675408 410 1.42e+08 1087 53675408 410 f <- **function** (x){ **print** ( **gc** ()) **.Internal** ( **inspect** (x)) **return** (x) } y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2021999 108 3.81e+06 203 2040200 109 ## Vcells 63675417 486 1.42e+08 1087 63706618 486 **.Internal** ( **inspect** (y))

91

---

[← -4.06 kB length ( serialize (mySeq, NULL )) ## [1] 133](47--4-06-kb-length-serialize-myseq-null-1-133.md) · [Up: contents](index.md) · [@7f02491a0010 14 REALSXP g1c7 [MARK,NAM(7)] (len=10000000, tl=0) →](49-7f02491a0010-14-realsxp-g1c7-mark-nam-7-len-10000000-tl-0.md)
