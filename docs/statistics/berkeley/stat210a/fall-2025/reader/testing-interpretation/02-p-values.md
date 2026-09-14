---
title: p-Values
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# p-Values

**Source:** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

## Informal definition {.anchored anchor-id="informal-definition"}

The <span class="math inline">\$p\$</span>-value <span class="math inline">\$p(X)\$</span> is a measure of whether our data set would have led us to reject the null at various different <span class="math inline">\$\\alpha\$</span> values. If we are rejecting for large values of a test statistic <span class="math inline">\$T(X)\$</span> then this boils down to asking how extreme <span class="math inline">\$T(X)\$</span> is relative to its null distribution, leading to the familiar informal definition of the <span class="math inline">\$p\$</span>-value:

**Definition (Informal):** The <span class="math inline">\$p\$</span>-value is the probability for a test statistic <span class="math inline">\$T(X)\$</span> to be at least as large as its realized value, under the assumption that the null is true. That is, for a fixed value <span class="math inline">\$x\\in\\cX\$</span>, the <span class="math inline">\$p\$</span>-value <span class="math inline">\$p(x)\$</span> should be <span class="math inline">\$\\PP\_{H\_0}(T(X)\\geq T(x))\$</span>, or more precisely <span class="math display">\\$$ p(x) = \\sup\_{\\theta\\in\\Theta\_0} \\PP\_{\\theta}(T(X) \\geq T(x)), \\$$</span> allowing for the possibility of a composite null. Then the random variable <span class="math inline">\$p(X)\$</span> is the <span class="math inline">\$p\$</span>-value.

**Example: Binomial** If <span class="math inline">\$X\\sim \\text{Binom}(n,\\theta)\$</span> and we want to test <span class="math inline">\$H\_0:\\;\\theta\\leq 0.5\$</span> vs <span class="math inline">\$H\_0:\\;\\theta &gt; 0.5\$</span>, the UMP test rejects for large values of <span class="math inline">\$X\$</span>. Thus, the <span class="math inline">\$p\$</span>-value is <span class="math display">\\$$ p(x) = \\sup\_{\\theta\\leq 0.5} \\PP\_\\theta(X\\geq x) = \\PP\_{0.5}(X\\geq x), \\$$</span> since <span class="math inline">\$X\$</span> is stochastically increasing and the probability is therefore maximized at the boundary.

**Example: <span class="math inline">\$Z\$</span>-test** If <span class="math inline">\$X\\sim N(\\theta,1)\$</span> and we are testing <span class="math inline">\$H\_0:\\;\\theta = 0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta \\neq 0\$</span>, the two-sided test rejects for large <span class="math inline">\$T(X)=\|X\|\$</span>. The two-sided <span class="math inline">\$p\$</span>-value is therefore <span class="math display">\\$$ p(x) = \\PP\_0(\|X\|&gt;\|x\|) = 2(1-\\Phi(\|x\|)). \\$$</span>

## Formal definition {.anchored anchor-id="formal-definition"}

Not all tests are easily characterized as rejecting when some <span class="math inline">\$T(X)\$</span> is above a threshold; for example, a two-sided UMPU test rejects when some <span class="math inline">\$T(X)\$</span> is either large or small. Thus it is useful to have a more general definition:

Assume we are testing <span class="math inline">\$H\_0:\\;\\theta\\in\\Theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta\\in\\Theta\_1\$</span> in a model <span class="math inline">\$\\cP\$</span> based on data <span class="math inline">\$X\$</span>, and that we have a test <span class="math inline">\$\\phi\_\\alpha\$</span> for every significance <span class="math inline">\$\\alpha \\in $$0,1$$\$</span>: <span class="math display">\\$$ \\sup\_{\\theta\\in\\Theta\_0} \\EE\_\\theta \\phi\_\\alpha(X) \\leq \\alpha. \\$$</span> Assume further that <span class="math inline">\$\\phi\_{\\alpha}\$</span> is non-decreasing in <span class="math inline">\$\\alpha\$</span> (when the test rejects for smaller/stricter <span class="math inline">\$\\alpha\$</span>, it also rejects for larger/more lenient <span class="math inline">\$\\alpha\$</span>): <span class="math display">\\$$ \\phi\_{\\alpha\_1}(X) \\leq \\phi\_{\\alpha\_2}(X) \\quad \\text{ if } \\alpha\_1\\leq \\alpha\_2. \\$$</span>

