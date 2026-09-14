---
title: 3 Two-sided alternatives {.anchored number="3" anchor-id="two-sided-alternatives"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-one-parameter.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Two-sided alternatives {.anchored number="3" anchor-id="two-sided-alternatives"}

**Source:** [`reader/testing-one-parameter.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Often we want to test a null hypothesis against the alternative that the parameter is larger *or* smaller than a null value, or range of values. This section will consider a null hypothesis of the form <span class="math inline">\$H\_0:\\; \|\\theta - \\theta\_0\| \\leq \\delta\$</span> against the alternative <span class="math inline">\$H\_1:\\; \|\\theta - \\theta\_0\| &gt; \\delta\$</span>, for some tolerance <span class="math inline">\$\\delta \\geq 0\$</span>. In the important special case <span class="math inline">\$\\delta = 0\$</span> we will call <span class="math inline">\$H\_0\$</span> a *point null*, and if <span class="math inline">\$\\delta &gt; 0\$</span> we will call <span class="math inline">\$H\_0\$</span> an *interval null*.

### <span class="header-section-number">3.1</span> Two-tailed tests {.anchored number="3.1" anchor-id="two-tailed-tests"}

To test a two-sided alternative, we will generally employ a *two-tailed test* based on some test statistic <span class="math inline">\$T(X)\$</span>. We will say that <span class="math inline">\$\\phi(X)\$</span> *rejects for extreme <span class="math inline">\$T(X)\$</span>* (i.e., for large or small values of <span class="math inline">\$T(X)\$</span>) if <span class="math display">\\$$ \\phi(X) = \\begin{cases} 1 & \\quad \\text{ if } T(X) &lt; c\_1 \\text{ or } T(X) &gt; c\_2\\\\ 0 & \\quad \\text{ if } c\_1 &lt; T(X) &lt; c\_2\\\\ \\gamma\_i &\\quad \\text{ if } T(X) = c\_i, \\; i = 1,2 \\end{cases} \\$$</span>

When we test with a two-sided alternative we will generally not be able to optimize power everywhere. For example, if we test <span class="math inline">\$H\_0:\\; \\theta = 0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta \\neq 0\$</span> in the <span class="math inline">\$z\$</span>-test problem <span class="math inline">\$X \\sim N(\\theta,1)\$</span>, we can choose any test of the form <span class="math display">\\$$ \\phi\_{\\alpha\_1}(x) = 1\\{x &lt; -z\_{\\alpha\_1}\\} + 1\\{x &gt; z\_{\\alpha - \\alpha\_1}\\}, \\$$</span> for any <span class="math inline">\$\\alpha\_1 \\in $$0,\\alpha$$\$</span>. We obtain the right- and left-tailed tests in the limit where <span class="math inline">\$\\alpha\$</span> is <span class="math inline">\$0\$</span> or <span class="math inline">\$\\alpha\$</span> respectively, and the usual symmetric two-tailed test when <span class="math inline">\$\\alpha\_1 = \\alpha/2\$</span>.

<figure class="figure">
<p><img src="testing-one-parameter_files/figure-html/unnamed-chunk-3-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Note that two of the three tests shown above have the undesirable property that the power falls below <span class="math inline">\$\\alpha\$</span> on part of the alternative: that is, there are alternative values of <span class="math inline">\$\\theta\$</span> for which our chance of rejecting the null is even less than it would be if the null were true.

None of the tests plotted above is as powerful for <span class="math inline">\$\\theta &gt; 0\$</span> as the right-tailed test (<span class="math inline">\$\\alpha\_1 = 0\$</span>), and none is as powerful for <span class="math inline">\$\\theta &lt; 0\$</span> as the left-tailed test (<span class="math inline">\$\\alpha\_1 = \\alpha\$</span>), and intuitively it is clear that we cannot hope to find a test that maximizes power on both parts of the alternative.

As in the case with estimation, one way that we can proceed when there is no UMP test is to impose a constraint that rules out all but one test. In the <span class="math inline">\$z\$</span>-test above, the test with <span class="math inline">\$\\alpha\_1 = \\alpha/2\$</span> is symmetric in two respects:

1.  It is *equal-tailed*, meaning that we have dedicated an equal portion of our total Type I error budget to the left and right lobes of the rejection region, and

2.  It is *unbiased*, meaning that the power is at least <span class="math inline">\$\\alpha\$</span> everywhere on the alternative.

The idea of an equal-tailed test makes sense when <span class="math inline">\$H\_0\$</span> is simple, but it is not obvious how it extends to the more common situation where <span class="math inline">\$H\_0\$</span> is composite. We will focus on the latter condition, unbiasedness.

### <span class="header-section-number">3.2</span> Exponential example {.anchored number="3.2" anchor-id="exponential-example"}

Consider testing <span class="math inline">\$H\_0:\\;\\theta = 1\$</span> vs <span class="math inline">\$H\_1:\\;\\theta \\neq 1\$</span> in the model where <span class="math inline">\$X \\sim \\text{Exp}(\\theta)\$</span>, with cdf <span class="math display">\\$$F\_\\theta(t) = \\PP\_\\theta(X \\leq t) = 1-e^{-t/\\theta}.\\$$</span> To solve for the equal-tailed test cutoffs we set <span class="math inline">\$c\_1^{\\text{ET}}=F\_1^{-1}(1-\\alpha/2) = -\\log(1-\\alpha/2)\$</span> and <span class="math inline">\$c\_2^{\\text{ET}}= F\_1^{-1}(\\alpha/2) = -\\log(\\alpha/2)\$</span>. Then the power function of the equal-tailed test <span class="math inline">\$\\phi^{\\text{ET}}\$</span> is

<span class="math display">\\$$ \\begin{aligned} \\beta\_{\\phi^{\\text{ET}}}(\\theta) &= \\PP\_\\theta(X &lt; c\_1^{\\text{ET}}) + \\PP\_\\theta(X &gt; c\_2^{\\text{ET}})\\\\ &= 1 - e^{-c\_1^{\\text{ET}}/\\theta} +e^{-c\_2^{\\text{ET}}/\\theta}\\\\ &= 1 - (1-\\alpha/2)^{1/\\theta} + (\\alpha/2)^{1/\\theta} \\end{aligned} \\$$</span> This test does indeed have power equal to <span class="math inline">\$\\alpha\$</span> at <span class="math inline">\$\\theta = 1\$</span>, but its power is also <span class="math inline">\$\\alpha\$</span> at <span class="math inline">\$\\theta = 1/2\$</span>, and the power is actually below <span class="math inline">\$\\alpha\$</span> on <span class="math inline">\$(1/2,1)\$</span>. So this is not an unbiased test. If we want an unbiased test, we need to set the *derivative* of the power equal to <span class="math inline">\$0\$</span> at <span class="math inline">\$\\theta = 1\$</span>. We can solve this numerically in terms of the left-lobe rejection probability <span class="math inline">\$\\alpha\_1\$</span>, taking <span class="math display">\\$$ \\begin{aligned} c\_1(\\alpha\_1) &=-\\log(1-\\alpha\_1), \\quad\\text{ and }\\\\ c\_2(\\alpha\_1) &= -\\log(\\alpha\_2)=-\\log(\\alpha-\\alpha\_1). \\end{aligned} \\$$</span> If <span class="math inline">\$\\alpha = 0.1\$</span> we obtain <span class="math inline">\$\\alpha\_1 = 0.080\$</span>, <span class="math inline">\$c\_1 = 0.083\$</span>, and <span class="math inline">\$c\_2 = 3.9\$</span> for the unbiased test, vs <span class="math inline">\$c\_1 = 0.051\$</span> and <span class="math inline">\$c\_2 = 3.0\$</span> for the equal-tailed test. The unbiased test is not as powerful for <span class="math inline">\$\\theta &gt; 1\$</span>, but it is more powerful for <span class="math inline">\$\\theta &lt; 1\$</span>, and its power is minimized at <span class="math inline">\$\\alpha\$</span> when <span class="math inline">\$\\theta = 1\$</span>. We plot both power curves below.

<figure class="figure">
<p><img src="testing-one-parameter_files/figure-html/unnamed-chunk-4-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

The following widget gives the range of options for two-tailed tests of the point hypothesis <span class="math inline">\$H\_0:\\;\\theta = 1\$</span> for the Gamma distribution with shape parameter <span class="math inline">\$k\$</span> and scale parameter <span class="math inline">\$\\theta\$</span>:

``` {.sourceCode .js .code-with-copy}
jStat = require("https://cdn.jsdelivr.net/npm/jstat@latest/dist/jstat.min.js")

// Define gamma PDF
gammaPDF = (x, k, theta) => {
  if (x <= 0) return 0;
  return Math.pow(x, k-1) * Math.exp(-x/theta) / (Math.pow(theta, k) * jStat.gammafn(k));
}

// Define gamma CDF using jStat
gammaCDF = (x, k, theta) => {
  if (x <= 0) return 0;
  return jStat.gamma.cdf(x, k, theta);
}

// Define gamma quantile using jStat
gammaQuantile = (p, k, theta) => {
  return jStat.gamma.inv(p, k, theta);
}

// Fixed parameters
alpha = 0.1

// Interactive controls
viewof k = Inputs.range([0.5, 10], {value: 2, step: 0.1, label: "k (shape)"})

// For unbiased test, we need E[X | X in rejection region] = k
// This requires finding alpha1 such that the conditional expectation equals k
getUnbiasedAlpha1 = (k) => {
  // Function to compute E[X | X <= c1 or X >= c2] for given alpha1
  const conditionalExpectation = (a1) => {
    const a2 = alpha - a1;
    const c1 = gammaQuantile(a1, k, 1);
    const c2 = gammaQuantile(1 - a2, k, 1);

    // E[X * I(X <= c1)] for Gamma(k, 1)
    // This is the incomplete gamma function times k
    const leftExpectation = k * gammaCDF(c1, k + 1, 1);

    // E[X * I(X >= c2)] for Gamma(k, 1)
    const rightExpectation = k * (1 - gammaCDF(c2, k + 1, 1));

    // Total expectation in rejection region divided by total probability
    return (leftExpectation + rightExpectation) / alpha;
  };

  // Use bisection to find alpha1 where conditional expectation equals k
  let low = 0.001;
  let high = alpha - 0.001;
  let mid;
  const tolerance = 0.0001;
  const maxIter = 50;

  for (let i = 0; i < maxIter; i++) {
    mid = (low + high) / 2;
    const condExp = conditionalExpectation(mid);

    if (Math.abs(condExp - k) < tolerance) {
      break;
    }

    // For Gamma, increasing alpha1 typically decreases conditional expectation
    if (condExp > k) {
      low = mid;
    } else {
      high = mid;
    }
  }

  return mid;
}

// Calculate the unbiased value for current k
unbiasedAlpha1 = getUnbiasedAlpha1(k)

// Create the slider
viewof alpha1 = Inputs.range([0, alpha], {
  value: alpha / 2,
  step: 0.001,
  label: "α₁ (left tail mass)"
})

// Calculate alpha2 (right tail mass)
alpha2 = alpha - alpha1

// Calculate critical values under null (theta = 1)
c1 = gammaQuantile(alpha1, k, 1)
c2 = gammaQuantile(1 - alpha2, k, 1)

// Generate data for null distribution plot
nullData = {
  const xMin = 0;
  const xMax = gammaQuantile(0.999, k, 1);
  const numPoints = 1000;
  const dx = (xMax - xMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const x = xMin + i * dx;
    const density = gammaPDF(x, k, 1);
    const inRejection = (x <= c1 || x >= c2);
    return {
      x: x,
      density: density,
      densityRej: inRejection ? density : 0
    };
  });
}

// Power function calculation
powerFunction = (theta) => {
  // Power = P(reject H0 | theta) = P(X <= c1 | theta) + P(X >= c2 | theta)
  return gammaCDF(c1, k, theta) + (1 - gammaCDF(c2, k, theta));
}

// Generate data for power function plot
powerData = {
  const thetaMin = 0.1;
  const thetaMax = 3;
  const numPoints = 300;
  const dtheta = (thetaMax - thetaMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const theta = thetaMin + i * dtheta;
    return {
      theta: theta,
      power: powerFunction(theta)
    };
  });
}

