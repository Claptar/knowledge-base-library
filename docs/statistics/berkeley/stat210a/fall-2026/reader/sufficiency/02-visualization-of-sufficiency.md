---
title: Visualization of sufficiency
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Visualization of sufficiency

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The applet below illustrates the concept of sufficiency for a pair of random variables $X_1,X_2 \simiid p_\theta(x)$, where $p_\theta(x)$ is a univariate probability mass function on $\{0,\ldots,n\}$. We illustrate two cases, first the case where $p_\theta(x)$ is the binomial
$$
p_\theta(x) = \binom{n}{x}\theta^x(1-\theta)^{n-x},
$$
and second the case where $p_\theta(x)$ is a simple pmf we can call the "discrete Laplace" on $\{0,\ldots,n\}$ that decays exponentially with $|x-n \theta|$:
$$
p_\theta(x) \propto e^{-|x-n\theta|}.
$$
As we will see shortly, $T(X) = X_1+X_2$ is a sufficient statistic in the binomial case, but it is not sufficient in the discrete Laplace case. To see this directly, select a value of $n$ and $t$, and observe how the conditional distribution of $X$ given $T(X)=t$ does or does not change as you adjust the value of $\theta$.

In either case, changing $\theta$ has a major effect on the joint probability distribution of $X = (X_1,X_2)$; that is precisely why observing $X$ is informative about $\theta$. But in the binomial case, having already observed $T(X)$, $\theta$ has *no effect* on the conditional distribution of $X$; that is why observing $X$ gives us no additional information about $\theta$, once we've already seen $T(X)$. In the discrete Laplace case, $T(X)$ is not sufficient: if $\theta = 0.3$, $X = (1,2)$ is much more likely than $X=(0,3)$; but as $\theta$ approaches $0$ or $1$ they become equally likely.

```ojs
//| echo: false

// Binomial probability mass function
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

To understand why $T(X)$ is sufficient in the binomial case, we can make a simple calculation on the joint pmf of the random vector $X = (X_1,X_2)$:
$$
\begin{aligned}
\PP_\theta(X = x) &= \binom{n}{x_1} \theta^{x_1}(1-\theta)^{n-x_1} \cdot \binom{n}{x_2} \theta^{x_2}(1-\theta)^{n-x_2}\\[7pt]
&= \theta^{T(x)}(1-\theta)^{2n-T(x)} \binom{n}{x_1}\binom{n}{x_2},
\end{aligned}
$$

When we calculate the conditional distribution of $X$ given $T(X) = t$ by Bayes' rule, the factor that depends on $\theta$ drops out as before:
$$
\begin{aligned}
\PP_\theta(X = x \mid T(X) = t) &= \frac{\theta^{t}(1-\theta)^{2n-t} \binom{n}{x_1}\binom{n}{x_2}1\{x_1+x_2=t\} }{\sum_{k=0}^t \theta^t(1-\theta)^{2n-t} \binom{n}{k}\binom{n}{t-k}}\cdot\\[7pt]
&= \frac{\binom{n}{x_1}\binom{n}{x_2}1\{x_1+x_2=t\}}{\sum_{k=0}^t \binom{n}{k}\binom{n}{t-k}},
\end{aligned}
$$
giving a conditional distribution with no dependence on $\theta$. Applying the combinatorial identity $\sum_{k=0}^t \binom{n}{k}\binom{n}{t-k} = \binom{2n}{t}$, we obtain a hypergeometric distribution for $x_1$ (or for $x_2$):
$$
\PP_\theta(X_1 = x_1 \mid T(X) = t) = \frac{\binom{n}{x_1}\binom{n}{t-x_1}}{\binom{2n}{t}} = \text{Hypergeom}(2n,n,t).
$$

The next section generalizes this calculation to any density that can be factorized in a similar way, giving us an easy way to recognize sufficient statistics just by inspecting the joint density.

---

[← Sufficiency](01-sufficiency.md) · [Up: contents](index.md) · [Factorization theorem →](03-factorization-theorem.md)
