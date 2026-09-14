---
title: Unit 05 — debug Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — debug Part 06 —

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## [1] "<-" "==" "-" "!" ## [5] "!=" "[" "[[<-" "{" ## [9] "$<-" "*" "&&" "as.vector" ## [13] "attr" "c" "class<-" "eval" ## [17] "gettextf" ".getXlevels" "if" "is.empty.model" ## [21] "is.matrix" "is.null" "is.numeric" "length" ## [25] "list" f <- **function** () { y <- 3 **print** (x + y) } **findGlobals** (f)

---

[← 3 Debugging Strategies](05-3-debugging-strategies.md) · [Up: contents](index.md) · [[1] "<-" "{" "+" "print" "x" →](07-1---print-x.md)
