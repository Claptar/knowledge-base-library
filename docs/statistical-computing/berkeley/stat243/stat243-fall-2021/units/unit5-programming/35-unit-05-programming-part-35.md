---
title: Unit 05 — programming Part 35 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 35 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

x <- **environment** (lm) **while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) _# enclosing env't, NOT parent frame!_ } ## [1] "stats" ## [1] "imports:stats" ## [1] "base" ## [1] "R_GlobalEnv" ## [1] "package:codetools" ## [1] "package:fields"

63

- ## [1] "package:viridis" ## [1] "package:viridisLite" ## [1] "package:spam" ## [1] "package:grid" ## [1] "package:dotCall64" ## [1] "package:R6" ## [1] "package:dplyr" ## [1] "package:pryr" ## [1] "package:knitr" ## [1] "package:stats" ## [1] "package:graphics" ## [1] "package:grDevices" ## [1] "package:utils" ## [1] "package:datasets" ## [1] "package:SCF" ## [1] "package:methods" ## [1] "Autoloads" ## [1] "base"

**library** (pryr)

x <- **environment** (lm)

**parenvs** (x, all = TRUE)

|##||label||
|---|---|---|---|
|##|1|<environment:|namespace:stats>|
|##|2|<environment:|0x556916ad1830>|
|##|3|<environment:|namespace:base>|
|##|4|<environment:|R_GlobalEnv>|
|##|5|<environment:|package:codetools>|
|##|6|<environment:|package:fields>|
|##|7|<environment:|package:viridis>|
|##|8|<environment:|package:viridisLite>|
|##|9|<environment:|package:spam>|
|##|10|<environment:|package:grid>|
|##|11|<environment:|package:dotCall64>|
|##|12|<environment:|package:R6>|
|##|13|<environment:|package:dplyr>|


64

- ## 14 <environment: package:pryr> ## 15 <environment: package:knitr> ## 16 <environment: package:stats> ## 17 <environment: package:graphics> ## 18 <environment: package:grDevices> ## 19 <environment: package:utils> ## 20 <environment: package:datasets> ## 21 <environment: package:SCF> ## 22 <environment: package:methods> ## 23 <environment: 0x556915403598> ## 24 <environment: base> ## 25 <environment: R_EmptyEnv> ## name ## 1 "" ## 2 "imports:stats" ## 3 "" ## 4 "" ## 5 "package:codetools" ## 6 "package:fields" ## 7 "package:viridis" ## 8 "package:viridisLite" ## 9 "package:spam" ## 10 "package:grid" ## 11 "package:dotCall64" ## 12 "package:R6" ## 13 "package:dplyr" ## 14 "package:pryr" ## 15 "package:knitr" ## 16 "package:stats" ## 17 "package:graphics" ## 18 "package:grDevices" ## 19 "package:utils" ## 20 "package:datasets" ## 21 "package:SCF" ## 22 "package:methods" ## 23 "Autoloads"

65

---

[← Unit 05 — programming Part 34 —](34-unit-05-programming-part-34.md) · [Up: contents](index.md) · [Unit 05 — programming Part 36 — →](36-unit-05-programming-part-36.md)
