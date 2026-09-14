---
title: Consider contraction
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Consider contraction

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

xh = xs[2,:]  # Suppose the original point is better than the reflection
xc = beta * xh + (1 - beta) * xbar
plt.plot(xc[0], xc[1], 'ro', marker='o', markersize=4, color='blue')
plt.text(xc[0], xc[1], 'x[c]')

plotseg(xc, 0, 'blue')
plotseg(xc, 1, 'blue')
plotseg(0, 1, 'blue')

---

[← Consider expansion](19-consider-expansion.md) · [Up: contents](index.md) · [Shrinkage →](21-shrinkage.md)
