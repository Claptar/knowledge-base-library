---
title: Unit 06 — numbers Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 18 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The spacing of possible computer numbers that have a magnitude of about 1 leads us to another definition of _machine epsilon_ (an alternative, but essentially equivalent definition to that given previously in this Unit). Machine epsilon tells us also about the relative spacing of numbers. First let’s consider numbers of magnitude one. The difference between 1 = 1 _._ 00 _..._ 00 _×_ 2<sup>0</sup> and 1 _._ 000 _..._ 01 _×_ 2<sup>0</sup> is 1 _×_ 2<sup>_−_52</sup> _≈_ 2 _._ 2 _×_ 10<sup>_−_16</sup> . Machine epsilon gives the _absolute spacing_ for numbers near 1 and the _relative spacing_ for numbers with a different order of magnitude and therefore a different absolute magnitude of the error in representing a real. The relative spacing at _x_ is


since the next largest number from _x_ is given by (1+ _ϵ_ ) _x_ . Suppose _x_ = 1 _×_ 10<sup>6</sup> . Then the absolute error in representing a number of this magnitude is _xϵ ≈_ 2 _×_ 10<sup>_−_10</sup> . (Actually the error would be one-half of the spacing, but that’s a minor distinction.) We can see by looking at the numbers in decimal form, where we are accurate to the order 10<sup>_−_10</sup> but not 10<sup>_−_11</sup> .

**dg** (1000000.1)

---

[← Unit 06 — numbers Part 17 —](17-unit-06-numbers-part-17.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 19 — →](19-unit-06-numbers-part-19.md)
