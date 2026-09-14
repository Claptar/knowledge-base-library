---
title: Unit 04 — programming partial Part 27 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 27 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

28

sam <- **new** ("bear", name = "Z%a B''*", age = 20, birthday = **as.Date** ('91-08-03')) sam@age <- 150 # so our validity check is not foolproof

To deal with this latter issue of the user mucking with the slots, it’s recommended when using OOP that slots only be accessible through methods that operate on the object, e.g., a setAge() method, and then check the validity of the supplied age within setAge().

Here’s how we create generic and class-specific methods. Note that in some cases the generic will already exist.

---

[← Bear of age 20 whose name is Yogi the Bear.](26-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 28 — →](28-unit-04-programming-partial-part-28.md)
