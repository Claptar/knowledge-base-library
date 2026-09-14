---
title: Unit 05 — programming Part 55 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 55 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**.Internal** ( **inspect** (y)) ## @7ff6a0d8b010 14 REALSXP g1c7 [MARK,NAM(7)] (len=10000000, tl=0) **.Internal** ( **inspect** (out)) ## @7ff6a0d8b010 14 REALSXP g1c7 [MARK,NAM(7)] (len=10000000, tl=0)

Note that in this example, if you use _address()_ instead of _.Internal(inspect())_ it’s not really clear what is going on.

In fact, this occurs outside function calls as well. Copies of objects are not made until one of the objects is actually modified. Initially, the copy points to the same memory location as the

89

original object.

y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2038003 109 3.79e+06 202 3.22e+06 172 ## Vcells 63687485 486 1.14e+08 870 1.32e+08 1006 **address** (y) ## [1] "0x7ff68de5c010" x <- y **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2038021 109 3.79e+06 202 3.22e+06 172 ## Vcells 53687520 410 1.14e+08 870 1.32e+08 1006 **object_size** (x, y) _# from pryr_ ## 80 MB **address** (x) ## [1] "0x7ff68de5c010" x[1] <- 5 **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 2038054 109 3.79e+06 202 3.22e+06 172 ## Vcells 63687568 486 1.14e+08 870 1.32e+08 1006 **address** (x) ## [1] "0x7ff692aa8010" **object_size** (x, y)

90

---

[← Unit 05 — programming Part 54 —](54-unit-05-programming-part-54.md) · [Up: contents](index.md) · [Unit 05 — programming Part 56 — →](56-unit-05-programming-part-56.md)
