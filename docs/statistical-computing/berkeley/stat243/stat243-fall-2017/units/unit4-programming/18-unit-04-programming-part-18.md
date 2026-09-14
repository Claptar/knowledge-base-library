---
title: Unit 04 — programming Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 18 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can _inherit_ from other classes; for example, the _glm_ class inherits characteristics from the _lm_ class. We’ll see more on the details of object-oriented programming shortly.

We can create objects with our own defined class.

bart <- **list** (firstname = 'Bart', surname = 'Simpson', hometown = "Springfield") **class** (bart) <- 'personClass' _## it turns out R already has a 'person' class_ **class** (bart)

13

---

[← 4 Types, classes, and object-oriented programming](17-4-types-classes-and-object-oriented-programming.md) · [Up: contents](index.md) · [Unit 04 — programming Part 19 — →](19-unit-04-programming-part-19.md)
