---
title: 7 Functions, variable scoping, and frames
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Functions, variable scoping, and frames

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Functions are at the heart of R. In general, you should try to have functions be self-contained - operating only on arguments provided to them, and producing no side effects, though in some cases there are good reasons for making an exception.

Functions that are not implemented internally in R (i.e., user-defined functions) are also referred to offically as _closures_ (this is their _type_ ) - this terminology sometimes comes up in error messages.

### **7.1 Inputs**

Arguments can be specifed in the correct order, or given out of order by specifying _name = value_ . In general the more important arguments are specified first. You can see the arguments and defaults for a function using _args()_ :

41

**args** (lm)

---

[← 6 Formulas](28-6-formulas.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 30 — →](30-unit-04-usingr-part-30.md)
