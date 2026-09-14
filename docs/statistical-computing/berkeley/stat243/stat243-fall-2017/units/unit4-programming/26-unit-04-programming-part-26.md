---
title: Unit 04 — programming Part 26 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 26 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can have method signatures involve multiple objects. Here’s some syntax where we’d fill in the function body with appropriate code - perhaps the plus operator would create a child.

**setMethod** (`+`, signature = **c** ("bear", "bear"), definition = **function** (bear1, bear2) { _## method code goes here_ }

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a _superclass_ .

**setClass** ("grizzly_bear", **representation** ( number_of_people_eaten = "numeric" ), contains = "bear" ) sam <- **new** ("grizzly_bear", name = "Sam", age = 20, birthday = **as.Date** ('91-08-03'), number_of_people_eaten = 3)

30

**isVoter** (sam) ## Sam is of voting age. **is** (sam, "bear")

---

[← Bear of age 20 whose name is Yogi the Bear.](25-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [[1] TRUE →](27-1-true.md)
