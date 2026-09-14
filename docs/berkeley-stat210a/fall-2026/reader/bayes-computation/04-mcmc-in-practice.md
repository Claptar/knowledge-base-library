---
title: MCMC in practice
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-computation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# MCMC in practice

**Source:** [`reader/bayes-computation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The magic of MCMC is that running an irreducible and aperiodic Markov chain with stationary distribution $\lambda(\theta\mid X)$ for *long enough* will eventually give us samples that are approximately drawn from the posterior. The only trouble, in practice, is that this can be very long indeed.

The applet below is meant to give some intuition for why the Gibbs sampler (for instance) does not always mix very quickly. The left plot shows the "trace" $\theta_1^{(0)},\ldots,\theta_1^{(T)}$ for a run of the Gibbs sampler on a mixture between two bivariate Gaussian distributions centered at $\pm \binom{\mu}{\mu}$
$$
\theta \sim \frac{1}{2}\cdot \left(p\left(\theta-\binom{\mu}{\mu}\right)  + p\left(\theta-\binom{-\mu}{-\mu}\right)\right),
$$
where each component has covariance matrix $\Sigma = \begin{pmatrix}1&\rho\\ \rho & 1\end{pmatrix}$:

$$
p(z) = \frac{1}{2\pi\sqrt{1-\rho^2}}\exp\left\{-\frac{1}{2} z'\Sigma^{-1}z\right\}.
$$
As you can see by playing with the parameters $\mu$ and $\rho$, it can take very long to move between components, or it can take many steps to move around within the components. This bivariate example is somewhat stylized, but the problems evident here can be significantly worse in high dimensions. The trace plot is commonly used as a diagnostic to see how well the chain is mixing. As you can see, it is good at picking up when we are switching back and forth between posterior modes or exploring the sample space very slowly (both potentially signs that we might need to come up with a different MCMC strategy) but it cannot pick up the more worrying possiblility that we are simply missing one high probability region of the posterior.

```ojs
//| echo: false

d3 = require("d3@7")

viewof mu = Inputs.range([0, 4], {value: 2, step: 0.1, label: "μ"})

viewof rho = Inputs.range([-0.99, 0.99], {value: 0.5, step: 0.01, label: "ρ"})

viewof theta1_init = Inputs.range([-6, 6], {value: 1, step: 0.1, label: "θ₁⁽⁰⁾"})

viewof theta2_init = Inputs.range([-6, 6], {value: 1, step: 0.1, label: "θ₂⁽⁰⁾"})

viewof runButton = Inputs.button("Run New Chain")

bivariateNormalPDF = (x1, x2, mu1, mu2, rho) => {
  const z1 = x1 - mu1
  const z2 = x2 - mu2
  const denom = 2 * Math.PI * Math.sqrt(1 - rho * rho)
  const exponent = -1 / (2 * (1 - rho * rho)) * (z1 * z1 - 2 * rho * z1 * z2 + z2 * z2)
  return Math.exp(exponent) / denom
}

mixtureDensity = (x1, x2, mu, rho) => {
  return 0.5 * bivariateNormalPDF(x1, x2, mu, mu, rho) +
         0.5 * bivariateNormalPDF(x1, x2, -mu, -mu, rho)
}

sampleTheta1GivenTheta2 = (theta2, mu, rho) => {
  const sd = Math.sqrt(1 - rho * rho)
  const mean1 = mu + rho * (theta2 - mu)
  const mean2 = -mu + rho * (theta2 + mu)

  const marginalSD = 1
  const p1 = Math.exp(-0.5 * Math.pow((theta2 - mu) / marginalSD, 2))
  const p2 = Math.exp(-0.5 * Math.pow((theta2 - (-mu)) / marginalSD, 2))

  const component = Math.random() < p1 / (p1 + p2) ? 1 : 2

  const mean = component === 1 ? mean1 : mean2
  return mean + sd * d3.randomNormal()()
}

sampleTheta2GivenTheta1 = (theta1, mu, rho) => {
  const sd = Math.sqrt(1 - rho * rho)
  const mean1 = mu + rho * (theta1 - mu)
  const mean2 = -mu + rho * (theta1 + mu)

  const marginalSD = 1
  const p1 = Math.exp(-0.5 * Math.pow((theta1 - mu) / marginalSD, 2))
  const p2 = Math.exp(-0.5 * Math.pow((theta1 - (-mu)) / marginalSD, 2))

  const component = Math.random() < p1 / (p1 + p2) ? 1 : 2

  const mean = component === 1 ? mean1 : mean2
  return mean + sd * d3.randomNormal()()
}

allSamples = {
  runButton

  const nSteps = 200
  const result = [[theta1_init, theta2_init]]

  for (let i = 0; i < nSteps; i++) {
    const current = result[result.length - 1]
    const newTheta1 = sampleTheta1GivenTheta2(current[1], mu, rho)
    const newTheta2 = sampleTheta2GivenTheta1(newTheta1, mu, rho)
    result.push([newTheta1, newTheta2])
  }

  return result
}

animatedSamples = {
  let steps = []

  // Start with initial point
  steps.push({
    theta1: allSamples[0][0],
    theta2: allSamples[0][1],
    type: "initial"
  })

  // For each Gibbs iteration, create two steps: theta1 update, then theta2 update
  for (let i = 1; i < allSamples.length; i++) {
    const prev = allSamples[i - 1]
    const curr = allSamples[i]

    // Step 1: Update theta1 (horizontal move)
    steps.push({
      theta1: curr[0],
      theta2: prev[1],
      type: "theta1",
      fromTheta1: prev[0],
      fromTheta2: prev[1]
    })

    // Step 2: Update theta2 (vertical move)
    steps.push({
      theta1: curr[0],
      theta2: curr[1],
      type: "theta2",
      fromTheta1: curr[0],
      fromTheta2: prev[1]
    })
  }

  let currentIndex = 0

  while (currentIndex <= steps.length) {
    yield steps.slice(0, currentIndex)
    currentIndex++
    await Promises.delay(25)
  }
}

contourData = {
  const grid = []
  const xMin = -6
  const xMax = 6
  const yMin = -6
  const yMax = 6
  const resolution = 200

  for (let i = 0; i < resolution; i++) {
    for (let j = 0; j < resolution; j++) {
      const x = xMin + (xMax - xMin) * j / (resolution - 1)
      const y = yMin + (yMax - yMin) * i / (resolution - 1)
      grid.push({
        x: x,
        y: y,
        z: mixtureDensity(x, y, mu, rho)
      })
    }
  }
  return grid
}

traceData = {
  const fullUpdates = []
  for (let i = 0; i < animatedSamples.length; i++) {
    const step = animatedSamples[i]
    if (step && (step.type === "initial" || step.type === "theta2")) {
      fullUpdates.push({
        iteration: fullUpdates.length,
        theta1: step.theta1,
        theta2: step.theta2
      })
    }
  }
  return fullUpdates
}

spatialData = {
  return animatedSamples.map(step => ({
    theta1: step.theta1,
    theta2: step.theta2,
    type: step.type,
    fromTheta1: step.fromTheta1,
    fromTheta2: step.fromTheta2
  }))
}

html`<div>
  <div style="margin-bottom: 20px;">
    <style>
      button {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        cursor: pointer !important;
        border-radius: 4px !important;
      }
      button:hover {
        background-color: #45a049 !important;
      }
    </style>
    ${viewof runButton}
  </div>
  <div style="display: flex; gap: 20px;">
    <div>${tracePlot}</div>
    <div>${spatialPlot}</div>
  </div>
</div>`

tracePlot = Plot.plot({
  width: 500,
  height: 500,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 120,
  style: {fontSize: "25px"},
  x: {
    domain: [0, 200],
    label: "Iteration",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [-6, 6],
    label: "Value",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    Plot.line(traceData, {x: "iteration", y: "theta1", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(traceData, {x: "iteration", y: "theta2", stroke: "red", strokeWidth: 2}),
    Plot.ruleY([0]),
    Plot.text(["Trace Plot"], {
      x: 100,
      y: 7,
      fontSize: 28,
      fontWeight: "bold",
      textAnchor: "middle"
    }),
    Plot.lineX([{x: 140, y: 5.5}, {x: 150, y: 5.5}], {
      x: "x", y: "y", stroke: "steelblue", strokeWidth: 2
    }),
    Plot.text(["θ₁"], {
      x: 152,
      y: 5.5,
      fontSize: 24,
      fill: "black",
      textAnchor: "start"
    }),
    Plot.lineX([{x: 140, y: 4.8}, {x: 150, y: 4.8}], {
      x: "x", y: "y", stroke: "red", strokeWidth: 2
    }),
    Plot.text(["θ₂"], {
      x: 152,
      y: 4.8,
      fontSize: 24,
      fill: "black",
      textAnchor: "start"
    })
  ]
})

spatialPlot = Plot.plot({
  width: 500,
  height: 500,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: {fontSize: "25px"},
  x: {
    domain: [-6, 6],
    label: "θ₁",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [-6, 6],
    label: "θ₂",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    Plot.contour(contourData, {
      x: "x",
      y: "y",
      value: "z",
      stroke: "gray",
      strokeWidth: 1.5,
      thresholds: 10,
      smooth: true
    }),
    Plot.link(spatialData.filter(d => d.type === "theta1"), {
      x1: "fromTheta1",
      y1: "fromTheta2",
      x2: "theta1",
      y2: "fromTheta2",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.link(spatialData.filter(d => d.type === "theta2"), {
      x1: "fromTheta1",
      y1: "fromTheta2",
      x2: "theta1",
      y2: "theta2",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.dot(spatialData.slice(-1), {
      x: "theta1",
      y: "theta2",
      r: 5,
      fill: "purple"
    }),
    Plot.dot(spatialData.slice(0, 1), {
      x: "theta1",
      y: "theta2",
      r: 4,
      fill: "green",
      stroke: "darkgreen",
      strokeWidth: 2
    }),
    Plot.ruleX([0]),
    Plot.ruleY([0]),
    Plot.text(["Parameter Space"], {
      x: 0,
      y: 7,
      fontSize: 28,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})
```

Two additional implementation details commonly used in MCMC are **burn-in**, where we run the chain for some number $B$ of steps to wait for the Markov chain to converge, and **thinning**, where we run the chain for some number $s$ of steps between successive samples in order to get posterior draws that are less correlated with each other. That is, we take $\theta^{(B)},\theta^{(B+s)},\theta^{(B+2s)},\ldots$ as our "sample" from $\lambda(\theta\mid X)$. Armed with this proxy sample, we can do anything we'd do if we knew the actual posterior: calculate posterior means, give return high-probability "credible intervals," or minimize any other expected loss function we like.

---

[← The Gibbs sampler](03-the-gibbs-sampler.md) · [Up: contents](index.md)
