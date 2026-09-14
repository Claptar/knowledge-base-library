---
title: Unit 03 — Rinput Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 15 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_# suppose we only want the country locations of the loans_ countries <- **sapply** ( **xmlChildren** (loansNode), **function** (node) **xmlValue** (node[['location']][['country']]))

countries[1:10]

---

[← Unit 03 — Rinput Part 14 —](14-unit-03-rinput-part-14.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 16 — →](16-unit-03-rinput-part-16.md)
