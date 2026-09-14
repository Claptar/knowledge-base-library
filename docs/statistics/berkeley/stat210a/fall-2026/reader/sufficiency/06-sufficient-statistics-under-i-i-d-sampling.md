---
title: Sufficient statistics under i.i.d. sampling
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sufficient statistics under i.i.d. sampling

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```ojs
//| echo: false

function matchInputSpacing(customElement, referenceInput = Inputs.range([0, 1])) {
  // Temporarily add reference to DOM to compute styles
  document.body.appendChild(referenceInput);

  const computedStyle = window.getComputedStyle(referenceInput);

  // Extract relevant spacing properties
  customElement.style.marginTop = computedStyle.marginTop;
  customElement.style.marginBottom = computedStyle.marginBottom;
  customElement.style.marginLeft = computedStyle.marginLeft;
  customElement.style.marginRight = computedStyle.marginRight;

  // Clean up
  document.body.removeChild(referenceInput);

  return customElement;
}


// Interactive controls
viewof n2 = Inputs.range([1, 8], {value: 4, step: 1, label: "n"})
viewof theta2 = Inputs.range([0.01, 0.99], {value: 0.30, step: 0.01, label: "θ"})
// Method 3: Using a single combined input
viewof S = {
  const form = html`<form style="font: 13px / var(--sans-serif); display: flex; flex-direction: column; gap: 8px;">
    <div style="display: flex; align-items: center; padding: 3px 0px 0px 0px; ">
      <label style="display: flex; align-items: center; gap: 0.43em; min-width: 180px;">
        <span style="width: 7em;">S₁ = s₁</span>
        <input id="s1-text" type="number" min="0" max="${n2}" step="1" value="1"
               style="width: 5.37em;  height: 25px; font: inherit;">
        <input name="s1" type="range" min="0" max="${n2}" step="1" value="1"
               style="width: 8em; flex: 1">
      </label>
    </div>
    <div style="display: flex; align-items: center; padding: 0px 0px 10px 0px; ">
      <label style="display: flex; align-items: center; gap: 0.43em; min-width: 180px;">
        <span style="width: 7em;">S₂ = s₂</span>
        <input id="s2-text" type="number" min="0" max="${n2}" step="1" value="3"
               style="width: 5.37em; height: 25px; font: inherit;">
        <input name="s2" type="range" min="0" max="${n2}" step="1" value="3"
               style="width: 8em; flex: 1">
      </label>
    </div>
  </form>`;

  const s1Input = form.querySelector('input[name="s1"]');
  const s2Input = form.querySelector('input[name="s2"]');
  const s1TextInput = form.querySelector('#s1-text');
  const s2TextInput = form.querySelector('#s2-text');

  function updateConstraints(changedInput) {
    const s1Val = parseFloat(s1Input.value);
    const s2Val = parseFloat(s2Input.value);

    // Enforce s1 <= s2 by adjusting the input that wasn't changed
    if (s1Val > s2Val) {
      if (changedInput === 's1') {
        // s1 was changed and went above s2, so adjust s2 up
        s2Input.value = s1Val;
        s2TextInput.value = s1Val;
      } else {
        // s2 was changed and went below s1, so adjust s1 down
        s1Input.value = s2Val;
        s1TextInput.value = s2Val;
      }
    }

    // Update text displays to match sliders
    s1TextInput.value = s1Input.value;
    s2TextInput.value = s2Input.value;

    // Update the form's value property for Observable
    form.value = {
      s1: parseFloat(s1Input.value),
      s2: parseFloat(s2Input.value)
    };

    // Dispatch input event
    form.dispatchEvent(new CustomEvent("input"));
  }

  function updateFromText(changedInput) {
    // Update slider from text input
    if (changedInput === 's1') {
      s1Input.value = s1TextInput.value;
    } else {
      s2Input.value = s2TextInput.value;
    }
    // Then apply constraints
    updateConstraints(changedInput);
  }

  // Listen to slider changes
  s1Input.addEventListener("input", () => updateConstraints('s1'));
  s2Input.addEventListener("input", () => updateConstraints('s2'));

  // Listen to text input changes
  s1TextInput.addEventListener("input", () => updateFromText('s1'));
  s2TextInput.addEventListener("input", () => updateFromText('s2'));

  updateConstraints('s1'); // Initialize

  matchInputSpacing(form);

  return form;
}

// Extract x and y from range
s1_select = S.s1
s2_select = S.s2
viewof distributionType2 = Inputs.radio(["Binomial", "Discrete Laplace"], {value: "Binomial", label: "Distribution"})

// Select which PMF to use based on dropdown selection
pmf2 = distributionType2 === "Binomial" ? binomPMF : expPMF

// Generate joint distribution data
jointData2 = {
  const data = [];
  for (let x1 = 0; x1 <= n2; x1++) {
    for (let x2 = 0; x2 <= n2; x2++) {
      const prob = pmf(x1, n2, theta2) * pmf(x2, n2, theta2);
      const x_min = Math.min(x1, x2);
      const x_max = Math.max(x1, x2);
      data.push({
        x1: x1,
        x2: x2,
        prob: prob,
        x_min: x_min,
        x_max: x_max,
        selected: x_min === s1_select && x_max === s2_select
      });
    }
  }
  return data;
}

// Generate conditional distribution data (X given T = t)
conditionalData2 = {
  const data = [];
  const validPairs = jointData2.filter(d => d.x_min === s1_select && d.x_max === s2_select);
  const totalCondProb = validPairs.reduce((sum, d) => sum + d.prob, 0);

  validPairs.forEach(d => {
    if (totalCondProb > 0) {
      data.push({
        x1: d.x1,
        x2: d.x2,
        condProb: d.prob / totalCondProb,
        x_min: d.x_min,
        x_max: d.x_max
      });
    }
  });

  return data;
}

// Calculate maximum probability for scaling
maxProb2 = Math.max(...jointData2.map(d => d.prob))
maxCondProb2 = conditionalData2.length > 0 ? Math.max(...conditionalData2.map(d => d.condProb)) : 1

// Generate marginal distributions
marginalX12 = {
  const data = [];
  for (let x1 = 0; x1 <= n2; x1++) {
    data.push({
      x1: x1,
      prob: pmf(x1, n2, theta2)
    });
  }
  return data;
}

marginalX22 = {
  const data = [];
  for (let x2 = 0; x2 <= n2; x2++) {
    data.push({
      x2: x2,
      prob: pmf(x2, n2, theta2)
    });
  }
  return data;
}

// Generate conditional marginal distributions
conditionalMarginalX12 = {
  const data = [];

  if (conditionalData2.length > 0) {
    // Group by x1 and sum probabilities
    const x1Probs = new Map();
    conditionalData2.forEach(d => {
      x1Probs.set(d.x1, (x1Probs.get(d.x1) || 0) + d.condProb);
    });

    for (let x1 = 0; x1 <= n2; x1++) {
      if (x1Probs.has(x1)) {
        data.push({
          x1: x1,
          prob: x1Probs.get(x1)
        });
      }
    }
  }

  return data;
}

conditionalMarginalX22 = {
  const data = [];

  if (conditionalData2.length > 0) {
    // Group by x2 and sum probabilities
    const x2Probs = new Map();
    conditionalData2.forEach(d => {
      x2Probs.set(d.x2, (x2Probs.get(d.x2) || 0) + d.condProb);
    });

    for (let x2 = 0; x2 <= n2; x2++) {
      if (x2Probs.has(x2)) {
        data.push({
          x2: x2,
          prob: x2Probs.get(x2)
        });
      }
    }
  }

  return data;
}

maxRad2 = 20 * 5 / (n2 + 1)

maxMarginalProb2 = Math.max(...marginalX12.map(d => d.prob), ...marginalX22.map(d => d.prob))
maxCondMarginalProb2 = conditionalMarginalX12.length > 0 && conditionalMarginalX22.length > 0 ?
  Math.max(...conditionalMarginalX12.map(d => d.prob), ...conditionalMarginalX22.map(d => d.prob)) : 1


jointPlot2 = Plot.plot({
  width: 480,
  height: 480,
  marginTop: 140,
  marginLeft: 80,
  marginBottom: 80,
  marginRight: 120,
  style: { fontSize: "20px" },

  r: {
    type: "linear",
    domain: [0, maxRad2],  // Fixed domain from 0 to 20
    range: [0, maxRad2],   // Maps directly to pixel sizes
    clamp: true       // Prevents values outside domain
  },


  x: {
    domain: [-0.5, n2 + 0.5],
    ticks: Array.from({length: n2 + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n2 + 0.5],
    ticks: Array.from({length: n2 + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },

  marks: [
    // Grid lines
    Plot.ruleX(Array.from({length: n2 + 1}, (_, i) => i), {stroke: "#f0f0f0"}),
    Plot.ruleY(Array.from({length: n2 + 1}, (_, i) => i), {stroke: "#f0f0f0"}),

    // Probability circles
    Plot.dot(jointData2, {
      x: "x1",
      y: "x2",
      r: d => Math.sqrt(d.prob / maxProb2) * maxRad2,
      fill: d => d.selected ? "red" : "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Top marginal histogram (X₁)
    Plot.rect(marginalX12, {
      x1: d => d.x1 - 0.3,
      x2: d => d.x1 + 0.3,
      y1: n2 + 0.56 + n2 * .06,
      y2: d => n2 + 0.56 + n2 * .06 + (d.prob / maxMarginalProb2) * (n2 + 1) * 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right marginal histogram (X₂)
    Plot.rect(marginalX22, {
      x1: n2 + 0.56 + n2 * .06,
      x2: d => n2 + 0.56 + n2 * .06 + (d.prob / maxMarginalProb2) * (n2 + 1) * 0.3,
      y1: d => d.x2 - 0.3,
      y2: d => d.x2 + 0.3,
      fill: "steelblue",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Title
    Plot.text(["Joint Distribution of X = (X₁, X₂)"], {
      x: n2/2,
      y: n2 + 0.5 + (n2 + 1) * .45,
      fontSize: 24,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})

conditionalPlot2 = Plot.plot({
  width: 480,
  height: 480,
  marginTop: 140,
  marginLeft: 80,
  marginBottom: 80,
  marginRight: 120,
  style: { fontSize: "20px" },

  r: {
    type: "linear",
    domain: [0, maxRad2],  // Fixed domain from 0 to 20
    range: [0, maxRad2],   // Maps directly to pixel   sizes
    clamp: false       // Prevents values outside domain
  },
  x: {
    domain: [-0.5, n2 + 0.5],
    ticks: Array.from({length: n2 + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₁",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },
  y: {
    domain: [-0.5, n2 + 0.5],
    ticks: Array.from({length: n2 + 1}, (_, i) => i),
    tickFormat: d => d.toString(),
    label: "X₂",
    labelAnchor: "center",
    labelOffset: 50,
    labelArrow: "none"
  },

  marks: [
    // Grid lines
    Plot.ruleX(Array.from({length: n2 + 1}, (_, i) => i), {stroke: "#f0f0f0"}),
    Plot.ruleY(Array.from({length: n2 + 1}, (_, i) => i), {stroke: "#f0f0f0"}),

    // All possible points (faded)
    Plot.dot(jointData2, {
      x: "x1",
      y: "x2",
      r: 3,
      fill: "lightgray",
      fillOpacity: 0.3
    }),

    // Conditional probability circles
    Plot.dot(conditionalData2, {
      x: "x1",
      y: "x2",
      r: d => conditionalData2.length > 0 ? Math.sqrt(d.condProb / maxCondProb2) * maxRad2 : 5,
      fill: "red",
      fillOpacity: 0.8,
      stroke: "black",
      strokeWidth: 1
    }),

    // Top conditional marginal histogram (X₁ | T = t)
    Plot.rect(conditionalMarginalX12, {
      x1: d => d.x1 - 0.3,
      x2: d => d.x1 + 0.3,
      y1: n2 + 0.56 + n2 * .06,
      y2: d => n2 + 0.56 + n2 * .06 + (d.prob / maxCondMarginalProb2) * (n2 + 1) * 0.3,
      fill: "red",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Right conditional marginal histogram (X₂ | S = s)
    Plot.rect(conditionalMarginalX22, {
      x1: n2 + 0.56 + n2 * .06,
      x2: d => n2 + 0.56 + n2 * .06 + (d.prob / maxCondMarginalProb2) * (n2 + 1) * 0.3,
      y1: d => d.x2 - 0.3,
      y2: d => d.x2 + 0.3,
      fill: "red",
      fillOpacity: 0.7,
      stroke: "black",
      strokeWidth: 0.5
    }),

    // Title
    Plot.text([`Conditional Distribution P(X | S = (${s1_select}, ${s2_select}))`], {
      x: n2/2,
      y: n2 + 0.5 + (n2 + 1) * .45,
      fontSize: 24,
      fontWeight: "bold",
      textAnchor: "middle"
    })
  ]
})

// Display plots side by side
html`<div style="display: flex; gap: 20px; align-items: center; justify-content: center;">
  ${jointPlot2}
  ${conditionalPlot2}
</div>`
```

---

[← Examples](05-examples.md) · [Up: contents](index.md) · [Minimal sufficiency →](07-minimal-sufficiency.md)
