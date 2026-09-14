---
title: 4 Types, classes, and object-oriented programming
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Types, classes, and object-oriented programming

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Types and classes**

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Vectors are either _atomic vectors_ or _lists_ . Atomic vectors generally contain one of the four following types: _logical_ , _integer_ , _double/numeric_ , and _character_ .

Objects in general have a type, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

Let’s look at Adler’s Table 7.1 to see some other types.

a <- **data.frame** (x = 1:2) **class** (a)

12

---

[← 3 Text manipulation, string processing and regular expressions (regex)](16-3-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [Unit 04 — programming Part 18 — →](18-unit-04-programming-part-18.md)
