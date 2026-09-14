---
title: Exponential tilting
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exponential tilting

**Source:** [`units/reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

To help interpret what it means for a model to have an exponential family structure, we can think of <span class="math inline">\$p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)} h(x)\$</span> as an *exponential tilt* of the carrier density <span class="math inline">\$h(x)\$</span>. That is, beginning with <span class="math inline">\$h(x)\$</span>, we first multiply by <span class="math inline">\$e^{\\eta'T(x)}\$</span>, increasing the density of points in the sample space for which <span class="math inline">\$\\eta'T(x)\$</span> is largest relative to those for which <span class="math inline">\$\\eta'T(x)\$</span> is smaller. Then, we re-normalize by <span class="math inline">\$e^{-A(\\eta)}\$</span> to obtain a probability distribution.

This is easiest to understand in a one-parameter family with sufficient statistic <span class="math inline">\$T(X) = X\$</span>, (need to finish)

---

[← Other parameterizations](04-other-parameterizations.md) · [Up: contents](index.md) · [Visualization of exponential tilting →](06-visualization-of-exponential-tilting.md)
