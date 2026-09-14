---
title: Unit 05 — programming Part 31 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 31 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _clone()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

   - R6Class("tsSimClass", inherit = "simClass", ...)

- Here we see that use of private fields shields them from modification by users, which might cause problems:

_## the next line would be dangerous if 'times' were public, since ## currentU would no longer be accurate_ master$times <- 1:10

**## Error in master$times <- 1:10: cannot add bindings to a locked environment**

- If you need to refer to methods and fields you refer to the entire object as either _self_ or _private_ .

- There is a older, more complicated, slower variation on R6 classes called ReferenceClasses. See the _help(ReferenceClasses)_ .

More details on R6 classes can be found in the Advanced R book: https://adv-r.hadley.nz/r6.html.

---

[← Unit 05 — programming Part 30 —](30-unit-05-programming-part-30.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](32-5-standard-dataset-manipulations.md)
