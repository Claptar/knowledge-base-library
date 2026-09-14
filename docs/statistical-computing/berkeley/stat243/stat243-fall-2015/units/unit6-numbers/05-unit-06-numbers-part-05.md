---
title: Unit 06 — numbers Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 05 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can easily calculate the number of megabytes (Mb) a vector of floating points (in double precision) will use as the number of elements times 8 (bytes/double) divided by 10<sup>6</sup> to convert from bytes to megabytes. (In some cases when considering computer memory, a megabyte is 1 _,_ 048 _,_ 576 = 2<sup>20</sup> = 1024<sup>2</sup> bytes so slightly different than 10<sup>6</sup> ). Finally, R has a special object that tells us about the characteristics of computer numbers on the machine that R is running on called _.Machine._ For example, _.Machine$integer.max_ is 2147483647 = 2<sup>31</sup> _−_ 1, which confirms how many bytes R is using for each integer (and that R is using a bit for the sign of the integer). We have 2 _·_ 2<sup>31</sup> = 2<sup>32</sup> = (2<sup>8</sup> )<sup>4</sup> , i.e., 4 bytes, with each byte having 8 bits.

**bits** (.Machine$integer.max) ## [1] "01111111 11111111 11111111 11111111" **bits** (-.Machine$integer.max) ## [1] "10000000 00000000 00000000 00000001" **bits** (-1L) ## [1] "11111111 11111111 11111111 11111111"

4

---

[← Unit 06 — numbers Part 04 —](04-unit-06-numbers-part-04.md) · [Up: contents](index.md) · [2 Floating point basics →](06-2-floating-point-basics.md)
