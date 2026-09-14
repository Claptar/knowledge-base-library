---
title: Multiparameter exponential families
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Multiparameter exponential families

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Consider a generic exponential family where we can partition the natural parameter into a parameter of interest $\theta\in\RR^s$ and nuisance parameter $\lambda\in\RR^r$:
$$
X \sim p_{\theta,\lambda}(x) = e^{\theta'T(x) + \lambda'U(x) - A(\theta,\lambda)}h(x).
$$
Both $\theta$ and $\lambda$ are assumed unknown, and we want to test a hypothesis about $\theta$ with $\lambda$ as a nuisance parameter, i.e. $H_0:\;\theta \in \Theta_0$ vs $H_1:\; \theta \in \Theta_1$. Our basic recipe is to condition on $U(X)$, and then base our inferences on the conditional model for $T(X)$, which depends on $\theta$ alone.

Without loss of generality, we can make a sufficiency reduction to $(T,U)$, since any test $\phi(X)$ has the same power function as $\psi(T(X),U(X))$ where $\psi(t,u) = \EE \left[\phi(X) \mid T=t,U=u\right]$. Then we have
$$
(T, U) \sim p_{\theta,\lambda}(t,u) = e^{\theta't + \lambda'u - A(\theta,\lambda)}g(t,u).
$$
When we calculate the conditional density for $T$ given $U$, the factor $e^{\lambda'u-A(\theta,\lambda)}$ in the numerator and denominator cancels, leaving
$$
q_\theta(t \mid u) = \frac{p_{\theta,\lambda}(t,u)}{\int p_{\theta,\lambda}(z,u)\,dz} = \frac{e^{\theta't} g(t,u)}{\int e^{\theta'z} g(z,u)\,dz} = e^{\theta't-B_u(\theta)} g(t,u),
$$
for $B_u(\theta) = \log\int e^{\theta'z}g(z,u)\,dz$. Because $q_\theta(t \mid u)$ is an exponential family with sufficient statistic $T$ and natural parameter $\theta$, the conditional model $\mathcal{Q}_u$ is an $s$-parameter exponential family, allowing for us to use standard techniques to perform inference on $\theta$ with $\lambda$ removed from the problem.

If $s=1$, the conditional model $\mathcal{Q}_u$ has monotone likelihood ratios in $T$. This makes conditional inference especially simple and appealing, leading to standard one- and two-sided conditional tests and conditional confidence intervals.

The Poisson comparison problem was an example of this:
$$
\begin{aligned}
p_{\mu,\nu}(x,y)
&= \frac{\mu^x e^{-\mu}}{x!}\cdot\frac{\nu^y e^{-\nu}}{y!} \\
&= \exp\{ x\log \mu + y\log \nu - (\mu+\nu) \}\cdot \frac{1}{x!y!}\\[5pt]
&= \exp\left\{ x\log \frac{\mu}{\nu} + (y+x)\log \nu - (\mu + \nu)\right\}\cdot \frac{1}{x!y!}
\end{aligned}
$$
By adding and subtracting $x\log \nu$ in the exponent in the last step, we have obtained a model of the desired form with $\theta = \log \frac{\mu}{\nu}$, $T(X,Y)=X$, $\lambda = \log \nu$, and $U(X,Y) = X+Y$. Thus, our general strategy tells us to condition on $X+Y$, and once we have done so the optimal conditional test rejects for large values of $X$.

As you will show in the problem set, the binomial comparison problem introduced in the first section is another example of this type of setting, which we can deal with in much the same way. The widget below illustrates how the conditional distribution given $T(X) = X_1+X_2$ depends only on the log odds ratio $\rho = \frac{\pi_1}{1-\pi_1} / \frac{\pi_2}{1-\pi_2}$, and not on the nuisance parameter $\pi_2$ (the case $n_1=n_2=n$ is illustrated, but the same is true for general $n_1,n_2$).


```ojs
//| echo: false

// Binomial probability mass function
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
viewof n = Inputs.range([4, 20], {value: 8, step: 1, label: "n"})
viewof theta2 = Inputs.range([0.01, 0.99], {value: 0.30, step: 0.01, label: "π₂"})
viewof rho = Inputs.range([0.02, 50], {value: 1, transform: Math.log, label: "ρ (odds ratio)"})
viewof t_select = Inputs.range([0, 2*n], {value: Math.min(6, 2*n), step: 1, label: "T = t"})

odds1 = rho * theta2 / (1-theta2)

theta1 = odds1 / (1 + odds1)

// Select which PMF to use based on dropdown selection
pmf = binomPMF

// Generate joint distribution data
jointData = {
  const data = [];
  for (let x1 = 0; x1 <= n; x1++) {
    for (let x2 = 0; x2 <= n; x2++) {
      const prob = pmf(x1, n, theta1) * pmf(x2, n, theta2);
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
      prob: pmf(x1, n, theta1)
    });
  }
  return data;
}

marginalX2 = {
  const data = [];
  for (let x2 = 0; x2 <= n; x2++) {
    data.push({
      x2: x2,
      prob: pmf(x2, n, theta2)
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
        totalProb += pmf(x1, n, theta1) * pmf(x2, n, theta2);
      }
    }

    for (let x1 = 0; x1 <= n; x1++) {
      const x2 = totalT - x1;
      if (x2 >= 0 && x2 <= n && totalProb > 0) {
        const jointProb = pmf(x1, n, theta1) * pmf(x2, n, theta2);
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
        totalProb += pmf(x1, n, theta1) * pmf(x2, n, theta2);
      }
    }

    for (let x2 = 0; x2 <= n; x2++) {
      const x1 = totalT - x2;
      if (x1 >= 0 && x1 <= n && totalProb > 0) {
        const jointProb = pmf(x1, n, theta1) * pmf(x2, n, theta2);
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

maxMarginalProb1 = Math.max(...marginalX1.map(d => d.prob))
maxMarginalProb2 = Math.max(...marginalX2.map(d => d.prob))
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
    ticks: Array.from({length: Math.floor(n/2) + 1}, (_, i) => 2 * i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: Math.floor(n/2) + 1}, (_, i) => 2 * i),
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
      y2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb1) * (n + 1) * 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right marginal histogram (X₂)
    Plot.rect(marginalX2, {
      x1: n + 0.56 + n * .06,
      x2: d => n + 0.56 + n * .06 + (d.prob / maxMarginalProb2) * (n + 1) * 0.3,
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
    ticks: Array.from({length: Math.floor(n/2) + 1}, (_, i) => 2 * i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n + 0.5],
    ticks: Array.from({length: Math.floor(n/2) + 1}, (_, i) => 2 * i),
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

---

[← Conditional testing](02-conditional-testing.md) · [Up: contents](index.md) · [Permutation tests →](04-permutation-tests.md)
