---
title: Create a grid of x values
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create a grid of x values

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

x1, x2 = np.meshgrid(gr, gr)
xs = np.column_stack((x1.ravel(), x2.ravel()))

---

[← 4. Convergence ideas](08-4-convergence-ideas.md) · [Up: contents](index.md) · [Calculate the Rastrigin function for each point in the grid →](10-calculate-the-rastrigin-function-for-each-point-in-the-grid.md)
