---
title: Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Confidence Regions

**Source:** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Suppose we are testing <span class="math inline">\$H\_0:\\theta = 0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta \\neq 0\$</span>. When the <span class="math inline">\$p\$</span>-value is very small, it gives us a strong indication that the data set we observed is inconsistent with the parameter value <span class="math inline">\$\\theta=0\$</span>. It does *not* necessarily follow that the data set is indicating that the <span class="math inline">\$\\theta\$</span> value is *far* from zero: for example, if we have a huge data set we might be able to say with very high confidence that <span class="math inline">\$\\theta\$</span> is in the range <span class="math inline">\$$$0.0011,0.0012$$\$</span>. Depending on the context, this could practically amount to *confirming* the informal scientific null that <span class="math inline">\$\\theta\$</span> is too small to care about. But if we looked at the <span class="math inline">\$p\$</span>-value it will tell us (accurately) that the formal statistical null <span class="math inline">\$\\theta=0\$</span> is highly implausible.

By the same token, we could also be mistaken if we observe that the <span class="math inline">\$p\$</span>-value is large and conclude that <span class="math inline">\$\\theta\$</span> must be close to zero. It *could* be the case that the data set establishes that <span class="math inline">\$\\theta\$</span> is in a narrow range around zero, *or* it could simply be that the data give very poor evidence about <span class="math inline">\$\\theta\$</span> so we still don’t know very much about it.

Confidence intervals, and more generally confidence regions, are a more reliable guide than <span class="math inline">\$p\$</span>-values if we want to know what range of <span class="math inline">\$\\theta\$</span> values are plausible in light of the data. As we will see, they can be obtained using the same machinery we have developed for hypothesis tests. Whereas the <span class="math inline">\$p\$</span>-value tells us what our test would decide for all values of <span class="math inline">\$k\$</span>, we can think of a confidence region as telling us what our test of a point null <span class="math inline">\$H\_0:\\; \\theta = \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta\\neq 0\$</span> would decide for all values of <span class="math inline">\$\\theta\_0\$</span>.

## Definition of a confidence region {.anchored anchor-id="definition-of-a-confidence-region"}

**Definition:** We say that <span class="math inline">\$C(X)\$</span> is a <span class="math inline">\$1-\\alpha\$</span> confidence region for <span class="math inline">\$g(\\theta)\$</span> if:

<span class="math display">\\$$ \\PP\_\\theta(C(X) \\ni g(\\theta)) \\geq 1-\\alpha, \\quad \\text{for all } \\theta \\in \\Theta \\$$</span> We say that <span class="math inline">\$C(x)\$</span> **covers** <span class="math inline">\$g(\\theta)\$</span> if <span class="math inline">\$C(x) \\ni g(\\theta)\$</span>, and the **coverage probability** at a parameter value <span class="math inline">\$\\theta\$</span> is <span class="math inline">\$\\PP\_\\theta(C(X) \\ni g(\\theta))\$</span>. The **confidence level** of <span class="math inline">\$C(X)\$</span> is <span class="math inline">\$\\inf\_{\\theta\\in\\Theta} \\mathbb{P}\_\\theta(C(X) \\ni g(\\theta))\$</span>.

The use of the “<span class="math inline">\$\\ni\$</span>” symbol in the above definition is deliberate. To avoid common misinterpretations, we should always think and speak of the interval or region <span class="math inline">\$C(X)\$</span> as the random “subject” of the mathematical sentence and the estimand <span class="math inline">\$g(\\theta)\$</span> as the fixed “object.”

The confidence interval is commonly misinterpreted as a Bayesian guarantee, where <span class="math inline">\$C(X)\$</span> is first realized and then <span class="math inline">\$g(\\theta)\$</span> has some probability of falling into <span class="math inline">\$C(X)\$</span>. This interpretation is incorrect: confidence intervals are frequentist objects whose guarantee is intended to apply for fixed <span class="math inline">\$\\theta\$</span> values. Once <span class="math inline">\$X\$</span> is realized <span class="math inline">\$C(X)\$</span> either does or does not contain the estimand <span class="math inline">\$g(\\theta)\$</span>; there is no remaining randomness in the problem.

Thus, while the following formulations are technically mathematically equivalent, the second one tends to give people the wrong impression and is not recommended:

- **Formulation 1 (recommended):** <span class="math inline">\$C(X)\$</span> has a <span class="math inline">\$95\\%\$</span> chance of covering <span class="math inline">\$g(\\theta)\$</span>

