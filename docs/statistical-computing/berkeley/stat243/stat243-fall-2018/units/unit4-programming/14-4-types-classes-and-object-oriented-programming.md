---
title: 4 Types, classes, and object-oriented programming
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Types, classes, and object-oriented programming

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Types and classes**

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Vectors are either _atomic vectors_ or _lists_ . Atomic vectors generally contain one of the four following types: _logical_ , _integer_ , _double/numeric_ , and _character_ .

Objects in general have a type, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

Let’s look at Adler’s Table 7.1 to see some other types.

a <- **data.frame** (x = 1:2) **class** (a) ## [1] "data.frame" **typeof** (a) ## [1] "list" **is.data.frame** (a) ## [1] TRUE **is.matrix** (a) ## [1] FALSE **is** (a, "matrix")

12

**## Error in is(a, "matrix"): could not find function "is"** m <- **matrix** (1:4, nrow = 2) **class** (m) ## [1] "matrix" **typeof** (m) ## [1] "integer"

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can _inherit_ from other classes; for example, the _glm_ class inherits characteristics from the _lm_ class. We’ll see more on the details of object-oriented programming shortly.

We can create objects with our own defined class.

bart <- **list** (firstname = 'Bart', surname = 'Simpson', hometown = "Springfield") **class** (bart) <- 'personClass' _## it turns out R already has a 'person' class_ **class** (bart)

---

[← 3 Text manipulation, string processing and regular expressions (regex)](13-3-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [Unit 04 — programming Part 15 — →](15-unit-04-programming-part-15.md)
