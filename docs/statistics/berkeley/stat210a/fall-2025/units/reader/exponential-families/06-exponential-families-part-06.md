---
title: Exponential families Part 06 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exponential families Part 06 —

**Source:** [`units/reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Below we visualize an exponential family with `triangular'' base density $h(x) = \max\{0, 1-|x|\}$ and three sufficient statistics $T_1(X) = X, T_2(X) = X^2, and T_3(X) = \cos(100 X)$. Use the dials to`tilt’’ the density toward each statistic, and see how the density changes.

``` {.sourceCode .js .code-with-copy}
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

[← Exponential tilting {.anchored anchor-id="exponential-tilting"}](05-exponential-tilting-anchored-anchor-id-exponential-tilting.md) · [Up: contents](index.md) · [Exponential families Part 07 — →](07-exponential-families-part-07.md)
