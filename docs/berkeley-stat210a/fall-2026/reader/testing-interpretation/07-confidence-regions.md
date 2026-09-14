---
title: Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Confidence Regions

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Suppose we are testing $H_0:\theta = 0$ vs $H_1:\; \theta \neq 0$. When the $p$-value is very small, it gives us a strong indication that the data set we observed is inconsistent with the parameter value $\theta=0$. It does *not* necessarily follow that the data set is indicating that the $\theta$ value is *far* from zero: for example, if we have a huge data set we might be able to say with very high confidence that $\theta$ is in the range $[0.0011,0.0012]$. Depending on the context, this could practically amount to *confirming* the informal scientific null that $\theta$ is too small to care about. But if we looked at the $p$-value it will tell us (accurately) that the formal statistical null $\theta=0$ is highly implausible.

By the same token, we could also be mistaken if we observe that the $p$-value is large and conclude that $\theta$ must be close to zero. It *could* be the case that the data set establishes that $\theta$ is in a narrow range around zero, *or* it could simply be that the data give very poor evidence about $\theta$ so we still don't know very much about it.

Confidence intervals, and more generally confidence regions, are a more reliable guide than $p$-values if we want to know what range of $\theta$ values are plausible in light of the data. As we will see, they can be obtained using the same machinery we have developed for hypothesis tests. Whereas the $p$-value tells us what our test would decide for all values of $k$, we can think of a confidence region as telling us what our test of a point null $H_0:\; \theta = \theta_0$ vs $H_1:\; \theta\neq 0$ would decide for all values of $\theta_0$.

## Definition of a confidence region

**Definition:** We say that $C(X)$ is a $1-\alpha$ confidence region for $g(\theta)$ if:

$$
\PP_\theta(C(X) \ni g(\theta)) \geq 1-\alpha, \quad \text{for all } \theta \in \Theta
$$
We say that $C(x)$ **covers** $g(\theta)$ if $C(x) \ni g(\theta)$, and the **coverage probability** at a parameter value $\theta$ is $\PP_\theta(C(X) \ni g(\theta))$. The **confidence level** of $C(X)$ is $\inf_{\theta\in\Theta} \mathbb{P}_\theta(C(X) \ni g(\theta))$.

The use of the "$\ni$" symbol in the above definition is deliberate. To avoid common misinterpretations, we should always think and speak of the interval or region $C(X)$ as the random "subject" of the mathematical sentence and the estimand $g(\theta)$ as the fixed "object."

The confidence interval is commonly misinterpreted as a Bayesian guarantee, where $C(X)$ is first realized and then $g(\theta)$ has some probability of falling into $C(X)$. This interpretation is incorrect: confidence intervals are frequentist objects whose guarantee is intended to apply for fixed $\theta$ values. Once $X$ is realized $C(X)$ either does or does not contain the estimand $g(\theta)$; there is no remaining randomness in the problem.

Thus, while the following formulations are technically mathematically equivalent, the second one tends to give people the wrong impression and is not recommended:

- **Formulation 1 (recommended):** $C(X)$ has a $95\%$ chance of covering $g(\theta)$

- **Formulation 2 (not recommended):** $g(\theta)$ has a $95\%$ chance of falling in $C(X)$

Once we have calculated, say, $C(X) = [0.8, 1.1]$, it is *never* correct to say "there is a $95\%$ chance $g(\theta) \in [0.8, 1.1]$" on the basis of a confidence interval guarantee. Under a frequentist model this is a category error since $g(\theta)$ is not random, and even under a Bayesian model where there is an *a posteriori* probability, that probability depends on our prior.

## Duality of tests and confidence regions

Confidence regions are closely related to hypothesis tests, and one can be constructed from the other, as we see below.

Suppose we have a level $\alpha$ test $\phi(X; a)$ of $H_0: g(\theta) = a$ vs $H_1: g(\theta) \neq a$, for every value $a$. Then we can use these tests to construct a (non-randomized) confidence region for $g(\theta)$ as follows:

$$
C(X) = \{a: \phi(X; a) < 1\}
$$
That is, $C(X)$ is all *non-rejected* values of $a$. $C(X)$ is a valid confidence region because
$$
\mathbb{P}_\theta(C(X) \ni g(\theta)) = \mathbb{P}_\theta(\phi(X; g(\theta)) < 1) \geq 1-\alpha
$$
Constructing an interval in this way is called **inverting** a test (or more precisely, a family of tests, one for each $a$ value).

Conversely, we can obtain a test by inverting a confidence region. Suppose $C(X)$ is a $1-\alpha$ confidence region for $g(\theta)$. Then
$$
\phi(x; a) = 1\{a \notin C(x)\}
$$
is a valid level-$\alpha$ test of the null $H_0: g(\theta) = a$ vs. the alternative $H_1: g(\theta) \neq a$, because
$$
\mathbb{E}_\theta \phi(X; g(\theta)) = \mathbb{P}_\theta(g(\theta) \notin C(X)) \leq \alpha
$$
A confidence region is called **unbiased** if its probability of including any value *other than* the true $g(\theta)$ is *at most* $1-\alpha$:
$$
\PP_\theta( C(X) \ni a) \leq 1-\alpha, \quad \text{ for all } a \neq g(\theta).
$$
It is immediate from the definition that $C(X)$ is unbiased if and only if the test we obtain by inverting it is unbiased. Likewise, the confidence region obtained by inverting an unbiased *non-randomized* test is also unbiased.

