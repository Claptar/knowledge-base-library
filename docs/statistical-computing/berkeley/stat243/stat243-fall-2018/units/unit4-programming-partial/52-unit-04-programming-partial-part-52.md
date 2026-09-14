---
title: Unit 04 — programming partial Part 52 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 52 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also see the nestedness of environments using the following code, using environmentName(), which prints out a nice-looking version of the environment name.

x <- **environment** (lm)

**while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) } ## [1] "stats" ## [1] "imports:stats" ## [1] "base" ## [1] "R_GlobalEnv" ## [1] "package:codetools" ## [1] "package:fields" ## [1] "package:maps" ## [1] "package:spam" ## [1] "package:grid" ## [1] "package:dotCall64" ## [1] "package:R6" ## [1] "package:methods" ## [1] "package:dplyr" ## [1] "package:pryr"

60

---

[← Unit 04 — programming partial Part 51 —](51-unit-04-programming-partial-part-51.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 53 — →](53-unit-04-programming-partial-part-53.md)
