---
title: Visualization of sufficiency
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Visualization of sufficiency

**Source:** [`reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

The applet below illustrates the concept of sufficiency for a pair of random variables <span class="math inline">\$X\_1,X\_2 \\simiid p\_\\theta(x)\$</span>, where <span class="math inline">\$p\_\\theta(x)\$</span> is a univariate probability mass function on <span class="math inline">\$\\{0,\\ldots,n\\}\$</span>. We illustrate two cases, first the case where <span class="math inline">\$p\_\\theta(x)\$</span> is the binomial <span class="math display">\\$$ p\_\\theta(x) = \\binom{n}{x}\\theta^x(1-\\theta)^{n-x}, \\$$</span> and second the case where <span class="math inline">\$p\_\\theta(x)\$</span> is a simple pmf we can call the “discrete Laplace” on <span class="math inline">\$\\{0,\\ldots,n\\}\$</span> that decays exponentially with <span class="math inline">\$\|x-n \\theta\|\$</span>: <span class="math display">\\$$ p\_\\theta(x) \\propto e^{-\|x-n\\theta\|}. \\$$</span> As we will see shortly, <span class="math inline">\$T(X) = X\_1+X\_2\$</span> is a sufficient statistic in the binomial case, but it is not sufficient in the discrete Laplace case. To see this directly, select a value of <span class="math inline">\$n\$</span> and <span class="math inline">\$t\$</span>, and observe how the conditional distribution of <span class="math inline">\$X\$</span> given <span class="math inline">\$T(X)=t\$</span> does or does not change as you adjust the value of <span class="math inline">\$\\theta\$</span>.

In either case, changing <span class="math inline">\$\\theta\$</span> has a major effect on the joint probability distribution of <span class="math inline">\$X = (X\_1,X\_2)\$</span>; that is precisely why observing <span class="math inline">\$X\$</span> is informative about <span class="math inline">\$\\theta\$</span>. But in the binomial case, having already observed <span class="math inline">\$T(X)\$</span>, <span class="math inline">\$\\theta\$</span> has *no effect* on the conditional distribution of <span class="math inline">\$X\$</span>; that is why observing <span class="math inline">\$X\$</span> gives us no additional information about <span class="math inline">\$\\theta\$</span>, once we’ve already seen <span class="math inline">\$T(X)\$</span>. In the discrete Laplace case, <span class="math inline">\$T(X)\$</span> is not sufficient: if <span class="math inline">\$\\theta = 0.3\$</span>, <span class="math inline">\$X = (1,2)\$</span> is much more likely than <span class="math inline">\$X=(0,3)\$</span>; but as <span class="math inline">\$\\theta\$</span> approaches <span class="math inline">\$0\$</span> or <span class="math inline">\$1\$</span> they become equally likely.

``` {.sourceCode .js .code-with-copy}
binomPMF = (k, n, p) => {
  if (k < 0 || k > n) return 0;
  const binomCoeff = factorial(n) / (factorial(k) * factorial(n - k));
  return binomCoeff * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

// Exponential-based probability mass function
expPMF = (k, n, theta) => {
  if (k < 0 || k > n) return 0;
  // Calculate unnormalized probabilities
  const unnormalized = [];
  let sum = 0;
  for (let i = 0; i <= n; i++) {
    const val = Math.exp(-Math.abs(i - n * theta));
    unnormalized.push(val);
    sum += val;
  }
  // Return normalized probability
  return unnormalized[k] / sum;
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
viewof distributionType = Inputs.radio(["Binomial", "Discrete Laplace"], {value: "Binomial", label: "Distribution"})

// Select which PMF to use based on dropdown selection
pmf = distributionType === "Binomial" ? binomPMF : expPMF

// Generate joint distribution data
jointData = {
  const data = [];
  for (let x1 = 0; x1 <= n; x1++) {
    for (let x2 = 0; x2 <= n; x2++) {
      const prob = pmf(x1, n, theta) * pmf(x2, n, theta);
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

  // Only process if t_select is valid
  if (t_select <= 2 * n) {
    // Find all (x1, x2) pairs where x1 + x2 = t
    const validPairs = jointData.filter(d => d.t === t_select);
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
  }

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
      prob: pmf(x1, n, theta)
    });
  }
  return data;
}

marginalX2 = {
  const data = [];
  for (let x2 = 0; x2 <= n; x2++) {
    data.push({
      x2: x2,
      prob: pmf(x2, n, theta)
    });
  }
  return data;
}

// Generate conditional marginal distributions
conditionalMarginalX1 = {
  const data = [];
  const totalT = Math.min(t_select, 2 * n);

  // Only process if t_select is valid
  if (t_select <= 2 * n) {
    // Calculate total probability for normalization
    let totalProb = 0;
    for (let x1 = Math.max(0, totalT - n); x1 <= Math.min(n, totalT); x1++) {
      const x2 = totalT - x1;
      if (x2 >= 0 && x2 <= n) {
        totalProb += pmf(x1, n, theta) * pmf(x2, n, theta);
      }
    }

    for (let x1 = 0; x1 <= n; x1++) {
      const x2 = totalT - x1;
      if (x2 >= 0 && x2 <= n && totalProb > 0) {
        const jointProb = pmf(x1, n, theta) * pmf(x2, n, theta);
        data.push({
          x1: x1,
          prob: jointProb / totalProb
        });
      }
    }
  }
  return data;
}

conditionalMarginalX2 = {
  const data = [];
  const totalT = Math.min(t_select, 2 * n);

  // Only process if t_select is valid
  if (t_select <= 2 * n) {
    // Calculate total probability for normalization
    let totalProb = 0;
    for (let x2 = Math.max(0, totalT - n); x2 <= Math.min(n, totalT); x2++) {
      const x1 = totalT - x2;
      if (x1 >= 0 && x1 <= n) {
        totalProb += pmf(x1, n, theta) * pmf(x2, n, theta);
      }
    }

    for (let x2 = 0; x2 <= n; x2++) {
      const x1 = totalT - x2;
      if (x1 >= 0 && x1 <= n && totalProb > 0) {
        const jointProb = pmf(x1, n, theta) * pmf(x2, n, theta);
        data.push({
          x2: x2,
          prob: jointProb / totalProb
        });
      }
    }
  }
  return data;
}

maxRad = 15 * 5 / (n + 1)

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
  style: { fontSize: "20px" },

  r: {
    type: "linear",
    domain: [0, maxRad],  // Fixed domain from 0 to maxRad
    range: [0, maxRad],   // Maps directly to pixel sizes
    clamp: false       // Prevents values outside domain
  },


  x: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },

  marks: [
    // Grid lines
    Plot.ruleX(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),
    Plot.ruleY(Array.from({length: n + 1}, (_, i) => i), {stroke: "#f0f0f0"}),

    // Probability circles
    Plot.dot(jointData, {
      x: "x1",
      y: "x2",
      r: d => Math.sqrt(d.prob / maxProb) * maxRad,
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
      y2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb) * (n + 1) * 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right marginal histogram (X₂)
    Plot.rect(marginalX2, {
      x1: n + 0.56 + n * .06,
      x2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb) * (n + 1) * 0.3,
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
      y: n + 0.5 + (n + 1) * .45,
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
  style: { fontSize: "20px" },

  r: {
    type: "linear",
    domain: [0, maxRad],  // Fixed domain from 0 to 20
    range: [0, maxRad],   // Maps directly to pixel   sizes
    clamp: false       // Prevents values outside domain
  },
  x: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: n + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
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
      r: d => conditionalData.length > 0 ? Math.sqrt(d.condProb / maxCondProb) * maxRad : 5,
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
      y2: d => n + 0.56 + n * .06 + (d.prob / maxCondMarginalProb) * (n + 1) * 0.3,
      fill: "red",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right conditional marginal histogram (X₂ | T = t)
    Plot.rect(conditionalMarginalX2, {
      x1: n + 0.56 + n * .06,
      x2: d => n + 0.56 + n * .06 + (d.prob / maxCondMarginalProb) * (n + 1) * 0.3,
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
      y: n + 0.5 + (n + 1) * .45,
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

To understand why <span class="math inline">\$T(X)\$</span> is sufficient in the binomial case, we can make a simple calculation on the joint pmf of the random vector <span class="math inline">\$X = (X\_1,X\_2)\$</span>: <span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(X = x) &= \\binom{n}{x\_1} \\theta^{x\_1}(1-\\theta)^{n-x\_1} \\cdot \\binom{n}{x\_2} \\theta^{x\_2}(1-\\theta)^{n-x\_2}\\\\\[7pt$$ &= \\theta^{T(x)}(1-\\theta)^{2n-T(x)} \\binom{n}{x\_1}\\binom{n}{x\_2}, \\end{aligned} \\\]</span>

When we calculate the conditional distribution of <span class="math inline">\$X\$</span> given <span class="math inline">\$T(X) = t\$</span> by Bayes’ rule, the factor that depends on <span class="math inline">\$\\theta\$</span> drops out as before: <span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(X = x \\mid T(X) = t) &= \\frac{\\theta^{t}(1-\\theta)^{2n-t} \\binom{n}{x\_1}\\binom{n}{x\_2}1\\{x\_1+x\_2=t\\} }{\\sum\_{k=0}^t \\theta^t(1-\\theta)^{2n-t} \\binom{n}{k}\\binom{n}{t-k}}\\cdot\\\\\[7pt$$ &= \\frac{\\binom{n}{x\_1}\\binom{n}{x\_2}1\\{x\_1+x\_2=t\\}}{\\sum\_{k=0}^t \\binom{n}{k}\\binom{n}{t-k}}, \\end{aligned} \\\]</span> giving a conditional distribution with no dependence on <span class="math inline">\$\\theta\$</span>. Applying the combinatorial identity <span class="math inline">\$\\sum\_{k=0}^t \\binom{n}{k}\\binom{n}{t-k} = \\binom{2n}{t}\$</span>, we obtain a hypergeometric distribution for <span class="math inline">\$x\_1\$</span> (or for <span class="math inline">\$x\_2\$</span>): <span class="math display">\\$$ \\PP\_\\theta(X\_1 = x\_1 \\mid T(X) = t) = \\frac{\\binom{n}{x\_1}\\binom{n}{t-x\_1}}{\\binom{2n}{t}} = \\text{Hypergeom}(2n,n,t). \\$$</span>

The next section generalizes this calculation to any density that can be factorized in a similar way, giving us an easy way to recognize sufficient statistics just by inspecting the joint density.

---

[← Sufficiency](02-sufficiency.md) · [Up: contents](index.md) · [Factorization theorem →](04-factorization-theorem.md)
