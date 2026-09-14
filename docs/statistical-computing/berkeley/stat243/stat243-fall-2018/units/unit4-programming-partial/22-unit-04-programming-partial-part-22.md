---
title: Unit 04 — programming partial Part 22 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 22 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the $ operator.

Creating our own class We can create an object with a new class as follows: yog <- **list** (firstname = 'Yogi', surname = 'the Bear', age = 20) **class** (yog) <- 'bear'

Actually, if we want to create a new class that we’ll use again, we want to create a constructor function that initializes new bears:

bear <- **function** (firstname = NA, surname = NA, age = NA){ # constructor for 'indiv' class obj <- **list** (firstname = firstname, surname = surname, age = age) **class** (obj) <- 'bear' **return** (obj) } smoke <- **bear** ('Smokey','Bear')

For those of you used to more formal OOP, the following is probably disconcerting:

**class** (yog) <- "silly" **class** (yog) <- "bear"

Methods The real power of OOP comes from defining methods. For example,

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = 'binomial') **summary** (gmod)

22

Here summary() is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods plot(), print(), summary(), ‘[‘, and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

summary

---

[← Unit 04 — programming partial Part 21 —](21-unit-04-programming-partial-part-21.md) · [Up: contents](index.md) · [function (object, ...) ## UseMethod("summary") ## ## →](23-function-object-usemethod-summary.md)
