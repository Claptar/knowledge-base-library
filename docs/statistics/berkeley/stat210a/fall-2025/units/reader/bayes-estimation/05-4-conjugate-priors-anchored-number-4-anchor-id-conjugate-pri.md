---
title: 4 Conjugate Priors {.anchored number="4" anchor-id="conjugate-priors"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Conjugate Priors {.anchored number="4" anchor-id="conjugate-priors"}

**Source:** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In both examples, the prior and likelihood have a similar functional form, and the posterior comes from the same exponential family as the prior. When the posterior is from the same family as the prior, we say the prior is conjugate to the likelihood.

### <span class="header-section-number">4.1</span> Conjugate Priors for Exponential Families {.anchored number="4.1" anchor-id="conjugate-priors-for-exponential-families"}

Suppose <span class="math inline">\$p\_\\theta(x) = h(x)\\exp(\\eta(\\theta)'T(x) - A(\\theta))\$</span> for carrier <span class="math inline">\$h\$</span>. Define:

<span class="math display">\\$$ \\pi(\\theta) = g(\\theta)\\exp(\\lambda'u(\\theta) - \\psi(\\lambda)) \\$$</span>

Then:

<span class="math display">\\$$ \\pi(\\theta\|x) \\propto \\exp((\\lambda + T(x))'u(\\theta) - (A(\\theta) + \\psi(\\lambda))) \\$$</span>

Often, <span class="math inline">\$u(\\theta) = \\eta(\\theta)\$</span> and <span class="math inline">\$\\lambda\$</span> is interpreted as pseudo-observations.

### <span class="header-section-number">4.2</span> Conjugate Prior Examples {.anchored number="4.2" anchor-id="conjugate-prior-examples"}

1.  Normal-Normal:

    - <span class="math inline">\$X\_i\|\\theta \\sim N(\\theta, \\sigma^2)\$</span>, <span class="math inline">\$\\sigma^2\$</span> known
    - <span class="math inline">\$\\theta \\sim N(\\mu, \\tau^2)\$</span>

2.  Poisson-Gamma:

    - <span class="math inline">\$X\|\\theta \\sim \\text{Poisson}(\\theta)\$</span>, <span class="math inline">\$\\theta &gt; 0\$</span>
    - <span class="math inline">\$\\theta \\sim \\text{Gamma}(\\alpha, \\beta)\$</span>, <span class="math inline">\$\\alpha, \\beta &gt; 0\$</span>

    Posterior: <span class="math inline">\$\\theta\|X \\sim \\text{Gamma}(\\alpha + \\sum x\_i, \\beta + n)\$</span>

    Interpret <span class="math inline">\$\\alpha\$</span> as pseudo-counts and <span class="math inline">\$\\beta\$</span> as pseudo-exposure.

### <span class="header-section-number">4.3</span> Beta-binomial example {.anchored number="4.3" anchor-id="beta-binomial-example"}

``` {.sourceCode .js .code-with-copy}
betaPDF = (x, alpha, beta) => {
  if (x <= 0 || x >= 1) return 0;

  // For small integer values, use exact calculation
  if (alpha === Math.floor(alpha) && beta === Math.floor(beta) && alpha <= 10 && beta <= 10) {
    const numerator = Math.pow(x, alpha - 1) * Math.pow(1 - x, beta - 1);
    // Beta function B(alpha, beta) = Gamma(alpha) * Gamma(beta) / Gamma(alpha + beta)
    // For integers: Gamma(n) = (n-1)!
    const betaFunction = factorial(alpha - 1) * factorial(beta - 1) / factorial(alpha + beta - 1);
    return numerator / betaFunction;
  }

  // For general case, use log form for numerical stability
  const logPdf = (alpha - 1) * Math.log(x) + (beta - 1) * Math.log(1 - x) - logBeta(alpha, beta);
  return Math.exp(logPdf);
}

// Factorial function
factorial = (n) => {
  if (n <= 1) return 1;
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

// Log Beta function approximation
logBeta = (alpha, beta) => {
  // Use Stirling's approximation for log-gamma
  const logGammaApprox = (z) => {
    if (z <= 0) return Infinity;
    return (z - 0.5) * Math.log(z) - z + 0.5 * Math.log(2 * Math.PI);
  };

  return logGammaApprox(alpha) + logGammaApprox(beta) - logGammaApprox(alpha + beta);
}

// Interactive controls
viewof n = Inputs.range([1, 50], {value: 10, step: 1, label: "n"})
viewof x = Inputs.range([0, 50], {value: 6, step: 1, label: "X"})
viewof pseudoHeads = Inputs.range([0.1, 20], {value: 2, step: 0.1, label: "α (pseudo-heads)"})
viewof pseudoTails = Inputs.range([0.1, 20], {value: 2, step: 0.1, label: "β (pseudo-tails)"})

// Ensure X doesn't exceed n
xClamped = Math.min(x, n)

// Calculate posterior parameters
posteriorAlpha = pseudoHeads + xClamped
posteriorBeta = pseudoTails + (n - xClamped)

// Generate data for plotting
data = {
  const thetaMin = 0.001;
  const thetaMax = 0.999;
  const numPoints = 1000;
  const dTheta = (thetaMax - thetaMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const theta = thetaMin + i * dTheta;
    return {
      theta: theta,
      prior: betaPDF(theta, pseudoHeads, pseudoTails),
      posterior: betaPDF(theta, posteriorAlpha, posteriorBeta)
    };
  });
}

// Find maximum values for y-axis scaling
maxPrior = Math.max(...data.map(d => d.prior))
maxPosterior = Math.max(...data.map(d => d.posterior))
maxY = Math.max(maxPrior, maxPosterior)

// Create the plot
Plot.plot({
  width: 800,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 120,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [0, 1],
    label: "θ",
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
    Plot.line(data, {x: "theta", y: "prior", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(data, {x: "theta", y: "posterior", stroke: "red", strokeWidth: 2}),
    Plot.ruleY([0]),

    // Title
    Plot.text([`Beta Prior and Posterior: X = ${xClamped}, n = ${n}`], {
      x: 0.5,
      y: maxY * 1.15,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Legend with colored lines
    Plot.lineX([{x: 0.72, y: maxY * 0.95}, {x: 0.78, y: maxY * 0.95}], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text([`Prior: Beta(${pseudoHeads.toFixed(1)}, ${pseudoTails.toFixed(1)})`], {
      x: 0.8,
      y: maxY * 0.95,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),
    Plot.lineX([{x: 0.72, y: maxY * 0.88}, {x: 0.78, y: maxY * 0.88}], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text([`Posterior: Beta(${posteriorAlpha.toFixed(1)}, ${posteriorBeta.toFixed(1)})`], {
      x: 0.8,
      y: maxY * 0.88,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

---

[← 3 Examples {.anchored number="3" anchor-id="examples"}](04-3-examples-anchored-number-3-anchor-id-examples.md) · [Up: contents](index.md)
