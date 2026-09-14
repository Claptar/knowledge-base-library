---
title: 4 Types, classes, and object-oriented programming
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Types, classes, and object-oriented programming

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### 4.1 Types and classes

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Vectors are either atomic vectors or lists. Atomic vectors generally contain one of the four following types: logical, integer, double/numeric, and character.

Objects in general have a type, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

Let’s look at Adler’s Table 7.1 to see some other types.

a <- **data.frame** (x = 1:2) **class** (a) ## [1] "data.frame" **typeof** (a) ## [1] "list" **is.data.frame** (a) ## [1] TRUE **is.matrix** (a) ## [1] FALSE **is** (a, "matrix")

12

**## Error in is(a, "matrix"): could not find function "is"** m <- **matrix** (1:4, nrow = 2) **class** (m) ## [1] "matrix" **typeof** (m)

---

[← Unit 04 — programming partial Part 15 —](15-unit-04-programming-partial-part-15.md) · [Up: contents](index.md) · [[1] "integer" →](17-1-integer.md)
