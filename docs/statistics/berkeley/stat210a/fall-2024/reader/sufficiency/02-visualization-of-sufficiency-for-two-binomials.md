---
title: Visualization of sufficiency for two binomials
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Visualization of sufficiency for two binomials

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We now illustrate the concept of sufficiency with a visualization for a closely related example where now the initial data set is a pair of independent binomial random variables $X_1, X_2 \simiid \text{Binom}(n, \theta)$. We can make a similar calculation to show that $T(X) = X_1 + X_2$ is sufficient:

$$
p_\theta(x) = \binom{n}{x_1} \theta^{x_1}(1-\theta)^{n-x_1} \cdot \binom{n}{x_2} \theta^{x_2}(1-\theta)^{n-x_2} = \theta^{T(x)}(1-\theta)^{2n-T(x)} \binom{n}{x_1}\binom{n}{x_2}.
$$

```ojs
//| echo: false

// CSS for layout
html`
<style>
  .plot-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  .plot {
    flex: 0 1 450px;
    margin: 10px;
  }
  .plot-title {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
  }
</style>
`

// Helper functions
function binomialProbability(n, k, p) {
  return combination(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

function combination(n, k) {
  return factorial(n) / (factorial(k) * factorial(n - k));
}

function factorial(n) {
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

// Input parameters
viewof n = Inputs.range([2, 10], {step: 1, value: 5, label: "n:"})
viewof theta = Inputs.range([0, 1], {step: 0.01, value: 0.5, label: "θ:"})
viewof t = Inputs.range([0, 2 * n], {step: 1, value: n, label: "T(X) = X₁ + X₂:"})

// Calculate probabilities
probabilities = {
  let probs = [];
  for (let x1 = 0; x1 <= n; x1++) {
    for (let x2 = 0; x2 <= n; x2++) {
      let prob = binomialProbability(n, x1, theta) * binomialProbability(n, x2, theta);
      probs.push({x1, x2, prob, sum: x1 + x2});
    }
  }
  return probs;
}

// Calculate conditional probabilities
conditionalProbs = {
  let totalProb = probabilities.filter(p => p.sum === t).reduce((sum, p) => sum + p.prob, 0);
  return Array.from({length: n + 1}, (_, x1) => {
    let x2 = t - x1;
    let prob = (x2 >= 0 && x2 <= n) ? probabilities.find(p => p.x1 === x1 && p.x2 === x2)?.prob || 0 : 0;
    return {x1, prob: prob / totalProb};
  });
}

// Create plot container
html`<div class="plot-container">
  <div class="plot">
    <div class="plot-title">P(X₁, X₂)</div>
    ${
      Plot.plot({
        width: 450,
        height: 450,
        margin: 60,
        style: {
          fontSize: "14px",
          fontWeight: "normal"
        },
        x: {
          label: "X₂",
          domain: [-1, n],
          tickFormat: d => d >= 0 ? d : "",
        },
        y: {
          label: "X₁",
          domain: [-1, n],
          tickFormat: d => d >= 0 ? d : "",
        },
        marks: [
          Plot.dot(probabilities, {
            x: "x2",
            y: "x1",
            r: d => Math.sqrt(d.prob) * 200,
            fill: d => d.sum === t ? "red" : "black",
          }),
          Plot.text([{x: n/2, y: -1.5}], {
            text: ["Distribution of (X₁, X₂)"],
            fontSize: 16,
          }),
        ]
      })
    }
  </div>
  <div class="plot">
    <div class="plot-title">P(X₁ | T(X))</div>
    ${
      Plot.plot({
        width: 450,
        height: 450,
        margin: 60,
        style: {
          fontSize: "14px",
          fontWeight: "normal"
        },
        x: {
          label: "X₁",
        },
        y: {
          label: "Probability",
          domain: [0, Math.max(...conditionalProbs.map(d => d.prob)) * 1.1],
        },
        marks: [
          Plot.barY(conditionalProbs, {x: "x1", y: "prob", fill: "red"}),
        ]
      })
    }
  </div>
</div>`
```

---

[← Sufficiency](01-sufficiency.md) · [Up: contents](index.md) · [Factorization theorem →](03-factorization-theorem.md)
