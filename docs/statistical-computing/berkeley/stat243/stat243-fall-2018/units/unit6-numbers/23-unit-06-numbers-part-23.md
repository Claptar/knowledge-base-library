---
title: Unit 06 — numbers Part 23 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 23 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

12

**dg** (12345678123456780000 - 12345678123456770000) ## [1] "10240.00000000000000000000" **dg** (.1234567812345678 - .1234567812345677) ## [1] "0.00000000000000009714" **dg** (.12345678123456788888 - .12345678123456788887) ## [1] "0.00000000000000000000"

**dg** (.00001234567812345678 - .00001234567812345677) ## [1] "0.00000000000000000001" _# not as close as we'd expect, should be 1e-20_ **dg** (.000012345678123456788888 - .000012345678123456788887) ## [1] "0.00000000000000000000" **dg** (123456781234 - .0000123456781234) ## [1] "123456781233.99998474121093750000" _## the correct answer is 123456781233.99998765...._

Suppose we try this calculation: 123456781234 _− ._ 0000123456781234. How many decimal places do we expect to be accurate?

The spacing of possible computer numbers that have a magnitude of about 1 leads us to another definition of _machine epsilon_ (an alternative, but essentially equivalent definition to that given previously in this Unit). Machine epsilon tells us also about the relative spacing of numbers. First let’s consider numbers of magnitude one. The difference between 1 = 1 _._ 00 _..._ 00 _×_ 2<sup>0</sup> and 1 _._ 000 _..._ 01 _×_ 2<sup>0</sup> is 1 _×_ 2<sup>_−_52</sup> _≈_ 2 _._ 2 _×_ 10<sup>_−_16</sup> . Machine epsilon gives the _absolute spacing_ for numbers near 1 and the _relative spacing_ for numbers with a different order of magnitude and therefore a different absolute magnitude of the error in representing a real. The relative spacing at _x_ is


since the next largest number from _x_ is given by (1+ _ϵ_ ) _x_ . Suppose _x_ = 1 _×_ 10<sup>6</sup> . Then the absolute

13

error in representing a number of this magnitude is _xϵ ≈_ 2 _×_ 10<sup>_−_10</sup> . (Actually the error would be one-half of the spacing, but that’s a minor distinction.) We can see by looking at the numbers in decimal form, where we are accurate to the order 10<sup>_−_10</sup> but not 10<sup>_−_11</sup> .

**dg** (1000000.1)

---

[← Unit 06 — numbers Part 22 —](22-unit-06-numbers-part-22.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 24 — →](24-unit-06-numbers-part-24.md)
