---
title: Unit 06 — numbers Part 43 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 43 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

But the result is accurate only to 8 places + 20 = 28 decimal places, as expected from a machine precision-based calculation, since the “1” is in the 13th position, after 12 zeroes (12+16=28). Ideally, we would have accuracy to 36 places (16 digits + the 20 zeroes), but we’ve lost 8 digits to catastrophic cancellation.

It’s best to do any subtraction on numbers that are not too large. For example, we can get catastrophic cancellation when computing a sum of squares in a naive way:


x <- **c** (-1, 0, 1) + 1e8 n <- **length** (x) **sum** (x^2)-n* **mean** (x)^2 _# that's not good!_ ## [1] 0 **sum** ((x - **mean** (x))^2) ## [1] 2

A good principle to take away is to subtract off a number similar in magnitude to the values (in this case ¯ _x_ is obviously ideal) and adjust your calculation accordingly. In general, you can

20

sometimes rearrange your calculation to avoid catastrophic cancellation. Another example involves the quadratic formula for finding a root (p. 101 of Gentle).

- Adding or subtracting numbers that are very different in magnitude. The precision will be that of the large magnitude number, since we can only represent that number to a certain absolute accuracy, which is much less than the absolute accuracy of the smaller number:

**dg** (123456781234 - 0.000001)

---

[← Unit 06 — numbers Part 42 —](42-unit-06-numbers-part-42.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 44 — →](44-unit-06-numbers-part-44.md)
