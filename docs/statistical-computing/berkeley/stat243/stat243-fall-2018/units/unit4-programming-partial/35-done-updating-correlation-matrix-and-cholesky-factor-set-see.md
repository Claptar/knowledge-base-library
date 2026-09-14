---
title: Done updating correlation matrix and Cholesky factor. set.seed (1)
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Done updating correlation matrix and Cholesky factor. set.seed (1)

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

devs <- master$ **simulate** () **lines** (master$ **getTimes** (), devs, col = 'red')


<!-- Start of picture text -->
0 20 40 60 80 100<br>4<br>3<br>2<br>1<br>process values<br>0<br><!-- End of picture text -->

time

34

mycopy <- master myRealCopy <- master$ **clone** () master$ **changeTimes** ( **seq** (0,1000, length = 100)) ## Done updating correlation matrix and Cholesky factor. mycopy$ **getTimes** ()[1:5] ## [1] 0.0 10.1 20.2 30.3 40.4 myRealCopy$ **getTimes** ()[1:5] ## [1] 1 2 3 4 5

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the clone() method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a simClass and we wanted the tsSimClass to inherit from it:

R6Class("tsSimClass", inherit = "simClass", ...)

- Here we see that use of private fields shields them from modification by users, which might cause problems:

---

[← Unit 04 — programming partial Part 34 —](34-unit-04-programming-partial-part-34.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 36 — →](36-unit-04-programming-partial-part-36.md)
