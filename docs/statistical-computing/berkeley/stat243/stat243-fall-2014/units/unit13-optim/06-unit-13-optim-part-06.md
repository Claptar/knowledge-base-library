---
title: Unit 13 — optim Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit13-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 13 — optim Part 06 —

**Source:** [`units/unit13-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit13-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**points** (xvals, **fp** (xvals), pch = **as.character** (1: **length** (xvals)), col = 'red') _# whoops ############################################# # mistakenly climbing uphill_ f <- **function** (x) **cos** (x) fp <- **function** (x) - **sin** (x) fpp <- **function** (x) - **cos** (x) xs <- **seq** (0, 2*pi, len = 300) **plot** (xs, **f** (xs), type = 'l', lwd = 2) **lines** (xs, **fp** (xs)) **lines** (xs, **fpp** (xs), lty = 2) x0 <- 0.2 _# starting point_ **fp** (x0) _# negative_ ## [1] -0.1986693 **fpp** (x0) _# negative_

7

---

[← Unit 13 — optim Part 05 —](05-unit-13-optim-part-05.md) · [Up: contents](index.md) · [Unit 13 — optim Part 07 — →](07-unit-13-optim-part-07.md)
