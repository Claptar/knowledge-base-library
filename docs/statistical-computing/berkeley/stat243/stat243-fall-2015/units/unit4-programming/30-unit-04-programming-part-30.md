---
title: Unit 04 — programming Part 30 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 30 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**searchpaths** ()

- ## [1] ".GlobalEnv" ## [2] "/system/linux/lib/R/3.2/x86_64/site-library/fields" ## [3] "/system/linux/lib/R/3.2/x86_64/site-library/maps" ## [4] "/system/linux/lib/R/3.2/x86_64/site-library/spam" ## [5] "/usr/lib/R/library/grid" ## [6] "/usr/lib/R/library/methods" ## [7] "/system/linux/lib/R/3.2/x86_64/site-library/pryr" ## [8] "/system/linux/lib/R/3.2/x86_64/site-library/knitr" ## [9] "/usr/lib/R/library/stats" ## [10] "/usr/lib/R/library/graphics" ## [11] "/usr/lib/R/library/grDevices" ## [12] "/usr/lib/R/library/utils" ## [13] "/usr/lib/R/library/datasets" ## [14] "/system/linux/lib/R/3.2/x86_64/site-library/SCF" ## [15] "Autoloads" ## [16] "/usr/lib/R/library/base"

52

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

x <- .GlobalEnv **parent.env** (x) _# poorly-named - this returns the enclosing env't_ ## <environment: package:fields> ## attr(,"name") ## [1] "package:fields" ## attr(,"path") ## [1] "/system/linux/lib/R/3.2/x86_64/site-library/fields" **while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) } ## [1] "R_GlobalEnv" ## [1] "package:fields" ## [1] "package:maps" ## [1] "package:spam" ## [1] "package:grid" ## [1] "package:methods" ## [1] "package:pryr" ## [1] "package:knitr" ## [1] "package:stats" ## [1] "package:graphics" ## [1] "package:grDevices" ## [1] "package:utils" ## [1] "package:datasets" ## [1] "package:SCF" ## [1] "Autoloads" ## [1] "base" **parenvs** (all = TRUE) _# from pryr_ ## label ## 1 <environment: R_GlobalEnv>

53

- ## 2 <environment: package:fields> ## 3 <environment: package:maps> ## 4 <environment: package:spam> ## 5 <environment: package:grid> ## 6 <environment: package:methods> ## 7 <environment: package:pryr> ## 8 <environment: package:knitr> ## 9 <environment: package:stats> ## 10 <environment: package:graphics> ## 11 <environment: package:grDevices> ## 12 <environment: package:utils> ## 13 <environment: package:datasets> ## 14 <environment: package:SCF> ## 15 <environment: 0x22eae28> ## 16 <environment: base> ## 17 <environment: R_EmptyEnv> ## name ## 1 "" ## 2 "package:fields" ## 3 "package:maps" ## 4 "package:spam" ## 5 "package:grid" ## 6 "package:methods" ## 7 "package:pryr" ## 8 "package:knitr" ## 9 "package:stats" ## 10 "package:graphics" ## 11 "package:grDevices" ## 12 "package:utils" ## 13 "package:datasets" ## 14 "package:SCF" ## 15 "Autoloads" ## 16 "" ## 17 ""

Note that eventually the global environment and the environments of the packages are nested

54

within the base environment (of the base package) and the empty environment. Note that here _parent_ **is** referring to the enclosing environment, even though it is best to talk about _enclosing environment_ rather than parent environment.

Here’s a full example of the nested environments for a function in a package, such as _lm()_ in the _stats_ package:

x <- **environment** (lm) x ## <environment: namespace:stats>

**while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) {

**print** ( **environmentName** (x)) x <- **parent.env** (x) }

---

[← Unit 04 — programming Part 29 —](29-unit-04-programming-part-29.md) · [Up: contents](index.md) · [Unit 04 — programming Part 31 — →](31-unit-04-programming-part-31.md)
