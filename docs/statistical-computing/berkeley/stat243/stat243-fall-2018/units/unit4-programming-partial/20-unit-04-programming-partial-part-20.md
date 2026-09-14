---
title: Unit 04 — programming partial Part 20 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 20 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))** # OK: **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.004 0.000 0.001

Here’s another example:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) ## [1] 0 1

17

---

[← $names ## [1] "x" "y" ## ## $row.names ## [1] 1 2 ## ## $class ## [1] "data.frame"](19-row-names-1-1-2-class-1-data-frame.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 21 — →](21-unit-04-programming-partial-part-21.md)