**Example (Multivariate Gaussian confidence ellipse)** Suppose that we observe $X \sim N_d(\mu, \Sigma)$, where the covariance matrix $\Sigma$ is known and $\mu\in\RR^d$ is unknown. We can define
$$
Z = \Sigma^{-1/2}(X-\mu) \sim N_d(0,I_d).
$$

A natural test of the point null $H_0:\; \mu = \mu_0$ vs $H_1:\; \mu \neq \mu_0$ is to reject for large values of
$$
\|\Sigma^{-1/2} (X-\mu_0)\|^2 \stackrel{H_0}{\sim} \chi_d^2.
$$
Let $c_\alpha$ denote the upper $\alpha$ quantile of the null distribution. The confidence region we obtain by inverting this test is the ellipse:
$$
C(X) = \left\{\mu_0:\; \|\Sigma^{-1/2}(X-\mu_0)\|^2 \leq c_\alpha\right\}.
$$

The widget below illustrates the process of sampling these confidence regions.

```ojs
//| echo: false

// Import jStat for statistical functions
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

// User controls for parameters
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

// Display coverage statistics
html`<div style="font-size: 16px; margin-top: 20px; font-family: sans-serif;">
  <strong>Coverage statistics:</strong>
  ${ellipseData.filter(e => e.covers).length} of ${ellipseData.length} ellipses cover μ
  ${ellipseData.length > 0 ? ` (${(100 * ellipseData.filter(e => e.covers).length / ellipseData.length).toFixed(1)}%)` : ''}
</div>`
```


## Confidence intervals and confidence bounds

While confidence regions can come in all shapes (with ellipses and rectangles being common in dimensions greater than one), the most common shape in $\RR$ is an interval or half-interval. When $C(X) = [C_L(X), C_U(X)] \subseteq \RR$, we call it a **confidence interval** (CI); when it is of the form $[C_L(X), \infty)$ or $(-\infty, C_U(X)]$ we call $C_L(X)$ a **lower confidence bound** (LCB), and $C_U(X)$ an **upper confidence bound** (UCB). We typically obtain confidence intervals by inverting a two-sided test of a point null, and confidence bounds by inverting a one-sided test in the appropriate direction.

A confidence bound is called **uniformly most accurate** (UMA) if it inverts a (non-randomized) UMP test, and a confidence interval is called **uniformly most accurate unbiased** (UMAU) if it inverts a (non-randomized) UMPU test.

**Example (Exponential):** As an example, suppose we observe $X\sim \text{Exp}(\theta)$ and want to construct confidence bounds or a confidence interval for $\theta$. The cumulative distribution function is $\PP_\theta(X\leq x) = 1-e^{-x/\theta}$, for $x>0$.

To find a lower confidence bound, we invert the UMP test of $H_0:\;\theta \leq \theta_0$ vs $H_1:\; \theta > \theta_0$, which rejects for large values of $X$. The cutoff solves for
$$
\alpha = \PP_{\theta_0}(X>c_\alpha) = e^{-c_\alpha/\theta_0} \iff c_\alpha = -\theta_0 \log (\alpha).
$$
To invert this test, observe that the test rejects $H_0$ if and only if $X > -\theta_0\log (\alpha)$. Hence, our confidence region is
$$
C(X) = \{\theta_0:\;  X \leq -\theta_0\log(\alpha)\} = \left[\frac{X}{-\log(\alpha)}, \infty\right),
$$
giving lower confidence bound $C_L(X) = \frac{X}{-\log \alpha}$.

By the same token, we can obtain an upper confidence bound by inverting the UMP test for $H_0:\; \theta \geq \theta_0$ vs $H_1:\;\theta < \theta_0$. That test rejects when $X < -\theta_0\log (1-\alpha)$, giving confidence region
$$
C(X) = \left\{\theta_0:\; X \geq -\theta_0\log(1-\alpha)\right\} = \left(-\infty, \frac{X}{-\log(1-\alpha)}\right],
$$
and UCB $C_U(X)=\frac{X}{-\log(1-\alpha)}$.

To obtain a $1-\alpha$ confidence interval by inverting the equal-tailed test, we simply intersect the two confidence regions above, both computed at level $1-\alpha/2$; hence
$$
C(X)=\left[\frac{X}{-\log(\alpha/2)}, \frac{X}{-\log(1-\alpha/2)}\right]
$$

To invert the UMPU test can be more involved in general, but we can exploit the fact that the exponential is a scale family. If $c_1$ and $c_2$ are the left and right cutoff for the UMPU test of $H_0:\;\theta=1$ vs $H_0:\;\theta\neq 1$, then the corresponding cutoffs for testing $H_0:\;\theta=\theta_0$ are $\theta_0 c_1$ and $\theta_0 c_2$. Hence, the confidence interval is
$$
C(X) = \left\{ \theta_0:\; \theta_0 c_1 \leq X \leq \theta_0 c_2  \right\} = \left[\frac{X}{c_2}, \frac{X}{c_1}\right].
$$

---

[← Pre-compute for a reasonable range of d and k](06-pre-compute-for-a-reasonable-range-of-d-and-k.md) · [Up: contents](index.md) · [(Mis-)Interpreting Hypothesis Tests →](08-mis--interpreting-hypothesis-tests.md)
