---
title: Initial polytope
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Initial polytope

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

xs = np.array([[-2, 3], [-6, 4], [-4, 2]], dtype=np.float64)

plt.figure()
plt.plot(xs[:, 0], xs[:, 1], 'o-', color = 'black')
plt.xlim(-7, -1)
plt.ylim(1, 8)

plotseg(0, 1, 'black')
plotseg(0, 2, 'black')
plotseg(1, 2, 'black')

xbar = np.mean(xs[:2], axis=0)
plt.text(xs[2, 0], xs[2, 1], 'x[p+1]')
plt.plot(xbar[0], xbar[1], 'ro')

---

[← Auxiliary function to plot line segments](16-auxiliary-function-to-plot-line-segments.md) · [Up: contents](index.md) · [Reflection →](18-reflection.md)