**Definition (Formal):** Then, we can define the <span class="math inline">\$p\$</span>-value with respect to this family of tests as the value of <span class="math inline">\$\\alpha\$</span> for which the test barely rejects: <span class="math display">\\$$ p(x) = \\sup \\{\\alpha:\\; \\phi\_\\alpha(x) &lt; 1\\} = \\inf \\{\\alpha:\\; \\phi\_\\alpha(x) = 1\\}, \\$$</span> and in terms of the rejection regions: <span class="math display">\\$$ p(x) = \\sup \\{\\alpha:\\; x \\notin R\_\\alpha\\} = \\inf\\{\\alpha:\\; x \\in R\_\\alpha\\}. \\$$</span>

**Example: Exponential** Suppose that we are testing <span class="math inline">\$H\_0:\\;\\theta=1\$</span> vs <span class="math inline">\$H\_1:\\;\\theta\\neq 1\$</span> in the model <span class="math inline">\$X \\sim \\text{Exp}(\\theta)\$</span>. We can use either the equal-tailed test, or the UMPU test. Consider a value <span class="math inline">\$x&gt;1\$</span>, which will be in the acceptance region (for sufficiently small <span class="math inline">\$\\alpha\$</span>) or the right lobe of the rejection region (for sufficiently large <span class="math inline">\$\\alpha\$</span>). For either test, the acceptance region’s right boundary decreases continuously with <span class="math inline">\$\\alpha\$</span>, so the <span class="math inline">\$p\$</span>-value is the unique value of <span class="math inline">\$\\alpha\$</span> for which <span class="math inline">\$x\$</span> is on the boundary. For the equal-tailed test, we have at that <span class="math inline">\$\\alpha\$</span> value <span class="math display">\\$$ \\alpha/2 = \\PP\_1(X&gt;x) = e^{-x}, \\$$</span> so <span class="math inline">\$p(x) = 2e^{-x}\$</span>. For the UMPU test <span class="math inline">\$p(x)\$</span> is defined implicitly as the value of <span class="math inline">\$\\alpha\$</span> for which <span class="math inline">\$c\_2(\\alpha) = x\$</span>, which we can solve for numerically.

This formal definition reduces to our informal definition if the test <span class="math inline">\$\\phi\_\\alpha\$</span> rejects for large <span class="math inline">\$T(X)\$</span> and the critical threshold is tight:

**Proposition:** Assume that for each <span class="math inline">\$\\alpha\$</span>, we reject for large <span class="math inline">\$T(X)\$</span>, taking the threshold <span class="math inline">\$c\_\\alpha\$</span> as small as possible while achieving Type I error control:$$^1$$ <span class="math display">\\$$ c\_\\alpha = \\min \\left\\{c:\\; \\PP\_\\theta(T(X) &gt; c) \\leq \\alpha, \\text{ for all } \\theta\\in\\Theta\_0 \\right\\}, \\$$</span> noting that the minimum is well-defined because (complementary) CDFs are right-continuous.

At the boundary, we either

- (non-randomized <span class="math inline">\$\\phi\$</span>) reject if <span class="math inline">\$\\PP\_\\theta(T(X) \\geq c\_\\alpha) \\leq \\alpha\$</span> for all <span class="math inline">\$\\theta\\in\\Theta\_0\$</span>, or

- (randomized <span class="math inline">\$\\phi\$</span>) reject with probability <span class="math display">\\$$ \\gamma\_\\alpha = \\max\\left\\{ \\gamma:\\; \\PP\_\\theta(T &gt; c\_\\alpha) + \\gamma\\PP\_\\theta(T = c\_\\alpha) \\leq \\alpha, \\forall \\theta\\in\\Theta\_0\\right\\} \\$$</span>

Then the two definitions of <span class="math inline">\$p(x)\$</span> coincide.

*Proof:* In the non-randomized case, define <span class="math inline">\$\\gamma\_\\alpha = 1\$</span> if we reject at the boundary and <span class="math inline">\$0\$</span> otherwise.

