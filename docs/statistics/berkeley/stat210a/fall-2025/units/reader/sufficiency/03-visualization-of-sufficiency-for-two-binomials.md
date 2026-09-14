---
title: Visualization of sufficiency for two binomials
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Visualization of sufficiency for two binomials

**Source:** [`units/reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We now illustrate the concept of sufficiency with a visualization for a closely related example where now the initial data set is a pair of independent binomial random variables <span class="math inline">\$X\_1, X\_2 \\simiid \\text{Binom}(n, \\theta)\$</span>. We can make a similar calculation to show that <span class="math inline">\$T(X) = X\_1 + X\_2\$</span> is sufficient:

<span class="math display">\\$$ p\_\\theta(x) = \\binom{n}{x\_1} \\theta^{x\_1}(1-\\theta)^{n-x\_1} \\cdot \\binom{n}{x\_2} \\theta^{x\_2}(1-\\theta)^{n-x\_2} = \\theta^{T(x)}(1-\\theta)^{2n-T(x)} \\binom{n}{x\_1}\\binom{n}{x\_2}. \\$$</span>

``` {.sourceCode .js .code-with-copy}
binomPMF = (k, n, p) => {
  if (k < 0 || k > n) return 0;
  const binomCoeff = factorial(n) / (factorial(k) * factorial(n - k));
  return binomCoeff * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

// Factorial function with memoization
factorial = (n) => {
  if (n <= 1) return 1;
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

// Interactive controls
viewof n = Inputs.range([1, 8], {value: 4, step: 1, label: "n"})
viewof theta = Inputs.range([0.01, 0.99], {value: 0.30, step: 0.01, label: "θ"})
viewof t_select = Inputs.range([0, 2*n], {value: Math.min(3, 2*n), step: 1, label: "T = t"})

// Generate joint distribution data
jointData = {
  const data = [];
  for (let x1 = 0; x1 <= n; x1++) {
    for (let x2 = 0; x2 <= n; x2++) {
      const prob = binomPMF(x1, n, theta) * binomPMF(x2, n, theta);
      const t = x1 + x2;
      data.push({
        x1: x1,
        x2: x2,
        prob: prob,
        t: t,
        selected: t === t_select
      });
    }
  }
  return data;
}

// Generate conditional distribution data (X given T = t)
conditionalData = {
  const data = [];
  const totalT = Math.min(t_select, 2 * n);

  // Find all (x1, x2) pairs where x1 + x2 = t
  const validPairs = jointData.filter(d => d.t === totalT);
  const totalCondProb = validPairs.reduce((sum, d) => sum + d.prob, 0);

  validPairs.forEach(d => {
    if (totalCondProb > 0) {
      data.push({
        x1: d.x1,
        x2: d.x2,
        condProb: d.prob / totalCondProb,
        t: d.t
      });
    }
  });

  return data;
}

// Calculate maximum probability for scaling
maxProb = Math.max(...jointData.map(d => d.prob))
maxCondProb = conditionalData.length > 0 ? Math.max(...conditionalData.map(d => d.condProb)) : 1

// Generate marginal distributions
marginalX1 = {
  const data = [];
  for (let x1 = 0; x1 <= n; x1++) {
    data.push({
      x1: x1,
      prob: binomPMF(x1, n, theta)
    });
  }
  return data;
}

marginalX2 = {
  const data = [];
  for (let x2 = 0; x2 <= n; x2++) {
    data.push({
      x2: x2,
      prob: binomPMF(x2, n, theta)
    });
  }
  return data;
}

// Generate conditional marginal distributions
conditionalMarginalX1 = {
  const data = [];
  const totalT = Math.min(t_select, 2 * n);

  // Calculate total probability for normalization
  let totalProb = 0;
  for (let x1 = Math.max(0, totalT - n); x1 <= Math.min(n, totalT); x1++) {
    const x2 = totalT - x1;
    if (x2 >= 0 && x2 <= n) {
      totalProb += binomPMF(x1, n, theta) * binomPMF(x2, n, theta);
    }
  }

  for (let x1 = 0; x1 <= n; x1++) {
    const x2 = totalT - x1;
    if (x2 >= 0 && x2 <= n && totalProb > 0) {
      const jointProb = binomPMF(x1, n, theta) * binomPMF(x2, n, theta);
      data.push({
        x1: x1,
        prob: jointProb / totalProb
      });
    }
  }
  return data;
}

conditionalMarginalX2 = {
  const data = [];
  const totalT = Math.min(t_select, 2 * n);

  // Calculate total probability for normalization
  let totalProb = 0;
  for (let x2 = Math.max(0, totalT - n); x2 <= Math.min(n, totalT); x2++) {
    const x1 = totalT - x2;
    if (x1 >= 0 && x1 <= n) {
      totalProb += binomPMF(x1, n, theta) * binomPMF(x2, n, theta);
    }
  }

  for (let x2 = 0; x2 <= n; x2++) {
    const x1 = totalT - x2;
    if (x1 >= 0 && x1 <= n && totalProb > 0) {
      const jointProb = binomPMF(x1, n, theta) * binomPMF(x2, n, theta);
      data.push({
        x2: x2,
        prob: jointProb / totalProb
      });
    }
  }
  return data;
}

maxMarginalProb = Math.max(...marginalX1.map(d => d.prob), ...marginalX2.map(d => d.prob))
maxCondMarginalProb = conditionalMarginalX1.length > 0 && conditionalMarginalX2.length > 0 ?
  Math.max(...conditionalMarginalX1.map(d => d.prob), ...conditionalMarginalX2.map(d => d.prob)) : 1

// Create joint distribution plot with marginal histograms
jointPlot = Plot.plot({
  width: 480,
  height: 480,
  marginTop: 140,
  marginLeft: 80,
  marginBottom: 80,
  marginRight: 120,
  style: { fontSize: "16px" },

  r: {
    domain: [0, 20],  // Fixed domain from 0 to 20
    range: [0, 20],   // Maps directly to pixel sizes
    clamp: true       // Prevents values outside domain
  },


  x: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50
  },

  marks: [
    // Grid lines
    Plot.ruleX(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),
    Plot.ruleY(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),

    // Probability circles
    Plot.dot(jointData, {
      x: "x1",
      y: "x2",
      r: d => Math.sqrt(d.prob / maxProb) * 15,
      fill: d => d.selected ? "red" : "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Top marginal histogram (X₁)
    Plot.rect(marginalX1, {
      x1: d => d.x1 - 0.3,
      x2: d => d.x1 + 0.3,
      y1: n + 0.56 + n * .06,
      y2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb) * n * 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right marginal histogram (X₂)
    Plot.rect(marginalX2, {
      x1: n + 0.56 + n * .06,
      x2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb) * n * 0.3,
      y1: d => d.x2 - 0.3,
      y2: d => d.x2 + 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Title
    Plot.text(["Joint Distribution of X = (X₁, X₂)"], {
      x: n/2,
      y: n + 0.56 + n * .5,
      fontSize: 24,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})

// Create conditional distribution plot with conditional marginal histograms
conditionalPlot = Plot.plot({
  width: 480,
  height: 480,
  marginTop: 140,
  marginLeft: 80,
  marginBottom: 80,
  marginRight: 120,
  style: { fontSize: "16px" },

  r: {
    domain: [0, 20],  // Fixed domain from 0 to 20
    range: [0, 20],   // Maps directly to pixel sizes
    clamp: true       // Prevents values outside domain
  },
  x: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50
  },

  marks: [
    // Grid lines
    Plot.ruleX(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),
    Plot.ruleY(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),

    // All possible points (faded)
    Plot.dot(jointData, {
      x: "x1",
      y: "x2",
      r: 3,
      fill: "lightgray",
      fillOpacity: 0.3
    }),

    // Conditional probability circles
    Plot.dot(conditionalData, {
      x: "x1",
      y: "x2",
      r: d => conditionalData.length > 0 ? Math.sqrt(d.condProb / maxCondProb) * 15 : 5,
      fill: "red",
      fillOpacity: 0.8,
      stroke: "black",
      strokeWidth: 1
    }),

    // Top conditional marginal histogram (X₁ | T = t)
    Plot.rect(conditionalMarginalX1, {
      x1: d => d.x1 - 0.3,
      x2: d => d.x1 + 0.3,
      y1: n + 0.56 + n * .06,
      y2: d => n + 0.56 + n * .06 + (d.prob / maxCondMarginalProb) * n * 0.3,
      fill: "red",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right conditional marginal histogram (X₂ | T = t)
    Plot.rect(conditionalMarginalX2, {
      x1: n + 0.56 + n * .06,
      x2: d => n + 0.56 + n * .06 + (d.prob / maxCondMarginalProb) * n * 0.3,
      y1: d => d.x2 - 0.3,
      y2: d => d.x2 + 0.3,
      fill: "red",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Title
    Plot.text([`Conditional Distribution P(X | T = ${t_select})`], {
      x: n/2,
      y: n + 0.56 + n * .5,
      fontSize: 24,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})

// Display plots side by side
html`<div style="display: flex; gap: 20px; align-items: center; justify-content: center;">
  ${jointPlot}
  ${conditionalPlot}
</div>`
```

---

[← Sufficiency](02-sufficiency.md) · [Up: contents](index.md) · [Factorization theorem →](04-factorization-theorem.md)
