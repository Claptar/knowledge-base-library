---
title: Conjugate Priors
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conjugate Priors

**Source:** [`reader/bayes-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In both examples, the prior and likelihood have a similar functional form, and the posterior comes from the same exponential family as the prior. When the posterior is from the same family as the prior, we say the prior is conjugate to the likelihood.

### Conjugate Priors for Exponential Families

Suppose $p_\theta(x) = h(x)\exp(\eta(\theta)'T(x) - A(\theta))$ for carrier $h$. Define:

$$
\pi(\theta) = g(\theta)\exp(\lambda'u(\theta) - \psi(\lambda))
$$

Then:

$$
\pi(\theta|x) \propto \exp((\lambda + T(x))'u(\theta) - (A(\theta) + \psi(\lambda)))
$$

Often, $u(\theta) = \eta(\theta)$ and $\lambda$ is interpreted as pseudo-observations.

### Conjugate Prior Examples

1. Normal-Normal:
   - $X_i|\theta \sim N(\theta, \sigma^2)$, $\sigma^2$ known
   - $\theta \sim N(\mu, \tau^2)$

2. Poisson-Gamma:
   - $X|\theta \sim \text{Poisson}(\theta)$, $\theta > 0$
   - $\theta \sim \text{Gamma}(\alpha, \beta)$, $\alpha, \beta > 0$

   Posterior: $\theta|X \sim \text{Gamma}(\alpha + \sum x_i, \beta + n)$

   Interpret $\alpha$ as pseudo-counts and $\beta$ as pseudo-exposure.


### Beta-binomial example


```ojs
// Import necessary libraries
import {Plotly} from '@observablehq/plotly'
import {jStat} from 'jstat'

// Input sliders and text boxes
viewof priorMean = Inputs.range([0.01, 0.99], {value: 0.5, step: 0.01, label: "Prior Mean"})
viewof priorPseudoFlips = Inputs.range([0.1, 100], {value: 20, step: 0.1, label: "Prior Pseudo-Flips"})
viewof n = Inputs.number({value: 500, min: 1, step: 1, label: "n"})
viewof xVal = Inputs.number({value: 125, min: 0, max: n, step: 1, label: "X"})

// Compute alpha and beta from prior mean and pseudo-flips
alpha = priorMean * priorPseudoFlips
beta = (1 - priorMean) * priorPseudoFlips

// Create theta values
theta = Array.from({length: 1000}, (_, i) => i / 999)

// Calculate prior, likelihood, and posterior densities
priorDensity = theta.map(t => jStat.beta.pdf(t, alpha, beta))
posteriorDensity = theta.map(t => jStat.beta.pdf(t, alpha + xVal, beta + n - xVal))

// Compute log-likelihood to prevent underflow issues
logLikelihood = theta.map(t => {
  if (t <= 0 || t >= 1) return -Infinity
  return xVal * Math.log(t) + (n - xVal) * Math.log(1 - t)
})
maxLogLikelihood = Math.max(...logLikelihood)
likelihoodScaled = logLikelihood.map(l => Math.exp(l - maxLogLikelihood))

// Scale likelihood to match plot dimensions
maxPriorDensity = Math.max(...priorDensity)
maxPosteriorDensity = Math.max(...posteriorDensity)
ymax = 1.1 * Math.max(maxPriorDensity, maxPosteriorDensity)
likelihoodScaled = likelihoodScaled.map(l => l * ymax / 1.1)

// Prepare data for plotting
data = [
  {
    x: theta,
    y: priorDensity,
    name: 'Prior',
    mode: 'lines',
    line: {color: 'blue'}
  },
  {
    x: theta,
    y: likelihoodScaled,
    name: 'Likelihood',
    mode: 'lines',
    line: {color: 'black'}
  },
  {
    x: theta,
    y: posteriorDensity,
    name: 'Posterior',
    mode: 'lines',
    line: {color: 'red'}
  }
]

// Compute estimates for vertical lines
UMVU_estimate = xVal / n
Bayes_estimate = (alpha + xVal) / (alpha + beta + n)

// Define layout with vertical lines and annotations
layout = {
  title: 'Beta-Binomial',
  xaxis: {title: 'theta', range: [0, 1]},
  yaxis: {title: 'Density', range: [0, ymax]},
  shapes: [
    {
      type: 'line',
      x0: UMVU_estimate,
      x1: UMVU_estimate,
      y0: 0,
      y1: ymax,
      line: {color: 'black', dash: 'dot'}
    },
    {
      type: 'line',
      x0: Bayes_estimate,
      x1: Bayes_estimate,
      y0: 0,
      y1: ymax,
      line: {color: 'red', dash: 'dot'}
    },
    {
      type: 'line',
      x0: 0.5,
      x1: 0.5,
      y0: 0,
      y1: ymax,
      line: {color: 'gray', dash: 'solid'}
    }
  ],
  annotations: [
    {
      x: UMVU_estimate,
      y: ymax,
      xref: 'x',
      yref: 'y',
      text: 'UMVU',
      showarrow: true,
      arrowhead: 2,
      ax: 0,
      ay: -40
    },
    {
      x: Bayes_estimate,
      y: ymax,
      xref: 'x',
      yref: 'y',
      text: 'Bayes',
      showarrow: true,
      arrowhead: 2,
      ax: 0,
      ay: -40
    }
  ],
  legend: {x: 0.8, y: 0.9},
  margin: {t: 40}
}

// Create the plot
Plotly.newPlot(plotDiv, data, layout)

// Display the plot
plotDiv = html`<div id="plotDiv"></div>`
```

---

[← Examples](03-examples.md) · [Up: contents](index.md)
