---
title: Exponential families Part 06 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exponential families Part 06 —

**Source:** [`reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Below we visualize an exponential family on <span class="math inline">\$$$-1,1$$\$</span> with “triangular” base density <span class="math inline">\$h(x) = 1-\|x\|\$</span> and three sufficient statistics <span class="math inline">\$T\_1(X) = X, T\_2(X) = X^2,\$</span> and <span class="math inline">\$T\_3(X) = \\cos(100 X)\$</span>. That is, <span class="math display">\\$$ p\_\\eta(x) \\propto e^{\\eta\_1 x + \\eta\_2 x^2 + \\eta\_3 \\cos(100 x)} \\cdot (1-\|x\|) \\$$</span>

Use the sliders to “tilt” the density toward each statistic, and see how the density changes.

``` {.sourceCode .js .code-with-copy}
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

[← Exponential tilting {.anchored anchor-id="exponential-tilting"}](05-exponential-tilting-anchored-anchor-id-exponential-tilting.md) · [Up: contents](index.md) · [Exponential families Part 07 — →](07-exponential-families-part-07.md)
