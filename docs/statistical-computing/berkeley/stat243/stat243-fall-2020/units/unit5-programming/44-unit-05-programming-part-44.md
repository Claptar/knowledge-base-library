---
title: Unit 05 — programming Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 44 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can reset the value given for max used, with gc(reset = TRUE). In Windows only, _memory.size()_ tells how much memory is being used. You can check the amount of memory used by individual objects with _object.size()_ . Here is a useful function, _ls.sizes()_ , that wraps _object.size()_ to report the largest _n_ objects in a

83

given environment:

ls.sizes <- **function** (howMany = 10, minSize = 1){ pf <- **parent.frame** () obj <- **ls** (pf) _# or ls(sys.frame(-1))_ objSizes <- **sapply** (obj, **function** (x) { pryr:: **object_size** ( **get** (x, pf)) }) _## or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()_ objNames <- **names** (objSizes) howmany <- **min** (howMany, **length** (objSizes)) ord <- **order** (objSizes, decreasing = TRUE) objSizes <- objSizes[ord][1:howMany] objSizes <- objSizes[objSizes > minSize] objSizes <- **matrix** (objSizes, ncol = 1) **rownames** (objSizes) <- objNames[ord][1: **length** (objSizes)] **colnames** (objSizes) <- "bytes" **cat** ('object') **print** ( **format** (objSizes, justify = "right", width = 11), quote = FALSE) }

Unfortunately with R6 and ReferenceClasses, closures, environments, and other such “containers”, it can be hard to see how much memory the object is using, including all the components of the object. Here’s a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

_## size of a closure_ x <- **rnorm** (1e7) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) **object.size** (myFun)

84

---

[← 8 Evaluating memory use](43-8-evaluating-memory-use.md) · [Up: contents](index.md) · [Unit 05 — programming Part 45 — →](45-unit-05-programming-part-45.md)
