---
title: Unit 05 — programming Part 56 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 56 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.4 Parsing replacement expressions**

Let’s consider replacement expressions.

animals <- **c** ('cat', 'dog', 'rat','mouse') out1 <- **quote** (animals[4] <- 'rat') out2 <- **quote** ( ` **<-** ` (animals[4], 'rat')) out3 <- **quote** ('[<-'(animals,4,'rat')) **as.list** (out1) ## [[1]] ## ` <- ` ## ## [[2]] ## animals[4] ## ## [[3]] ## [1] "rat" **as.list** (out2) ## [[1]] ## ` <- ` ## ## [[2]] ## animals[4] ##

111

---

[← Unit 05 — programming Part 55 —](55-unit-05-programming-part-55.md) · [Up: contents](index.md) · [Unit 05 — programming Part 57 — →](57-unit-05-programming-part-57.md)
