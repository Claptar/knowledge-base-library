---
title: Visualization of exponential tilting
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Visualization of exponential tilting

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Below we visualize an exponential family on $[-1,1]$ with "triangular" base density $h(x) = 1-|x|$ and three sufficient statistics $T_1(X) = X, T_2(X) = X^2,$ and $T_3(X) = \cos(100 X)$. That is,
$$
p_\eta(x) \propto e^{\eta_1 x + \eta_2 x^2 + \eta_3 \cos(100 x)} \cdot (1-|x|)
$$

Use the sliders to "tilt" the density toward each statistic, and see how the density changes.

```ojs
//| echo: false

// Define the exponential family distribution function
explDistribution = (eta1, eta2, eta3, n = 2000) => {
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

// Interactive controls
viewof eta1 = Inputs.range([-5, 5], {step: 0.1, label: "η₁", value: 0})
viewof eta2 = Inputs.range([-5, 5], {step: 0.1, label: "η₂", value: 0})
viewof eta3 = Inputs.range([-0.3, 0.3], {step: 0.01, label: "η₃", value: 0})

// Generate data
data = explDistribution(eta1, eta2, eta3)

// Find maximum y value for plot scaling
maxY = d3.max(data, d => d.y)

// Create plot
Plot.plot({
  width: 800,
  height: 600,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: { fontSize: "18px" },

  x: {
    domain: [-1, 1],
    label: "X",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [0, maxY * 1.1],
    label: "Density",
    labelAnchor: "center",
    labelOffset: 70
  },

  marks: [
    Plot.line(data, {x: "x", y: "y", stroke: "steelblue", strokeWidth: 2}),
    Plot.ruleY([0]),

    // Title
    Plot.text(["Exponential Family Distribution"], {
      x: 0,
      y: maxY * 1.15,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})
```

---

[← Exponential tilting](04-exponential-tilting.md) · [Up: contents](index.md) · [Repeated sampling from exponential families →](06-repeated-sampling-from-exponential-families.md)
