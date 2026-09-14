---
title: Unit 05 — programming Part 27 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 27 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A few additional points:

36

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _clone()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

R6Class("tsSimClass", inherit = "simClass", ...)

- Here we see that use of private fields shields them from modification by users. In this example, the correlation matrix and the Cholesky factor U are both functions of the vector of times. So we don’t want to allow a user to directly modify _times_ . Instead we force them to use _setTimes()_ , which correctly keeps all the fields in the object internally consistent (by calling _calcMats()_ ):

_## the next line would be dangerous if 'times' were public, since ## changing 'times' should result in changing the correlation matrix and ## changing U._ master$times <- 1:10

**## Error in master$times <- 1:10: cannot add bindings to a locked environment**

- If you need to refer to methods and fields you refer to the entire object as either _self_ or _private_ .

- There is a older, more complicated, slower variation on R6 classes called ReferenceClasses. See the _help(ReferenceClasses)_ .

More details on R6 classes can be found in the Advanced R book: https://adv-r.hadley.nz/r6.html.

---

[← Unit 05 — programming Part 26 —](26-unit-05-programming-part-26.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](28-5-standard-dataset-manipulations.md)
