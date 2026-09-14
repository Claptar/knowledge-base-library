---
title: Reflection
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Reflection

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

xr = (1 + alpha) * xbar - alpha * xs[2]
plt.plot(xr[0], xr[1], 'ro', marker='o', markersize=4, color='red')
plt.text(xr[0], xr[1], 'x[r]')

plotseg(xr, 0, 'red')
plotseg(xr, 1, 'red')
plotseg(0, 1, 'red')

---

[← Initial polytope](17-initial-polytope.md) · [Up: contents](index.md) · [Consider expansion →](19-consider-expansion.md)
