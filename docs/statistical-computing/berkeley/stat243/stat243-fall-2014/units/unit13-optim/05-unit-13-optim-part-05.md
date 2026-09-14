---
title: Unit 13 — optim Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit13-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — optim Part 05 —

**Source:** [`units/unit13-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**points** (xvals, **fp** (xvals), pch = **as.character** (1: **length** (xvals))) _# bad starting point_ x0 <- 2.5 xvals <- **c** (x0, **rep** (NA,9)) **for** (t **in** 2:10){ xvals[t]=xvals[t-1] - **fp** (xvals[t-1]) / **fpp** (xvals[t-1]) }

**print** (xvals)

---

[← 3 Univariate function optimization](04-3-univariate-function-optimization.md) · [Up: contents](index.md) · [Unit 13 — optim Part 06 — →](06-unit-13-optim-part-06.md)
