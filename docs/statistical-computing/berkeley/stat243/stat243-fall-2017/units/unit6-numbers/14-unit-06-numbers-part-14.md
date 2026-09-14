---
title: Unit 06 — numbers Part 14 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 14 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we try this calculation: 123456781234 _− ._ 0000123456781234. How many decimal places do we expect to be accurate?

The spacing of possible computer numbers that have a magnitude of about 1 leads us to another definition of _machine epsilon_ (an alternative, but essentially equivalent definition to that given previously in this Unit). Machine epsilon tells us also about the relative spacing of numbers. First let’s consider numbers of magnitude one. The difference between 1 = 1 _._ 00 _..._ 00 _×_ 2<sup>0</sup> and 1 _._ 000 _..._ 01 _×_ 2<sup>0</sup> is 1 _×_ 2<sup>_−_52</sup> _≈_ 2 _._ 2 _×_ 10<sup>_−_16</sup> . Machine epsilon gives the _absolute spacing_ for numbers near 1 and the _relative spacing_ for numbers with a different order of magnitude and therefore a different absolute magnitude of the error in representing a real. The relative spacing at _x_ is


since the next largest number from _x_ is given by (1+ _ϵ_ ) _x_ . Suppose _x_ = 1 _×_ 10<sup>6</sup> . Then the absolute error in representing a number of this magnitude is _xϵ ≈_ 2 _×_ 10<sup>_−_10</sup> . (Actually the error would be one-half of the spacing, but that’s a minor distinction.) We can see by looking at the numbers in decimal form, where we are accurate to the order 10<sup>_−_10</sup> but not 10<sup>_−_11</sup> .

1000000.1 ## [1] 1000000.099999999976717

Let’s see what arithmetic we can do exactly with integers stored as doubles and how that relates to the absolute spacing of numbers we’ve just seen:

13

2^52 ## [1] 4503599627370496 2^52+1 ## [1] 4503599627370497 2^53 ## [1] 9007199254740992 2^53+1 ## [1] 9007199254740992 2^53+2 ## [1] 9007199254740994 2^54 ## [1] 18014398509481984 2^54+2 ## [1] 18014398509481984 2^54+4 ## [1] 18014398509481988 **bits** (2^53) ## [1] "01000011 01000000 00000000 00000000 00000000 00000000 00000000 00000000" **bits** (2^53+1) ## [1] "01000011 01000000 00000000 00000000 00000000 00000000 00000000 00000000" **bits** (2^53+2) ## [1] "01000011 01000000 00000000 00000000 00000000 00000000 00000000 00000001" **bits** (2^54) ## [1] "01000011 01010000 00000000 00000000 00000000 00000000 00000000 00000000" **bits** (2^54+2) ## [1] "01000011 01010000 00000000 00000000 00000000 00000000 00000000 00000000" **bits** (2^54+4) ## [1] "01000011 01010000 00000000 00000000 00000000 00000000 00000000 00000001"

14

The absolute spacing is _xϵ_ , so 2<sup>52</sup> _×_ 2<sup>_−_52</sup> = 1, 2<sup>53</sup> _×_ 2<sup>_−_52</sup> = 2, 2<sup>54</sup> _×_ 2<sup>_−_52</sup> = 4.

With a bit more work (e.g., using Mathematica), one can demonstrate that doubles in R in general are represented as the nearest number that can stored with the 64-bit structure we have discussed and that the spacing is as we have discussed. The results below show the spacing that results, in base 10, for numbers around 1. The numbers R reports are spaced in increments of individual bits in the base 2 representation.

0.1234567812345678 ## [1] 0.1234567812345677972896 0.12345678123456781 ## [1] 0.1234567812345678111674 0.12345678123456782 ## [1] 0.1234567812345678250452 0.12345678123456783 ## [1] 0.1234567812345678250452 0.12345678123456784 ## [1] 0.123456781234567838923 **bits** (0.1234567812345678)

---

[← Unit 06 — numbers Part 13 —](13-unit-06-numbers-part-13.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 15 — →](15-unit-06-numbers-part-15.md)
