---
title: '$y ## [1] 2 ## ## $z ## 1/y class (args) ## [1] "pairlist"'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $y ## [1] 2 ## ## $z ## 1/y class (args) ## [1] "pairlist"

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

### **2.6 Promises and lazy evaluation**

One additional concept that it’s useful to be aware of is the idea of a _promise_ object. In function calls, when R matches user input arguments to formal argument names, it does not (usually) evaluate the arguments until they are needed, which is called _lazy evaluation_ . Instead the formal arguments are of a special type called a _promise_ . Let’s see lazy evaluation in action. Do you think the following code will run?

f <- **function** (a, b = d) { d <- **log** (a) **return** (a * b) } **f** (7)

What’s strange about that? Another example:

f <- **function** (x) **print** ("hi") **system.time** ( **mean** ( **rnorm** (1e+06))) ## user system elapsed ## 0.092 0.000 0.089 **system.time** ( **f** (3))

26

---

[← Unit 06 — Rprog Part 07 —](07-unit-06-rprog-part-07.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 09 — →](09-unit-06-rprog-part-09.md)
