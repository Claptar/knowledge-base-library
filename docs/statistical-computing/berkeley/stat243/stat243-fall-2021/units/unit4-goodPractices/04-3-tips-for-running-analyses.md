---
title: 3 Tips for running analyses
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit4-goodPractices.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Tips for running analyses

**Source:** [`units/unit4-goodPractices.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Save your output at intermediate steps (including the random seed state) so you can restart if an error occurs or a computer fails. Using _save()_ and _save.image()_ to write to _.Rda_ ( _.RData_ ) files work well for this.

Run your code on a small subset of the problem before setting off a job that runs for hours or days. Make sure that the code works on the small subset and saves what you need properly at the end.

---

[← 2 Debugging and recommendations for avoiding bugs](03-2-debugging-and-recommendations-for-avoiding-bugs.md) · [Up: contents](index.md) · [4 Reproducible research →](05-4-reproducible-research.md)
