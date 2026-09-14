---
title: Unit 04 — programming Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 44 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.4 Parsing replacement expressions**

Let’s consider replacement expressions.

animals <- **c** ('cat', 'dog', 'rat','mouse') out1 <- **quote** (animals[4] <- 'rat') out2 <- **quote** ( **`<-`** (animals[4], 'rat')) out3 <- **quote** ('[<-'(animals,4,'rat')) **as.list** (out1) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ## ## [[3]] ## [1] "rat" **as.list** (out2) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ##

92

---

[← Unit 04 — programming Part 43 —](43-unit-04-programming-part-43.md) · [Up: contents](index.md) · [Unit 04 — programming Part 45 — →](45-unit-04-programming-part-45.md)
