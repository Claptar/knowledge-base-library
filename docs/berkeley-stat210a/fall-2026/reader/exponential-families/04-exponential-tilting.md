---
title: Exponential tilting
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Exponential tilting

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

To help interpret what it means for a model to have an exponential family structure, we can think of $p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x)$ as an *exponential tilt* of the carrier density $h(x)$. That is, beginning with $h(x)$, we first multiply by $e^{\eta'T(x)}$, increasing the density of points in the sample space for which $\eta'T(x)$ is largest relative to those for which $\eta'T(x)$ is smaller. Then, we re-normalize by $e^{-A(\eta)}$ to obtain a probability distribution.

This is easiest to understand in a one-parameter family with sufficient statistic $T(X) = X$, (need to finish)

---

[← Other parameterizations](03-other-parameterizations.md) · [Up: contents](index.md) · [Visualization of exponential tilting →](05-visualization-of-exponential-tilting.md)
