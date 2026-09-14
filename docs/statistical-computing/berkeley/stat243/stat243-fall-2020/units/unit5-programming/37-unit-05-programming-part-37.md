---
title: Unit 05 — programming Part 37 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 37 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

62

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

|x <|- **environment**(lm)|
|---|---|
|**whi**|**le** (**environmentName**(x) != **environmentName**(**emptyenv**())) {|
||**print**(**environmentName**(x))|
|}|x <- **parent.env**(x) _# enclosing env't, NOT parent frame!_|
|##|[1] "stats"|
|##|[1] "imports:stats"|
|##|[1] "base"|
|##|[1] "R_GlobalEnv"|
|##|[1] "package:codetools"|
|##|[1] "package:fields"|
|##|[1] "package:maps"|
|##|[1] "package:spam"|
|##|[1] "package:grid"|
|##|[1] "package:dotCall64"|
|##|[1] "package:R6"|
|##|[1] "package:dplyr"|
|##|[1] "package:pryr"|
|##|[1] "package:knitr"|
|##|[1] "package:stats"|
|##|[1] "package:graphics"|
|##|[1] "package:grDevices"|
|##|[1] "package:utils"|
|##|[1] "package:datasets"|
|##|[1] "package:SCF"|
|##|[1] "package:methods"|
|##|[1] "Autoloads"|
|##|[1] "base"|
|**lib**|**rary**(pryr)|
|x <|- **environment**(lm)|
|**par**|**envs**(x, all = TRUE)|
|##|label|


63

- ## 1 <environment: namespace:stats> ## 2 <environment: 0x5639abb4c930> ## 3 <environment: namespace:base> ## 4 <environment: R_GlobalEnv> ## 5 <environment: package:codetools> ## 6 <environment: package:fields> ## 7 <environment: package:maps> ## 8 <environment: package:spam> ## 9 <environment: package:grid> ## 10 <environment: package:dotCall64> ## 11 <environment: package:R6> ## 12 <environment: package:dplyr> ## 13 <environment: package:pryr> ## 14 <environment: package:knitr> ## 15 <environment: package:stats> ## 16 <environment: package:graphics> ## 17 <environment: package:grDevices> ## 18 <environment: package:utils> ## 19 <environment: package:datasets> ## 20 <environment: package:SCF> ## 21 <environment: package:methods> ## 22 <environment: 0x5639ab98e310> ## 23 <environment: base> ## 24 <environment: R_EmptyEnv> ## name ## 1 "" ## 2 "imports:stats" ## 3 "" ## 4 "" ## 5 "package:codetools" ## 6 "package:fields" ## 7 "package:maps"

- ## 8 "package:spam" ## 9 "package:grid" ## 10 "package:dotCall64" ## 11 "package:R6"

64

---

[← Unit 05 — programming Part 36 —](36-unit-05-programming-part-36.md) · [Up: contents](index.md) · [Unit 05 — programming Part 38 — →](38-unit-05-programming-part-38.md)
