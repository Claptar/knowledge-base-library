---
title: Consider expansion
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Consider expansion

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

xe = gamma * xr + (1 - gamma) * xbar
plt.plot(xe[0], xe[1], 'ro', marker='o', markersize=4, color='green')
plt.text(xe[0], xe[1], 'x[e]')

plotseg(xe, 0, 'green')
plotseg(xe, 1, 'green')
plotseg(0, 1, 'green')

---

[← Reflection](18-reflection.md) · [Up: contents](index.md) · [Consider contraction →](20-consider-contraction.md)
