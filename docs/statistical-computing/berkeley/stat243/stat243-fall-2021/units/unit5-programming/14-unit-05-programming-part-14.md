---
title: Unit 05 — programming Part 14 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 14 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

18

### **4.3 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

mean

---

[← $names ## [1] "x" "y"](13-names-1-x-y.md) · [Up: contents](index.md) · [function (x, ...) ## UseMethod("mean") ## ## →](15-function-x-usemethod-mean.md)
