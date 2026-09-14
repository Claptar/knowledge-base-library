---
title: Unit 04 — programming Part 25 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 25 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
0 20 40 60 80 100<br>4<br>3<br>2<br>1<br>process values<br>0<br><!-- End of picture text -->

time

34

mycopy <- master myRealCopy <- master$ **clone** () master$ **changeTimes** ( **seq** (0,1000, length = 100)) ## Done updating correlation matrix and Cholesky factor. mycopy$ **getTimes** ()[1:5] ## [1] 0.0 10.1 20.2 30.3 40.4 myRealCopy$ **getTimes** ()[1:5] ## [1] 1 2 3 4 5

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _clone()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

R6Class("tsSimClass", inherit = "simClass", ...)

- Here we see that use of private fields shields them from modification by users, which might cause problems:

_## the next line would be dangerous if 'times' were public, since ## currentU would no longer be accurate_ master$times <- 1:10

**## Error in master$times <- 1:10: cannot add bindings to a locked environment**

- If you need to refer to methods and fields you refer to the entire object as either _self_ or _private_ .

- There is a older, more complicated, slower variation on R6 classes called ReferenceClasses. See the _help(ReferenceClasses)_ .

More details on R6 classes can be found in the Advanced R book: https://adv-r.hadley.nz/r6.html.

35

---

[← Unit 04 — programming Part 24 —](24-unit-04-programming-part-24.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](26-5-standard-dataset-manipulations.md)
