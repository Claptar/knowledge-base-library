---
title: Unit 04 — programming Part 41 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 41 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can reset the value given for max used, with gc(reset = TRUE). In Windows only, _memory.size()_ tells how much memory is being used. You can check the amount of memory used by individual objects with _object.size()_ . Here is a useful function, _ls.sizes()_ , that wraps _object.size()_ to report the largest _n_ objects in a given environment:

ls.sizes <- **function** (howMany = 10, minSize = 1){ pf <- **parent.frame** () obj <- **ls** (pf) _# or ls(sys.frame(-1))_ objSizes <- **sapply** (obj, **function** (x) { pryr:: **object_size** ( **get** (x, pf)) }) _## or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()_ objNames <- **names** (objSizes) howmany <- **min** (howMany, **length** (objSizes)) ord <- **order** (objSizes, decreasing = TRUE) objSizes <- objSizes[ord][1:howMany] objSizes <- objSizes[objSizes > minSize] objSizes <- **matrix** (objSizes, ncol = 1) **rownames** (objSizes) <- objNames[ord][1: **length** (objSizes)] **colnames** (objSizes) <- "bytes"

76

**cat** ('object') **print** ( **format** (objSizes, justify = "right", width = 11), quote = FALSE) }

Unfortunately with environments, ReferenceClasses, and other such “containers”, it can be hard to see how much memory the object is using, including all the components of the object. Here’s a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

_## size of an environment_ e <- **new.env** () e$x <- **rnorm** (1e7) **object.size** (e) ## 56 bytes **object_size** (e) ## 80 MB **length** ( **serialize** (e, **NULL** )) ## [1] 80000183 _## size of a closure_ x <- **rnorm** (1e7) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) **object.size** (myFun) ## 1560 bytes **object_size** (myFun)

77

---

[← 8 Evaluating memory use](40-8-evaluating-memory-use.md) · [Up: contents](index.md) · [Unit 04 — programming Part 42 — →](42-unit-04-programming-part-42.md)
