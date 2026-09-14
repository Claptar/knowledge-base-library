---
title: Unit 04 — programming Part 55 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 55 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.4 Parsing replacement expressions**

Let’s consider replacement expressions.

animals <- **c** ('cat', 'dog', 'rat','mouse') out1 <- **quote** (animals[4] <- 'rat') out2 <- **quote** ( **`<-`** (animals[4], 'rat')) out3 <- **quote** ('[<-'(animals,4,'rat')) **as.list** (out1) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ## ## [[3]] ## [1] "rat" **as.list** (out2) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ##

101

---

[← Unit 04 — programming Part 54 —](54-unit-04-programming-part-54.md) · [Up: contents](index.md) · [Unit 04 — programming Part 56 — →](56-unit-04-programming-part-56.md)
