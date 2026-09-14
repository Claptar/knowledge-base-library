---
title: Unit 07 — numbers Part 09 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — numbers Part 09 —

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The absolute error here, based on the larger value (which has the fewest error-free decimal places) is of the order _ϵx_ = 2 _._ 2 _×_ 10<sup>_−_16</sup> _·_ 1 _×_ 10<sup>12</sup> _≈_ 1 _×_ 10<sup>_−_4</sup> = _._ 0001, so while we might think that the result is close to the value 1 and should have error of about machine epsilon, we actually only have about four significant digits in our result.

This is called _catastrophic cancellation_ , because most of the digits that are left represent rounding error - all the significant digits have cancelled with each other.

Here’s catastrophic cancellation with small numbers. The right answer here is exactly 0.000000000000000000001234.

a = .000000000000123412341234

b = .000000000000123412340000

a - b

---

[← Unit 07 — numbers Part 08 —](08-unit-07-numbers-part-08.md) · [Up: contents](index.md) · [[1] 1.233999993151397490851e-21 →](10-1-1-233999993151397490851e-21.md)