// Left panel: Null distribution with rejection region
leftPlot = Plot.plot({
  width: 400,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: { fontSize: "18px" },

  x: {
    domain: [0, Math.max(...nullData.map(d => d.x))],
    label: "x",
    labelAnchor: "center",
    labelOffset: 60,
    labelArrow: "none"
  },
  y: {
    domain: [0, Math.max(...nullData.map(d => d.density)) * 1.15],
    label: "p₁(x)",
    labelAnchor: "center",
    labelOffset: 70,
    labelArrow: "none"
  },

  marks: [
    // Fill rejection region
    Plot.areaY(nullData, {x: "x", y: "densityRej", fill: "red", opacity: 0.3}),
    // Null density curve
    Plot.line(nullData, {x: "x", y: "density", stroke: "steelblue", strokeWidth: 2}),
    // Critical values
    Plot.ruleX([c1], {stroke: "red", strokeWidth: 1.5, strokeDasharray: "5,5"}),
    Plot.ruleX([c2], {stroke: "red", strokeWidth: 1.5, strokeDasharray: "5,5"}),
    Plot.ruleY([0]),

    // Title above plot
    Plot.text(["Null Distribution (θ=1)"], {
      x: Math.max(...nullData.map(d => d.x))/2,
      y: Math.max(...nullData.map(d => d.density)) * 1.12,
      fontSize: 16,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Annotations for critical values (moved lower)
    Plot.text([`c₁=${c1.toFixed(2)}`], {
      x: c1,
      y: -Math.max(...nullData.map(d => d.density)) * 0.15,
      fontSize: 14,
      textAnchor: "middle"
    }),
    Plot.text([`c₂=${c2.toFixed(2)}`], {
      x: c2,
      y: -Math.max(...nullData.map(d => d.density)) * 0.15,
      fontSize: 14,
      textAnchor: "middle"
    })
  ]
})

// Right panel: Power function
rightPlot = Plot.plot({
  width: 400,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: { fontSize: "18px" },

  x: {
    domain: [0, 3],
    label: "θ (scale parameter)",
    labelAnchor: "center",
    labelOffset: 60,
    labelArrow: "none"
  },
  y: {
    domain: [0, 1],
    label: "Power",
    labelAnchor: "center",
    labelOffset: 70,
    labelArrow: "none"
  },

  marks: [
    // Power function curve
    Plot.line(powerData, {x: "theta", y: "power", stroke: "steelblue", strokeWidth: 2}),
    // Significance level line
    Plot.ruleY([alpha], {stroke: "gray", strokeWidth: 1, strokeDasharray: "5,5"}),
    // Null hypothesis point
    Plot.dot([{theta: 1, power: powerFunction(1)}], {
      x: "theta",
      y: "power",
      r: 5,
      fill: "red"
    }),
    Plot.ruleY([0]),
    Plot.ruleX([1], {stroke: "gray", strokeWidth: 1, strokeDasharray: "3,3"}),

    // Title above plot
    Plot.text(["Power Function"], {
      x: 1.5,
      y: 0.98,
      fontSize: 16,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Annotation for significance level
    Plot.text([`α=${alpha}`], {
      x: 2.8,
      y: alpha + 0.03,
      fontSize: 14,
      textAnchor: "end"
    })
  ]
})

// Combine plots and buttons
html`<div>
  <div style="text-align: center; margin-bottom: 20px;">
    <h3 style="font-size: 20px; font-weight: bold;">Unbiased Two-Sided Test for Gamma Scale Parameter</h3>
    <p style="font-size: 16px;">Testing H₀: θ = 1 vs H₁: θ ≠ 1 with significance level α = ${alpha}</p>
    <p style="font-size: 14px;">Left tail: α₁ = ${alpha1.toFixed(3)}, Right tail: α₂ = ${alpha2.toFixed(3)}</p>
  </div>

  <div style="margin: 10px 0; text-align: center;">
    <span style="font-size: 14px; margin-right: 10px;">Quick presets:</span>
    <button onclick="
      const sliders = document.querySelectorAll('input[type=range]');
      if (sliders.length >= 2) {
        sliders[1].value = 0.05;
        sliders[1].dispatchEvent(new Event('input', {bubbles: true}));
      }
    "
            style="margin: 0 5px; padding: 5px 10px; background: ${Math.abs(alpha1 - 0.05) < 0.001 ? '#4682b4' : '#f0f0f0'};
                   color: ${Math.abs(alpha1 - 0.05) < 0.001 ? 'white' : 'black'};
                   border: 1px solid #ccc; border-radius: 4px; cursor: pointer;">
      Equal-tailed (α₁ = 0.050)
    </button>
    <button onclick="
      const sliders = document.querySelectorAll('input[type=range]');
      if (sliders.length >= 2) {
        sliders[1].value = ${unbiasedAlpha1};
        sliders[1].dispatchEvent(new Event('input', {bubbles: true}));
      }
    "
            style="margin: 0 5px; padding: 5px 10px; background: ${Math.abs(alpha1 - unbiasedAlpha1) < 0.001 ? '#4682b4' : '#f0f0f0'};
                   color: ${Math.abs(alpha1 - unbiasedAlpha1) < 0.001 ? 'white' : 'black'};
                   border: 1px solid #ccc; border-radius: 4px; cursor: pointer;">
      Unbiased (α₁ ≈ ${unbiasedAlpha1.toFixed(3)})
    </button>
  </div>

  <div style="display: flex; gap: 20px; justify-content: center;">
    ${leftPlot}
    ${rightPlot}
  </div>
</div>`
```

### <span class="header-section-number">3.3</span> Optimal unbiased tests {.anchored number="3.3" anchor-id="optimal-unbiased-tests"}

If we are testing a point null against a two-sided alternative, we can take our choice between the equal-tailed and unbiased test, but the unbiasedness criterion is conceptually appealing for more general testing problems because the definition naturally extends to the case where <span class="math inline">\$H\_0\$</span> is composite. For example, if we want to test an interval null against a two-sided alternative, it is not clear what it means to set <span class="math inline">\$\\PP\_{H\_0}(T(X) &lt; c\_1) = \\alpha/2\$</span>, because that probability varies over the null parameter space <span class="math inline">\$\\Theta\_0\$</span>. By contrast, the unbiased criterion is well-defined for any hypothesis testing problem.

If the power function is differentiable in <span class="math inline">\$\\theta\$</span>, and <span class="math inline">\$\\theta\_0\$</span> is in <span class="math inline">\$\\Theta^{\\circ}\$</span>, the interior of the parameter space, then any unbiased test <span class="math inline">\$\\phi\$</span> must have <span class="math inline">\$\\beta\_\\phi(\\theta\_0) = \\alpha\$</span> and <span class="math inline">\$\\dot{\\beta}\_{\\phi}(\\theta\_0) = 0\$</span>. Otherwise, the power would be strictly less than <span class="math inline">\$\\alpha\$</span> at either <span class="math inline">\$\\theta\_0 +\\varepsilon\$</span> or <span class="math inline">\$\\theta\_0- \\varepsilon\$</span>, for sufficiently small <span class="math inline">\$\\varepsilon&gt;0\$</span>.

In exponential family models, we can use these facts to obtain a simple characterization of the criterion that the power function has zero derivative at <span class="math inline">\$\\theta\_0\$</span>, as. Let <span class="math inline">\$X \\sim p\_\\theta(x) = e^{\\theta T(x) - A(\\theta)}h(x)\$</span>, and differentiate the power function to obtain <span class="math display">\\$$ \\begin{aligned} \\dot{\\beta}\_{\\phi}(\\theta\_0) &= \\frac{d}{d\\theta} \\left. \\int \\phi(x)e^{\\theta T(x) - A(\\theta)}h(x)\\,d\\mu(x)\\right\|\_{\\theta=\\theta\_0} \\\\ &= \\int \\phi(x)(T(x)-\\dot{A}(\\theta\_0))e^{\\theta\_0 T(x) - A(\\theta\_0)}h(x)\\,d\\mu(x)\\\\ &= \\EE\_{\\theta\_0}\\left\[\\phi(X)(T(X) - \\EE\_{\\theta\_0}T(X))\\right$$\\\\$$5pt$$ &= \\text{Cov}\_{\\theta\_0}(T(X), \\phi(X))\\\\$$5pt$$ &= \\EE\_{\\theta\_0}\\left$$(\\phi(X)-\\alpha)T(X)\\right$$. \\end{aligned} \\\]</span> Setting the last expression to 0 and massaging the equation a bit, we obtain <span class="math display">\\$$ \\EE\_{\\theta\_0}T(X) = \\frac{\\EE\_{\\theta\_0}\[\\phi(X)T(X)$$}{\\alpha} = \\EE\_{\\theta\_0}$$T(X) \\mid \\phi(X) \\text{ rejects } H\_0$$. \\\]</span> Thus, the conditional expectation of <span class="math inline">\$T(X)\$</span> under the null, given that it falls in the rejection region, is the same as the marginal expectation. For instance, both the acceptance region and the rejection region for our unbiased test of <span class="math inline">\$H\_0:\\;\\theta=1\$</span> in the exponential model share the same “balance point” at <span class="math inline">\$\\EE\_{1}X = 1\$</span>. Because the right lobe is farther out from 1, it has only about 1/4 as much probability mass as the right lobe.

<figure class="figure">
<p><img src="testing-one-parameter_files/figure-html/unnamed-chunk-6-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Recall that when we restricted our attention to unbiased estimators, we were able to find a unique best unbiased estimator. Likewise, we can sometimes find an optimal two-sided test if we restrict our attention to unbiased tests. We say that <span class="math inline">\$\\phi^\*\$</span> is *UMP unbiased* (UMPU) if, for any other unbiased level <span class="math inline">\$\\alpha\$</span> test <span class="math inline">\$\\phi\$</span>, we have <span class="math inline">\$\\beta\_{\\phi^\*}(\\theta) \\geq \\beta\_{\\phi}(\\theta)\$</span> for all <span class="math inline">\$\\theta \\in \\Theta\_1\$</span>. UMPU tests exist, at least, for one-parameter exponential family models, as we show below.

**Theorem (UMP Unbiased tests):** Assume we want to test <span class="math inline">\$H\_0:\\;\|\\theta -\\theta\_0\| \\leq \\delta\$</span> vs <span class="math inline">\$H\_1:\\;\|\\theta - \\theta\_0\| &gt; \\delta\$</span> in the model <span class="math inline">\$X \\sim e^{\\theta T(x)-A(\\theta)}h(x)\$</span>, for <span class="math inline">\$\\delta \\geq 0\$</span> and <span class="math inline">\$\\theta\_0-\\delta, \\theta+\\delta \\in \\Theta^\\circ\$</span>, the interior of the parameter space. Suppose that the test <span class="math inline">\$\\phi^\*(X)\$</span> rejects for extreme values of <span class="math inline">\$T(X)\$</span>, with the cutoffs <span class="math inline">\$c\_1,c\_2,\\gamma\_1,\\gamma\_2\$</span> chosen so that

1.  <span class="math inline">\$\\phi^\*\$</span> attains power <span class="math inline">\$\\alpha\$</span> at the boundary of the null, i.e. <span class="math inline">\$\\beta\_{\\phi^\*}(\\theta\_0 - \\delta) = \\beta\_{\\phi^\*}(\\theta\_0 + \\delta) = \\alpha\$</span>, and

2.  if <span class="math inline">\$\\delta&gt; 0\$</span>, the power function is flat at <span class="math inline">\$\\theta\_0\$</span>, i.e. <span class="math inline">\$\\dot{\\beta}\_{\\phi^\*}(\\theta\_0) = 0\$</span>.

Then <span class="math inline">\$\\phi^\*\$</span> is UMPU.

**Proof:** Assume without loss of generality that <span class="math inline">\$\\theta\_0 = 0\$</span>, and first consider the case <span class="math inline">\$\\delta = 0\$</span>. Our proof will proceed much as it did for the Neyman-Pearson lemma. For <span class="math inline">\$\\theta \\neq 0\$</span>, we want to solve the problem <span class="math display">\\$$ \\begin{aligned} \\maxz\_\\phi &\\int \\phi(x)p\_{\\theta}(x)\\,d\\mu(x)\\\\ \\text{ subject to } &\\int \\phi(x)p\_0(x)\\,d\\mu(x) = \\alpha, \\quad\\text{ and }\\\\ &\\int \\phi(x)(T(x)-\\nu\_0)p\_0(x)\\,d\\mu(x) = 0, \\end{aligned} \\$$</span> where <span class="math inline">\$\\nu\_0 = \\EE\_0 T(X)\$</span>. Note that we have an equality constraint for the Type I error, because any unbiased test must have power exactly equal to <span class="math inline">\$\\alpha\$</span> at <span class="math inline">\$\\theta\_0\$</span>. The Lagrangian is <span class="math display">\\$$ \\begin{aligned} &\\int \\phi p\_{\\theta}\\,d\\mu - \\lambda\_1\\int \\phi p\_0\\,d\\mu - \\lambda\_2\\int \\phi (T-\\nu\_0)p\_0 \\,d\\mu \\\\ &\\quad = \\int \\phi\\left(p\_\\theta -\\lambda\_1 p\_0 - \\lambda\_2(T-\\nu\_0)p\_0\\right)\\,d\\mu \\\\ &\\quad = \\int \\phi\\left(\\frac{p\_\\theta}{p\_0} - \\lambda\_1 - \\lambda\_2(T-\\nu\_0)\\right)\\,dP\_0. \\end{aligned} \\$$</span> Since <span class="math inline">\$\\frac{p\_\\theta}{p\_0}(x) = e^{\\theta T(x) - A(\\theta)+A(0)}\$</span>, the test that maximizes this Lagrangian has <span class="math display">\\$$ \\phi^\*(x) = \\begin{cases} 1 &\\quad \\text{ if } e^{\\theta T(x)} &gt; a\_0 + a\_1 T(x)\\\\ 0 &\\quad \\text{ if } e^{\\theta T(x)} &lt; a\_0 + a\_1 T(x)\\\\ \\text{anything} &\\quad \\text{ if } e^{\\theta T(x)} = a\_0 + a\_1 T(x) \\end{cases} \\$$</span> for <span class="math inline">\$a\_0 = (\\lambda\_1 - \\lambda\_2\\nu\_0)e^{A(0)-A(\\theta)}\$</span> and <span class="math inline">\$a\_1 = \\lambda\_2 e^{A(0)-A(\\theta)}\$</span>.

For any <span class="math inline">\$c\_1,c\_2\$</span> we can find <span class="math inline">\$a\_1 &gt; 0\$</span> and <span class="math inline">\$a\_0\\in \\RR\$</span> for which <span class="math inline">\$e^{\\theta t} = a\_0 + a\_1 t\$</span> at <span class="math inline">\$t = c\_1,c\_2\$</span>, in which case <span class="math inline">\$e^{t\\theta} &gt; a\_0 + a\_1 t\$</span> for <span class="math inline">\$t &lt; c\_1\$</span> and <span class="math inline">\$t &gt; c\_2\$</span> and <span class="math inline">\$e^{t\\theta} &lt; a\_0 + a\_1 t\$</span> otherwise; then we can solve for <span class="math inline">\$\\lambda\_1,\\lambda\_2 \\in \\RR\$</span> for which our <span class="math inline">\$\\phi^\*\$</span> maximizes the Lagrangian.

Now, for any other test <span class="math inline">\$\\phi\$</span> that satisfies the unbiasedness constraints we can write <span class="math display">\\$$ \\begin{aligned} \\beta\_{\\phi}(\\theta) &= \\beta\_{\\phi}(\\theta) - \\lambda\_1\\left(\\beta\_{\\phi}(0) - \\alpha\\right) -\\lambda\_2 \\dot\\beta\_{\\phi}(0)\\\\ &\\leq \\beta\_{\\phi^\*}(\\theta) - \\lambda\_1\\left(\\beta\_{\\phi^\*}(0) - \\alpha\\right) -\\lambda\_2 \\dot\\beta\_{\\phi^\*}(0)\\\\ &= \\beta\_{\\phi^\*}(\\theta). \\end{aligned} \\$$</span> Since <span class="math inline">\$\\theta\$</span> was arbitrary, we have the result.

The proof for <span class="math inline">\$\\delta &gt; 0\$</span> is similar, with the constraints <span class="math inline">\$\\beta\_{\\phi}(0) = \\alpha\$</span> and <span class="math inline">\$\\dot{\\beta}\_{\\phi}(0) = 0\$</span> replaced by <span class="math inline">\$\\beta\_{\\phi}(-\\delta) = \\beta\_{\\phi}(\\delta) =\\alpha\$</span>.

---

[← 2 One-sided testing {.anchored number="2" anchor-id="one-sided-testing"}](03-2-one-sided-testing-anchored-number-2-anchor-id-one-sided-te.md) · [Up: contents](index.md)
