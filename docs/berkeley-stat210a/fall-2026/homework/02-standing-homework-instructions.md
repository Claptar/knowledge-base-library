---
title: Standing homework instructions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework.qmd
source_file: sources/berkeley-stat210a/fall-2026/homework.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Standing homework instructions

**Source:** [`homework.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Submission format

All homework will be submitted electronically, on Gradescope. Homework submissions do not need to be typeset in LaTeX, and they can be handwritten unless code or figures are required, so long as they are legible; points may be deducted for solutions that are difficult to read. Code can be written in any common programming language: R, Python, and Matlab are all acceptable, but if you want to use something more exotic, check with the GSI first.

If you need to write code to answer a question, show your code. If you need to include a plot, make sure the plot is readable, with appropriate axis labels and a legend if necessary. Points will be deducted for very hard-to-read code or plots.

### Monte Carlo methods

Anytime I ask you to calculate something numerically, it is implicit that Monte Carlo integration (calculating an expectation by repeatedly sampling data from an appropriate distribution and taking the average) is a valid numerical method. There is no need to ask permission, but please use good judgment about how many samples to take so that your numerical error is not too high: if you report a number it should be correct to a few significant digits; if you are comparing two numbers, the precision of your calculation should be high enough for the difference to be meaningful; and plots of smooth functions should appear smooth enough for the plot to be readable.

### Other conventions

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, "all functions" vs. "all measurable functions," etc. (unless the problem is explicitly asking about such issues).

Unless otherwise stated, assume asymptotic limits are taken as $n\to \infty$. If I ask for a "limiting distribution," I mean do an appropriate centering and scaling to find a limiting distribution that is non-degenerate (not converging in probability to a constant). That is, find sequences $a_n$ and $b_n$ such that $b_n(X_n−a_n)$ converges to a non-degenerate limiting distribution.

---

[← Assignments](01-assignments.md) · [Up: contents](index.md)
