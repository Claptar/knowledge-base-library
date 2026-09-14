---
title: Unit 04 — programming partial Part 28 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 28 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can have method signatures involve multiple objects. Here’s some syntax where we’d fill in the function body with appropriate code - perhaps the plus operator would create a child.

29

**setMethod** (`+`, signature = **c** ("bear", "bear"), definition = **function** (bear1, bear2) { ## method code goes here }

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a superclass.

**setClass** ("grizzly_bear", **representation** ( number_of_people_eaten = "numeric" ), contains = "bear" ) sam <- **new** ("grizzly_bear", name = "Sam", age = 20, birthday = **as.Date** ('91-08-03'), number_of_people_eaten = 3) **isVoter** (sam) ## Sam is of voting age. **is** (sam, "bear") ## [1] TRUE

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own initialize() method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on new() and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use setOldClass() - this creates a virtual class. This has been done, for example, for the data.frame class:

30

**showClass** ("data.frame")

---

[← Unit 04 — programming partial Part 27 —](27-unit-04-programming-partial-part-27.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 29 — →](29-unit-04-programming-partial-part-29.md)
