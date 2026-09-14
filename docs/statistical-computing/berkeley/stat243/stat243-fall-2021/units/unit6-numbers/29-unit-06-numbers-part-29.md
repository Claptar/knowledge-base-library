---
title: Unit 06 — numbers Part 29 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 29 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

But the result is accurate only to 8 places + 20 = 28 decimal places, as expected from a machine precision-based calculation, since the “1” is in the 13th position, after 12 zeroes (12+16=28). Ideally, we would have accuracy to 36 places (16 digits + the 20 zeroes), but we’ve lost 8 digits to catastrophic cancellation.

It’s best to do any subtraction on numbers that are not too large. For example, if we compute the sum of squares in a naive way, we can lose all of the information in the calculation because the information is in digits that are not computed or stored accurately:


_## No problem here:_ x <- **c** (-1, 0, 1) n <- **length** (x) **sum** (x^2)-n* **mean** (x)^2 ## [1] 2

20

**sum** ((x - **mean** (x))^2) ## [1] 2 _## Adding/subtracting a constant shouldn't change the result:_ x <- x + 1e8 **sum** (x^2)-n* **mean** (x)^2 _# that's not good!_ ## [1] 0 **sum** ((x - **mean** (x))^2) ## [1] 2

A good principle to take away is to subtract off a number similar in magnitude to the values (in this case ¯ _x_ is obviously ideal) and adjust your calculation accordingly. In general, you can sometimes rearrange your calculation to avoid catastrophic cancellation. Another example involves the quadratic formula for finding a root (p. 101 of Gentle).

- Adding or subtracting numbers that are very different in magnitude. The precision will be that of the large magnitude number, since we can only represent that number to a certain absolute accuracy, which is much less than the absolute accuracy of the smaller number:

**dg** (123456781234.2) ## [1] "123456781234.19999694824218750000" **dg** (123456781234.2 - 0.1) _# truth: 123456781234.1_ ## [1] "123456781234.09999084472656250000" **dg** (123456781234.2 - 0.01) _# truth: 123456781234.19_ ## [1] "123456781234.19000244140625000000" **dg** (123456781234.2 - 0.001) _# truth: 123456781234.199_

21

---

[← 3 Implications for calculations and comparisons](28-3-implications-for-calculations-and-comparisons.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 30 — →](30-unit-06-numbers-part-30.md)
