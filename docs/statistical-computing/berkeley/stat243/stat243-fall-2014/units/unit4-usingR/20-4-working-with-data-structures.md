---
title: 4 Working with data structures
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Working with data structures

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Lists and dataframes**

**Extraction** You extract from lists with “ _[[_ “ or with “ _[_ “

x <- **list** (a = 1:2, b = 3:4, sam = **rnorm** (4)) x[[2]] ## [1] 3 4 _# extracts the indicated component, which can be # anything, in this case just an integer vector_ x[2] _# extracts subvectors, which since it is a list,_ ## $b ## [1] 3 4 _# will also be a list_ x[ **c** (1, 3)] ## $a ## [1] 1 2 ## ## $sam ## [1] -0.631 1.878 0.422 1.622

When working with lists, it’s handy to be able to use the same function on each element of the list:

**lapply** (x, length) ## $a ## [1] 2 ##

19

---

[← Unit 04 — usingR Part 19 —](19-unit-04-usingr-part-19.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 21 — →](21-unit-04-usingr-part-21.md)