Let <span class="math inline">\$p\_1(x) = \\sup\_{\\theta\\in\\Theta\_0} \\PP\_\\theta(T(X)\\geq T(x))\$</span>, and <span class="math inline">\$p\_2(x) = \\sup\\{\\alpha:\\; \\phi\_\\alpha(x) &lt; 1\\}\$</span>. We have <span class="math display">\\$$ \\begin{aligned} p\_1(x) &gt; \\alpha &\\iff \\PP\_\\theta(T(X) \\geq T(x)) &gt; \\alpha, \\text{ for some } \\theta\\in\\Theta\_0\\\\ &\\iff c\_\\alpha &gt; x, \\text{ or } c\_\\alpha = x \\text{ and } \\gamma\_\\alpha &lt; 1\\\\ &\\iff \\phi\_\\alpha(x) &lt; 1. \\end{aligned} \\$$</span> But then <span class="math display">\\$$ p\_2(x) = \\sup\\{\\alpha:\\; p\_1(x) &gt; \\alpha\\} = p\_1(x), \\$$</span> as desired.<span class="math inline">\$\\blacksquare\$</span>

## Super-uniformity {.anchored anchor-id="super-uniformity"}

The <span class="math inline">\$p\$</span>-value for any valid test <span class="math inline">\$\\phi\_\\alpha\$</span> is **super-uniform** on the null, meaning it is stochastically larger than uniform: <span class="math display">\\$$ \\PP\_\\theta( p(X) \\leq \\alpha ) \\leq \\alpha, \\text{ for all } \\theta\\in\\Theta\_0. \\$$</span> Note that <span class="math inline">\$p(x) \\leq \\alpha\$</span> if and only <span class="math inline">\$\\phi\_{\\alpha+\\ep}(x) = 1\$</span>, for all <span class="math inline">\$\\ep&gt;0\$</span>. Thus, for <span class="math inline">\$\\theta \\in \\Theta\_0\$</span>, we have <span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(p(X) \\leq \\alpha) &= \\PP\_\\theta\\left( \\phi\_{\\alpha+\\ep}(X) = 1, \\text{ for all } \\ep&gt;0 \\right)\\\\ &= \\lim\_{\\ep \\downarrow 0} \\PP\_\\theta\\left(\\phi\_{\\alpha+\\ep}(X) = 1\\right)\\\\ &\\leq \\lim\_{\\ep \\downarrow 0} \\EE\_\\theta \\left\[ \\phi\_{\\alpha+\\ep}(X)\\right$$\\\\ &\\leq \\alpha \\end{aligned} \\\]</span>

## Interpreting the <span class="math inline">\$p\$</span>-value {.anchored anchor-id="interpreting-the-p-value"}

One important thing to remember when we interpret the <span class="math inline">\$p\$</span>-value that it depends on which statistical test we choose (as well as the data, the model, and the null hypothesis). When the null and/or alternative hypothesis are composite, there may be a range of different but justifiable choices of test. In that case, it would be a mistake to think of the <span class="math inline">\$p\$</span>-value for any one of those tests as the canonical summary of the evidence in the data against the null.

**Example: (Multivariate Gaussian)** Suppose we observe <span class="math inline">\$X \\sim N\_d(\\mu, I\_d)\$</span> and wish to test the point null <span class="math inline">\$H\_0: \\mu = 0\$</span> against the composite alternative <span class="math inline">\$H\_1: \\mu \\neq 0\$</span>. For <span class="math inline">\$d \\geq 1\$</span>, the alternative is bi-directional, but most analysts will agree on the standard two-sided test. By constrast, for <span class="math inline">\$d\\geq 2\$</span>, the alternative is *multidirectional*, so there are different tests we could choose depending on our beliefs about which alternatives are more likely than others; the higher the dimension of the problem, the higher the stakes of this choice.

For example, if we want our test to be invariant to the direction <span class="math inline">\$\\frac{\\theta}{\\\|\\theta\\\|}\$</span>, we should reject for large values of the two-norm <span class="math inline">\$\\\|X\\\|\_2\$</span>. But suppose instead we expect <span class="math inline">\$\\theta\$</span> to be sparse if it is nonzero; then <span class="math inline">\$\\\|X\\\|\_\\infty = \\max\_{i=1}^d \|X\_i\|\$</span> might be a much better choice. The first test is called the <span class="math inline">\$\\chi^2\$</span> test, because <span class="math inline">\$\\\|X\\\|\_2^2\$</span> has a <span class="math inline">\$\\chi\_d^2\$</span> distribution under the null, and the second is called the max test; each dominates the other in different sparsity regimes.

