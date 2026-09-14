---
title: Unit 04 — programming Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 15 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

13

### **4.2 Attributes**

_Attributes_ are information about an object attached to an object as something that looks like a named list. Attributes are often copied when operating on an object. This can lead to some weirdlooking formatting:

x <- **rnorm** (10 * 365) qs <- **quantile** (x, **c** (.025, .975)) qs ## 2.5% 97.5% ## -1.97 1.96 qs[1] + 3 ## 2.5% ## 1.03

Thus in an subsequent operations with _qs_ , the _names_ attribute will often get carried along. We can get rid of it:

**names** (qs) <- **NULL** qs ## [1] -1.97 1.96

A common use of attributes is that rows and columns may be named in matrices and data frames, and elements in vectors:

**row.names** (mtcars)[1:6] ## [1] "Mazda RX4" "Mazda RX4 Wag" ## [3] "Datsun 710" "Hornet 4 Drive" ## [5] "Hornet Sportabout" "Valiant" **names** (mtcars) ## [1] "mpg" "cyl" "disp" "hp" "drat" "wt" "qsec" ## [8] "vs" "am" "gear" "carb"

**attributes** (mtcars)

14

---

[← 4 Types, classes, and object-oriented programming](14-4-types-classes-and-object-oriented-programming.md) · [Up: contents](index.md) · [Unit 04 — programming Part 16 — →](16-unit-04-programming-part-16.md)
