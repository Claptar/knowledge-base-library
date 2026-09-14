---
title: Unit 06 — numbers Part 17 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 17 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The absolute spacing is _xϵ_ , so we have spacings of 2<sup>52</sup> _×_ 2<sup>_−_52</sup> = 1, 2<sup>53</sup> _×_ 2<sup>_−_52</sup> = 2, 2<sup>54</sup> _×_ 2<sup>_−_52</sup> = 4 for numbers of magnitude 2<sup>52</sup> , 2<sup>53</sup> , and 2<sup>54</sup> , respectively.

With a bit more work (e.g., using Mathematica), one can demonstrate that doubles in R in general are represented as the nearest number that can stored with the 64-bit structure we have discussed and that the spacing is as we have discussed. The results below show the spacing that results, in base 10, for numbers around 0.1. The numbers R reports are spaced in increments of individual bits in the base 2 representation.

15

**dg** (0.1234567812345678)

---

[← Unit 06 — numbers Part 16 —](16-unit-06-numbers-part-16.md) · [Up: contents](index.md) · [[1] "0.12345678123456779729" dg (0.12345678123456781) →](18-1-0-12345678123456779729-dg-0-12345678123456781.md)
