---
title: Standing homework instructions {.anchored anchor-id="standing-homework-instructions"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework.html
source_file: sources/berkeley-stat210a/fall-2025/units/homework.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Standing homework instructions {.anchored anchor-id="standing-homework-instructions"}

**Source:** [`units/homework.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/homework.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

If you need to write code to answer a question, show your code. If you need to include a plot, make sure the plot is readable, with appropriate axis labels and a legend if necessary. Points will be deducted for very hard-to-read code or plots.

Anytime I ask you to calculate things numerically, it is implicit that Monte Carlo integration (calculating an expectation by repeatedly sampling data from an appropriate distribution and taking the average) is a valid numerical method. There is no need to ask permission, but please use good judgment about how many samples to take so that your numerical error is not too high: if you report a number it should be correct to a few significant digits; if you are comparing two numbers, the precision of your calculation should be high enough for the difference to be meaningful; and plots of smooth functions should appear smooth enough for the plot to be readable.

Unless otherwise stated, assume asymptotic limits are taken as <span class="math inline">\$n\\to \\infty\$</span>. If I ask for a “limiting distribution,” I mean do an appropriate centering and scaling to find a limiting distribution that is non-degenerate (not converging in probability to a constant). That is, find sequences <span class="math inline">\$a\_n\$</span> and <span class="math inline">\$b\_n\$</span> such that <span class="math inline">\$b\_n(X\_n−a\_n)\$</span> converges to a non-degenerate limiting distribution.

---

[Up: contents](index.md) · [Assignments {.anchored anchor-id="assignments"} →](02-assignments-anchored-anchor-id-assignments.md)
