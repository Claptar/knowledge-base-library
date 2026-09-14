---
title: 3. Tips for running analyses
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit4-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Tips for running analyses

**Source:** [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Save your output at intermediate steps (including the random seed state)
so you can restart if an error occurs or a computer fails. Using
`pickle.dump()` to write to pickle files works
well for this.

Run your code on a small subset of the problem before setting off a job
that runs for hours or days. Make sure that the code works on the small
subset and saves what you need properly at the end.

---

[← 2. Debugging and recommendations for avoiding bugs](04-2-debugging-and-recommendations-for-avoiding-bugs.md) · [Up: contents](index.md) · [4. Reproducible research →](06-4-reproducible-research.md)
