---
title: Nuisance Parameters
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Nuisance Parameters

**Source:** [`reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-nuisance.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

One-parameter families are the exception in statistics, not the rule. In most testing problems, there are additional unknown quantities which are not of direct interest, but which will generically affect the rejection probability of any test we choose. Formally, we will consider a general setup where we observe <span class="math inline">\$X \\sim P\_{\\theta,\\lambda}\$</span> from a statistical model <span class="math display">\\$$ \\cP = \\{P\_{\\theta,\\lambda}:\\; (\\theta,\\lambda) \\in \\Omega\\}, \\$$</span> where as usual <span class="math inline">\$\\theta\$</span> and <span class="math inline">\$\\lambda\$</span> could be real vectors or could represent infinite-dimensional parameters such as unknown distributions.

We will assume the null and alternative hypotheses concern <span class="math inline">\$\\theta\$</span> only; that is, we still want to test <span class="math inline">\$H\_0:\\;\\theta\\in\\Theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta\\in\\Theta\_1\$</span>. We call <span class="math inline">\$\\theta\$</span> the **parameter of interest**, and <span class="math inline">\$\\lambda\$</span> the **nuisance parameter**.

**Example (Two-sample Gaussian problem):** We observe <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid N(\\mu,\\sigma^2)\$</span> and <span class="math inline">\$Y\_1,\\ldots,Y\_m \\simiid N(\\nu,\\sigma^2)\$</span>. All three parameters <span class="math inline">\$\\mu,\\nu\\in\\RR\$</span> and <span class="math inline">\$\\sigma^2&gt;0\$</span> are unknown, and we wish to test <span class="math inline">\$H\_0:\\;\\mu = \\nu\$</span> vs <span class="math inline">\$H\_1:\\;\\mu \\neq \\nu\$</span>. We can express our hypothesis in terms of a parameter of interest <span class="math inline">\$\\theta = \\mu - \\nu\$</span>, in which case our nuisance parameter is <span class="math inline">\$\\lambda = (\\mu + \\nu, \\sigma^2)\$</span>, or <span class="math inline">\$\\lambda = (\\mu, \\sigma^2)\$</span>, or any other representation of the remaining unknown information besides <span class="math inline">\$\\theta\$</span>.

**Example (Comparing two Poissons):** We observe <span class="math inline">\$X\\sim \\text{Pois}(\\mu)\$</span> and <span class="math inline">\$Y\\sim\\text{Pois}(\\nu)\$</span> and want to test <span class="math inline">\$H\_0:\\;\\mu\\leq \\nu\$</span> vs <span class="math inline">\$H\_1:\\;\\mu&gt;\\nu\$</span>. Here, we could call <span class="math inline">\$\\mu-\\nu\$</span> the parameter of interest, but as we will see shortly it is somewhat more natural to think about the ratio <span class="math inline">\$\\frac{\\mu}{\\nu}\$</span>, or <span class="math inline">\$\\theta = \\frac{\\mu}{\\mu+\\nu}\$</span>.

**Example (Two-sample binomial problem):** We might observe <span class="math inline">\$X\_1\\sim \\text{Binom}(n\_1,\\pi\_1)\$</span> and <span class="math inline">\$X\_2\\sim\\text{Binom}(n\_2,\\pi\_2)\$</span> and want to test <span class="math inline">\$H\_0:\\;\\pi\_1\\leq \\pi\_2\$</span> vs <span class="math inline">\$H\_1:\\;\\pi\_1&gt;\\pi\_2\$</span>. The sample sizes <span class="math inline">\$n\_1\$</span> and <span class="math inline">\$n\_2\$</span> are typically *known* (so they are not nuisance parameters). Here, we could call <span class="math inline">\$\\pi\_1-\\pi\_2\$</span> the parameter of interest, but it is somewhat more natural to think about the **odds ratio** <span class="math inline">\$\\rho = \\frac{\\pi\_1}{1-\\pi\_1}/\\frac{\\pi\_2}{1-\\pi\_2}\$</span>, whose log is the difference between the two natural parameters.

## Conditional testing {.anchored anchor-id="conditional-testing"}

Conditional testing offers very effective and fairly strategy for dealing with nuisance parameters. To introduce the idea, consider a simple problem where we observe a binomial random variable with a random sample size. This is a very common situation: for example, suppose that we conduct a survey asking people which of two candidates they favor, and the number of respondents is a random number.

Let <span class="math inline">\$N\$</span> represent the sample size and assume that, conditional on <span class="math inline">\$N = n\$</span>, we will observe a binomial random variable <span class="math inline">\$X \\sim \\text{Binom}(n,theta)\$</span>.

**Example (Random sample size with known distribution):** First, consider a simple setting where we actually know the distribution of <span class="math inline">\$N\$</span>, for example <span class="math inline">\$N \\sim \\text{Pois}(10)\$</span>; then having observed <span class="math inline">\$N\$</span> and <span class="math inline">\$X\$</span>, we want to test <span class="math inline">\$H\_0:\\;\\theta \\leq \\frac{1}{2}\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &gt; \\frac{1}{2}\$</span>. The full likelihood for the model is <span class="math display">\\$$ p\_\\theta(n,x) = \\frac{10^n e^{-10}}{n!} \\cdot \\binom{n}{x}\\theta^x(1-\\theta)^{n-x}, \\quad \\text{ for } 0 \\leq x \\leq n. \\$$</span> There is no UMP test[^1], but we have at least two natural options:

**Option 1: Marginal test** Marginally, we have <span class="math inline">\$X \\sim \\text{Pois}(10\\cdot \\theta)\$</span>. If we ignore <span class="math inline">\$N\$</span>, this distribution has monotone likelihood ratio in <span class="math inline">\$X\$</span>, so we could reject if <span class="math inline">\$X &gt; c\_\\alpha^{(1)}\$</span>, the upper-<span class="math inline">\$\\alpha\$</span> quantile of a <span class="math inline">\$\\text{Pois}(5)\$</span> distribution. This marginal test, which we can call <span class="math inline">\$\\phi\_1\$</span>, will certainly have <span class="math inline">\$\\EE\_\\theta \\phi\_1(X) \\leq \\alpha\$</span> for any <span class="math inline">\$\\theta \\leq \\frac{1}{2}\$</span>.

**Option 2: Conditional test** Conditionally, we have <span class="math inline">\$X \\mid N=n \\sim \\text{Binom}(n,\\theta)\$</span>, which also has monotone likelihood ratio in <span class="math inline">\$n\$</span>. So we can reject if <span class="math inline">\$X &gt; c\_\\alpha^{(2)}(n)\$</span>, the upper-<span class="math inline">\$\\alpha\$</span> quantile of a <span class="math inline">\$\\text{Binom}\\left(n,\\frac{1}{2}\\right)\$</span> distribution. This conditional test, which we can call <span class="math inline">\$\\phi\_2\$</span>, will have <span class="math display">\\$$ \\EE\_\\theta \\left\[\\phi\_2(X) \\mid N=n\\right$$ \\leq \\alpha, \\quad \\text{ for all } n\\geq 0, \\text{ and } \\theta \\leq \\frac{1}{2}, \\\]</span> hence we also have <span class="math inline">\$\\EE\_\\theta \\phi\_2(X) \\leq \\alpha\$</span> for <span class="math inline">\$\\theta \\leq \\frac{1}{2}\$</span>.

If we let <span class="math inline">\$q\_{\\theta}(x \\mid n)\$</span> represent the pmf of <span class="math inline">\$X\$</span> given <span class="math inline">\$N=n\$</span>, then the latter test <span class="math inline">\$\\phi\_2\$</span> is UMP in the **conditional model** <span class="math display">\\$$ \\mathcal{Q}\_n = \\{q\_\\theta(x \\mid n):\\; \\theta \\in \\Theta\\}, \\$$</span> consisting of the candidate conditional distributions for <span class="math inline">\$X\$</span> given <span class="math inline">\$N=n\$</span> (i.e., <span class="math inline">\$\\text{Binom}(n,\\theta)\$</span>).

In general, any level-<span class="math inline">\$\\alpha\$</span> (unbiased) test in the conditional model is also level-<span class="math inline">\$\\alpha\$</span> (unbiased) in the marginal model: the marginal power is the average conditional power, so any guarantee that the conditional power is below (or above) <span class="math inline">\$\\alpha\$</span> also holds perforce for the marginal power. For the same reason, any valid (unbiased) confidence interval in the conditional model is also valid (resp. unbiased) marginally.

The **conditionality principle** holds that, since <span class="math inline">\$N\$</span> is ancillary in this case, we should condition on its value. Informally, the observed value of <span class="math inline">\$N\$</span> has nothing to do with the parameter <span class="math inline">\$\\theta\$</span> that we care about, so we shouldn’t really think of it as data informing our inference about <span class="math inline">\$\\theta\$</span> even if it is random. Instead, we should just condition on its value and work in the conditional model, treating it as fixed.

Whether or not we accept the conditionality principle, conditioning on part of the data can be a very helpful way to deal with nuisance parameters, as we see next:

**Example (Random sample size with unknown distribution):** Now, we can modify the previous example to assume that <span class="math inline">\$N\$</span> is drawn from an *unknown* distribution <span class="math inline">\$P^N\$</span> on <span class="math inline">\$\\{0,1,\\ldots\\}\$</span>, but continuing to assume that <span class="math inline">\$X \\mid N=n \\sim \\text{Binom}(n,\\theta)\$</span>. Having introduced the infinite-dimensional nuisance parameter <span class="math inline">\$P^N\$</span>, we no longer have the option of rejecting for (marginally) large values of <span class="math inline">\$X\$</span>.

Now the marginal test is no longer even an option, but we can still use the conditional test just as before, since the conditional model <span class="math inline">\$\\mathcal{Q}\_n\$</span> is no different than it was when <span class="math inline">\$N\$</span> was ancillary. In other words, conditioning on <span class="math inline">\$N\$</span> completely removes the nuisance parameter <span class="math inline">\$P^N\$</span> from the problem. This might be a bad thing if <span class="math inline">\$N\$</span> were for some reason highly informative about <span class="math inline">\$\\theta\$</span>, but if we don’t think it is then we lose little and gain much by conditioning on <span class="math inline">\$N\$</span>.

**Example (Comparing two Poissons, continued):** We continue the previous example of comparing independent <span class="math inline">\$X\\sim\\text{Pois}(\\mu)\$</span> and <span class="math inline">\$Y\\sim\\text{Pois}(\\nu)\$</span>. If we let <span class="math inline">\$N = X + Y \\sim \\text{Pois}(\\mu + \\nu)\$</span>, then we have a submodel of the last example:[^2] <span class="math display">\\$$ X \\mid N = n \\sim \\text{Binom}(n,\\theta), \\quad \\text{ for } \\theta = \\frac{\\mu}{\\mu + \\nu}. \\$$</span>

Since <span class="math inline">\$Y = N-X\$</span> is recoverable from <span class="math inline">\$N\$</span> and <span class="math inline">\$X\$</span>, we can simply regard <span class="math inline">\$(N,X)\$</span> as our full data set. Conditioning on <span class="math inline">\$N\$</span> removes the nuisance parameter <span class="math inline">\$\\lambda = \\mu + \\nu\$</span> from the problem, leaving <span class="math inline">\$H\_0:\\;\\mu \\leq \\nu \\iff \\theta \\leq \\frac{1}{2}\$</span>, and <span class="math inline">\$H\_1:\\;\\mu &gt; \\nu \\iff \\theta &gt; \\frac{1}{2}\$</span>.

As we will see next, this beautiful reduction was not a miraculous coincidence, but a direct consequence of the exponential family structure of the model.

## Multiparameter exponential families {.anchored anchor-id="multiparameter-exponential-families"}

Consider a generic exponential family where we can partition the natural parameter into a parameter of interest <span class="math inline">\$\\theta\\in\\RR^s\$</span> and nuisance parameter <span class="math inline">\$\\lambda\\in\\RR^r\$</span>: <span class="math display">\\$$ X \\sim p\_{\\theta,\\lambda}(x) = e^{\\theta'T(x) + \\lambda'U(x) - A(\\theta,\\lambda)}h(x). \\$$</span> Both <span class="math inline">\$\\theta\$</span> and <span class="math inline">\$\\lambda\$</span> are assumed unknown, and we want to test a hypothesis about <span class="math inline">\$\\theta\$</span> with <span class="math inline">\$\\lambda\$</span> as a nuisance parameter, i.e. <span class="math inline">\$H\_0:\\;\\theta \\in \\Theta\_0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta \\in \\Theta\_1\$</span>. Our basic recipe is to condition on <span class="math inline">\$U(X)\$</span>, and then base our inferences on the conditional model for <span class="math inline">\$T(X)\$</span>, which depends on <span class="math inline">\$\\theta\$</span> alone.

Without loss of generality, we can make a sufficiency reduction to <span class="math inline">\$(T,U)\$</span>, since any test <span class="math inline">\$\\phi(X)\$</span> has the same power function as <span class="math inline">\$\\psi(T(X),U(X))\$</span> where <span class="math inline">\$\\psi(t,u) = \\EE \\left$$\\phi(X) \\mid T=t,U=u\\right$$\$</span>. Then we have <span class="math display">\\$$ (T, U) \\sim p\_{\\theta,\\lambda}(t,u) = e^{\\theta't + \\lambda'u - A(\\theta,\\lambda)}g(t,u). \\$$</span> When we calculate the conditional density for <span class="math inline">\$T\$</span> given <span class="math inline">\$U\$</span>, the factor <span class="math inline">\$e^{\\lambda'u-A(\\theta,\\lambda)}\$</span> in the numerator and denominator cancels, leaving <span class="math display">\\$$ q\_\\theta(t \\mid u) = \\frac{p\_{\\theta,\\lambda}(t,u)}{\\int p\_{\\theta,\\lambda}(z,u)\\,dz} = \\frac{e^{\\theta't} g(t,u)}{\\int e^{\\theta'z} g(z,u)\\,dz} = e^{\\theta't-B\_u(\\theta)} g(t,u), \\$$</span> for <span class="math inline">\$B\_u(\\theta) = \\log\\int e^{\\theta'z}g(z,u)\\,dz\$</span>. Because <span class="math inline">\$q\_\\theta(t \\mid u)\$</span> is an exponential family with sufficient statistic <span class="math inline">\$T\$</span> and natural parameter <span class="math inline">\$\\theta\$</span>, the conditional model <span class="math inline">\$\\mathcal{Q}\_u\$</span> is an <span class="math inline">\$s\$</span>-parameter exponential family, allowing for us to use standard techniques to perform inference on <span class="math inline">\$\\theta\$</span> with <span class="math inline">\$\\lambda\$</span> removed from the problem.

If <span class="math inline">\$s=1\$</span>, the conditional model <span class="math inline">\$\\mathcal{Q}\_u\$</span> has monotone likelihood ratios in <span class="math inline">\$T\$</span>. This makes conditional inference especially simple and appealing, leading to standard one- and two-sided conditional tests and conditional confidence intervals.

The Poisson comparison problem was an example of this: <span class="math display">\\$$ \\begin{aligned} p\_{\\mu,\\nu}(x,y) &= \\frac{\\mu^x e^{-\\mu}}{x!}\\cdot\\frac{\\nu^y e^{-\\nu}}{y!} \\\\ &= \\exp\\{ x\\log \\mu + y\\log \\nu - (\\mu+\\nu) \\}\\cdot \\frac{1}{x!y!}\\\\\[5pt$$ &= \\exp\\left\\{ x\\log \\frac{\\mu}{\\nu} + (y+x)\\log \\nu - (\\mu + \\nu)\\right\\}\\cdot \\frac{1}{x!y!} \\end{aligned} \\\]</span> By adding and subtracting <span class="math inline">\$x\\log \\nu\$</span> in the exponent in the last step, we have obtained a model of the desired form with <span class="math inline">\$\\theta = \\log \\frac{\\mu}{\\nu}\$</span>, <span class="math inline">\$T(X,Y)=X\$</span>, <span class="math inline">\$\\lambda = \\log \\nu\$</span>, and <span class="math inline">\$U(X,Y) = X+Y\$</span>. Thus, our general strategy tells us to condition on <span class="math inline">\$X+Y\$</span>, and once we have done so the optimal conditional test rejects for large values of <span class="math inline">\$X\$</span>.

As you will show in the problem set, the binomial comparison problem introduced in the first section is another example of this type of setting, which we can deal with in much the same way. The widget below illustrates how the conditional distribution given <span class="math inline">\$T(X) = X\_1+X\_2\$</span> depends only on the log odds ratio <span class="math inline">\$\\rho = \\frac{\\pi\_1}{1-\\pi\_1} / \\frac{\\pi\_2}{1-\\pi\_2}\$</span>, and not on the nuisance parameter <span class="math inline">\$\\pi\_2\$</span> (the case <span class="math inline">\$n\_1=n\_2=n\$</span> is illustrated, but the same is true for general <span class="math inline">\$n\_1,n\_2\$</span>).

``` {.sourceCode .js .code-with-copy}
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

## Permutation tests {.anchored anchor-id="permutation-tests"}

Even when we can’t get a UMPU test, conditional testing can be very useful.

**Example (Two-sample permutation test):** We observe two independent samples of real-valued random variables <span class="math inline">\$X\_1, \\ldots, X\_n \\simiid P\$</span>, and <span class="math inline">\$Y\_1, \\ldots, Y\_m \\simiid Q\$</span>, and we want to test whether the distributions are the same or different; i.e., we test <span class="math inline">\$H\_0: P=Q\$</span> vs <span class="math inline">\$H\_1: P \\neq Q\$</span>.

We cannot write this model as an exponential family, but we can condition on a statistic that is sufficient under the null hypothesis. If <span class="math inline">\$P=Q\$</span>, then we have <span class="math display">\\$$ X\_1, \\ldots, X\_n, Y\_1, \\ldots, Y\_m \\simiid P \\$$</span> Define the vector <span class="math inline">\$Z = (Z\_1, \\ldots, Z\_{n+m}) = (X\_1, \\ldots, X\_n, Y\_1, \\ldots, Y\_m)\$</span> which concatenates the two samples. Under <span class="math inline">\$H\_0\$</span>, the vector of **pooled order statistics** <span class="math inline">\$U(Z) = (Z\_{(1)}, Z\_{(2)}, \\ldots, Z\_{(n+m)})\$</span> is complete sufficient for <span class="math inline">\$Z=(X,Y)\$</span>, and the conditional distribution of <span class="math inline">\$Z\$</span> is uniform on all permutations of <span class="math inline">\$U\$</span>; that is, if <span class="math inline">\$\\mathcal{S}\_{n+m}\$</span> is the group of all permutations on <span class="math inline">\$n+m\$</span> items, then <span class="math display">\\$$ Z \\mid U(Z) = u \\stackrel{H\_0}{\\sim} \\text{Unif}\\{\\pi u:\\; \\pi \\in \\mathcal{S}\_{n+m}\\}. \\$$</span> Because <span class="math inline">\$U\$</span> is sufficient for the null model, <span class="math inline">\$H\_0\$</span> is a *simple null* in the conditional model. But the alternative in the conditional model is highly composite: For example, if <span class="math inline">\$Q\$</span> is stochastically larger than <span class="math inline">\$P\$</span>, then the last <span class="math inline">\$m\$</span> observations in <span class="math inline">\$Z\$</span> (the <span class="math inline">\$Y\$</span> values) should be systematically larger than the first <span class="math inline">\$n\$</span> (the <span class="math inline">\$X\$</span> values); or, if <span class="math inline">\$Q\$</span> has more variability, then the sample variance of the last <span class="math inline">\$m\$</span> observations should be systematically larger than that of the first <span class="math inline">\$n\$</span>, and so on.

Because there are so many ways that <span class="math inline">\$P\$</span> and <span class="math inline">\$Q\$</span> could differ from each other, there is no generically optimal test statistic for us to use. But the good news is that we can perform a valid conditional test using *any* statistic <span class="math inline">\$T(X,Y)\$</span>, by conditioning on <span class="math inline">\$U(X,Y)\$</span> (we will slightly abuse notation by using <span class="math inline">\$(X,Y)\$</span> and <span class="math inline">\$Z\$</span> interchangeably as arguments to <span class="math inline">\$T\$</span> and <span class="math inline">\$U\$</span>).

In principle, if we had unlimited computational resources (or a way of analytically simplifying the problem) we could simply reject when <span class="math inline">\$T(X)\$</span> is above its conditional <span class="math inline">\$\\alpha\$</span> quantile; or equivalently, we reject for small values of the corresponding <span class="math inline">\$p\$</span>-value <span class="math display">\\$$ p(x,y \\mid u) = \\PP\_{H\_0}(T(X,Y) \\geq T(x,y) \\mid U(X,Y) = u) = \\frac{1}{(n+m)!}\\sum\_{\\pi \\in \\mathcal{S}\_{n+m}} 1\\{T(\\pi u) \\geq T(x,y)\\}. \\$$</span> In practice, enumerating all <span class="math inline">\$(n+m)!\$</span> permutations is unnecessary, so we sample permutations to perform a **Monte Carlo test**: for <span class="math inline">\$\\pi\_1,\\ldots,\\pi\_B \\simiid \\text{Unif}(\\mathcal{S}\_{n+m})\$</span>, define the Monte Carlo <span class="math inline">\$p\$</span>-value <span class="math display">\\$$ p = \\frac{1}{B+1} \\left(1 + \\sum\_{b=1}^B 1\\left\\{T(\\pi\_b u) \\geq T(x,y)\\right\\}\\right). \\$$</span> This test is exact: if we let <span class="math inline">\$\\pi\_0\$</span> denote the permutation for which <span class="math inline">\$\\pi\_0u = (x,y)\$</span>, then under <span class="math inline">\$H\_0\$</span>, <span class="math inline">\$\\pi\_0,\\pi\_1,\\ldots,\\pi\_B\$</span> are i.i.d. draws from <span class="math inline">\$\\mathcal{S}\_{n+m}\$</span>, so <span class="math inline">\$(x,y)=\\pi\_0 u\$</span> has exactly the same chance to give the largest test statistic as every other permutation has.

Note that usually permutation tests are defined by randomly permutating <span class="math inline">\$(x,y)\$</span>, rather than randomly permuting <span class="math inline">\$u\$</span>; this is equivalent, since <span class="math inline">\$\\tilde\\pi\_b = \\pi\_b \\circ \\pi\_0^{-1}\$</span> are also i.i.d. draws from <span class="math inline">\$\\mathcal{S}\_{n+m}\$</span>.

It is worth noting that the concept of a Monte Carlo test can be applied to any situation where we prefer to sample <span class="math inline">\$B\$</span> values from the null distribution rather than directly calculate an exact quantile. There are very interesting extensions to Markov Chain Monte Carlo, that allow us to perform *exact* tests even when we cannot sample

Crucially, <span class="math inline">\$U(Z)\$</span> is *not* sufficient for <span class="math inline">\$Z\$</span> under the *full* model where <span class="math inline">\$P\$</span> and <span class="math inline">\$Q\$</span> vary arbitrarily. Suppose we instead conditioned on the order statistics of each sample separately: <span class="math display">\\$$ V(X,Y) = (X\_{(1)},\\ldots,X\_{(n)},Y\_{(1)},\\ldots,Y\_{(m)}). \\$$</span> Then, the distribution of <span class="math inline">\$(X,Y)\$</span> given <span class="math inline">\$V\$</span> would be fully known under the null or the alternative: we would have conditioned away the distinction between the null and the alternative, rendering the entire model a singleton. This is *not* what we want to do: whereas conditioning on <span class="math inline">\$U\$</span> and collapsing the null hypothesis to a singleton is convenient, conditioning on <span class="math inline">\$V\$</span> and collapsing the entire model to a singleton renders the data useless.

## Footnotes {#footnotes .anchored .quarto-appendix-heading}

[^1]: The likelihood ratio for each alternative <span class="math inline">\$\\theta\_1 &gt; \\frac{1}{2}\$</span> is a different linear combination of <span class="math inline">\$x\$</span> and <span class="math inline">\$n\$</span>: <span class="math inline">\$\\log \\frac{p\_{\\theta\_1}}{p\_{1/2}}(n,x) = x \\log \\frac{\\theta\_1}{1-\\theta\_1} - n\\log2(1-\\theta\_1)\$</span>

[^2]: To derive this, note that <span class="math display">\\$$ \\begin{aligned} \\PP\_{\\mu,\\nu}(X=x \\mid X+Y=n) &= \\frac{\\PP\_\\mu(X=x)\\PP\_\\nu(Y=x-n)}{\\PP\_{\\mu+\\nu}(X+Y=n)}\\\\\[5pt$$ &= \\frac{\\mu^x\\nu^{n-x}e^{-\\mu-\\nu}}{x!y!} \\,\\big/\\, \\frac{n!}{(\\mu+\\nu)^ne^{-(\\mu+\\nu)}}\\\\$$5pt$$ &= \\binom{n}{x}\\theta^x(1-\\theta)^{n-x}. \\end{aligned} \\\]</span>

---

[← Testing with Nuisance Parameters](01-testing-with-nuisance-parameters.md) · [Up: contents](index.md)
