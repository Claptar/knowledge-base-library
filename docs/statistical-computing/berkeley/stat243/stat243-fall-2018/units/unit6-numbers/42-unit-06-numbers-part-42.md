---
title: Unit 06 — numbers Part 42 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 42 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Actually, we probably want to use a number slightly larger than _.Machine$double.eps_ to be safe. You can also take a look at the R function _all.equal.numeric()_ .

Finally, in computing, we often encounter the use of an unusual integer as a symbol for missing values. E.g., a datafile might store missing values as -9999. Testing for this using == in R should generally be ok: x [ x == -9999 ] <- NA, both because integers of this magnitude are stored exactly and because the -9999 values would presumably have been created in the same way. To be really careful, you can read in as character type and do the assessment before converting to numeric.

### **3.4 Calculations**

Given the limited _precision_ of computer numbers, we need to be careful when:

- Subtracting large numbers that are nearly equal (or adding negative and positive numbers of the same magnitude). You won’t have the precision in the answer that you would like.

_# catastrophic cancellation w/ large numbers_ **dg** (123456781234.56 - 123456781234.00) ## [1] "0.55999755859375000000" _# how many accurate decimal places?_

The absolute error in the original numbers here, is of the order _ϵx_ = 2 _._ 2 _×_ 10<sup>_−_16</sup> _·_ 1 _×_ 10<sup>11</sup> _≈_ 1 _×_ 10<sup>_−_5</sup> = _._ 00001. While we might think that the result is close to the value 1 and should have error of about machine epsilon, the relevant absolute error is in the original numbers, so we actually only have about five significant digits in our result because we cancel out the other digits.

19

This is called _catastrophic cancellation_ , because most of the digits that are left represent rounding error - all the significant digits have cancelled with each other. Here’s catastrophic cancellation with small numbers. The right answer here is exactly 0.000000000000000000001234.

_# catastrophic cancellation w/ small numbers_ a = .000000000000123412341234 b = .000000000000123412340000

_# so we know the right answer is .000000000000000000001234 EXACTLY_ **dg** (a-b, 35)

---

[← 3 Implications for calculations and comparisons](41-3-implications-for-calculations-and-comparisons.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 43 — →](43-unit-06-numbers-part-43.md)
