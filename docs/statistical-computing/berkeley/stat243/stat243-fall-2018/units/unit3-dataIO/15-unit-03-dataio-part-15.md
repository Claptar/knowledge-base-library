---
title: Unit 03 — dataIO Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 15 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits that R displays to the screen, controlled by _options()$digits_ . But note that _options()$digits_ seems to have some variability in behavior across operating systems. If you want finer control, use _sprintf()_ , e.g., to print out print out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

31

temps <- **c** (12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10) **sprintf** ("%9.4f C", temps)

---

[← 4 Output from R](14-4-output-from-r.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 16 — →](16-unit-03-dataio-part-16.md)
