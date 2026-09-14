---
title: Unit 06 — numbers Part 31 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 31 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The absolute spacing is _xϵ_ , so 2<sup>52</sup> _×_ 2<sup>_−_52</sup> = 1, 2<sup>53</sup> _×_ 2<sup>_−_52</sup> = 2, 2<sup>54</sup> _×_ 2<sup>_−_52</sup> = 4.

With a bit more work (e.g., using Mathematica), one can demonstrate that doubles in R in general are represented as the nearest number that can stored with the 64-bit structure we have discussed and that the spacing is as we have discussed. The results below show the spacing that results, in base 10, for numbers around 1. The numbers R reports are spaced in increments of individual bits in the base 2 representation.

**dg** (0.1234567812345678)

---

[← Unit 06 — numbers Part 30 —](30-unit-06-numbers-part-30.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 32 — →](32-unit-06-numbers-part-32.md)
