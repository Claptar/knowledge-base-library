---
title: Visualization of exponential tilting
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Visualization of exponential tilting

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Below we visualize an exponential family with ``triangular'' base density $h(x) = \max\{0, 1-|x|\}$ and three sufficient statistics $T_1(X) = X, T_2(X) = X^2, and T_3(X) = \cos(100 X)$. Use the dials to ``tilt'' the density toward each statistic, and see how the density changes.

```ojs
//| echo: false

// Import libraries
Plot = require("@observablehq/plot")
d3 = require("d3")

katex = require("https://cdn.jsdelivr.net/npm/katex@0.16.7/dist/katex.min.js")

// Function to render LaTeX
function tex(string) {
  let span = document.createElement('span');
  katex.render(string, span, {output: "mathml", throwOnError: false});
  return span;
}

// Create sliders for mean and standard deviation
viewof eta1 = Inputs.range([-5, 5], {step: 0.1, label: tex("\\eta_1"), value: 0})
viewof eta2 = Inputs.range([-5, 5], {step: 0.1, label: tex("\\eta_2"), value: 0})
viewof eta3 = Inputs.range([-0.3, 0.3], {step: 0.01, label: tex("\\eta_3"), value: 0})

// Function to generate normal distribution data
function explDistribution(eta1, eta2, eta3, n = 2000) {
  const x = d3.range(-1, 1, 2/n);
  const unnorm = x.map(x => ({
    x: x,
    y: Math.exp(eta1 * x + eta2 * x * x + eta3 * Math.cos(30 * x * Math.PI)) * (1 - Math.abs(x))
  }));
  const normConst = d3.sum(unnorm, point => point.y) * 2 / n;
  return unnorm.map(point => ({
    x: point.x,
    y: point.y / normConst
  }));
}

// Create the plot
Plot.plot({
  width: 640,
  height: 400,
  x: {label: "X"},
  y: {label: "Density"},
  marks: [
    Plot.line(explDistribution(eta1, eta2, eta3), {x: "x", y: "y", stroke: "steelblue"}),
    Plot.ruleY([0])
  ]
})
```

---

[← Exponential tilting](04-exponential-tilting.md) · [Up: contents](index.md) · [Repeated sampling from exponential families →](06-repeated-sampling-from-exponential-families.md)
