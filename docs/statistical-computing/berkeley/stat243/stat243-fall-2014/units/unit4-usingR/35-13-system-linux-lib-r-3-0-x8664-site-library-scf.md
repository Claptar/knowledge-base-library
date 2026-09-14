---
title: '[13] "/system/linux/lib/R/3.0/x8664/site-library/SCF"'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [13] "/system/linux/lib/R/3.0/x8664/site-library/SCF"

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- ## [14] "Autoloads" ## [15] "/usr/lib/R/library/base"

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

x <- .GlobalEnv **parent.env** (x) _# poorly-named - this returns the enclosing env't_ ## <environment: package:fields> ## attr(,"name") ## [1] "package:fields"

51

---

[← [11] "/usr/lib/R/library/utils"](34-11-usr-lib-r-library-utils.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 36 — →](36-unit-04-usingr-part-36.md)
