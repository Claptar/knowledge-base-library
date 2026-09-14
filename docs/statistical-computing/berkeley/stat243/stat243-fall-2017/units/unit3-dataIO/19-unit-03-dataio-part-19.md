---
title: Unit 03 — dataIO Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 19 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits that R displays to the screen, controlled by _options()$digits_ . If you want finer control, use _sprintf()_ , e.g., to print out print out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

temps <- **c** (12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10) **sprintf** ("%9.4f C", temps)

---

[← 4 Output from R](18-4-output-from-r.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 20 — →](20-unit-03-dataio-part-20.md)
