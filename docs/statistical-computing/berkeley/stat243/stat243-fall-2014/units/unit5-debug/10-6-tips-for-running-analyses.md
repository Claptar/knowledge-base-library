---
title: 6 Tips for running analyses
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Tips for running analyses

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Save your output at intermediate steps (including the random seed state) so you can restart if an error occurs or a computer fails. Using _save()_ and _save.image()_ to write to _.RData_ files work well for this.

14

Run your code on a small subset of the problem before setting off a job that runs for hours or days. Make sure that the code works on the small subset and saves what you need properly at the end.

---

[← 5 Good coding practices](09-5-good-coding-practices.md) · [Up: contents](index.md) · [7 Reproducible research →](11-7-reproducible-research.md)
