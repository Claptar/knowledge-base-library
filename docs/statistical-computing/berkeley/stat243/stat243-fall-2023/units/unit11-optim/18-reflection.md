---
title: Reflection
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Reflection

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

xr = (1 + alpha) * xbar - alpha * xs[2]
plt.plot(xr[0], xr[1], 'ro', marker='o', markersize=4, color='red')
plt.text(xr[0], xr[1], 'x[r]')

plotseg(xr, 0, 'red')
plotseg(xr, 1, 'red')
plotseg(0, 1, 'red')

---

[← Initial polytope](17-initial-polytope.md) · [Up: contents](index.md) · [Consider expansion →](19-consider-expansion.md)
