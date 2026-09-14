---
title: Unit 05 — programming Part 41 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 41 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

x <- **environment** (lm) **while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) } ## [1] "stats" ## [1] "imports:stats" ## [1] "base" ## [1] "R_GlobalEnv" ## [1] "package:codetools" ## [1] "package:fields"

63

|##|[1] "package|:maps"|
|---|---|---|
|##|[1] "package|:spam"|
|##|[1] "package|:grid"|
|##|[1] "package|:dotCall64"|
|##|[1] "package|:R6"|
|##|[1] "package|:dplyr"|
|##|[1] "package|:pryr"|
|##|[1] "package|:knitr"|
|##|[1] "package|:stats"|
|##|[1] "package|:graphics"|
|##|[1] "package|:grDevices"|
|##|[1] "package|:utils"|
|##|[1] "package|:datasets"|
|##|[1] "package|:RhpcBLASctl"|
|##|[1] "package|:SCF"|
|##|[1] "package|:methods"|
|##|[1] "Autoloa|ds"|
|##|[1] "base"||
|**lib**|**rary**(pryr)||


x <- **environment** (lm)

**parenvs** (x, all = TRUE)

|##||label||
|---|---|---|---|
|##|1|<environment:|namespace:stats>|
|##|2|<environment:|0x5560f5b58b08>|
|##|3|<environment:|namespace:base>|
|##|4|<environment:|R_GlobalEnv>|
|##|5|<environment:|package:codetools>|
|##|6|<environment:|package:fields>|
|##|7|<environment:|package:maps>|
|##|8|<environment:|package:spam>|
|##|9|<environment:|package:grid>|
|##|10|<environment:|package:dotCall64>|
|##|11|<environment:|package:R6>|
|##|12|<environment:|package:dplyr>|
|##|13|<environment:|package:pryr>|


64

- ## 14 <environment: package:knitr> ## 15 <environment: package:stats> ## 16 <environment: package:graphics> ## 17 <environment: package:grDevices> ## 18 <environment: package:utils> ## 19 <environment: package:datasets> ## 20 <environment: package:RhpcBLASctl> ## 21 <environment: package:SCF> ## 22 <environment: package:methods> ## 23 <environment: 0x5560f4e15360> ## 24 <environment: base> ## 25 <environment: R_EmptyEnv> ## name ## 1 "" ## 2 "imports:stats" ## 3 "" ## 4 "" ## 5 "package:codetools" ## 6 "package:fields" ## 7 "package:maps" ## 8 "package:spam" ## 9 "package:grid" ## 10 "package:dotCall64" ## 11 "package:R6" ## 12 "package:dplyr" ## 13 "package:pryr" ## 14 "package:knitr" ## 15 "package:stats" ## 16 "package:graphics" ## 17 "package:grDevices" ## 18 "package:utils" ## 19 "package:datasets" ## 20 "package:RhpcBLASctl" ## 21 "package:SCF" ## 22 "package:methods" ## 23 "Autoloads"

65

---

[← Unit 05 — programming Part 40 —](40-unit-05-programming-part-40.md) · [Up: contents](index.md) · [Unit 05 — programming Part 42 — →](42-unit-05-programming-part-42.md)
