---
title: '[1] "integer"'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "integer"

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can inherit from other classes; for example, the glm class inherits characteristics from the lm class. We’ll see more on the details of object-oriented programming shortly.

We can create objects with our own defined class.

bart <- **list** (firstname = 'Bart', surname = 'Simpson', hometown = "Springfield") **class** (bart) <- 'personClass' ## it turns out R already has a 'person' class **class** (bart)

---

[← 4 Types, classes, and object-oriented programming](16-4-types-classes-and-object-oriented-programming.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 18 — →](18-unit-04-programming-partial-part-18.md)
