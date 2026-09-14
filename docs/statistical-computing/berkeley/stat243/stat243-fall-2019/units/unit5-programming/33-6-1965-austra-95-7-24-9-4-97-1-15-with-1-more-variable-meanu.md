---
title: '6 1965 Austra~ 95.7 24.9 4.97 1.15 ## # ... with 1 more variable: meanunemp'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 1965 Austra~ 95.7 24.9 4.97 1.15 ## # ... with 1 more variable: meanunemp

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This ’magic’ is done by capturing the code expression you write and evaluating it in a special way in the context of the data frame. I believe this uses R’s environment class (discussed in Section 6), but haven’t looked more deeply.

While this has benefits, this so-called non-standard evaluation makes it harder to program functions in the usual way, as illustrated in the following code chunk, where neither attempt to use the function works.

add_mean <- **function** (data, group_var, summarize_var) { data %>% **group_by** (group_var) %>% **mutate** (mean_of_var = **mean** (summarize_var)) } **try** (cpds2 <- **add_mean** (cpds, country, unemp)) ## Error : Column `group_var` is unknown **try** (cpds2 <- **add_mean** (cpds, 'country', 'unemp')) ## Error : Column `group_var` is unknown

For more details on how to avoid this problem when writing functions that involve tidyverse manipulations, see https://dplyr.tidyverse.org/articles/programming.html.

Note that the tidyverse is not the only place where non-standard evaluation is used. Consider this _lm()_ call:

**<mark>lm</mark>** <mark>(y ~ x, weights = w, data = mydf)</mark>

Where is the non-standard evaluation there?

---

[← 5 Standard dataset manipulations](32-5-standard-dataset-manipulations.md) · [Up: contents](index.md) · [6 Functions, variable scope, and frames →](34-6-functions-variable-scope-and-frames.md)