- **Formulation 2 (not recommended):** <span class="math inline">\$g(\\theta)\$</span> has a <span class="math inline">\$95\\%\$</span> chance of falling in <span class="math inline">\$C(X)\$</span>

Once we have calculated, say, <span class="math inline">\$C(X) = $$0.8, 1.1$$\$</span>, it is *never* correct to say “there is a <span class="math inline">\$95\\%\$</span> chance <span class="math inline">\$g(\\theta) \\in $$0.8, 1.1$$\$</span>” on the basis of a confidence interval guarantee. Under a frequentist model this is a category error since <span class="math inline">\$g(\\theta)\$</span> is not random, and even under a Bayesian model where there is an *a posteriori* probability, that probability depends on our prior.

## Duality of tests and confidence regions {.anchored anchor-id="duality-of-tests-and-confidence-regions"}

Confidence regions are closely related to hypothesis tests, and one can be constructed from the other, as we see below.

Suppose we have a level <span class="math inline">\$\\alpha\$</span> test <span class="math inline">\$\\phi(X; a)\$</span> of <span class="math inline">\$H\_0: g(\\theta) = a\$</span> vs <span class="math inline">\$H\_1: g(\\theta) \\neq a\$</span>, for every value <span class="math inline">\$a\$</span>. Then we can use these tests to construct a (non-randomized) confidence region for <span class="math inline">\$g(\\theta)\$</span> as follows:

<span class="math display">\\$$ C(X) = \\{a: \\phi(X; a) &lt; 1\\} \\$$</span> That is, <span class="math inline">\$C(X)\$</span> is all *non-rejected* values of <span class="math inline">\$a\$</span>. <span class="math inline">\$C(X)\$</span> is a valid confidence region because <span class="math display">\\$$ \\mathbb{P}\_\\theta(C(X) \\ni g(\\theta)) = \\mathbb{P}\_\\theta(\\phi(X; g(\\theta)) &lt; 1) \\geq 1-\\alpha \\$$</span> Constructing an interval in this way is called **inverting** a test (or more precisely, a family of tests, one for each <span class="math inline">\$a\$</span> value).

Conversely, we can obtain a test by inverting a confidence region. Suppose <span class="math inline">\$C(X)\$</span> is a <span class="math inline">\$1-\\alpha\$</span> confidence region for <span class="math inline">\$g(\\theta)\$</span>. Then <span class="math display">\\$$ \\phi(x; a) = 1\\{a \\notin C(x)\\} \\$$</span> is a valid level-<span class="math inline">\$\\alpha\$</span> test of the null <span class="math inline">\$H\_0: g(\\theta) = a\$</span> vs. the alternative <span class="math inline">\$H\_1: g(\\theta) \\neq a\$</span>, because <span class="math display">\\$$ \\mathbb{E}\_\\theta \\phi(X; g(\\theta)) = \\mathbb{P}\_\\theta(g(\\theta) \\notin C(X)) \\leq \\alpha \\$$</span> A confidence region is called **unbiased** if its probability of including any value *other than* the true <span class="math inline">\$g(\\theta)\$</span> is *at most* <span class="math inline">\$1-\\alpha\$</span>: <span class="math display">\\$$ \\PP\_\\theta( C(X) \\ni a) \\leq 1-\\alpha, \\quad \\text{ for all } a \\neq g(\\theta). \\$$</span> It is immediate from the definition that <span class="math inline">\$C(X)\$</span> is unbiased if and only if the test we obtain by inverting it is unbiased. Likewise, the confidence region obtained by inverting an unbiased *non-randomized* test is also unbiased.

**Example (Multivariate Gaussian confidence ellipse)** Suppose that we observe <span class="math inline">\$X \\sim N\_d(\\mu, \\Sigma)\$</span>, where the covariance matrix <span class="math inline">\$\\Sigma\$</span> is known and <span class="math inline">\$\\mu\\in\\RR^d\$</span> is unknown. We can define <span class="math display">\\$$ Z = \\Sigma^{-1/2}(X-\\mu) \\sim N\_d(0,I\_d). \\$$</span>

A natural test of the point null <span class="math inline">\$H\_0:\\; \\mu = \\mu\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\mu \\neq \\mu\_0\$</span> is to reject for large values of <span class="math display">\\$$ \\\|\\Sigma^{-1/2} (X-\\mu\_0)\\\|^2 \\stackrel{H\_0}{\\sim} \\chi\_d^2. \\$$</span> Let <span class="math inline">\$c\_\\alpha\$</span> denote the upper <span class="math inline">\$\\alpha\$</span> quantile of the null distribution. The confidence region we obtain by inverting this test is the ellipse: <span class="math display">\\$$ C(X) = \\left\\{\\mu\_0:\\; \\\|\\Sigma^{-1/2}(X-\\mu\_0)\\\|^2 \\leq c\_\\alpha\\right\\}. \\$$</span>

