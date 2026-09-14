---
title: Pre-compute for a reasonable range of d and k
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Pre-compute for a reasonable range of d and k

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

d_vals <- 2:100
k_vals <- 1:20

power_data <- map_dfr(d_vals, function(d_val) {
  map_dfr(k_vals[k_vals <= 20], function(k_val) {
    compute_power_curve(d_val, k_val)
  })
})

ojs_define(power_data_r = power_data)
```

```ojs
//| echo: false

// Standard normal CDF approximation
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

Thus, depending on what test we use on the same data set, we can get very different $p$-values.


<!-- ### Randomized $p$-values -->

<!-- We do not usually bother to randomize the $p$-value, but if we want to, we can augment the data with a uniform random variable $U \sim \text{Unif}[0,1]$ independently of $X$, and define a new test on the augmented sample space: -->
<!-- $$ -->
<!-- \tilde\phi_\alpha(x,u) = 1\{\phi_\alpha(x) > 1-u\}. -->
<!-- $$ -->
<!-- The test $\tilde\phi$ has conditional rejection probability $\phi_\alpha(x)$ given $X=x$,  so -->
<!-- $$ -->
<!-- \EE_\theta \tilde\phi_\alpha(X,U) = \EE_\theta \phi_\alpha(X), -->
<!-- $$ -->
<!-- and it is is monotone in $\alpha$ if $\phi_\alpha$ was. Then we can define  -->

---

[← Function that computes power curve for given d and k](05-function-that-computes-power-curve-for-given-d-and-k.md) · [Up: contents](index.md) · [Confidence Regions →](07-confidence-regions.md)
