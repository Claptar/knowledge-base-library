---
title: Minimal sufficiency {.anchored anchor-id="minimal-sufficiency"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Minimal sufficiency {.anchored anchor-id="minimal-sufficiency"}

**Source:** [`reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Consider again the example with <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid N(\\theta,1)\$</span>. We have shown that <span class="math inline">\$\\sum\_i X\_i\$</span> is sufficient. It follows that <span class="math inline">\$\\overline{X} = \\frac{1}{n}\\sum\_i X\_i\$</span> is also sufficient. But we have also shown that the vector of order statistics <span class="math inline">\$S(X) = (X\_{(1)}, \\ldots, X\_{(n)})\$</span> is another sufficient statistic. Finally, the full data set <span class="math inline">\$X\$</span> is always a sufficient statistic, by definition.

While these are indeed all sufficient statistics, some of them represent more significant compressions of the data than others. We can see this from the fact that <span class="math inline">\$\\sum\_i X\_i\$</span> and <span class="math inline">\$\\overline{X}\$</span> are recoverable from each other, and can also be recovered from either <span class="math inline">\$S(X)\$</span> or <span class="math inline">\$X\$</span> itself, but <span class="math inline">\$S(X)\$</span> cannot be recovered from <span class="math inline">\$\\sum\_i X\_i\$</span> or <span class="math inline">\$\\overline{X}\$</span>. The full data <span class="math inline">\$X\$</span> cannot be recovered from any of the other three, but any of the other three can be recovered from it. Among these statistics, the first two represent the greatest reduction of the data, and <span class="math inline">\$X\$</span> represents no reduction at all, while <span class="math inline">\$S(X)\$</span> sits in the middle.

Any statistic from which a sufficient statistic can be recovered is immediately a sufficient statistic:

**Proposition:** If <span class="math inline">\$T(X)\$</span> is sufficient and <span class="math inline">\$T(X) = f(S(X))\$</span> then <span class="math inline">\$S(X)\$</span> is also sufficient.

*Proof:* By the factorization theorem we can find densities with <span class="math display">\\$$ p\_\\theta(x) = g\_\\theta(T(x))h(x) = (g\_\\theta \\circ f)(S(x)) h(x), \\$$</span> showing that <span class="math inline">\$S(X)\$</span> is sufficient as well.

We say that a sufficient statistic is **minimal** if it can be recovered from any other sufficient statistic. That is, <span class="math inline">\$T(X)\$</span> is **minimal sufficient** if

1.  <span class="math inline">\$T(X)\$</span> is sufficient, and

2.  For any other sufficient statistic <span class="math inline">\$S(X)\$</span>, we have <span class="math inline">\$T(X) = f(S(X))\$</span> for some <span class="math inline">\$f\$</span> (almost surely in <span class="math inline">\$\\cP\$</span>).

We would like to be able to recognize minimal sufficient statistics when we can. For a model <span class="math inline">\$\\cP\$</span> with densities <span class="math inline">\$p\_\\theta\$</span>, we can say that two data sets <span class="math inline">\$x,y\\in \\cX\$</span> are *equivalent* (with respect to statistical inference in <span class="math inline">\$\\cP\$</span>) if <span class="math inline">\$p\_\\theta(x)/p\_\\theta(y)\$</span> does not depend on <span class="math inline">\$\\theta\$</span>. We can write <span class="math inline">\$x \\equiv\_{\\cP} y\$</span> if this is the case.

Note that, for any sufficient statistic <span class="math inline">\$T(X)\$</span>, values that map to the same output value <span class="math inline">\$t\$</span> must be equivalent: if <span class="math inline">\$T(x)=T(y)=t\$</span>, we have <span class="math display">\\$$ \\frac{p\_\\theta(x)}{p\_\\theta(y)} = \\frac{\\PP\_\\theta(X = x \\text{ and } T(X) = t)}{\\PP\_\\theta(X = y \\text{ and } T(X) = t)} = \\frac{\\PP(X = x \\mid T(X) = t)}{\\PP(X = y \\mid T(X) = t)}, \\$$</span> which does not depend on <span class="math inline">\$\\theta\$</span> by sufficiency of <span class="math inline">\$T(X)\$</span>. Thus, for *any* sufficient statistic we have <span class="math inline">\$T(x) = T(y) \\Rightarrow x \\equiv\_{\\cP} y\$</span>: the function <span class="math inline">\$T\$</span> is only allowed to collapse values that are equivalent to each other. For a *minimal sufficient statistic*, this implication goes both ways since <span class="math inline">\$T\$</span> collapses the sample space as much as possible. That is,

**Proposition:** Assume <span class="math inline">\$\\cP\$</span> has densities <span class="math inline">\$p\_\\theta(x)\$</span>, and <span class="math inline">\$T(X)\$</span> is any statistic. If we have <span class="math display">\\$$x \\equiv\_{\\cP} y \\iff T(x) = T(y),\\$$</span> then <span class="math inline">\$T(X)\$</span> is minimal sufficient.

*Proof (discrete* <span class="math inline">\$\\cX\$</span>): First, we show <span class="math inline">\$T(X)\$</span> is sufficient. For any <span class="math inline">\$x\$</span> with <span class="math inline">\$T(x) = t\$</span>, we have

<span class="math display">\\$$ \\PP\_\\theta(X = x \\mid T(X) = t) = \\frac{p\_\\theta(x)}{\\sum\_{z: T(z) = t} p\_\\theta(z)} = \\frac{1}{\\sum\_{z:\\; T(z) = t} p\_\\theta(z)/p\_\\theta(x)}, \\$$</span> which does not depend on <span class="math inline">\$\\theta\$</span> because all of the values <span class="math inline">\$z\$</span> that we sum over in the denominator map to the same <span class="math inline">\$t\$</span>, and are therefore equivalent to <span class="math inline">\$x\$</span> by assumption.

Next, assume <span class="math inline">\$S(X)\$</span> is any other sufficient statistic. If <span class="math inline">\$S(x) = S(y) = s\$</span>, then <span class="math inline">\$x \\equiv\_{\\cP} y\$</span>, by the argument above the theorem, and consequently <span class="math inline">\$T(x) = T(y)\$</span> by assumption. Then we can set <span class="math inline">\$f(s) = T(x)\$</span>. For any other value <span class="math inline">\$z\$</span> with <span class="math inline">\$S(z) = s\$</span>, we must also have <span class="math inline">\$x \\equiv\_{\\cP} z\$</span> so <span class="math inline">\$T(z) = T(x) = f(S(z))\$</span>. Since <span class="math inline">\$s\$</span> was arbitrary, we have the result.

``` {.sourceCode .js .code-with-copy}
nMax = 50
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

  // Create evaluation points: -thetaMax, sorted data points, +thetaMax
  const evalPoints = [-thetaMax, ...sortedData, thetaMax];

  return evalPoints.map(theta => ({
    theta: theta,
    loglik: logLikelihood(theta, currentData, nLaplace),
    isDataPoint: sortedData.includes(theta)
  }));
}

// Find y-axis limits to show all knots
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

// Create the plot
Plot.plot({
  width: 800,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [-thetaMax, thetaMax],
    label: "θ",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [yLimits.min, yLimits.max],
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

    // Vertical reference line at theta = 0
    Plot.ruleX([0], {stroke: "gray", strokeDasharray: "3,3", opacity: 0.5}),

    // Title
    Plot.text([`Log-likelihood for ${nLaplace} i.i.d. Laplace observations`], {
      x: 0,
      y: yLimits.max + 0.05 * (yLimits.max - yLimits.min),
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})
```

---

[← Sufficiency Part 07 —](07-sufficiency-part-07.md) · [Up: contents](index.md)
