---
title: function (x, y) .Primitive("%%")
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# function (x, y) .Primitive("%%")

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.2 Parsing code and understanding language objects**

R code can be manipulated in text form and we can actually write R code that will create or manipulate R code. We can then evaluate that R code using _eval()_ .

_quote()_ will parse R code, but not evaluate it. This allows you to work with the code rather than the results of evaluating that code. The _print()_ method for language objects is not very helpful! But we can see the parsed code by treating the result as a list.

obj <- **quote** ( **if** (x > 1) "orange" **else** "apple") **as.list** (obj)

97

---

[← Unit 05 — programming Part 61 —](61-unit-05-programming-part-61.md) · [Up: contents](index.md) · [Unit 05 — programming Part 63 — →](63-unit-05-programming-part-63.md)