The widget below illustrates the process of sampling these confidence regions.

``` {.sourceCode .js .code-with-copy}
jStat = require("jstat@1.9.4")

// Custom CSS for button styling
html`<style>
  button {
    background-color: #4682b4 !important;
    color: white !important;
    border: none !important;
    padding: 8px 16px !important;
    border-radius: 4px !important;
    cursor: pointer !important;
    font-size: 14px !important;
  }
  button:hover {
    background-color: #5a9bd4 !important;
  }
</style>`
```

``` {.sourceCode .js .code-with-copy}
viewof rho = Inputs.range([-0.95, 0.95], {value: 0.5, step: 0.05, label: "ρ"})
viewof mu1 = Inputs.range([-3, 3], {value: 0, step: 0.5, label: "μ₁"})
viewof mu2 = Inputs.range([-3, 3], {value: 0, step: 0.5, label: "μ₂"})
viewof alpha = Inputs.range([0.01, 0.5], {value: 0.05, step: 0.01, label: "α"})

// Buttons for sampling and clearing
viewof sampleButton = Inputs.button("Sample new ellipse")
viewof clearButton = Inputs.button("Clear all ellipses")

// State management: store all sampled ellipses
mutable ellipses = []

// Reset ellipses when parameters change
paramHash = `${rho}_${mu1}_${mu2}_${alpha}`
resetEllipses = {
  mutable ellipses = [];
  return paramHash;
}

// Sample from bivariate normal
sampleBivariateNormal = (mu1, mu2, rho) => {
  // Generate two independent standard normals
  const z1 = jStat.normal.sample(0, 1);
  const z2 = jStat.normal.sample(0, 1);

  // Apply Cholesky transformation for correlation
  const x1 = mu1 + z1;
  const x2 = mu2 + rho * z1 + Math.sqrt(1 - rho * rho) * z2;

  return {x1, x2};
}

// Check if true mean is inside ellipse (coverage check)
checkCoverage = (x1, x2, mu1, mu2, rho, alpha) => {
  // Quadratic form: (X - mu)^T Sigma^{-1} (X - mu)
  // For Sigma = ((1, rho), (rho, 1)), Sigma^{-1} = 1/(1-rho^2) * ((1, -rho), (-rho, 1))
  const det = 1 - rho * rho;
  const dx1 = mu1 - x1;  // Note: checking if mu is in ellipse around X
  const dx2 = mu2 - x2;

  const quadForm = (dx1 * dx1 - 2 * rho * dx1 * dx2 + dx2 * dx2) / det;

  // Chi-squared critical value for (1-alpha) confidence with 2 df
  const critVal = jStat.chisquare.inv(1 - alpha, 2);

  return quadForm <= critVal;
}

// Generate ellipse points
generateEllipse = (x1, x2, rho, alpha, numPoints = 100) => {
  const critVal = jStat.chisquare.inv(1 - alpha, 2);

  // Eigenvalues of Sigma = ((1, rho), (rho, 1))
  const lambda1 = 1 + Math.abs(rho);  // Larger eigenvalue
  const lambda2 = 1 - Math.abs(rho);  // Smaller eigenvalue

  // Semi-axes lengths scaled by chi-squared critical value
  const a = Math.sqrt(critVal * lambda1);
  const b = Math.sqrt(critVal * lambda2);

  // For positive rho: eigenvector for lambda1 is (1,1)/sqrt(2) - 45 degree angle
  // For negative rho: eigenvector for lambda1 is (1,-1)/sqrt(2) - 135 degree angle
  const angle = rho >= 0 ? Math.PI / 4 : -Math.PI / 4;

  const points = [];
  for (let i = 0; i <= numPoints; i++) {
    const theta = (2 * Math.PI * i) / numPoints;

    // Ellipse in canonical form (aligned with principal axes)
    const xCanon = a * Math.cos(theta);
    const yCanon = b * Math.sin(theta);

    // Rotate to align with eigenvectors and translate to center
    const xRot = xCanon * Math.cos(angle) - yCanon * Math.sin(angle);
    const yRot = xCanon * Math.sin(angle) + yCanon * Math.cos(angle);

    points.push({
      x: x1 + xRot,
      y: x2 + yRot
    });
  }

  return points;
}

// Handle sample button click
sampleCount = sampleButton
ellipseData = {
  if (sampleCount > 0) {
    const sample = sampleBivariateNormal(mu1, mu2, rho);
    const covers = checkCoverage(sample.x1, sample.x2, mu1, mu2, rho, alpha);
    const points = generateEllipse(sample.x1, sample.x2, rho, alpha);

    mutable ellipses = [...mutable ellipses, {
      id: Date.now(),
      center: sample,
      points: points,
      covers: covers
    }];
  }
  return mutable ellipses;
}

// Handle clear button click
clearCount = clearButton
clearedEllipses = {
  if (clearCount > 0) {
    mutable ellipses = [];
  }
  return clearCount;
}

// Calculate plot domain
plotDomain = {
  const padding = 3;
  let xMin = mu1 - padding;
  let xMax = mu1 + padding;
  let yMin = mu2 - padding;
  let yMax = mu2 + padding;

  // Expand domain to include all ellipses
  ellipseData.forEach(ellipse => {
    ellipse.points.forEach(p => {
      xMin = Math.min(xMin, p.x);
      xMax = Math.max(xMax, p.x);
      yMin = Math.min(yMin, p.y);
      yMax = Math.max(yMax, p.y);
    });
  });

  return {xMin, xMax, yMin, yMax};
}

// Create the plot
Plot.plot({
  width: 800,
  height: 600,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 120,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [plotDomain.xMin, plotDomain.xMax],
    label: "x₁",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [plotDomain.yMin, plotDomain.yMax],
    label: "x₂",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    // Coordinate axes
    Plot.ruleX([0], {stroke: "gray", strokeWidth: 1}),
    Plot.ruleY([0], {stroke: "gray", strokeWidth: 1}),

    // All ellipses
    ...ellipseData.flatMap(ellipse => [
      Plot.line(ellipse.points, {
        x: "x",
        y: "y",
        stroke: ellipse.covers ? "steelblue" : "red",
        strokeWidth: 2
      })
    ]),

    // True mean point
    Plot.dot([{x: mu1, y: mu2}], {
      x: "x",
      y: "y",
      fill: "black",
      r: 5
    }),

    // Label for true mean
    Plot.text([{x: mu1, y: mu2, label: "μ"}], {
      x: "x",
      y: d => d.y + 0.3,
      text: "label",
      fontSize: 16,
      fontWeight: "bold",
      fill: "black",
      textAnchor: "middle"
    }),

    // Title
    Plot.text([`${(100 * (1 - alpha)).toFixed(0)}% Confidence Ellipses for Bivariate Normal`], {
      x: (plotDomain.xMin + plotDomain.xMax) / 2,
      y: plotDomain.yMax + (plotDomain.yMax - plotDomain.yMin) * 0.08,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Legend
    Plot.lineX([
      {x: plotDomain.xMax - 1.5, y: plotDomain.yMax - 0.3},
      {x: plotDomain.xMax - 0.9, y: plotDomain.yMax - 0.3}
    ], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text(["Covers μ"], {
      x: plotDomain.xMax - 0.8,
      y: plotDomain.yMax - 0.3,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),
    Plot.lineX([
      {x: plotDomain.xMax - 1.5, y: plotDomain.yMax - 0.7},
      {x: plotDomain.xMax - 0.9, y: plotDomain.yMax - 0.7}
    ], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text(["Fails to cover"], {
      x: plotDomain.xMax - 0.8,
      y: plotDomain.yMax - 0.7,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

``` {.sourceCode .js .code-with-copy}
html`<div style="font-size: 16px; margin-top: 20px; font-family: sans-serif;">
  <strong>Coverage statistics:</strong>
  ${ellipseData.filter(e => e.covers).length} of ${ellipseData.length} ellipses cover μ
  ${ellipseData.length > 0 ? ` (${(100 * ellipseData.filter(e => e.covers).length / ellipseData.length).toFixed(1)}%)` : ''}
</div>`
```

## Confidence intervals and confidence bounds {.anchored anchor-id="confidence-intervals-and-confidence-bounds"}

While confidence regions can come in all shapes (with ellipses and rectangles being common in dimensions greater than one), the most common shape in <span class="math inline">\$\\RR\$</span> is an interval or half-interval. When <span class="math inline">\$C(X) = $$C\_L(X), C\_U(X)$$ \\subseteq \\RR\$</span>, we call it a **confidence interval** (CI); when it is of the form <span class="math inline">\$$$C\_L(X), \\infty)\$</span> or <span class="math inline">\$(-\\infty, C\_U(X)$$\$</span> we call <span class="math inline">\$C\_L(X)\$</span> a **lower confidence bound** (LCB), and <span class="math inline">\$C\_U(X)\$</span> an **upper confidence bound** (UCB). We typically obtain confidence intervals by inverting a two-sided test of a point null, and confidence bounds by inverting a one-sided test in the appropriate direction.

A confidence bound is called **uniformly most accurate** (UMA) if it inverts a (non-randomized) UMP test, and a confidence interval is called **uniformly most accurate unbiased** (UMAU) if it inverts a (non-randomized) UMPU test.

**Example (Exponential):** As an example, suppose we observe <span class="math inline">\$X\\sim \\text{Exp}(\\theta)\$</span> and want to construct confidence bounds or a confidence interval for <span class="math inline">\$\\theta\$</span>. The cumulative distribution function is <span class="math inline">\$\\PP\_\\theta(X\\leq x) = 1-e^{-x/\\theta}\$</span>, for <span class="math inline">\$x&gt;0\$</span>.

To find a lower confidence bound, we invert the UMP test of <span class="math inline">\$H\_0:\\;\\theta \\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta &gt; \\theta\_0\$</span>, which rejects for large values of <span class="math inline">\$X\$</span>. The cutoff solves for <span class="math display">\\$$ \\alpha = \\PP\_{\\theta\_0}(X&gt;c\_\\alpha) = e^{-c\_\\alpha/\\theta\_0} \\iff c\_\\alpha = -\\theta\_0 \\log (\\alpha). \\$$</span> To invert this test, observe that the test rejects <span class="math inline">\$H\_0\$</span> if and only if <span class="math inline">\$X &gt; -\\theta\_0\\log (\\alpha)\$</span>. Hence, our confidence region is <span class="math display">\\$$ C(X) = \\{\\theta\_0:\\; X \\leq -\\theta\_0\\log(\\alpha)\\} = \\left\[\\frac{X}{-\\log(\\alpha)}, \\infty\\right), \\$$</span> giving lower confidence bound <span class="math inline">\$C\_L(X) = \\frac{X}{-\\log \\alpha}\$</span>.

By the same token, we can obtain an upper confidence bound by inverting the UMP test for <span class="math inline">\$H\_0:\\; \\theta \\geq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &lt; \\theta\_0\$</span>. That test rejects when <span class="math inline">\$X &lt; -\\theta\_0\\log (1-\\alpha)\$</span>, giving confidence region <span class="math display">\\$$ C(X) = \\left\\{\\theta\_0:\\; X \\geq -\\theta\_0\\log(1-\\alpha)\\right\\} = \\left(-\\infty, \\frac{X}{-\\log(1-\\alpha)}\\right$$, \\\]</span> and UCB <span class="math inline">\$C\_U(X)=\\frac{X}{-\\log(1-\\alpha)}\$</span>.

To obtain a <span class="math inline">\$1-\\alpha\$</span> confidence interval by inverting the equal-tailed test, we simply intersect the two confidence regions above, both computed at level <span class="math inline">\$1-\\alpha/2\$</span>; hence <span class="math display">\\$$ C(X)=\\left\[\\frac{X}{-\\log(\\alpha/2)}, \\frac{X}{-\\log(1-\\alpha/2)}\\right$$ \\\]</span>

To invert the UMPU test can be more involved in general, but we can exploit the fact that the exponential is a scale family. If <span class="math inline">\$c\_1\$</span> and <span class="math inline">\$c\_2\$</span> are the left and right cutoff for the UMPU test of <span class="math inline">\$H\_0:\\;\\theta=1\$</span> vs <span class="math inline">\$H\_0:\\;\\theta\\neq 1\$</span>, then the corresponding cutoffs for testing <span class="math inline">\$H\_0:\\;\\theta=\\theta\_0\$</span> are <span class="math inline">\$\\theta\_0 c\_1\$</span> and <span class="math inline">\$\\theta\_0 c\_2\$</span>. Hence, the confidence interval is <span class="math display">\\$$ C(X) = \\left\\{ \\theta\_0:\\; \\theta\_0 c\_1 \\leq X \\leq \\theta\_0 c\_2 \\right\\} = \\left\[\\frac{X}{c\_2}, \\frac{X}{c\_1}\\right$$. \\\]</span>

---

[← p-Values](02-p-values.md) · [Up: contents](index.md) · [(Mis-)Interpreting Hypothesis Tests →](04-mis--interpreting-hypothesis-tests.md)
