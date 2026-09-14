---
title: Unit 04 — programming partial Part 39 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 39 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This ’magic’ is done by capturing the code expression you write and evaluating it in a special way in the context of the data frame. I believe this uses R’s environment class (discussed in Section 6), but haven’t looked more deeply.

While this has benefits, this so-called non-standard evaluation makes it harder to program functions in the usual way. (For some reason the error messages from running the following chunk are not being printed in the PDF, but you can see them by running the code yourself.)

add_mean <- **function** (data, group_var, summarize_var) { data %>% **group_by** (group_var) %>% **mutate** (mean_of_var = **mean** (summarize_var)) } **try** (cpds2 <- **add_mean** (cpds, country, unemp)) **try** (cpds2 <- **add_mean** (cpds, 'country', 'unemp'))

For more details on how to avoid this problem when writing functions that involve tidyverse manipulations, see https://dplyr.tidyverse.org/articles/programming.html.

---

[← Unit 04 — programming partial Part 38 —](38-unit-04-programming-partial-part-38.md) · [Up: contents](index.md) · [6 Functions, variable scope, and frames →](40-6-functions-variable-scope-and-frames.md)