The widget below shows the power curves as a function of <span class="math inline">\$\\theta\$</span> when <span class="math inline">\$\\mu\$</span> is a <span class="math inline">\$k\$</span>-sparse unit vector with equal nonzero entries and total norm <span class="math inline">\$\\\|\\mu\\\|\_2=\\theta\$</span>: <span class="math display">\\$$ \\mu = \\theta \\cdot \\frac{1}{\\sqrt{k}} \\binom{1\_k}{0\_{d-k}}, \\$$</span> where <span class="math inline">\$1\_n\$</span> and <span class="math inline">\$0\_n\$</span> are respectively the all-ones and all-zeros vectors in <span class="math inline">\$\\RR^n\$</span>. By playing with <span class="math inline">\$d\$</span> and <span class="math inline">\$k\$</span> you can see that the max-test outperforms the <span class="math inline">\$\\chi^2\$</span> test when <span class="math inline">\$\\mu\$</span> is sufficiently sparse, but the reverse is true if <span class="math inline">\$\\mu\$</span> is dense; and the differences become more pronounced as <span class="math inline">\$d\$</span> grows larger.

``` {.sourceCode .js .code-with-copy}
normalCDF = (x) => {
  const t = 1 / (1 + 0.2316419 * Math.abs(x));
  const d = 0.3989423 * Math.exp(-x * x / 2);
  const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
  return x > 0 ? 1 - prob : prob;
}

// Interactive controls
viewof d = Inputs.range([2, 100], {value: 10, step: 1, label: "d"})
viewof k = Inputs.range([1, 20], {value: 3, step: 1, label: "k"})

// Filter power data for current d and k
chiPowerData = transpose(power_data_r).filter(row => row.d === d && row.k === k)

// Infinity norm critical value
criticalInf = {
  const alpha = 0.05;
  let low = 0, high = 5;
  while (high - low > 0.0001) {
    const mid = (low + high) / 2;
    const pNull = 1 - Math.pow(2 * normalCDF(mid) - 1, d);
    if (pNull > alpha) low = mid;
    else high = mid;
  }
  return (low + high) / 2;
}

// Calculate power functions
data = chiPowerData.map(row => {
  const theta = row.theta;
  const muVal = k > 0 ? theta / Math.sqrt(k) : 0;

  // Chi-squared test power from R
  const powerChi = row.chi_power;

  // Infinity norm test power
  const probOneSignalBelow = normalCDF(criticalInf - muVal) - normalCDF(-criticalInf - muVal);
  const probOneNonSignalBelow = 2 * normalCDF(criticalInf) - 1;

  const powerInf = 1 - Math.pow(probOneSignalBelow, k) * Math.pow(probOneNonSignalBelow, d - k);

  return {
    theta: theta,
    chi: Math.max(0, Math.min(1, powerChi)),
    inf: Math.max(0, Math.min(1, powerInf))
  };
})

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
    domain: [0, 3 * Math.pow(d, 0.25)],
    label: "θ",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [0, 1],
    label: "Power",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    Plot.line(data, {x: "theta", y: "chi", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(data, {x: "theta", y: "inf", stroke: "red", strokeWidth: 2}),
    Plot.ruleY([0]),
    Plot.ruleY([0.05], {stroke: "gray", strokeDasharray: "4 4"}),
    Plot.text(["Power Comparison: Chi-Squared Test vs Infinity Norm Test"], {
      x: 1.5 * Math.pow(d, 0.25),
      y: 1.08,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),
    // Legend for chi-squared test (top left)
    Plot.lineX([{x: 0.3, y: 0.95},
                {x: 0.7, y: 0.95}], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text(["‖X‖₂ test"], {
      x: 0.75,
      y: 0.95,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),
    // Legend for infinity norm test (top left)
    Plot.lineX([{x: 0.3, y: 0.88},
                {x: 0.7, y: 0.88}], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text(["‖X‖∞ test"], {
      x: 0.75,
      y: 0.88,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

Thus, depending on what test we use on the same data set, we can get very different <span class="math inline">\$p\$</span>-values.

---

[← p-values, confidence regions, and (mis-)interpreting Tests](01-p-values-confidence-regions-and-mis--interpreting-tests.md) · [Up: contents](index.md) · [Confidence Regions →](03-confidence-regions.md)
