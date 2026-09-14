---
title: Unit 04 — usingR Part 36 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 36 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that eventually the global environment and the environments of the packages are nested within the base environment (of the base package) and the empty environment. Note that here _parent_ **is** referring to the enclosing environment, even though it is best to talk about _enclosing environment_ rather than parent environment.

We can look at the objects of an environment as follows:

**ls** (pos = 8)[1:5] _# what does this do?_ ## [1] "acf" "acf2AR" "add1" "addmargins" ## [5] "add.scope" **ls** ("package:stats")[1:5] ## [1] "acf" "acf2AR" "add1" "addmargins" ## [5] "add.scope"

52

**environment** (lm)

---

[← [13] "/system/linux/lib/R/3.0/x8664/site-library/SCF"](35-13-system-linux-lib-r-3-0-x8664-site-library-scf.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 37 — →](37-unit-04-usingr-part-37.md)
