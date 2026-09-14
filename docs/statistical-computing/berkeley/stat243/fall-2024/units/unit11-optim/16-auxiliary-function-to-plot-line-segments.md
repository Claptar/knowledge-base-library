---
title: Auxiliary function to plot line segments
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Auxiliary function to plot line segments

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def plotseg(ind1, ind2, col=1):
    if not isinstance(ind1, np.ndarray):
        plt.plot([xs[ind1, 0], xs[ind2, 0]], [xs[ind1, 1], xs[ind2, 1],], color=col)
    else:
        plt.plot([ind1[0], xs[ind2, 0]], [ind1[1], xs[ind2, 1]], color=col)

---

[← 5. Multivariate optimization](15-5-multivariate-optimization.md) · [Up: contents](index.md) · [Initial polytope →](17-initial-polytope.md)
