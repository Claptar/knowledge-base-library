---
title: Unit 11 — optim Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 11 — optim Part 07 —

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

2.923566e-13 0.000000e+00

**plot** (xs, **f** (xs), type = 'l', xlab = 'x', ylab = "f'(x)", lwd = 2, main = 'uphill to local maximum',) **lines** (xs, **fp** (xs)) **lines** (xs, **fpp** (xs), lty = 2) **legend** ('bottomright', lty = **c** (1,1,2), lwd = **c** (2, 1, 1), legend = **c** ("f(x)", "f'(x)", 'f"(x)'), bty = 'n')

**points** (xvals, **fp** (xvals), pch = **as.character** (1: **length** (xvals)), col = 'red') _## and we've found a maximum rather than a minimum..._

_## in contrast, with better starting points we can find the minimum_ x0 <- 2 _# ok starting point_ **fp** (x0) ## [1] -0.9092974

**fpp** (x0) ## [1] 0.4161468 x1 <- x0 - **fp** (x0)/ **fpp** (x0) xvals <- **c** (x0, **rep** (NA,9)) **for** (t **in** 2:10){ xvals[t]=xvals[t-1]- **fp** (xvals[t-1])/ **fpp** (xvals[t-1]) } xvals

9

---

[← Unit 11 — optim Part 06 —](06-unit-11-optim-part-06.md) · [Up: contents](index.md) · [Unit 11 — optim Part 08 — →](08-unit-11-optim-part-08.md)
