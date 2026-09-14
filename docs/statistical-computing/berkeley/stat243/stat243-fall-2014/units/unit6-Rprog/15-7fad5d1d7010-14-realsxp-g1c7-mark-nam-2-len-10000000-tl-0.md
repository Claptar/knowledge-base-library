---
title: '@7fad5d1d7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# @7fad5d1d7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In fact, this occurs outside function calls as well. Copies of objects are not made until one of the objects is actually modified. Initially, the copy points to the same memory location as the original object.

y <- **rnorm** (1e+07) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 5550802 296.5 8125770 434 8125770 434 ## Vcells 113403481 865.2 212429759 1621 192393222 1468 **.Internal** ( **inspect** (y)) ## @7fad34954010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0) x <- y **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 5550823 296.5 8125770 434 8125770 434 ## Vcells 103403532 789.0 212429759 1621 192393222 1468

33

**.Internal** ( **inspect** (x))

---

[← Unit 06 — Rprog Part 14 —](14-unit-06-rprog-part-14.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 16 — →](16-unit-06-rprog-part-16.md)
