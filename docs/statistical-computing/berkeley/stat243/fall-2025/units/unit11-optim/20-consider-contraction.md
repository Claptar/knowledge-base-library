---
title: Consider contraction
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Consider contraction

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

xh = xs[2,:]  # Suppose the original point is better than the reflection
xc = beta * xh + (1 - beta) * xbar
plt.plot(xc[0], xc[1], 'ro', marker='o', markersize=4, color='blue')
plt.text(xc[0], xc[1], 'x[c]')

plotseg(xc, 0, 'blue')
plotseg(xc, 1, 'blue')
plotseg(0, 1, 'blue')

---

[← Consider expansion](19-consider-expansion.md) · [Up: contents](index.md) · [Shrinkage →](21-shrinkage.md)
