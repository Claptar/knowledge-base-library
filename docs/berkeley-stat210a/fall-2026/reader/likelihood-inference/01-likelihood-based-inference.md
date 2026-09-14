---
title: Likelihood-Based Inference
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/likelihood-inference.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/likelihood-inference.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Likelihood-Based Inference

**Source:** [`reader/likelihood-inference.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/likelihood-inference.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```ojs
//| echo: false

// Parameters
nMax = 200
thetaMax = Math.log(10 * nMax)

// Generate random Laplace samples with specified location parameter
generateLaplaceData = (theta) => {
  const data = [];
  for (let i = 0; i < nMax; i++) {
    // Generate Laplace(theta, 1) using inverse transform method
    const u = Math.random() - 0.5;
    const x = u > 0 ? theta - Math.log(1 - 2*u) : theta + Math.log(1 + 2*u);
    data.push(x);
  }
  return data;
}

// Slider for sample size n
viewof nLaplace = Inputs.range([1, nMax], {value: 5, step: 1, label: "n"})

// Slider for true theta value
viewof theta0 = Inputs.range([Math.ceil(-thetaMax), Math.floor(thetaMax)], {value: 0, step: 0.1, label: "θ₀"})

// Toggle for zoom
viewof zoomToggle = Inputs.toggle({label: "Zoom: local view", value: false})

// Button to generate new data
viewof generateButton = html`<button style="
  background-color: #2196F3;
  color: white;
  border: none;
  padding: 8px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s;
" onmouseover="this.style.backgroundColor='#1976D2'"
   onmouseout="this.style.backgroundColor='#2196F3'"
   onclick="this.value = this.value + 1; this.dispatchEvent(new CustomEvent('input'))">
Generate data
</button>`

// Current data - updates when button is pressed
currentData = generateButton ? generateLaplaceData(theta0) : generateLaplaceData(0)

// Calculate log-likelihood function
logLikelihood = (theta, data, sampleSize) => {
  const subset = data.slice(0, sampleSize);
  return -sampleSize * Math.log(2) - subset.reduce((sum, x) => sum + Math.abs(x - theta), 0);
}

// Create data for plotting - only evaluate at knots and endpoints
data = {
  const subset = currentData.slice(0, nLaplace);
  const sortedData = [...subset].sort((a, b) => a - b);

  // Determine evaluation range based on zoom
  const [xMin, xMax] = plotRanges.x;

  // Create evaluation points: range endpoints and sorted data points in range
  const dataInRange = sortedData.filter(x => x >= xMin && x <= xMax);
  const evalPoints = [xMin, ...dataInRange, xMax];

  // Remove duplicates and sort
  const uniquePoints = [...new Set(evalPoints)].sort((a, b) => a - b);

  return uniquePoints.map(theta => ({
    theta: theta,
    loglik: logLikelihood(theta, currentData, nLaplace),
    isDataPoint: sortedData.includes(theta)
  }));
}

// Find y-axis limits to show all knots (for full view)
yLimits = {
  const dataPoints = currentData.slice(0, nLaplace);
  const loglikAtData = dataPoints.map(x => logLikelihood(x, currentData, nLaplace));
  const minLoglik = Math.min(...loglikAtData);
  const maxLoglik = Math.max(...loglikAtData);
  const range = maxLoglik - minLoglik;
  return {
    min: minLoglik - 0.1 * range - Math.log(2),
    max: maxLoglik + 0.1 * range + 0.1 * Math.log(2)
  };
}

// Calculate plotting ranges based on zoom toggle
plotRanges = {
  if (zoomToggle) {
    // Zoomed view
    const halfWidth = 3 / Math.sqrt(nLaplace);
    const xMin = theta0 - halfWidth;
    const xMax = theta0 + halfWidth;

    // Find data points in this range
    const subset = currentData.slice(0, nLaplace);
    const dataInRange = subset.filter(x => x >= xMin && x <= xMax);

    // Calculate y-range for data points in the horizontal range
    let yMin, yMax;
    if (dataInRange.length > 0) {
      const loglikValues = dataInRange.map(x => logLikelihood(x, currentData, nLaplace));
      yMin = Math.min(...loglikValues);
      yMax = Math.max(...loglikValues);
    } else {
      // If no data points in range, evaluate at endpoints
      const leftLoglik = logLikelihood(xMin, currentData, nLaplace);
      const rightLoglik = logLikelihood(xMax, currentData, nLaplace);
      yMin = Math.min(leftLoglik, rightLoglik);
      yMax = Math.max(leftLoglik, rightLoglik);
    }

    const yRange = yMax - yMin;
    return {
      x: [xMin, xMax],
      y: [yMin - 0.1 * yRange - 0.1, yMax + 0.1 * yRange + 0.1]
    };
  } else {
    // Full view
    return {
      x: [-thetaMax, thetaMax],
      y: [yLimits.min, yLimits.max]
    };
  }
}

// Create the plot
Plot.plot({
  width: 800,
  height: 600,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: plotRanges.x,
    label: "θ",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: plotRanges.y,
    label: "Log-likelihood",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    // Main log-likelihood curve
    Plot.line(data, {
      x: "theta",
      y: "loglik",
      stroke: "steelblue",
      strokeWidth: 2
    }),

    // Mark data points as knots
    Plot.dot(data.filter(d => d.isDataPoint), {
      x: "theta",
      y: "loglik",
      fill: "steelblue",
      r: 4
    }),

    // Vertical reference line at theta0
    Plot.ruleX([theta0], {stroke: "gray", strokeDasharray: "3,3", opacity: 0.5}),

    // Title
    Plot.text([`Log-likelihood for ${nLaplace} i.i.d. Laplace observations${zoomToggle ? ' (zoomed)' : ''}`], {
      x: (plotRanges.x[0] + plotRanges.x[1]) / 2,
      y: plotRanges.y[1] + 0.05 * (plotRanges.y[1] - plotRanges.y[0]),
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})
```

### Setting

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x)$, $p_\theta \in \cP$, smooth in $\theta$

Assume:
- $\mathbb{E}_\theta[\nabla \ell_\theta(X)] = 0$
- $\text{Var}_\theta[\nabla \ell_\theta(X)] = \mathbb{E}_\theta[-\nabla^2 \ell_\theta(X)] = J(\theta) > 0$
- MLE $\hat{\theta}$ Consistent

Then if $\theta = \theta_0$:
- $\nabla \ell_n(\theta_0; X) \sim N(0, nJ(\theta_0))$
- $-\nabla^2 \ell_n(\theta_0; X) \xrightarrow{p} nJ(\theta_0)$

Used $\theta = \hat{\theta} + J^{-1}(\theta_0) \nabla \ell_n(\theta_0; X)/n + o_p(n^{-1/2})$
to get $\sqrt{n}(\hat{\theta} - \theta_0) \sim N(0, J^{-1}(\theta_0))$

Can use this for inference on $\theta_0$

---

[Up: contents](index.md) · [Wald-Type Confidence Regions →](02-wald-type-confidence-regions.md)
