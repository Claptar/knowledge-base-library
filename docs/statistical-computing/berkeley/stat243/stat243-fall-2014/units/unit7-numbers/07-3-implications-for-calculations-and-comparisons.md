---
title: 3 Implications for calculations and comparisons
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit7-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Implications for calculations and comparisons

**Source:** [`units/unit7-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit7-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Computer arithmetic is not mathematical arithmetic!**

As mentioned for integers, computer number arithmetic is not closed, unlike real arithmetic. For example, if we multiply two computer floating points, we can overflow and not get back another computer floating point. One term that is used, which might pop up in an error message (though probably not in R) is that an “exception” is “thrown”. Another mathematical concept we should consider here is that computer arithmetic does not obey the associative and distribute laws, i.e., ( _a_ + _b_ ) + _c_ may not equal _a_ + ( _b_ + _c_ ) on a computer and _a_ ( _b_ + _c_ ) may not be the same as _ab_ + _ac_ . Here’s an example:

val1 <- 1/10 val2 <- 0.31 val3 <- 0.57 res1 <- val1 * val2 * val3 res2 <- val3 * val2 * val1 **identical** (res1, res2) ## [1] FALSE res1 ## [1] 0.0176699999999999982081

12

---

[← Unit 07 — numbers Part 06 —](06-unit-07-numbers-part-06.md) · [Up: contents](index.md) · [Unit 07 — numbers Part 08 — →](08-unit-07-numbers-part-08.md)
