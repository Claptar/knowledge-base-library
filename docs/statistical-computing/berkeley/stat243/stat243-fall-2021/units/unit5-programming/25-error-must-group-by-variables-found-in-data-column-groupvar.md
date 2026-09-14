---
title: 'Error : Must group by variables found in .data . ## Column groupvar is not
  found.'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Error : Must group by variables found in .data . ## Column groupvar is not found.

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For more details on how to avoid this problem when writing functions that involve tidyverse manipulations, see https://dplyr.tidyverse.org/articles/programming.html.

Note that the tidyverse is not the only place where non-standard evaluation is used. Consider this _lm()_ call:

**<mark>lm</mark>** <mark>(y ~ x, weights = w, data = mydf)</mark>

Where is the non-standard evaluation there?

---

[← 5 Standard dataset manipulations](24-5-standard-dataset-manipulations.md) · [Up: contents](index.md) · [6 Functions, frames, and variable scope →](26-6-functions-frames-and-variable-scope.md)
