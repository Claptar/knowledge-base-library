---
title: 3 Conjugate priors
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Conjugate priors

**Source:** [`reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

A special class of easy-to-update prior distributions is the set of *conjugate priors*. For data <span class="math inline">\$X\$</span> drawn from a likelihood model <span class="math inline">\$\\cP = \\{P\_\\theta:\\; \\theta\\in\\Theta\\}\$</span>, we say a family <span class="math inline">\$\\mathcal{Q}\$</span> of priors is *conjugate* to <span class="math inline">\$\\cP\$</span> if the posterior distribution is also always in <span class="math inline">\$\\mathcal{Q}\$</span>. Conjugate priors exist for many exponential families.

**Example: Beta-Binomial**

Suppose that we observe a binomial random variable with a Beta prior: <span class="math display">\\$$ \\begin{aligned} \\theta \\sim \\text{Beta}(\\alpha,\\beta) &= \\theta^{\\alpha-1}(1-\\theta)^{\\beta-1} \\frac{\\Gamma(\\alpha)\\Gamma(\\beta)}{\\Gamma(\\alpha+\\beta)} \\\\ X \\mid \\theta \\sim \\text{Binom}(n,\\theta) &= \\theta^x(1-\\theta)^{n-x}\\binom{n}{x} \\end{aligned} \\$$</span> Recall that the <span class="math inline">\$\\text{Beta}(\\alpha,\\beta)\$</span> distribution is an exponential family on the unit interval with mean <span class="math inline">\$\\frac{\\alpha}{\\alpha + \\beta}\$</span> and variance <span class="math inline">\$\\frac{\\alpha\\beta}{(\\alpha+\\beta)^2(\\alpha+\\beta+1)}\$</span>. The marginal distribution of <span class="math inline">\$X\$</span> in this problem is called a *Beta-Binomial* distribution.

In this context, <span class="math inline">\$\\alpha\$</span> and <span class="math inline">\$\\beta\$</span> are not unknown parameters; rather, the analyst will specify them to define the prior for <span class="math inline">\$\\theta\$</span>. Parameters of the prior are commonly called *hyperparameters*. Note that the functional form in <span class="math inline">\$\\theta\$</span> is similar for the prior and the likelihood, but <span class="math inline">\$\\theta\$</span> plays different roles in each: in the Beta prior, <span class="math inline">\$\\theta\$</span> is the random variable, but in the binomial likelihood, <span class="math inline">\$\\theta\$</span> plays the role of the parameter.

Note that we only need to calculate the posterior up to a proportionality constant in <span class="math inline">\$\\theta\$</span>. Since we know it is a probability distribution, we can drop any multiplicative constants along the way and just normalize it at the very end. <span class="math display">\\$$ \\begin{aligned} \\lambda(\\theta \\mid X=x) &\\propto\_\\theta \\lambda(\\theta)p\_\\theta(x)\\\\ &\\propto\_\\theta \\theta^{\\alpha-1}(1-\\theta)^{\\beta-1} \\cdot \\theta^x (1-\\theta)^{n-x}\\\\ &= \\theta^{x + \\alpha-1} \\cdot (1-\\theta)^{n-x + \\beta-1}\\\\ &\\propto\_\\theta \\text{Beta}(x+\\alpha, n-x+\\beta) \\end{aligned} \\$$</span> Thus, we have calculated that <span class="math inline">\$\\theta \\mid X=x \\sim \\text{Beta}(x+\\alpha, n-x+\\beta)\$</span>, and in particular we have the posterior mean <span class="math display">\\$$ \\EE\[\\theta \\mid X$$ = \\frac{X + \\alpha}{n + \\alpha + \\beta} \\\]</span> We may recognize the form of this estimator as our estimators from [Lecture 2](../estimation/index.md) where we imagined we had observed <span class="math inline">\$k = \\alpha+\\beta\$</span> “pseudo-trials” with <span class="math inline">\$\\alpha\$</span> successes, and then report the success rate after combining the pseudo-trials with the <span class="math inline">\$n\$</span> trials represented by our binomial data. If we take <span class="math inline">\$\\alpha = \\beta = 1\$</span>, we get the uniform prior. Thus, the estimator <span class="math inline">\$\\frac{X+1}{n+2}\$</span> minimizes the corresponding Bayes risk <span class="math inline">\$\\int\_0^1 R(\\theta;\\delta)\\,d\\theta\$</span> over all possible estimators <span class="math inline">\$\\delta\$</span>.

By massaging the expression above, we can interpret the Bayes estimator as a weighted average of the UMVU estimator we’d obtain using the data alone, and the “pseudo-estimator” we’d obtain if we observed only the <span class="math inline">\$k\$</span> pseudo-trials, with the weights corresponding to the relative sample sizes of the real data and the pseudo-data: <span class="math display">\\$$ \\EE\[\\theta \\mid X$$ = \\frac{X}{n} \\cdot \\frac{n}{n+k} + \\frac{\\alpha}{k}\\cdot \\frac{k}{n+k} \\\]</span>

We can visualize this problem below:

### <span class="header-section-number">3.1</span> Beta-binomial example {.anchored number="3.1" anchor-id="beta-binomial-example"}

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
viewof n = Inputs.range([1, 500], {value: 10, step: 1, label: "n"})
viewof x = Inputs.range([0, 500], {value: 6, step: 1, label: "X"})
viewof pseudoHeads = Inputs.range([0.1, 200], {value: 2, step: 0.1, label: "α (pseudo-heads)"})
viewof pseudoTails = Inputs.range([0.1, 200], {value: 2, step: 0.1, label: "β (pseudo-tails)"})

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

**Example: Normal mean**

As another example, suppose we observe a single observation from a univariate Gaussian location family with a Gaussian prior on the location parameter <span class="math display">\\$$ \\begin{aligned} \\theta \\sim N(\\mu,\\tau^2) &\\propto\_\\theta e^{-(\\theta-\\mu)^2/2\\tau^2}\\\\ X \\mid \\theta \\sim N(\\theta,\\sigma^2) &\\propto\_\\theta e^{-(x-\\theta)^2/2\\sigma^2} \\end{aligned} \\$$</span> Again, <span class="math inline">\$\\theta\$</span> plays a different role in the two densities above, first as the random variable and then as a parameter. Note <span class="math inline">\$\\sigma^2\$</span> and <span class="math inline">\$\\tau^2\$</span> are both assumed known.

Multiplying the likelihood by the prior gives an expression proportional to the posterior density: <span class="math display">\\$$ \\begin{aligned} \\lambda(\\theta \\mid x) &\\propto\_\\theta \\exp\\left\\{ -\\frac{(x-\\theta)^2}{2\\sigma^2} -\\frac{(\\theta-\\mu)^2}{2\\tau^2}\\right\\}\\\\ &\\propto\_\\theta \\exp\\left\\{ \\theta\\left(\\frac{x}{\\sigma^2} + \\frac{\\mu}{\\tau^2}\\right)-\\theta^2\\left(\\frac{1}{2\\sigma^2} + \\frac{1}{2\\tau^2}\\right)\\right\\} \\end{aligned} \\$$</span> Since the log-posterior is quadratic in <span class="math inline">\$\\theta\$</span>, we recognize this as proportional to a Gaussian density. We can find the mean and variance by completing the square. Recalling that <span class="math display">\\$$ a\\theta^2-b\\theta = \\left(\\theta - \\frac{b}{2a}\\right)^2 a - c(a,b), \\$$</span> we can continue our calculation with <span class="math inline">\$a=\\frac{1}{2}\\left(\\sigma^{-2} + \\tau^{-2}\\right)\$</span> and <span class="math inline">\$b= x\\sigma^{-2} + \\mu\\tau^{-2}\$</span>, giving <span class="math display">\\$$ \\begin{aligned} \\lambda(\\theta \\mid x) &\\propto\_\\theta \\exp\\left\\{ -\\left(\\theta-\\frac{x\\sigma^{-2}+\\mu\\tau^{-2}}{\\sigma^{-2} + \\tau^{-2}}\\right)^2 \\bigg/ 2\\left(\\sigma^{-2}+\\tau^{-2}\\right)^{-1}\\right\\}\\\\ &\\propto\_\\theta N\\left( \\frac{x\\sigma^{-2}+\\mu\\tau^{-2}}{\\sigma^{-2} + \\tau^{-2}} , \\frac{1}{\\sigma^{-2}+\\tau^{-2}} \\right). \\end{aligned} \\$$</span> This formula becomes a bit less unlovely if we interpret it in terms of the *precision*, which is defined as the reciprocal of the variance. Then, the posterior precision is <span class="math inline">\$\\sigma^{-2} + \\tau^{-2}\$</span>, the sum of the precisions for the prior and likelihood, and the posterior mean is the precision-weighted average <span class="math display">\\$$ \\EE\[\\theta \\mid X$$ = \\frac{X\\sigma^{-2}+\\mu\\tau^{-2}}{\\sigma^{-2} + \\tau^{-2}} = X \\frac{\\sigma^{-2}}{\\sigma^{-2}+\\tau^{-2}} + \\mu \\frac{\\tau^{-2}}{\\sigma^{-2}+\\tau^{-2}}. \\\]</span> This suggests a pseudo-data interpretation, which we can make more concrete if we extend this example to an i.i.d. sample.

**Example: Gaussian i.i.d. sample**

Now, assume we have the same prior but instead of one draw, we have <span class="math inline">\$n\$</span> draws <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid N(\\theta,\\sigma^2)\$</span>. If we first make a sufficiency reduction to <span class="math inline">\$\\overline{X} \\sim N(\\theta,\\sigma^2/n)\$</span>, we can immediately apply our formula from before to obtain: <span class="math display">\\$$ \\theta \\mid X \\sim N\\left( \\frac{\\overline{X} n\\sigma^{-2}+\\mu\\tau^{-2}}{n\\sigma^{-2} + \\tau^{-2}}, \\frac{1}{n\\sigma^{-2}+\\tau^{-2}} \\right). \\$$</span> Since the likelihood precision is linear in the sample size <span class="math inline">\$n\$</span>, we could think of the prior as arising from an equivalent sample of <span class="math inline">\$k=\\sigma^2/\\tau^2\$</span> pseudo-observations with mean <span class="math inline">\$\\mu\$</span>. Then we have <span class="math display">\\$$ \\theta \\mid X \\sim N\\left( \\frac{n\\overline{X} + k\\mu}{n + k}, \\frac{\\sigma^2}{n+k} \\right), \\$$</span> giving a similar interpretation as in the Beta-Binomial example.

### <span class="header-section-number">3.2</span> Conjugate priors for exponential families {.anchored number="3.2" anchor-id="conjugate-priors-for-exponential-families"}

Conjugate priors are commonly available for exponential family models. To understand why, consider a generic <span class="math inline">\$s\$</span>-parameter exponential family model where <span class="math display">\\$$ X\_1,\\ldots,X\_n \\simiid p\_\\eta(x) = e^{\\eta'T(x)-A(\\eta)}h(x), \\$$</span> We can always define a conjugate <span class="math inline">\$(s+1)\$</span>-parameter prior that is also an exponential family model. For any carrier <span class="math inline">\$\\lambda\_0\$</span>, define for <span class="math inline">\$k\\in\\RR\$</span>, <span class="math inline">\$\\mu\\in \\RR^{s}\$</span>: <span class="math display">\\$$ \\lambda\_{\\mu,k}(\\eta) = e^{k\\mu'\\eta - kA(\\eta) - B(k\\mu,k)}\\lambda\_0(\\eta). \\$$</span> Recalling that <span class="math inline">\$\\eta\$</span> is no longer a parameter, but the sampled random variable, this is an exponential family model with sufficient statistic <span class="math inline">\$\\binom{\\eta}{-A(\\eta)}\$</span> and natural parameter <span class="math inline">\$\\binom{k\\mu}{k}\$</span>, both in <span class="math inline">\$\\RR^{s+1}\$</span>.

Then the posterior density is <span class="math display">\\$$ \\begin{aligned} \\lambda(\\eta \\mid x) &\\propto\_\\eta \\left(\\prod\_{i=1}^n e^{\\eta'T(x\_i)-A(\\eta)}h(x\_i)\\right) \\cdot \\lambda\_{k,\\mu}(\\eta)\\\\ &\\propto\_\\eta e^{ \\left(k\\mu + \\sum\_i T(x\_i)\\right)'\\eta - (k+n)A(\\eta)}\\lambda\_0(\\eta)\\\\ &\\propto\_\\eta \\lambda\_{\\mu\_{\\text{post}}(x),n+k}(\\eta), \\end{aligned} \\$$</span> where we have a similar pseudo-data interpretation for <span class="math inline">\$\\mu\_{\\text{post}}\$</span>. <span class="math display">\\$$ \\mu\_{\\text{post}}(x) = \\frac{n \\overline{T}(x) + k\\mu}{n+k}, \\quad\\text{for } \\overline{T}(x) = \\frac{1}{n}\\sum\_i T(x\_i) \\$$</span> In many examples, including the examples we saw above, <span class="math inline">\$\\mu\_{\\text{post}}\$</span> corresponds to the posterior expectation for the mean parameter <span class="math inline">\$\\EE\_\\eta T(X)\$</span>; but whether or not this is true depends on the functional form of the prior. Another caveat is that, again depending on the functional form of the exponential family distribution, we may not have a closed form for <span class="math inline">\$B(k\\mu,k)\$</span>.

---

[← 2 Bayes estimator](03-2-bayes-estimator.md) · [Up: contents](index.md)
