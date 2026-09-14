---
title: 5 Standard dataset manipulations
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Standard dataset manipulations

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Base R provides a variety of functions for manipulating data frames, but now many researchers use add-on packages (many written by Hadley Wickham as part of a group of packages called the tidyverse) to do these manipulations in a more elegant, often more efficient way. Module 5 of the R bootcamp describes some of these new tools, but I’ll summarize them here.

### 5.1 split-apply-combine

Often analyses are done in a stratified fashion - the same operation or analysis is done on subsets of the data set. The subsets might be different time points, different locations, different hospitals, different people, etc.

The split-apply-combine framework is intended to operate in this kind of context: first one splits the dataset by one or more variables, then one does something to each subset, and then one combines the results. The plyr and dplyr packages implement this framework, with dplyr newer and faster. One can also do similar operations using various flavors of the apply() family of functions such as by(), tapply(), and aggregate(), but the dplyr-based tools are often nicer to use.

### 5.2 Long and wide formats

Finally, we may want to convert between so-called ’long’ and ’wide’ formats, which we can motivate in the context of longitudinal data (multiple observations per subject) and panel data (temporal data for each of multiple units such as in econometrics). The wide format has repeated measurements for a subject in separate columns, while the long format has repeated measurements in separate rows, with a column for differentiating the repeated measurements. The wide format is useful for doing separate analyses by group, while the long format is useful for doing a single analysis that makes use of the groups, such as ANOVA or mixed models or for plotting, such as with ggplot2.

long <- **data.frame** (id = **c** (1, 1, 2, 2), time = **c** (1980, 1990, 1980, 1990), value = **c** (5, 8, 7, 4)) wide <- **data.frame** (id = **c** (1, 2), value_1980 = **c** (5, 7), value_1990 = **c** (8, 4)) long ## id time value ## 1 1 1980 5

36

---

[← Unit 04 — programming partial Part 36 —](36-unit-04-programming-partial-part-36.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 38 — →](38-unit-04-programming-partial-part-38.md)
