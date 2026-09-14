---
title: Unit 04 — programming partial Part 38 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 38 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are a variety of functions for converting between wide and long formats. I’d recommend the gather() and spread() functions in the tidyr package. There are also the melt() and cast() in the reshape2 package. These are easier to use than the functions in base R such as reshape() or stack() and unstack() functions.

### 5.3 Non-standard evaluation and the tidyverse

Many tidyverse packages use non-standard evaluation to make it easier to code. For example in the following dplyr example, you can refer directly to country and unemp, which are variables in the data frame, without using data$country or data$unemp and without using “country” or “unemp”.

**library** (dplyr)

cpds <- **read.csv** ( **file.path** ('..', 'data', 'cpds.csv'), stringsAsFactors = FALSE) cpds2 <- cpds %>% **group_by** (country) %>% **mutate** (mean_unemp = **mean** (unemp)) **head** (cpds2) ## # A tibble: 6 x 7 ## # Groups: country [1] ## year country vturn outlays realgdpgr unemp ## <int> <chr> <dbl> <dbl> <dbl> <dbl> ## 1 1960 Australia 95.5 NA NA 1.42 ## 2 1961 Australia 95.3 NA -0.07 2.79

37

---

[← 5 Standard dataset manipulations](37-5-standard-dataset-manipulations.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 39 — →](39-unit-04-programming-partial-part-39.md)
