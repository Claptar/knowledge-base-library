---
title: 3. Tips for running analyses
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit4-goodPractices.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Tips for running analyses

**Source:** [`units/unit4-goodPractices.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Save your output at intermediate steps (including the random seed state)
so you can restart if an error occurs or a computer fails. Using
*save()* and *save.image()* to write to *.Rda* (*.RData*) files work
well for this.

Run your code on a small subset of the problem before setting off a job
that runs for hours or days. Make sure that the code works on the small
subset and saves what you need properly at the end.

---

[← 2. Debugging and recommendations for avoiding bugs](03-2-debugging-and-recommendations-for-avoiding-bugs.md) · [Up: contents](index.md) · [4. Reproducible research →](05-4-reproducible-research.md)
